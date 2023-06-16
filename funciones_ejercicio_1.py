clientes={}

def sumando(n1,n2):
    resu=n1+n2
    return(resu)

num1=-1
num2=0


while num1!=0:
    num1=int(input("ingrese un numero (0 finaliza):"))
    if num1==0:
        break   
    
    print(sumando(num1,num2))
    num2=num1+num2
    