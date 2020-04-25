#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      andela
#
# Created:     25.04.2020
# Copyright:   (c) andela 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import likovi as l
import math
def main():
    pass

if __name__ == '__main__':
    main()

def opseg(objekt):
    if isinstance(objekt, l.Kruznica)==True:
        return 2*objekt.radijus*math.pi
    else:
        return 4*objekt.duljina

def povrsina(objekt):
    if isinstance(objekt, l.Kruznica)==True:
        return objekt.radijus*objekt.radijus*math.pi
    else:
        return objekt.duljina*objekt.duljina

print('*** test funkcije ***')
print(opseg.__name__)
print(povrsina.__name__)

