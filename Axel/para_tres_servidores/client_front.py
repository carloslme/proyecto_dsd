import sys
from tkinter import *
from tkinter import messagebox
import socket
import threading
import pickle
import random
import time
import re

HOSTCFront="70.37.61.169"
#HOSTCFront="104.44.136.187"
#HOSTCFront="127.0.0.1"
HOSTFront="127.0.0.1"
PORTFront=int(input("Puerto Servidor: "))
HOST="127.0.0.1"
PORT=PORTFront

time1 = ''
timerC= 0
Horas=random.randint(0,24)
Min=random.randint(0,59)
Seg=random.randint(0,59)
play=-1
turno=0

#########################################
#front
#########################################
class ClienteFront():
	"""docstring for Cliente"""
	#def __init__(self, host="localhost", port=4000):
	def __init__(self,host,port):
		self.Jerarquia_servers=[]
		#self.play=-1
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((str(host), int(port)))
		except Exception as e:
			print('Excepción: ', e)
			
		print("\nEspere a que lleguen todos los jugadores")


	def Rnumero_jugador(self):
		global play
		while play==-1:
			data = self.sock.recv(4096).decode()
			print("player: ",data)
			play=int(data)
			return play

	def Rjerarquia_servers(self):
		data = self.sock.recv(4096)
		self.Jerarquia_servers=pickle.loads(data)
		print("Jerarquia_servers:",self.Jerarquia_servers)
		return self.Jerarquia_servers


	def msg_recv(self):
		global turno
		while True:
			try:
				data = self.sock.recv(4096).decode()
				if(data):
					turno=int(data)
				else:
					print("Se perdio la conexion con el server, reconectando a otro...")
					self.reconexion()
			#except socket.error:
			#	print('############## Se perdio la conexion con el server')
			#	self.reconexion()
			except:
				pass

	def reconexion(self):
		global play
		for rec in self.Jerarquia_servers:
			try:
				self.sock.close() 
				time.sleep(0.1)
				self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				self.sock.connect((rec[0],rec[1]))
				self.sock.sendall(str.encode(str(play)))
				print("conectado al nuevo")
				break
			except Exception as e:
				print("Servidor: ",rec,"no disponible")

	def send_msg(self, msg):
		global turno
		self.sock.sendall(msg)
		time.sleep(0.2)
		turno=0
		print()

class Servidor():
	"""docstring for Servidor"""
	def __init__(self, host, port):
	# def __init__(self, host="10.100.71.107", port=4000):

		self.clientes = [] #lista de clientes
		self.ip = [] #lista de ips de los clientes

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((str(host), int(port)))
		self.sock.listen(10)
		self.sock.setblocking(False)

		self.numero_jugador=-1
		self.Jerarquia_servers=[]

		aceptar = threading.Thread(target=self.aceptarCon)   #demonio o proceso de aceptar conecciones
		
		aceptar.daemon = True
		aceptar.start()

		portc=int(input("Puerto: "))
		self.c = ClienteFront(HOSTCFront,portc)

		self.numero_jugador=str(self.c.Rnumero_jugador())
		self.Jerarquia_servers=self.c.Rjerarquia_servers()

		recvC = threading.Thread(target=self.c.msg_recv)
		recvC.daemon = True
		recvC.start() 
			
	def aceptarCon(self):   #funcion que es el demonio que acepta a los clientes 
		print("aceptarCon iniciado")
		while True:
			try:
				conn, addr = self.sock.accept()
				conn.setblocking(False)
				print(conn)
				self.clientes.append(conn)   #agrega al cliente a la lista de cleintes
				self.ip.append(addr)		 #agrega la ip de el cleinte a la lista de ips
				#hilo_cliente=threading.Thread(name="jugador",target=self.sendCon, args=(conn,))
				#hilo_cliente.daemon=True
				#hilo_cliente.start()

				hilo_clienterecv=threading.Thread(name="jugadorrecv",target=self.rcvCon, args=(conn,))
				hilo_clienterecv.daemon=True
				hilo_clienterecv.start()
				break
			except:
				pass

	def sendCon(self,c):	 # funcion que es el demonio que procesa a los clientes
		global turno
		while self.numero_jugador==-1:
			pass
		c.sendall(str.encode(self.numero_jugador))
		print("turno:",turno)
		while True:
			print("turno:",turno)
			try:
				c.sendall(str.encode(str(turno)))
				time.sleep(0.1)
			except socket.error:
				print('############## Se perdio la conexion con el cliente')
				break
			except:
				pass

	def rcvCon(self,c):	 # funcion que es el demonio que procesa a los clientes
		global turno
		while True:
			try:
				data=c.recv(4024)
				self.c.send_msg(data)
			except:
				pass



# enviamos a la clase server el host y el puerto
s = Servidor(HOSTFront,PORTFront)
#######################################################
#Cliente
#######################################################
class Cliente():
	"""docstring for Cliente"""
	#def __init__(self, host="localhost", port=4000):
	def __init__(self,host,port):
		global play
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((str(host), int(port)))
		except Exception as e:
			print('Excepción: ', e)
			
		#print("\nEspere a que lleguen todos los jugadores")

		#while play==-1:
		#	data = self.sock.recv(4096).decode()
		#	print("player: ",data)
		#	play=int(data)

		#recv = threading.Thread(target=self.msg_recv)
		#recv.daemon = True
		#recv.start() 

	#def msg_recv(self):
	#	global turno,play,HOSTS,PORTS
	#	while True:
	#		try:
	#			data = self.sock.recv(4096).decode()
	#			if(data):
	#				turno=int(data)
	#			else:
	#				#print("Se perdio la conexion con el server")
	#				print()
	#		except socket.error:
	#			#print('############## Se perdio la conexion con el server')
	#			print()
	#		except:
	#			pass
	#		time.sleep(0.2)

	def send_msg(self, msg,hora):
		global turno
		mensaje=msg+","+hora
		self.sock.sendall(str.encode(mensaje))
		turno=0
		print()


