#!/usr/bin/python3
#This program is written by Qi ZhenHua!
#Description: for simple math calculating. 2019/04/22
#Usage: pass
#code is below.

def factorization(number):
    factorlist=[]
    for i in range(1,number):
        if number%i==0:
            factorlist.append(i)
    return factorlist[1:]

def primenumber(number):
    primelist=[]
    for i in range(1,number):
        if factorization(i)==[]:
            primelist.append(i)
    return primelist[1:]

def factorizationintoprimes(number,factorlist=[]):
    mylist=factorization(number)
    if mylist != []:
        factorlist.append(mylist[0])
        factorizationintoprimes(mylist[-1],factorlist)
    if mylist ==[]:
        factorlist.append(number)

    return factorlist 
        

b=int(input("Input a positive integer: "))

print(factorization(b))
print(primenumber(b))
print(factorizationintoprimes(b))


#if you want to make it as a module, remove below code's #
#def main():
#
#if __name__=="__main__":
#    main()

