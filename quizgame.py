print("Hey welcome to my very first python game!")

playing = input("Do you wanna play this game? ")

if playing.lower() != "yes" :
    quit("Okay bye!")

print("Okay let's play :)")

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score = 1
else:
    print("Incorrect!")   

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")    

answer = input("What does PSU stand for? ").lower()

if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("Your score is " + str((score/4) * 100) + " %")
