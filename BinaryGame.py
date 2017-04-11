import random # to generate random number

bit = 5 # how many bit do you want the game to be

print("Binary game : 5-bit max") # print simple instructions
print()

# generate a random number
def getRandomNum():
    return random.randrange(0,2**bit) # return a randomly generated number

# number to binary
def getBinary(num):
    return bin(num)[2:] # return the binary number of the parameter

# get user attempt
def getUserNum():
    userNumber = input() # get an input from the user
    try:
        userNumber = int(userNumber) # if it works,
        return userNumber # return the number
    except:
        getUserNum() # otherwise, try till the answer is good

# check if user attempt and random number are the same
def check(x,y):
    return x == y # returna boolean : true is they are the same and false if not

# main function
def main():
    randNum = getRandomNum() # get the random number
    randBin = getBinary(randNum) # translate it to binary

    print("Here is you new number : "), # print short info
    print(randBin) # print the binary
    #print(randomNumber) # just for easy debugging

    userNum = getUserNum() # get the users attempt

    if check(randNum,userNum): # check and if it is good
        print("Correct.") # print correct
    else : # otherwise
        print("Not correct. The answer was " + str(randNum)) #print incorrect and print the number so that the user can learn

    print()
    print()

# infinite loop
while 1: 
    main() # call the main function
