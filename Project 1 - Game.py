print ("Welcome to my computer quiz")

playing = input("Do you want to play?")

if playing != "yes":
    quit()
    
print("Ok! Let's play :)")
score = 0

answer = input("What does DNS stand for?")
if answer == "domain name system":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does HDD stand for?")
if answer == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does BIOS stand for?")
if answer == "basic input output service":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does FTP stand for?")
if answer == "file transfer protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does HTTP stand for?")
if answer == "hypertext transfer protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does LCD stand for?")
if answer == "liquid crystal display":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " out of 6 questions correct!")
print("you got " + str((score /6) * 100) + "%.")