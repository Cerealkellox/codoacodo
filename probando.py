lista=[]
lista=list()

lista=["hola","1.4",[10, 20, 30],False,78]

var1=lista[0]
var2=lista[4]
var3=lista[3]

print(f"los tipos: \nvar1 es {type(var1)} \nvar2 es {type(var2)} \nvar3 es {type(var3)}")

print(f"los tipos: \nvar1 es {type(var1)}:{var1}\nvar2 es {type(var2)}:{var2}\nvar3 es {type(var3)}:{var3}")

numeros=[3,5,8.3,90,21,1]
frutas=["manzana", "anana", "uva", "frutilla"]

print(frutas)
print(numeros)

frutas.sort()
numeros.sort()

print(frutas)
print(numeros)

frutas.sort(reverse=True)
numeros.sort(reverse=True)

print(frutas)
print(numeros)

tupla=()
tupla=tuple()

tupla=("hola", 1.4,78,[10,20,30],False,78)

tupla="hola", 1.4,78,[10,20,30],False,78

tupla=tuple("hola")

tupla=tuple(range(5))

no_tupla=(3-4)
no_tupla=("hola")

tupla=("hola",)
tupla=(3-4,)

tupla=1,"python", True,(1,2),list("abcd")

print(tupla)

tupla=5,"python", True,(1,2), list("abc")

print(tupla)

lista=list("abcd")
tupla=1, "python", True, (1,2), lista

print(tupla)

lista[0]="E"
print(tupla)