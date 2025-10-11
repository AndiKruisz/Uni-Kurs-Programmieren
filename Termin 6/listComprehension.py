##liste=[ausdruck for x (alternativ _) in range(0,10)]
##siehe https://www.w3schools.com/python/python_lists_comprehension.asp

##funktioniert auch mit Sets (geschwungene statt eckige klammern)
##für tuples kann eine liste an tuple() übergeben werden


##liste mit 10 mal der zahl 10
werte=[10 for _ in range(0,10)]
print(werte)

##liste mit 10 zufallszahlen
import random as rnd
werte=[rnd.randint(1,1000) for _ in range(0,10)]
print(werte)

##liste mit geraden range-werten, sonst 0
werte=[x if x%2==0 else 0 for x in range(1,11)]
print(werte)

##alternativ
werte=[_ if _%2==0 else 0 for _ in range(1,11)]
print(werte)

##neue liste aus werte mit zahlen <> 0
werte1=[x for x in werte if x!=0]
print(werte1)

##alternativ
werte1=[_ for _ in werte if _!=0]
print(werte1)

##neue liste aus werte multipliziert mit 100
werte1=[x*100 for x in werte]
print(werte1)

##alternativ
werte1=[_*100 for _ in werte]
print(werte1)

##looping
[print(_) for _ in werte1]

##list of lists
multiple=[[_ for _ in range(0,10)] for _ in range(0,5)]
print(multiple)

##with random numbers
multiple=[[rnd.randint(1,100) for _ in range(0,10)] for _ in range(0,5)]
print(multiple)

##Liste mit 5 Benutzereingaben
autos=[input("Auto: ") for _ in range(0,5)]
print(autos)
