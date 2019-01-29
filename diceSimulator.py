# Author: aliasEnv
# Date Started: Sunday, October 28th, 2018
# Date Finished: Sunday, October 28th, 2018

# importing from random library and the radint function
from random import randint
print (randint(0, 5))
# assigning variables for user input answers
yes= "yes"
no= "no"
 #asks if user would like to reroll with yes or no, if yes, roll again
answer = input('Would you like to roll again? Please enter ' + yes + " or " + no + ":  ")
#.lower allows the answer to be capital and lower case
#while answer in ('yes', 'no'):
if answer.lower() == yes:
   print (randint(0, 5))
elif answer.lower() == no:
    print('Thanks for playing! Goodbye!')

