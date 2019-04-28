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

def factorizationintoprimes(number):
    mylist=factorization(number)
    result=[]
    if mylist != []:
        result.append(mylist[0])
        result=result+factorizationintoprimes(mylist[-1])
    if mylist == []:
        result.append(number)
    return result 
        
def greatestcommonfactor(n1,n2):
    list1=factorization(n1)
    result=0
    for i in list1:
        if n2 % i == 0:
            result=i
    return result 

def leastcommonmultiple(n1,n2):
    bigger=max(n1,n2)
    smaller=min(n1,n2)
    for i in range(1,smaller+1):
        if (i*bigger) % smaller == 0:
            return i*bigger
    return n1*n2

a=int(input("Input a positive integer: "))
b=int(input("input another positive integer: "))

print(factorization(a))
#print(primenumber(b))
print(factorizationintoprimes(a))
print(factorization(b))
print(factorizationintoprimes(b))
print(greatestcommonfactor(a,b))
print(leastcommonmultiple(a,b))

#if you want to make it as a module, remove below code's #
#def main():
#
#if __name__=="__main__":
#    main()

