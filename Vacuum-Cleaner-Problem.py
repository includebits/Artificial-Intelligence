import random

def display(room):
    print(room)
    
room = [1,1,1,1]
print("All the room are dirty")
display(room)

x = 0
y = 0

while x < 4:
    room[x] = random.choice([0,1])
    x+=1

print("Before cleaning the room detect all of these random dirts")
display(room)
x=0
z=0

while x < 4:
    if room[x] == 1:
        y+=1
        print("Vaccuum in this location now, ",x+1)
        room[x] = 0
        print("cleaned", x+1)
        z+=1
    x+=1
pro = (100-((z/4)*100))
print("Room is now clean")
display(room)
print('performance= ', pro, "%")
print('moving cost= ', y)
