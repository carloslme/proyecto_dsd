import pymysql
import socket
import datetime

HOSTMYSQL="localhost"
USERMYSQL="root"
PASSWORDMYSQL="1234"
DBMYSQL="dbservertime"
	
# Funcion que conecta a la base de datos y registra un registro en la base
def mysqlconn(ip,puerto, hora_enviada):
	try:
		connection = pymysql.connect(   
			host="localhost",
			user="root",   #modificar tu usuario
			password="1234", # poner tu contraseña
			db="dbservertime"  #el nombre de la base de datos
			)
		cursor = connection.cursor()
		sql= "INSERT INTO data(ip,puerto,hora_enviada) VALUES(%s, %s, %s)"
		cursor.execute(sql, (ip,puerto, hora_enviada))
		connection.commit()
		connection.close()
	except Exception as e:
		print(str(e))
		pass
	

# function used to initiate the Clock Server
def initiateClockServer():

	s = socket.socket()
	print("Socket successfully created")

	# Server port
<<<<<<< HEAD
<<<<<<< HEAD
	port = 5000
=======
	port = 6000
>>>>>>> 34b60189b50c6ac0c6bad177c34d26faa09e5289
=======
	port = 7000
>>>>>>> 49a2fda4aece4ebd1d53cf6302dec825fd609b6e

	s.bind(('', port))

	# Start listening to requests
	s.listen(5)
	print("Socket is listening...")

	# Clock Server Running forever
	while True:
		# Establish connection with client
		connection, address = s.accept()
		print('Server connected to', address, ' --> Time sent ', str(datetime.datetime.now()).encode(), 'Time saved')

		# Respond the client with server clock time
		connection.send(str(datetime.datetime.now()).encode())

		# Data sent is saved
		#mysqlconn(address[0], address[1], str(datetime.datetime.now()).encode())

		# Close the connection with the client process
		connection.close()

# Driver function   
if __name__ == '__main__':

	# Trigger the Clock Server
	initiateClockServer()