import random # to generate random number

bit = 5

print("Binary game : 10-bit max")
print()

def getRandomNum():
    return random.randrange(0,2**bit) # generate a random number

def getBinary(num):
    return bin(num)[2:] # put that random number to binary

def getUserNum():
    userNumber = input()
    try:
        userNumber = int(userNumber)
        return userNumber
    except:
        getUserNum()

def check(x,y):
    return x == y

def main():
    randNum = getRandomNum()
    randBin = getBinary(randNum)

    print("Here is you new number : "),
    print(randBin)
    #print(randomNumber) # just for easy debugging

    userNum = getUserNum()

    if check(randNum,userNum):
        print("Correct.")
    else :
        print("Not correct. The answer was " + str(randNum))

    print()
    print()

while 1:
    main()
