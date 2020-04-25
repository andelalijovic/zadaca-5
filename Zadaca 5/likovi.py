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

def main():
    pass

if __name__ == '__main__':
    main()
class Kruznica(object):
    def __init__(self,radijus):
        self.radijus=radijus
    def __str__(self):
        return "kruznica radijusa "+'{0:.2f}'.format(float(self.radijus))


class Kvadrat (object):
    def __init__(self,duljina):
        self.duljina=duljina
    def __str__(self):
        return "kvadrat stranice "+'{0:.2f}'.format(float(self.duljina))

print('*** test likovi ***')
kruznica = Kruznica(3)
kvadrat = Kvadrat(4.5)
print(kruznica)
print(kvadrat)