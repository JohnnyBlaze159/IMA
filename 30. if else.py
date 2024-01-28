people = 30
cars = 40
trucks = 15

if cars > people or trucks < cars:
    print ("We should take the cars.")
elif cars < people:
    print ("We should not take the cars.")
else:
    print ("We cannot decide.")

if trucks > cars or people > trucks:
    print ("That's too many trucks.")
elif trucks < cars:
    print ("Maybe we could take the trucks.")
else:
    print ("We still cannot decide.")

if people > trucks:
    print ("Alright, let us just take the trucks.")
else:
    print ("Fine, let us stay home then.")