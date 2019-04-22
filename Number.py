#!/usr/bin/python3
#This program is written by Qi ZhenHua!
#Description: for simple math calculating. 2019/04/22
#Usage: pass
#code is below.

class PositiveInteger(int):

    def __init__(self):
        pass

    def factorization(self,mynumber):
        factorlist=[]
        for i in range(1,mynumber):
            if mynumber%i==0:
                factorlist.append(i)
        return factorlist[1:]

    def primenumber(self,mynumber):
        primelist=[]
        for i in range(1,mynumber):
            if self.factorization(i)==[]:
                primelist.append(i)
        return primelist[1:]

a=PositiveInteger()
b=int(input("Input a positive integer: "))
print(a.factorization(b))
print(a.primenumber(b))


#if you want to make it as a module, remove below code's #
#def main():
#
#if __name__=="__main__":
#    main()

