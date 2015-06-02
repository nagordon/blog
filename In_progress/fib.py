# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:12:01 2015

@author: Neal
"""
https://timwolverson.wordpress.com/2014/02/08/plot-a-fibonacci-spiral-in-excel/
http://www.dcs.gla.ac.uk/~jhw/spirals/

from math import *
from PIL import Image as I, ImageDraw as D
n=100
G=(1+5**.5)/2
w=int(G**(4*(n//4)))
i=I.new("RGB",(w,w),"white")
d=D.Draw(i)
k=pi/180
d.line([(G**(j/90)*cos(j*k)+w/2,G**(j/90)*sin(j*k)+w/2)for j in range(n*90)],fill=0)
i.save("s.png","PNG")