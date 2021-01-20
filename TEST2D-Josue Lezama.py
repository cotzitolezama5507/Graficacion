"""
@author Josue Lezama
@date 14/Diciembre/2020
Examen TEST2D
Si el ultimo de tu digito es par
Numero de control: 18390742
"""


import matplotlib.pyplot as plt
import numpy as np
import math as mt
#Mis dimensiones y mi titulo
plt.axis("on")
plt.axis([0,100,0,100])
plt.title("TEST")
#Radio del circuclo basado en el numero de control SIN MULTIPLICAR
NumControl=2
PenultimoNumControl=4
#Mi radio= numero de control multiplicado por 5
r=NumControl*5
#Valores profe Rz,Sy,Sx
Rz=PenultimoNumControl*6
Sx=NumControl/5
Sy=PenultimoNumControl/5
#Mi punto inicial
xc=40
yc=40
Rz=(xc,yc)
alpha1=mt.radians(1)
alpha2=mt.radians(360)
dalpha=mt.radians(1)
#Punto del circulo
plt.scatter(xc,yc,s=1,color=(7/10, 4/10, 2/10))
print (np.arange(alpha1,alpha2,dalpha))
for alpha in np.arange(alpha1,alpha2,dalpha):
    x=xc+r*mt.sin(alpha)
    y=yc+r*mt.cos(alpha)
    plt.scatter(x,y,s=1,color=(7/10, 4/10, 2/10))

#ORIGINAL FIGURE1 IN THE POINT LEFT
x1=xc
x2=5
y1=yc
y2=5

#DRAWE FIGURE
plt.plot([x1,x1],[y1,y2],linewidth=1,color=(7/10, 4/10, 2/10))
plt.plot([x2,x2],[y1,y2],linewidth=1,color=(7/10, 4/10, 2/10))
plt.plot([x1,x2],[y1,y1],linewidth=1,color=(7/10, 4/10, 2/10))
plt.plot([x1,x2],[y2,y2],linewidth=1,color=(7/10, 4/10, 2/10))

#ORIGINAL FIGURE2 AROUND OF THE CIRCLE
#Con escalado u.u usando Sy y Sx xd

xx1=x1+(x1*(Sx+0.1))
xx2=x2+15
yy1=y1+ (y1*(Sx+0.1))
yy2=y2+15

#DRAWE FIGURE
plt.plot([xx1,xx1],[yy1,yy2],linewidth=1,color=(7/10, 4/10, 2/10))
plt.plot([xx2,xx2],[yy1,yy2],linewidth=1,color=(7/10, 4/10, 2/10))
plt.plot([xx1,xx2],[yy1,yy1],linewidth=1,color=(7/10, 4/10, 2/10))
plt.plot([xx1,xx2],[yy2,yy2],linewidth=1,color=(7/10, 4/10, 2/10))


plt.show()