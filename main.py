# COLOR DATA PRACTICE
import json

# Load Color Data from JSON file
file = open("color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)

#First
def nameFam(anArray):
    for i in range(len(anArray)):
        print("The color is: " + anArray[i]["name"])
        print("The family of the color is, " + anArray[i]["family"])


#Second
def nameBright(anArray):
    for i in range(len(anArray)):
        brightness = anArray[i]["brightness"]
        if brightness >= 200:
            print(anArray[i]["name"]  + "With a brightness of, " + str(brightness))

#Third
def redPink(anArray):
    count = 0
    for i in range(len(anArray)):
        family = anArray[i]["family"]
        if family == "Red" or family == "Pink":
            count += 1
    print(count)


#Fourth
def  colorUser(anArray):
    userInput = input("Please enter the name Of the Family:\n")
    count = 0
    print("For the family, " + userInput + ". These are the colors:")
    for i in range(len(anArray)):
        if anArray[i]["family"] == userInput:
            print(anArray[i]["name"])
            count += 1
    print("The total count is: " + str(count))


#Fifth
def letterUser(anArray):
    userInput = input("What is your letter:\n").upper()
    counter = 0
    for i in range(len(anArray)):
        if anArray[i]["name"].startswith(userInput):
            print(anArray[i]["name"])
            counter += 1
    print("The total number of colors that starts with " + userInput + " is:\n" + str(counter))
