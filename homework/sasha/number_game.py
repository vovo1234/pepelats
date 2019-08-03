import sys
player_number = 0
python_number = 1
total = 0
print ('welcome to the... NUMBER GAMESHOW!!!(this is live btw)\n'
       'the rules are fairly straight forward: the two players\n'
       'take turns naming a number from 1 to 10. the player to\n'
       'name the number that gets the sum of all the named numbers\n'
       'to 100 WINS!! you are going to compete aigainst the world\n'
       'champion! oh, and if you win you get a million bucks, no joke. ready, set, GO!')



for x in range (1,10):
    print (f'hmm... okay, my number is {python_number}.')
    total = total + python_number
    python_number = python_number - python_number
    print (f'the running total is {total}!')
    print ('please enter your number:')
    player_number = int(input())
    total = total + player_number
    python_number = 11 - player_number
    print (f'the running total is {total}!')

    
print (f'hmm... okay, my number is {python_number}.')
print ('looks like we have a WINNER!!!\n'
       '    ')
print ("better luck next time...")
