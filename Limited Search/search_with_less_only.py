import math
import sys
import numpy as np

global the_number

guess_count = 0
larger_count = 0
the_number = 100

'''
Guessing a number where you can only make two guesses that are larger.
1 <= number <= n
Function is_this_smaller is given
Most optimal number of guess O(sqrt(2n))
'''
def guess_limited(n, is_this_smaller):
	iguess = 0
	guess = math.ceil(math.sqrt(2*n))
	temp = guess - 1
	while is_this_smaller(guess) == True:
		iguess = guess
		guess = guess + temp
		temp = temp - 1
	while is_this_smaller(iguess) != False:
		iguess = iguess + 1
	return iguess
	


def _is_this_smaller(candidate):
    global guess_count
    global larger_count 
    guess_count = guess_count + 1
    if candidate >= the_number:
        larger_count = larger_count + 1
    return (candidate < the_number)

if __name__ == "__main__":

    # Guessing a number, with busting
    n = 1000
    the_number = 46
    print guess_limited(n,_is_this_smaller)
    print "Number of guesses: " + str(guess_count), ", Number of time busted: " + str(larger_count)

