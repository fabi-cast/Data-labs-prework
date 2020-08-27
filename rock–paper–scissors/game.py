# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
import math
from random import choice
# Assign to a list the 3 possible options: 'stone', 'paper' or 'scissors'.
opt=['stone', 'paper', 'scissors']
# Assign a variable to the maximum number of games: 1, 3, 5, etc ...
def max_rounds(x):
    N=int(input("Enter a number odd of rounds desired:"))
    while N%2==0:
        N= int(input("Number even! Enter a number odd of rounds desired:"))
    return N
# Define a function that randomly returns one of the 3 options.
# This will correspond to the play of the machine. Totally random.

def machine_game(x):
    if x in opt:
        return choice(opt)    
    
# Define a function that asks your choice: 'stone', 'paper' or 'scissors'
# you should only allow one of the 3 options. This is defensive programming.
# If it is not stone, paper or scissors keep asking until it is.


def user_game(x):
    a= input("'stone', 'paper' or 'scissors'?")
    while a not in opt:
        a= input("'stone', 'paper' or 'scissors'?")
    return a
        
# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins


def combat_points(x,y):
    if x==y:
        return 0
    elif (x=='stone' and y=='scissors') or (x=='paper' and y=='stone') or (x=='scissors' and y=='paper'):
        return 1
    else:
        return 2

# Create two variables that accumulate the wins of each participant
# We initialize 2 variables which store the points p_x for human, p_m for machine
 


# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated

# the argument for this function is an integer x and a list r of two elements
def combat(x, r):
    a= user_game(x)
    m_x= machine_game(a)
    h1=r[0]
    m1=r[1]
    print("My choice: %s" % m_x)
    p = combat_points(a, m_x)
    if p== 0:
        print("This round has a Tie")
        return [h1,m1]
    elif p==1:
        print("You won this round")
        return [h1+1,m1]
    elif p==2:
        print("I won this round")
        return [h1,m1+1]

def points_pr(x):
    print("Your points= %d" %x[0])
    print("My points= %d" % x[1])
    if x[0]> x[1]:
        print("Hooman is winning")
    elif x[0]==x[1]:
        print("We have a tie")
    else:
        print("Machine is winning")        

def game(M):
    N=max_rounds(M)
    N_win= math.ceil(2*N/3)
    points=[0,0]
    for i in range(N):
        p1= combat(i,points)
        points_pr(p1)
        if points[0]== N_win and points[1]< N_win:
            return print("Hooman is the winner at stage %d" % i)
            break
        elif points[0]< N_win and points[1]==N_win:
            return print("Machine is the winner at stage %d" %i)
            break
        else:
            points = p1
    if points[0]>points[1]:
        return print("Hooman is the winner of the game at %d stages" %N)
    if points[0] < points[1]:
        return print("Machine is the winner of the game at %d stages" %N)
    if points[0]== points[1]:
        return print("Tie at %d stages" %N)
        
def combat_points_2(x,y):
    if x==y:
        return 0
    elif (x=='stone' and y in {'scissors','lizard'}) or (x=='paper' and in {'stone','spock'}) or (x=='scissors' and y in {'paper', 'lizard'}) or (x=='spock' and y in {'stone', 'scissors'}) or (x=='lizard' and y in {'spock', 'paper'}):
        return 1
    else:
        return 2


        
        
        