import random # to generate random number

bit = int(input('Enter max number of bit wanted : ')) # how many bit do you want the game to be; caution, no fail safe here
print('Binary game : %s-bit max\n' %(bit)) # print simple instructions

def getUserNum(): # get the users answer
    try:
        return int(input('Enter your answer: ')) # return user input as an integer
    except:
        getUserNum() # otherwise, try till the answer is good

while True:
    randNum = random.randrange(0,2**bit) # get the random number
    print('Here is you number : ', str(bin(randNum)[2:]).zfill(bit)) # print the binary number
    print(('Correct.' if randNum == getUserNum() else 'Not correct. The answer was %s.' %(randNum)), '\n\n') # print the correct answer
