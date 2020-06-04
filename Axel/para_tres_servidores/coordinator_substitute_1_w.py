import pymysql
import socket
import threading
import sys
import pickle
import random
import time
import multiprocessing
from datetime import datetime
from dateutil import parser
from timeit import default_timer as timer

HOST="127.0.0.1"
PORT=int(input("Puerto Servidor 1: "))

HOST1="127.0.0.1"
HOST2="127.0.0.1"

HostServerTime="127.0.0.1"
PuertoServerTime=6000

HOSTMYSQL="localhost"
USERMYSQL="root"
PASSWORDMYSQL="1234"
DBMYSQL="baseserverp1"

def synchronizeTime(actual_time, host, port):
	try:
		s = socket.socket()
		# print('-------------------------')
		# print("Actual clock time at client side: " + str(actual_time))
		# connect to the clock server on local computer
		# s.connect(('13.84.128.25', port))
		s.connect((host, port))
		s.settimeout(1)
		request_time = timer()

		# receive data from the server
		server_time = parser.parse(s.recv(1024).decode())
		
		response_time = timer()
		# actual_time = datetime.datetime.now()

		# print("Time returned by server: " + str(server_time))

		process_delay_latency = response_time - request_time

		# print("Process Delay latency: " +
			#   str(process_delay_latency) + " seconds")

		# synchronize process client clock time
		client_time = server_time + timedelta(process_delay_latency)

		# print("Synchronized process client time: " + str(client_time))

		# calculate synchronization error
		error = actual_time - client_time
		# print("Synchronization error : " +
			#   str(error.total_seconds()) + " seconds")
		s.close()
		return client_time
	except Exception as e:
		print(
			'··········No se pudo realizar la conexión con el servidor de tiempo: ' + str(e))
		return addOneSecond(actual_time)
	finally:
		s.close()

def timedelta(process_delay_latency):
	import datetime
	return datetime.timedelta(seconds=(process_delay_latency) / 2)

def addOneSecond(actual_time):
	import datetime
	return actual_time + datetime.timedelta(0,1)

# Funcion que conecta a la base de datos y registra un registro en la base
class mysqlconn():
	def __init__(self):
		global HOSTMYSQL,USERMYSQL,PASSWORDMYSQL,DBMYSQL
		self.connection = pymysql.connect(	
			host=HOSTMYSQL,
			user=USERMYSQL,   #modificar tu usuario
			password=PASSWORDMYSQL, # poner tu contraseña
			db=DBMYSQL  #el nombre de la base de datos
			)
		self.cursor = self.connection.cursor()
		#connection.close()

	def myinsert(self,idpartida,ip,mensaje,horaC,horaS):   #inseta en la base
		sql= "INSERT INTO data(idpartida,ip,mensaje,horaClient,horaServer) VALUES(%s, %s, %s, %s, %s)"
		self.cursor.execute(sql, (idpartida,ip,mensaje,horaC,horaS))
		self.connection.commit()

	def myinsertresult(self,ip,jugador,letra,frase,ganado,horaJ,horaIn):   #inseta en la base
		sql= "INSERT INTO resultados(ipganador,jugador,letra,frase,ganado,horajugado,horainicio) VALUES(%s, %s, %s, %s, %s, %s, %s)"
		self.cursor.execute(sql, (ip,str(jugador),letra,frase,ganado,horaJ,horaIn))
		self.connection.commit()

	def myselect(self,i): # agarra un dato de la base
		sql= "select * from `frases` where `id` = %s"
		self.cursor.execute(sql,(i))
		dato = self.cursor.fetchall()
		return dato

	def maxid(self,tabla):
		sql= "SELECT MAX(id) AS id FROM %s" %tabla
		self.cursor.execute(sql);
		maxid = self.cursor.fetchone()
		if(maxid[0]==None):
			maxid=0
		else:
			maxid=maxid[0]
		print("dato:",maxid)
		return maxid

