from django.shortcuts import render
from django.http import HttpResponse
from coordinador.sustituto_1 import Servidor
import threading
import multiprocessing
import locale
from datetime import datetime
from dateutil import parser

PROGRESO_FRASE = ''
s = Servidor('',6000)
# image = "/static/images/hang0.gif"
flag = False
time = 1000

def index(request):
  
    # print('--------------------------- s.time1', s.time1)
    print('--------------------arya------- s.turno:', s.turno+1)
    print('--------------------------- s.frase:', s.frase)
    print('--------------------------- s.end:', s.end)
    
    if(s.end == 1):
        global time 
        time = 60000
        print('================== TIEMPO CAMBIADO ==================')
    
    #locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    

    image = "/static/images/hang" + str(10-s.errores) + ".gif"
    return render(request, 'index.html', {'pelicula': s.pelicula.upper(), 
                                          'frase':s.progresoS.upper(), 
                                          'image': image, 
                                          'status': s.end,
                                          'errors': s.errores,
                                          'player': s.Pganador,
                                          'phrase': s.frase.upper(),
                                          'timer': datetime.strftime(s.time1, "%A, %B %d %Y \n %H:%M:%S"),
                                          'time': time})




# enviamos a la clase server el host y el puerto
# s = Servidor(HOST,PORT)
# s.turno
# s.errores