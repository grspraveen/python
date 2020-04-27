#star in the parameter of function 

def movienames(*names):
    for i in names:
        print(i)

movienames("avengers","spiderman","ironman","thor")
movienames("dil","bahubali","murder")