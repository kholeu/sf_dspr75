"""Game - Guess number"""

import numpy as np

number = np.random.randint(1, 101) # Generate random number from 1 to 100

# attempt nunmber
count = 0

while True:
    count += 1
    predict_number = int(input('Enter number from 1 to 100: '))
    
    if predict_number > number:
        print('Number is less!')
        
    elif predict_number < number:
        print('Number is more!')
        
    else:
        print(f"You've guessed the number! The number is = {number}, using {count} attempts")
        break # end of game exit from loop