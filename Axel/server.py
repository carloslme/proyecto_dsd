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

def synchronizeTime(actual_time, host, port):##
	try:
		s = socket.socket()
		# print('-------------------------')
		#print("Actual clock time at client side: " + str(actual_time))
		# connect to the clock server on local computer
		# s.connect(('13.84.128.25', port))
		s.connect((host, port))

		request_time = timer()

		# receive data from the server
		server_time = parser.parse(s.recv(1024).decode())
		response_time = timer()
		# actual_time = datetime.datetime.now()

		# print("Time returned by server: " + str(server_time))

		process_delay_latency = response_time - request_time

		# print("Process Delay latency: " + str(process_delay_latency) + " seconds")

		# synchronize process client clock time
		client_time = server_time + timedelta(process_delay_latency)

		# print("Synchronized process client time: " + str(client_time))

		# calculate synchronization error
		error = actual_time - client_time
		# print("Synchronization error : " + str(error.total_seconds()) + " seconds")

		s.close()
		return client_time
	except Exception as e:
		print('··········No se pudo realizar la conexión con el servidor de tiempo: ' + str(e))
		return actual_time

def timedelta(process_delay_latency):
		import datetime
		return datetime.timedelta(seconds=(process_delay_latency) / 2)

# Funcion que conecta a la base de datos y registra un registro en la base
class mysqlconn():
	def __init__(self):
		self.connection = pymysql.connect(	
			host="localhost",
			user="root",   #modificar tu usuario
			password="9343", # poner tu contraseña
			db="BaseServerP"  #el nombre de la base de datos
			)
		self.cursor = self.connection.cursor()
		#connection.close()

	def myinsert(self,ip,mensaje,horaC,horaS):   #inseta en la base
		sql= "INSERT INTO data(ip,mensaje,horaClient,horaServer) VALUES(%s, %s, %s, %s)"
		self.cursor.execute(sql, (ip,mensaje,horaC,horaS))
		self.connection.commit()

	def myselect(self,i): # agarra un dato de la base
		sql= "select * from `frases` where `id` = %s"
		self.cursor.execute(sql,(i))
		dato = self.cursor.fetchall() 
		return dato

class Cliente():
	"""docstring for Cliente"""
	# def __init__(self, host="localhost", port=4000):
	def __init__(self,host,port):

		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((str(host), int(port)))
		except Exception as e:
			print('Excepción: ', e)

	def send_msg(self, msg,hora,ip):
		mensaje="2,"+msg+","+hora+","+ip
		self.sock.sendall(str.encode(mensaje))
		print()

	def send_msg1(self, msg):
		mensaje="1,"+str(msg)
		self.sock.sendall(str.encode(mensaje))
		print()


