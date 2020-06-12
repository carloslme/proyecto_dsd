from django.shortcuts import render
from django.http import HttpResponse
from coordinador.manager import Servidor
import threading
import multiprocessing
import locale
from datetime import datetime
from dateutil import parser

PROGRESO_FRASE = ''
s = Servidor('',5000)
# image = "/static/images/hang0.gif"
flag = False
time = 1000

def index(request):
  
    # print('--------------------------- s.time1', s.time1)
    print('--------------------------- s.turno:', s.turno+1)
    print('--------------------------- s.frase:', s.frase)
    print('--------------------------- s.end:', s.end)
    
    if s.end == True or s.end == 1:
        global time 
        time = 60000
        print('================== TIEMPO CAMBIADO ==================')
    
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    

    image = "/static/images/hang" + str(10-s.errores) + ".gif"
    return render(request, 'index.html', {'pelicula': s.pelicula.upper(), 
                                          'frase':s.progresoS.upper(), 
                                          'image': image, 
                                          'status': s.end,
                                          'errors': s.errores,
                                          'player': s.turno+1,
                                          'phrase': s.frase.upper(),
                                          'timer': datetime.strftime(s.time1, "%A, %d de %B de %Y \n %H:%M:%S"),
                                          'time': time})

def execute_server(request):
    server = threading.Thread(target=execute_thread)
    server.daemon = True
    server.start()
    import coordinador.manager as m
    return render(request, 'index.html', {'pelicula': m.PELICULA.upper(), 'frase':m.PROGRESO.upper()})
    
def execute_thread():
    s =  Servidor('',5000)
    print('--------------------------- s.frase', s.frase)


# enviamos a la clase server el host y el puerto
# s = Servidor(HOST,PORT)
# s.turno
# s.errores