c = Cliente(HOST,PORT)

shell=Tk()
shell.title("Jugador: "+str(play+1))
shell.geometry('310x210')
#shell.protocol('WM_DELETE_WINDOW',disable)

letra = Label(shell, text='Ingrese una letra',font=(30))
letra.place(x=10,y=5)
Sletra=StringVar() 
letraE=Entry(shell, width="5",textvariable =Sletra)
letraE.place(x=10,y=30)

frase = Label(shell, text='Ingrese la frase a mandar',font=(30))
frase.place(x=10,y=50)
SletraF=StringVar() 
fraseE=Entry(shell, width="30",textvariable =SletraF)
fraseE.place(x=10,y=70)

Chora = Label(shell, text='Cambia la hora',font=(30))
Chora.place(x=10,y=95)
ChoraE=Entry(shell, width="15")
ChoraE.place(x=10,y=115)

horario= Label(shell, text='Hora',font=(40))
horario.place(x=10,y=140)

hora=Label(shell, bg='#3C3B37', fg='white', bd=0 ,font=(40))
hora.pack(fill=BOTH, expand=1)
hora.place(x=10,y=160)

timer=Label(shell, bg='#3C3B37', fg='white', bd=0 ,font=(40), width="5")
timer.pack(fill=BOTH, expand=1)
timer.place(x=220,y=10)

	
Aceptar=Button(shell,text="Enviar", command=lambda: Aceptar(letraE.get(),fraseE.get()))
Aceptar.place(x=200,y=160)

ChoraB=Button(shell,text="Cambiar", command=lambda: Cambiar(ChoraE.get()))
ChoraB.place(x=150,y=115)


def Aceptar(letra,frase):
	global timerC,turno
	time.sleep(0.1)
	if(letra!='' and frase==''):
		if(turno!=0):
			c.send_msg(letra,time1)
			messagebox.showinfo("AYE","Letra enviada a las: "+time1)
			letraE.delete('0',END)
			#turno=0
		else:
			messagebox.showinfo("AYE","No es tu turno")
	elif(letra=='' and frase!=''):
		if(turno!=0):
			c.send_msg(frase,time1)
			messagebox.showinfo("AYE","Frase enviada a las: "+time1)
			#turno=0
			fraseE.delete('0',END)
		else:
			messagebox.showinfo("AYE","No es tu turno")
	elif(letra=='' and frase==''):
		if(turno!=0):
			c.send_msg("N/D",time1)
			messagebox.showinfo("AYE","No enviaste nada: "+time1)
			letraE.delete('0',END)
			#turno=0
		else:
			messagebox.showinfo("AYE","No es tu turno")

	timerC=0

def Cambiar(hora):
	global time1,Horas,Min,Seg
	try:
		horaN=hora.split(':')
		if(int(horaN[0])<25 and int(horaN[1])<60 and int(horaN[2])<60):
			Horas=int(horaN[0])
			Min=int(horaN[1])
			Seg=int(horaN[2])
			time1=horaN
			ChoraE.delete('0',END)
		else:
			messagebox.showinfo("AYE","Hora incorrecta")
	except:
		messagebox.showinfo("AYE","Formato erroneo, ejemplo: 00:00:00")
		ChoraE.delete('0',END)

####esta toma una hora aleatorea
def tick():
    global time1,Horas,Min,Seg,turno
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
    time1= str(Horas)+":"+str(Min)+":"+str(Seg)
    hora.config(text=time1)
    hora.after(1000, tick)
    Seg+=1

def cronometro():
	global timerC,turno
	if(timerC>20):
		Aceptar(letraE.get(),fraseE.get()) ##si se acaba el tiempo se ejecuta el boton aceptar
		messagebox.showinfo("AYE","Se acabo el timepo, pero se envio lo escrito")

	timer.config(text=timerC)
	timer.after(1000, cronometro)
	if(turno!=0):
		timerC+=1


def limitador(Sletra):
    if (len(Sletra.get()) > 0):
        #donde esta el :5 limitas la cantidad d caracteres
        Sletra.set(Sletra.get()[:1])

    #if(Sletra.get().isalpha()==False):
    if(not re.fullmatch(r"[A-Za-z ]+", Sletra.get())):
    	Sletra.set(Sletra.get()[:0])


def limitadadorF(SletraF):
	#re.fullmatch(r"[A-Za-z ]", cadena)
   # if (SletraF.get().isalpha()==False):
    if(not re.fullmatch(r"[A-Za-z ]+", SletraF.get())):
    	tam=len(Sletra.get())
    	SletraF.set(SletraF.get()[:tam-1])

###ESTA TOMA la hora de la pc
def tick2():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        hora.config(text=time2)
    hora.after(200, tick2)


tick() ##invoqua la funcion de la hora aleatorea
cronometro() #Invoque la funcion de el cronometro
Sletra.trace("w", lambda *args: limitador(Sletra)) ##llama ala funcion que limita que solo se meta un caracter en ingresa una letra
SletraF.trace("w", lambda *args: limitadadorF(SletraF))
shell.mainloop()
