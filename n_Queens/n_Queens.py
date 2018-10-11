import random

'''
Compute a random state. O(1)
'''
def get_random_state(n):
    state = []
    # Your code here 
    for i in range(0,n):
        temp= random.randrange(1,n+1)
        state.append(temp)
    return state

'''
Compute pairs of queens in conflict. O(n^2)
'''
def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    # Your code here 
    for i in range(0,len(state)-1):
        location = state[i]
        k=0
        for j in range(i+1,len(state)):
            k=k+1
            if(state[j]==location):
                number_attacking_pairs = number_attacking_pairs + 1
                continue
            elif(state[j]==location-k or state[j]==location+k):
                number_attacking_pairs = number_attacking_pairs + 1
                continue
    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens O(n^2)
'''
def hill_desending_n_queens(state, comp_att_pairs):
    final_state = []
    # Your code here
    n=len(state)
    temp = state
    min = 2147483647
    ansi = -1
    ansj = -1
    while(1):
        initialmin = min
        for i in range(0,n):
            k = state[i]
            for j in range(1,n+1):
                temp[i] = j
                x = comp_att_pairs(temp)
                if (x<min):
                    min = x
                    ansi = i
                    ansj = j
            temp[i] = k
        if(initialmin==min):
            final_state=temp
            return final_state
        else:
            temp[ansi] = ansj
        #print(str(temp) + " min: " + str(min))
    return final_state

'''
Hill-climing algorithm for n queens that runs until solution. O(n^2)
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = []
    # Your code here
    number_attacking_pairs = 2147483647
    while(number_attacking_pairs!=0):
        state = get_rand_st(n)
        state = hill_desending_n_queens(state, comp_att_pairs)
        number_attacking_pairs = comp_att_pairs(state)
    final_state = state
    return final_state


# This Algorithm runs in O(n^2) time

if __name__ == "__main__":
    print "The n-queens problem" 

    n = 7 
    # Get a basic state
    state = get_random_state(n)
    print "A random state: " + str(state) + ", conflicting pairs: " + str(compute_attacking_pairs(state))

    # Call hill-climbing once 
    new_state = hill_desending_n_queens(state, compute_attacking_pairs)
    print "Final state after hill-climbing: " + str(new_state) + ", conflicting pairs: " \
          + str(compute_attacking_pairs(new_state))

    # Get a fully solved state for a given n    
    print "A valid solution for " + str(n) + " Queens problem: " + str(n_queens(n,
        get_random_state, compute_attacking_pairs,hill_desending_n_queens))

    

