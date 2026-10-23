import random

lucky_number=random.randint(1,10)
uttar=input("mi manat 1 te 10 madhye ek number dharala aahe,olkha pahu konte?")

if int(uttar) ==lucky_number:
  print ("Abhinandan!Tumhi jinklat,to number hota:"+str(lucky_number))
else:
    print("Ohho!Chukale uttar.To number hota:" +str(lucky_number))
