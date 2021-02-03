"""
Josue Israel Lezama Canul
Examen Complementario 3D 03/02/2021
18390742
"""

import numpy as np
import matplotlib.pyplot as plt
#import functions tools3D

from math import ceil
from tkinter import *
from pynput import keyboard as kb 
from time import sleep
#Tiene que descargarlo pip install pynput
#Nombre de los ejes X y Y
plt.xlabel('Eje x')
plt.ylabel('Eje Y')
#Cordenadas iniciales 
xg=[]
yg=[]
zg=[]
#   Puinto centro
xc = 80;    yc = 40;    zc = 40
#Crear funcion para el cerrado de la terminal

def plotPlaneLine(xg,yg,zg):
    plt.axis([80,250,120,20])
    plt.axis()
    plt.grid()
    # Ploteo del plano usando los vevctores xg, yg, zg
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='BLUE')
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='BLUE')
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='BLUE')
    # Punto 3 
    plt.scatter(xg[3],yg[3],s=20,color='r')
    #Ploteo de la interseccion de los planos
    plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='PURPLE',linestyle=':')
    plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='PURPLE',linestyle=':')
    plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='PURPLE',linestyle=':')

    plt.show()


def hitPoint(x,y,z):
    # Distancia del punto con las coordenadas (0,1)
    """Union de los componentes de los vectores con los puntos(4,5)
    XAlfa = a/Q45
    yAlfa = b/Q45
    zAlfa = c/Q45"""

    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    Q01=np.sqrt(a*a+b*b+c*c)

    #Dustancia del punto con las coordenadas(1,2)
    a=x[2]-x[1]
    b=y[2]-y[1]
    c=z[2]-z[1]
    Q12=np.sqrt(a*a+b*b+c*c)
    """Union de los componentes de los vectores con los puntos(0,3)
    ux = a/Q03
    uy = b/Q03
    uz = c/Q03"""
    #Distancia del punto(0,2)
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    Q1=np.sqrt(a*a+b*b+c*c)
    
    #Tercer punto del triangulo
    #Distancia del punto(1,3)
    a=x[3]-x[1]
    b=y[3]-y[1]
    c=z[3]-z[1]
    Q2=np.sqrt(a*a+b*b+c*c)
    #Distancia del punto (2,3)
    a=x[2]-x[3]
    b=y[2]-y[3]
    c=z[2]-z[3]
    Q3=np.sqrt(a*a+b*b+c*c)
    #Distancia del punto (0,3)
    a=x[0]-x[3]
    b=y[0]-y[3]
    c=z[0]-z[3]
    Q4=np.sqrt(a*a+b*b+c*c)
    #Area del triangulo A de las diapositivas
    s=(Q01+Q12+Q1)/2
    A=np.sqrt(s*(s-Q01)*(s-Q12)*(s-Q1))
    #Area del triangulo A1 de las diapositivas
    s1=(Q01+Q4+Q2)/2
    A1=np.sqrt(s1*(s1-Q01)*(s1-Q4)*(s1-Q2))
    #Area del triangulo A2 de las diapositivas
    s2=(Q1+Q3+Q4)/2
    A2=np.sqrt(s2*(s2-Q1)*(s2-Q3)*(s2-Q4))


    return A,A1,A2
    

def plotLineaTriangulo(xc,yc,zc):
    

    [A,A1,A2]=hitPoint(x,y,z)

    #ploteo de textos A,A1,A2,A1+A2,In,ola
    if((A1+A2)>A):
        plt.text(180,80,'HOLA')
        plt.text(180,85,'Exterior del hoyo')
    elif((A1+A2)<A):
        plt.text(180,80,'IN')
        plt.text(180,85,'Interior del hoyo')
    A=ceil(A)
    A1=ceil(A1)
    A2=ceil(A2)
    A3=ceil(A1+A2)
    plt.text(100,100,'A=',color='PURPLE')
    plt.text(105,100,A,color='PURPLE')
    plt.text(80,60,'A1=',color='BLUE')
    plt.text(90,60,A1,color='BLUE')
    plt.text(160,100,'A2=',color='BLUE')
    plt.text(170,100,A2,color='BLUE')
    if((A1+A2)>A):
        plt.text(180,75,'A1+A2=',color=(.5,.2,.8))
        plt.text(200,75,A3,color=(.5,.2,.8))
    elif((A1+A2)<A):
        plt.text(180,75,'A1+A2=',color='BLUE')
        plt.text(200,75,A3,color='BLUE')

    plotPlaneLine(xg,yg,zg)

#plotSquareLinex(xc,yc,zc)
#Ploteo de figura


#Lectura del teclado
def suelta(tecla):
	if tecla == kb.KeyCode.from_char('ESCAPE'):
            
		return False

#Lo de la lectura de teclado, no supe como implementarlo dentro del while, aun que tuve varias ideas pero todas me daban un ciclo infinito, o si no me daban error :/
i2=0
while i2==0:
    #   Coordenadas del sistema local. este plato z no tiene profundidad :(
    #F

    x=[40,30,80,0]
    y=[60,10,60,0]
    z=[0,0,0,0]
    root=Tk()

    HITPOINTX=input('Cual es el punto en X? Escriba o pulse ESC para salir: ')  
  
    if HITPOINTX=='ESC':
        i2=1
        break
    else:
        x[3]=int(HITPOINTX)
        HITPOINTY=input('Cual es el punto en Y?: Escriva o Pulse ESC para salir: ')
        if HITPOINTY=='ESC':
            i2=1
            FALSE
            break

        else:
            y[3]=int(HITPOINTY)

            for i in range(len(x)):
                xg.append( x[i]+xc )
                yg.append( y[i]+yc )
                zg.append( z[i]+zc )
                i2=0
            plotLineaTriangulo(xc,yc,zc)

        

        break  


   

