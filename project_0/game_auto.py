"""Game - Guess number"""

import numpy as np
from numpy.random import rand

def random_predict(number:int=1) -> int:
    """Randomly guessing the number

    Args:
        number (int, optional): Generated number. Defaults to 1.

    Returns:
        int: Attempts number
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # assumed number
        if number == predict_number:
            break # quitting loop when guessed
        
    return(count) # attempts number

def score_game(random_predict) -> int:
    """Estimating average number of attempts to guess for used algorithm based on 1000 iterations

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average attempts number
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) # generated numbers list
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Current algorithm is guessing a number in average using {score} attempts')
    return(score)


if __name__ == '__main__':
    # RUN
    score_game(random_predict)
