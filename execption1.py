# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
x = float(input("enter x: "))
y = math.sqrt(x)

print("La raiz cuadrada root of",x,"igual to", y)

#######################################################

pnun = int(input("Ingrese el primer numero"))
snun = int(input("Ingrese el segundo numero"))

if snun != 0:
    print(pnun/snun) 
    
else:
    print("This operation canon be dame")
    
print("End")

######################################################

try:
    print("1")
    x = 1/0
    print("2")
    
except:
    print("oh, dear")
    
print("3")

###############################################

try:
    x = int(input("Ingrese un numero:"))
    y = 1/0
    print(y)
    
except ZeroDivisionError:
    print("you must enter an inter value")
    
except ValueError:
    print("You must enter an integer value")
    
except:
    print("oh, dear somethin went...")
print("THE END")
 

    
    
    
    
    
    
    
    