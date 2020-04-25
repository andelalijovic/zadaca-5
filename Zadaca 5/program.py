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
import funkcije

def main():
    pass

if __name__ == '__main__':
    main()
k1=l.Kruznica(3)
k2=l.Kvadrat(5)

print('*** test program ***')
print(k1, 'opsega', funkcije.opseg(k1), 'povrsine', funkcije.povrsina(k1))
print(k2, 'opsega', funkcije.opseg(k2), 'povrsine', funkcije.povrsina(k2))