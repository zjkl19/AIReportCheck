# -*- coding: utf-8 -*-
"""
洪塘大桥
矢高f=15.114
l=150
h=80.107-23.732=56.375
Created on Tue Mar 12 10:12:50 2019

@author: Lindinan
"""
import math
from sympy import  integrate ,cos,sin
from sympy.abc import  a,x,y
#print (integrate(sin(x)/x,(x,-float("inf"),float("inf"))))

h=0;f=9;l=70;

n=f/l;  #矢跨比

S=integrate((1+(-8*f*x/l**2+h/l+4*f/l)**2)**0.5,(x,0,l))
print(float(S))
#S=(l/2)*(1+16*n**2)**0.5+0.125*(l/n)*math.log(4*n+(1+16*n**2)**0.5);
#S=l*(1+8/(3*n^2)-32/(5*n^4));     #有应力索长估算公式

#空缆状态下主缆有应力索长
Ec=2.0*10**11;   #主缆弹性模量(国际单位）
Ac=0.25*3.14*0.10695**2;   #主缆面积（国际单位）

gb=168000;   #加劲梁自重

H=gb*l**2/(8*f);

#deltaS1=(H*l)*(1+(16*n**2/3))/(Ec*Ac);
deltaS1=((H*l)/(Ec*Ac))*integrate(1+(-8*f*x/l**2+h/l+4*f/l)**2,(x,0,l))
S1=S-deltaS1;
print(float(S1))

#无应力索长
gc=8.348*10**4;   #缆索自重
c=l**2/(8*f);
c=69.5058;
Hc=c*gc;    #缆索在自重状态下的水平拉力

deltaS2=Hc*(l+c*math.sinh(l/c))/(2*Ec*Ac);

S0=S-deltaS1-deltaS2;



