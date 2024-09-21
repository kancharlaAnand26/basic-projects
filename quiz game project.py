print("welcome to my quiz")

playing =input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play  :)")
score =0

answer = input("what is the capital of india? ")
if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("what is the capital of unitedstates? ")
if answer.lower() == "new york":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("what is the capital of england? ")
if answer.lower() == "london":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("what is the capital of germany? ")
if answer.lower() == "berlin":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the capital of japan? ")
if answer.lower() == "tokyo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the capital of russia? ")
if answer.lower() == "moscow":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("what is the capital of china? ")
if answer.lower() == "beijing":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the capital of brazil? ")
if answer.lower() == "brasilia":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the capital of southafrica? ")
if answer.lower() == "cape town":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the capital of newzealand? ")
if answer.lower() == "auckland":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
       
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10)  * 100) + "%.")
