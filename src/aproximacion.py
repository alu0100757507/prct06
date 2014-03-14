#!/usr/bin/python
def aproximacion(n):
   suma=0.0
   for i in range(1,n+1):
      x_i=(i-1.0/2)/float(n)
      fx_i=4.0/(1+x_i**2)
      suma=suma + fx_i
   pi=(1.0/n)*suma
   return pi


n=int(raw_input('Introduzca un numero n>0: '))
pi=aproximacion(n)
print pi