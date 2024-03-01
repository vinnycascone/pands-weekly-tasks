car={
    "make" : "ford", 
    "model" : "modeo",
    "year" :  2006, 
    "owner"  : {
         "name" :"Vincenzo" , 
         "owner_driving_number" :123
    }
}

for keys in car:
    print (keys, 'has the value of:', car[keys])
