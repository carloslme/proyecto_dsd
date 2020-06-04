import sys
from tkinter import *
from tkinter import messagebox
import socket
import threading
import pickle
import random
import time


HOST="127.0.0.1"
PORT=int(input("Puerto: "))

#HOSTS="127.0.0.1"
#PORTS=5000


time1 = ''
timerC= 0
Horas=random.randint(0,24)
Min=random.randint(0,59)
Seg=random.randint(0,59)
play=-1
turno=0

class Cliente():
	"""docstring for Cliente"""
	#def __init__(self, host="localhost", port=4000):
	def __init__(self,host,port):
		global play

		self.Jerarquia_servers=[]
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((str(host), int(port)))
		except Exception as e:
			print('Excepción: ', e)
			
		print("\nEspere a que lleguen todos los jugadores")

		while play==-1:
			data = self.sock.recv(4096).decode()
			print("player: ",data)
			play=int(data)

		data = self.sock.recv(4096)
		self.Jerarquia_servers=pickle.loads(data)
		print("Jerarquia_servers:",self.Jerarquia_servers)

		recv = threading.Thread(target=self.msg_recv)
		recv.daemon = True
		recv.start() 

	def msg_recv(self):
		global turno,play,HOSTS,PORTS
		while True:
			try:
				data = self.sock.recv(4096).decode()
				if(data):
					turno=int(data)
				else:
					print("Se perdio la conexion con el server, reconectando a otro...")
					self.reconexion()
			except socket.error:
				print('############## Se perdio la conexion con el server')
				self.reconexion()
				pass
			except:
				pass

	def reconexion(self):
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

	def send_msg(self, msg,hora):
		global turno
		mensaje=msg+","+hora
		self.sock.sendall(str.encode(mensaje))
		turno=0
		print()



#def disable(event=None):
#	pass

#HOST="192.168.100.130"
c = Cliente(HOST,PORT)

shell=Tk()
shell.title("Jugador: "+str(play+1))
shell.geometry('310x180')
#shell.protocol('WM_DELETE_WINDOW',disable)

letra = Label(shell, text='Ingrese una letra',font=(30))
letra.place(x=10,y=5)
Sletra=StringVar() 
letraE=Entry(shell, width="5",textvariable =Sletra)
letraE.place(x=10,y=30)

frase = Label(shell, text='Ingrese la frase a mandar',font=(30))
frase.place(x=10,y=50)
fraseE=Entry(shell, width="30")
fraseE.place(x=10,y=70)

horario= Label(shell, text='Hora',font=(40))
horario.place(x=10,y=95)

hora=Label(shell, bg='#3C3B37', fg='white', bd=0 ,font=(40))
hora.pack(fill=BOTH, expand=1)
hora.place(x=10,y=115)

timer=Label(shell, bg='#3C3B37', fg='white', bd=0 ,font=(40), width="5")
timer.pack(fill=BOTH, expand=1)
timer.place(x=220,y=10)

	
Aceptar=Button(shell,text="Enviar", command=lambda: Aceptar(letraE.get(),fraseE.get()))
Aceptar.place(x=200,y=115)


def Aceptar(letra,frase):
	global timerC,turno
	time.sleep(0.1)
	if(letra!='' and frase==''):
		if(turno==1):
			c.send_msg(letra,time1)
			messagebox.showinfo("AYE","Letra enviada a las: "+time1)
			letraE.delete('0',END)
			turno=0
		else:
			messagebox.showinfo("AYE","No es tu turno")
	elif(letra=='' and frase!=''):
		if(turno==1):
			c.send_msg(frase,time1)
			messagebox.showinfo("AYE","Frase enviada a las: "+time1)
			turno=0
			fraseE.delete('0',END)
		else:
			messagebox.showinfo("AYE","No es tu turno")
	elif(letra=='' and frase==''):
		if(turno==1):
			c.send_msg("N/D",time1)
			messagebox.showinfo("AYE","No enviaste nada: "+time1)
			letraE.delete('0',END)
			turno=0
		else:
			messagebox.showinfo("AYE","No es tu turno")

	timerC=0

####esta toma una hora aleatorea
def tick():
    global time1,Horas,Min,Seg
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
	if(turno==1):
		timerC+=1


def limitador(Sletra):
    if (len(Sletra.get()) > 0):
        #donde esta el :5 limitas la cantidad d caracteres
        Sletra.set(Sletra.get()[:1])



###ESTA TOMA la hora de la pc
def tick2():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        hora.config(text=time2)
    hora.after(200, tick2)

#recv = threading.Thread(target=c.msg_recv)

#recv.daemon = True
#recv.start() 

tick() ##invoqua la funcion de la hora aleatorea
cronometro() #Invoque la funcion de el cronometro
Sletra.trace("w", lambda *args: limitador(Sletra)) ##llama ala funcion que limita que solo se meta un caracter en ingresa una letra
shell.mainloop()