class Servidor():
	"""docstring for Servidor"""
	def __init__(self, host, port):
	# def __init__(self, host="10.100.71.107", port=4000):

		self.clientes = [] #lista de clientes jugadores
		self.Cserver = [] #lista de clientes servidores
		self.ip = [] #lista de ips de los clientes
		self.Hclient=[]
		self.name=[]
		self.turno=0
		self.Njugadores=0
		self.Cjugadores=0
		self.event=[]

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((str(host), int(port)))
		self.sock.listen(10)
		self.sock.setblocking(False)

		self.time1='' #variable donde se guarda la hora

		aceptar = threading.Thread(target=self.aceptarCon)   #demonio o proceso de aceptar conecciones
		#procesar = threading.Thread(target=self.procesarCon) #demonio o proceso de procesar a los clientes recibeindo sus mensajes y agregandolos a la a base
		#hora = threading.Thread(target=self.tick)
		self.conmysql= mysqlconn()

		dato=self.conmysql.myselect(1)
		print(dato[0][2])


		self.Njugadores=int(input("ingrese el numero de jugadores: "))
		aceptar.daemon = True
		aceptar.start()
		#procesar.daemon = True
		#procesar.start()

		#hora.daemon = True
		#hora.start()

		portc=int(input("Puerto Cliente Servidor 1: "))###
		self.c = Cliente(host,portc)####


		while True:  #ciclo infinito para que pueda enviar mensajes a todos los clientes
			msg = input()
			#cambiar_hora=msg.split(',')
			#cli=self.clientes[int(cambiar_hora[0])]
			#self.msg_to_c(cambiar_hora[1],cli)
			#self.msg_to_all(msg)
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
			global Horas,Min,Seg, Fecha
			if(Horas==24 and Min==59 and Seg==59):
				Horas=0
				Min=0
				Seg=0
			if(Min==59 and Seg==59):
				Horas+=1
				Min=0
				Seg=0
			if(Seg==59):
				Min+=1
				Seg=0
			hora_aleatoria = str(Horas)+":"+str(Min)+":"+str(Seg)
			hora_fecha_converted = datetime.strptime(Fecha + ' ' + hora_aleatoria, "%Y-%m-%d %H:%M:%S")
			if self.time1 == "":
				self.time1 = datetime.strptime(str(hora_fecha_converted), "%Y-%m-%d %H:%M:%S")
			else:
				#self.time1 = synchronizeTime(self.time1, '13.84.128.25', 10000)
				self.time1 = synchronizeTime(self.time1, '127.0.0.1', 60000)

				
			#print('Nueva hora: ' + str(self.time1))
			time.sleep(1)
			Seg+=1
			
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
				if(len(self.Cserver)==0):
					hilo_Cserver=threading.Thread(name="Server",target=self.procesarServer, args=(conn,))
					self.Cserver.append(conn)
					hilo_Cserver.daemon=True
					hilo_Cserver.start()
				else:
					e = threading.Event()
					hilo_Cjugador=threading.Thread(name=str(self.Cjugadores),target=self.procesarCon, args=(conn,e))
					self.Hclient.append(hilo_Cjugador)
					self.event.append(e)
					self.name.append(self.Cjugadores)
					self.Cjugadores+=1
					self.clientes.append(conn)   #agrega al cliente a la lista de cleintes
					self.c.send_msg1(self.Cjugadores)###
				self.ip.append(addr)		 #agrega la ip de el cleinte a la lista de ips
				# print(self.clientes)
			except: 
				pass
			if(self.Cjugadores==self.Njugadores):
				for h in self.Hclient:
					h.daemon = True
					h.start()
				cont=0
				for c in self.clientes:
					c.sendall(str.encode(str(self.name[cont])))
					cont+=1
				self.Cjugadores+=1  ##solo para que la condicion if se haga 1 vez

	def procesarCon(self,c,e):	 # funcion que es el demonio que procesa a los clientes
		name=int(threading.currentThread().getName()) 
		time.sleep(0.2)
		print("ProcesarCon iniciado: ",name)
		if(name==0):
			e.set() #nitifica al evento de el jugador 1 que puede pasar
		while True:
			# self.veric_client()
			event_is_set = e.wait()  ##espera  a que le notifiquen que puede pasar
			c.sendall(str.encode("1")) ##cuando envia 1  al cliente, para que sepa cuando avanzar el cronometro, yo boton aceptar sepa que puede enviar mensaje 
			try:
				data = c.recv(1024).decode()  #recibe el mensaje de el cleiente y la hora de el cliente
				if (data!=""):
					data=data.split(',')
					mensaje=str(data[0])
					horaC=str(data[1])
					index=self.clientes.index(c)
					ip=str(self.ip[index][0]) #calcula la ip de el cliente, no se si hay una forma mas facil, pero asi se me ocurrio
					print("=============== Cliente: ",ip,"\nMensaje: ",mensaje," A las: ",horaC)  #imprime la ip de el cliente, su mensaje , y su hora de el cliente
					self.c.send_msg(mensaje,horaC,ip) #le manda el mensaje que recibio al otro server####
					print()
					#self.conmysql.myinsert(ip,mensaje,horaC,self.time1)  #manda a la funcion de mysql, los datod que quieres guardar en la base
					self.turno+=1
					if(self.turno==self.Njugadores):
						self.turno=0
					e.clear() #despues de que proceso su mensaje bloquea al jugador para que no pueda tirar
					if(self.turno in self.name):
						index=self.name.index(self.turno)
						self.event[index].set() #notifica al evento de el jugador que es su turno y para poder acanzar,(desbloquea el hilo evento)
			except:
				pass

	def procesarServer(self,c):	 # funcion que es el demonio que procesa a los clientes Servidores
		print("procesarServer iniciado: ")
		while True:
			try:
				data = c.recv(1024).decode()  #recibe el mensaje de el cliente y la hora de el cliente
				if (data!=""):
					data=data.split(',')
					if(int(data[0])==1):
						self.Cjugadores=int(data[1])
					else:
						mensaje=str(data[1])
						horaC=str(data[2])
						ip=str(data[3])	
						print("Servidor: ",ip,"\nMensaje: ",mensaje," A las: ",horaC)
						print()
						self.turno+=1
						if(self.turno==self.Njugadores):
							self.turno=0

						if(self.turno in self.name):
							index=self.name.index(self.turno)
							self.event[index].set()
						#self.conmysql.myinsert(ip,mensaje,horaC,self.time1)  #manda a la funcion de mysql, los datod que quieres guardar en la base
			except:
				pass



# HOST="192.168.100.130"
HOST="127.0.0.1"
PORT=int(input("Puerto Servidor 1: "))

# variables para la hora random
Horas=random.randint(0,24)
Min=random.randint(0,59)
Seg=random.randint(0,59)
Fecha = datetime.today().strftime('%Y-%m-%d') # Se agrega fecha del sistema
# enviamos a la clase server el host y el puerto
s = Servidor(HOST,PORT)