class Cliente():
	"""docstring for Cliente"""
	# def __init__(self, host="localhost", port=4000):
	def __init__(self,host,port):
		self.inactivo=0
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((str(host), int(port)))
		except Exception as e:
			print('Excepción: ', e)

	def send_msg(self, msg,hora,ip,name):
		#mensaje="2,"+msg+","+hora+","+ip+","+str(name)
		mensaje=[2]
		mensaje.append(msg)
		mensaje.append(hora)
		mensaje.append(ip)
		mensaje.append(name)
		mensajeEncode=pickle.dumps(mensaje)
		if(self.inactivo!=1):
			self.sock.sendall(mensajeEncode)


	def send_replicar(self,Contjugadores,JC,jugadores_perdidos,turno,frase,errores,progreso,progresolist,ganado,end):
		vista=[1]
		vista.append(Contjugadores)
		vista.append(JC)
		vista.append(jugadores_perdidos)
		vista.append(turno)
		vista.append(frase)
		vista.append(errores)
		vista.append(progreso)
		vista.append(progresolist)
		vista.append(ganado)
		vista.append(end)
		vistaEncode=pickle.dumps(vista)
		try:
			self.sock.sendall(vistaEncode)
			print()
		except:
			pass


class Servidor():
	"""docstring for Servidor"""
	def __init__(self, host, port):
	# def __init__(self, host="10.100.71.107", port=4000):

		#self.principal=1 #bandera que indica que es el server pricipal si es 1, 0  si es secundario
		self.badera_error=0 #variable que se prende si se desconecto el Gestor principal

		self.clientes = [] #lista de clientes jugadores
		self.Cserver = [] #lista de clientes servidores
		self.ipServers = [] #lista de ips de los servers
		self.ipclientes = [] #lista de ips de los clientes
		self.Hclient=[]
		self.name=[]
		self.Jerarquia_servers=[]

		self.Njugadores=0
		self.turnoMaximo=0

		#varibles de vistas actualizables en los gestores
		self.Cjugadores=0
		self.jugConect=0
		self.jugadores_perdidos=[]
		self.turno=0
		self.frase="N/D"
		self.errores= (10)
		self.progresoS="N/D"
		self.end=0
		self.ganado=False

		self.fraselist =[]
		self.progresolist = []
		self.progreso = []
		self.maxidresultados=[]

		self.event=[]


		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((str(host), int(port)))
		self.sock.listen(10)
		self.sock.setblocking(False)

		self.time1="00:00:00" #variable donde se guarda la hora
		self.horainicio="00:00:00"

		aceptar = threading.Thread(target=self.aceptarCon)   #demonio o proceso de aceptar conecciones
		hora = threading.Thread(target=self.tick)

		self.conmysql= mysqlconn()
		idfrase=random.randint(1, 100)
		dato=self.conmysql.myselect(idfrase)
		self.frase=dato[0][2].lower()
		print(self.frase)
		self.fraselist = list(self.frase)

		self.maxidresultados=self.conmysql.maxid("resultados")+1


		self.Njugadores=int(input("ingrese el numero de jugadores: "))
		self.turnoMaximo=self.Njugadores
		aceptar.daemon = True
		aceptar.start()

		hora.daemon = True
		hora.start()
		# self.Jerarquia_servers.append(("127.0.0.1",9000))
		portc=int(input("Puerto Cliente Servidor 1: "))###
		self.c = Cliente(HOST1,portc)####
		Jcliente=(HOST1,portc)
		self.Jerarquia_servers.append(Jcliente)

		portc=int(input("Puerto Cliente Servidor 2: "))###
		self.c1 = Cliente(HOST2,portc)####
		Jcliente=(HOST2,portc)
		self.Jerarquia_servers.append(Jcliente)


		while True:  #ciclo infinito para que pueda enviar mensajes a todos los clientes
			msg = input()
			if msg == 'salir':	#si escribes salir se cierra el servidor
				self.sock.close()
				sys.exit()
			else:
				pass

	def tick(self):  #funcion  de hacer que funcione el reloj
		while True:
			# ESTO comentado tomaria la hora de la pc
			# time2 = time.strftime('%H:%M:%S')
			# if time2 != self.time1:
			#   self.time1 = time2
			# time.sleep(0.90)
			# print(self.time1)
			global Horas, Min, Seg, Fecha
			if(Horas == 23 and Min == 59 and Seg == 59):
				Horas = 0
				Min = 0
				Seg = 0
			if(Min == 59 and Seg == 59):
				Horas += 1
				Min = 0
				Seg = 0
			if(Seg == 59):
				Min += 1
				Seg = 0
			hora_aleatoria = str(Horas)+":"+str(Min)+":"+str(Seg)
			hora_fecha_converted = datetime.strptime(Fecha + ' ' + hora_aleatoria, "%Y-%m-%d %H:%M:%S")
			if self.time1 == "00:00:00":
				self.time1 = datetime.strptime(str(hora_fecha_converted), "%Y-%m-%d %H:%M:%S")
			# if self.time1 == "error":
			#	   print('····· Se dejo de recibir la hora del servidor: ' + str(e))
			#	   self.time1 = datetime.strptime(str(hora_fecha_converted), "%Y-%m-%d %H:%M:%S")
			else:
				self.time1 = synchronizeTime(self.time1, '104.210.151.197', 10000)
				#self.time1 = synchronizeTime(self.time1, '127.0.0.1', 60000)
			time.sleep(1)
			Seg += 1
				
	def msg_to_all(self, msg): #funcion que envia un mensaje a todos los clientes
		for c in self.clientes:
			try:
				c.sendall(str.encode(msg))
				print("mensaje enviado\n")
			except:
				self.clientes.remove(c)

	def aceptarCon(self):   #funcion que es el demonio que acepta a los clientes 
		print("aceptarCon iniciado")
		while True:
			try:
				conn, addr = self.sock.accept()
				conn.setblocking(False)
				print(conn)
				if(len(self.Cserver)<2):
					hilo_Cserver=threading.Thread(name="Server",target=self.procesarServer, args=(conn,))
					self.Cserver.append(conn)
					self.ipServers.append(addr)
					hilo_Cserver.daemon=True
					hilo_Cserver.start()
				else:
					if(self.badera_error==1):
						data=conn.recv(1024).decode() 
						print("mi usuario es:",data)
						player=data
					else:
						player=str(self.Cjugadores)
					e = threading.Event()
					hilo_Cjugador=threading.Thread(name=player,target=self.procesarCon, args=(conn,e))
					self.Hclient.append(hilo_Cjugador)
					self.event.append(e)
					self.name.append(int(player))
					self.Cjugadores+=1
					self.jugConect+=1
					self.clientes.append(conn)   #agrega al cliente a la lista de cleintes
					self.c.send_replicar(self.Cjugadores,self.jugConect,self.jugadores_perdidos,self.turno,self.frase,self.errores,self.progreso,self.progresolist,self.ganado,self.end)
					self.c1.send_replicar(self.Cjugadores,self.jugConect,self.jugadores_perdidos,self.turno,self.frase,self.errores,self.progreso,self.progresolist,self.ganado,self.end)
					self.ipclientes.append(addr)		 #agrega la ip de el cleinte a la lista de ips
				# print(self.clientes)
			except: 
				pass
			if(self.Cjugadores==self.Njugadores):
				if(self.badera_error!=1):
					cont=0
					for c in self.clientes:
						c.sendall(str.encode(str(self.name[cont])))
						time.sleep(0.1)
						cont+=1

					for n in self.fraselist:
						self.progresolist.append(' _ ')
					self.printGuessedLetter()
					print("Tienes :", self.errores, 'intentos')

				for h in self.Hclient:
					if(h.is_alive()==False):
						h.daemon = True
						h.start()
				self.bandera_error=0
				self.Cjugadores+=1  ##solo para que la condicion if se haga 1 vez

	def printGuessedLetter(self):
		print("Tu frase secreta es: " + ''.join(self.progresolist))

	def ahorcado(self,letter,name):
		if letter in self.progreso:
			print("Ya habian adivinado esta letra.")
			self.errores-=1
		else:
			self.progreso.append(letter)
			if(len(letter) == 1):
				if(letter in self.fraselist):
					print("¡Acertaste!")
					if(self.errores > 0):
						print("¡Te quedan ", self.errores, 'intentos!')
					for i in range(len(self.fraselist)):
						if(letter == self.fraselist[i]):
							letterIndex = i
							self.progresolist[letterIndex] = letter.upper()
					self.printGuessedLetter()
		
				else:
					self.errores-=1
					print("¡Ups! Intentalo de nuevo.")
					if(self.errores > 0):
						print("¡Te quedan ", self.errores, 'intentos!')
					self.printGuessedLetter()
			elif(letter.upper() == self.frase.upper()):
				print('¡Acertaste! La palabra secreta es: ', self.frase.upper())
				print()
				self.progresolist=self.frase.upper()
				print("¡Ha ganado el jugador:",name+1,"!")
				self.ganado=True
				self.end=1

			else:
				self.errores-=1
				if(self.errores > 0):
					print("¡Te quedan ", self.errores, 'intentos!')
				self.printGuessedLetter()

		#Win/loss logic for the game
		joinedList = ''.join(self.progresolist)
		if(joinedList.upper() == self.frase.upper()):
			print('¡Bien hecho!')
			print()
			print("¡Ha ganado el jugador:",name+1,"!")
			self.ganado=True
			self.end=1

		elif(self.errores == 0):
			print("Perdiste")
			print("La frase secreta era: "+ self.frase.upper())
			print('¡Adiós!')
			self.end=1

	def ver_conexion(self,c,name,h):
		while True:
			data =c.getsockopt(socket.IPPROTO_TCP,socket.TCP_INFO)
			if (data==8):
				if(name not in self.jugadores_perdidos):
					print("Se perdio la conexion con el jugador:",name+1)
					self.jugadores_perdidos.append(name)
					self.jugConect-=1
					self.c.send_replicar(self.Cjugadores,self.jugConect,self.jugadores_perdidos,self.turno,self.frase,self.errores,self.progreso,self.progresolist,self.ganado,self.end)
					self.c1.send_replicar(self.Cjugadores,self.jugConect,self.jugadores_perdidos,self.turno,self.frase,self.errores,self.progreso,self.progresolist,self.ganado,self.end)
					self.Hclient.remove(h)
					break

	def procesarCon(self,c,e):	 # funcion que es el demonio que procesa a los clientes
		name=int(threading.currentThread().getName()) 
		mensaje=""
		horaC=""
		ip=""
		time.sleep(0.2)
		print("ProcesarCon iniciado: ",name)
		if(name==self.turno):
			e.set() #nitifica al evento de el jugador 1 que puede pasar
		JeSe=pickle.dumps(self.Jerarquia_servers)
		c.sendall(JeSe)
		####
		verificar=threading.Thread(name="verificar "+str(name),target=self.ver_conexion, args=(c,name,threading.currentThread()))
		verificar.daemon=True
		verificar.start()
		####
		while True:
			event_is_set = e.wait()  ##espera  a que le notifiquen que puede pasar
			if(name in self.jugadores_perdidos):
				break
			try:
				c.sendall(str.encode("1")) ##cuando envia 1  al cliente, para que sepa cuando avanzar el cronometro, y/o boton aceptar sepa que puede enviar mensaje 
				time.sleep(0.1)
			except:
				pass
			try:
				data = c.recv(1024).decode()  #recibe el mensaje de el cleiente y la hora de el cliente
				if (data):
					data=data.split(',')
					mensaje=str(data[0])
					horaC=str(data[1])
					index=self.clientes.index(c)
					ip=str(self.ipclientes[index][0]) #calcula la ip xde el cliente
					#print("=============== Cliente: ",ip,"\nMensaje: ",mensaje," A las: ",horaC)  #imprime la ip de el cliente, su mensaje , y su hora de el cliente
					self.ahorcado(mensaje,name)
					time.sleep(0.1)
					self.c.send_msg(mensaje,horaC,ip,name) #le manda el mensaje que recibio al otro server####
					self.c1.send_msg(mensaje,horaC,ip,name)
					self.conmysql.myinsert(self.maxidresultados,ip,mensaje,horaC,self.time1)  #manda a la funcion de mysql, los datod que quieres guardar en la base

					
				time.sleep(0.2)
				self.turno+=1
				while True:
					if(self.turno==self.turnoMaximo):
						self.turno=0

					if(self.turno in self.jugadores_perdidos):
						self.turno+=1
					else:
						break
				self.progresoS=''.join(self.progresolist)
				print("jugConect:",self.jugConect,"Turno:",self.turno,"frase: ",self.frase,"errores: ",self.errores,"progreso:",self.progresoS)
				self.c.send_replicar(self.Cjugadores,self.jugConect,self.jugadores_perdidos,self.turno,self.frase,self.errores,self.progreso,self.progresolist,self.ganado,self.end)
				self.c1.send_replicar(self.Cjugadores,self.jugConect,self.jugadores_perdidos,self.turno,self.frase,self.errores,self.progreso,self.progresolist,self.ganado,self.end)
				e.clear() #despues de que proceso su mensaje bloquea al jugador para que no pueda tirar
				time.sleep(0.1)
				if (self.end==1):
					if(self.ganado==True):
						self.conmysql.myinsertresult(ip,name+1,mensaje,self.frase,self.ganado,horaC,self.horainicio)
					else:
						self.conmysql.myinsertresult('','','',self.frase,self.ganado,horaC,self.horainicio)
					self.end=0
					sys.exit()
				if(self.turno in self.name):
					index=self.name.index(self.turno)
					self.event[index].set() #notifica al evento de el jugador que es su turno y para poder acanzar,(desbloquea el hilo evento)
				print()
			except:
				pass

	def procesarServer(self,c):	 # funcion que es el demonio que procesa a los clientes Servidores
		print("procesarServer iniciado: ")
		namejugador=-1
		ipjugador=""
		mensaje=""
		horaC=""
		while True:
			try:
				data = c.recv(1024)  #recibe el mensaje de el cliente y la hora de el cliente
				if (data):
					data=pickle.loads(data)
					if(data[0]==1):
						self.Cjugadores=data[1]
						self.jugConect=data[2]
						self.jugadores_perdidos=data[3]
						self.turno=data[4]
						self.frase=data[5]
						self.errores=data[6]
						self.progreso=data[7]
						self.progresolist=data[8]
						self.ganado=data[9]
						self.end=data[10]
						self.fraselist=list(self.frase)
						self.progresoS=''.join(self.progresolist)
						self.printGuessedLetter()
						print("jugConect:",self.jugConect,"Turno:",self.turno,"frase: ",self.frase,"errores: ",self.errores,"progreso:",self.progresoS)
						time.sleep(0.1)
						if (self.end==1):
							if(self.ganado==True):
								self.conmysql.myinsertresult(ipjugador,namejugador+1,mensaje,self.frase,self.ganado,horaC,self.horainicio)
								print("El juego lo gano el jugador:",namejugador+1)
							else:
								self.conmysql.myinsertresult('','','',self.frase,self.ganado,horaC,self.horainicio)
								print("Juego perdido")
							print("El juego termino")
							self.end=0
							sys.exit()
						if(self.turno in self.name):
							index=self.name.index(self.turno) 
							self.event[index].set()
						print()
						if(self.errores==0):
							sys.exit()
					else:
						mensaje=data[1]
						horaC=data[2]
						ipjugador=data[3]	
						#print("Servidor: ",ip,"\nMensaje: ",mensaje," A las: ",horaC)
						namejugador=data[4]
						self.conmysql.myinsert(self.maxidresultados,ipjugador,mensaje,horaC,self.time1)  #manda a la funcion de mysql, los datod que quieres guardar en la base
				else:
					print("Se perdio la conexion con el servidor:",self.Cserver.index(c))
					if(self.Cserver.index(c)==0):
						self.c.inactivo=1
					else:
						self.c1.inactivo=1
					self.badera_error=1
					self.Njugadores=self.jugConect
					self.Cjugadores=0+len(self.Hclient)
					self.jugConect=0+len(self.Hclient)
					break
				
			except ConnectionResetError:
				print("Se perdio la conexion con el servidor:",self.Cserver.index(c))
				if(self.Cserver.index(c)==0):
					self.c.inactivo=1
				else:
					self.c1.inactivo=1
				self.badera_error=1
				self.Njugadores=self.jugConect
				self.Cjugadores=0+len(self.Hclient)
				self.jugConect=0+len(self.Hclient)
				break

			except:
				pass

# HOST="192.168.100.130"
#HOST="127.0.0.1"
#PORT=int(input("Puerto Servidor 1: "))

# variables para la hora random
Horas = random.randint(0, 24)
Min = random.randint(0, 59)
Seg = random.randint(0, 59)
Fecha = datetime.today().strftime('%Y-%m-%d')
# enviamos a la clase server el host y el puerto
s = Servidor(HOST,PORT)