

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import os 
import random 
name = ''
def ask_name():
    
    print("Type your name ")
    name = input()
    
    print("Lets Begin " + name + "!")

    return name


def get_puzzle():
   

    file_names = os.listdir("data/")

    for i,f in enumerate(file_names):
        with open("data/" + f,'r') as file:
            lines = file.readline()

        print(i, lines)
          
    print()

    

    choice = input("Which one? ")
    choice = int(choice)

    file = "data/" + file_names[choice - 1]

    with open(file,'r') as f:
        lines = f.read().splitlines()
    
  
    category = lines[0]
    puzzle = random.choice(lines[1:])

    
    print(category)
    return(puzzle)
    

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"
            
    return solved

def get_guess():
  while True:
    guess = input ("Enter a letter:")
    if len(guess)> 1 or guess.lower() not in alphabet:
        print("Please type 1 letter")
    else:
        print()
        return guess
        
def playball(strikes):
    if strikes == 1 :
        
        print("""
     ,--./,-.
    / #      \\
   |          |
    \\        /    
     `._,._,'
                 """)

    elif strikes == 2:
        print("""


        
     ,--/,--.
    / #      \\
   (       (_|
    \        /
     `._,._,'        
                 """)

    
        
    elif strikes == 3:
        
        print("""
           
            /")
     ,--/,-(=(
    / #     )=)
   (       (_/)
    \        /
     `._,._,'
                   hjw

                   """)
    elif strikes == 4:
        print("""

            /")
            )=) 
     ,--/,-(=(
    / #     )=)
   (       (_/)
    \        /
     `._,._,'
                   hjw

                   """)
    elif strikes == 5:
        print("""

     ,--./,-.
    /,-._.--~\
    
     __}  {
    \`-._,-`-,
     `._,._,'   hjw
                   

                   """)
    elif strikes == 6: 
        print("""


  ___              _        _____        ______             ______             
 / _ \            | |      |  __ \       | ___ \            | ___ \            
/ /_\ \_ __  _ __ | | ___  | |  \/ ___   | |_/ /_   _  ___  | |_/ /_   _  ___  
|  _  | '_ \| '_ \| |/ _ \ | | __ / _ \  | ___ \ | | |/ _ \ | ___ \ | | |/ _ \ 
| | | | |_) | |_) | |  __/ | |_\ \ (_) | | |_/ / |_| |  __/ | |_/ / |_| |  __/ 
\_| |_/ .__/| .__/|_|\___|  \____/\___/  \____/ \__, |\___| \____/ \__, |\___| 
      | |   | |                                  __/ |              __/ |      
      |_|   |_|                                 |___/              |___/  
                          """)

    
   

           






   
    
       
def display_board(solved,guesses):
    print(solved)
    print("""***************************""")
    print("Stikes:" + str(strikes) +"")
    print("")
    print("Limit:" + str(limit) + "")
    print("")
    print("Guessed:" + guesses + "")
    print("""***************************""")
    print()
    
def play_again(name):
    while True:
        decision = input("Would you like to play again? (y/n) ")
        
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand " + name + " . Please enter 'y' or 'n'.")
            
def show_credits(name):

       pic = open("art/end.txt","r")
       contents = pic.read()
       print(contents)
       pic.close()
       print()
     

       print("Brought to you by Savanna. Created on Nov. 15/2017")
       print("Thanks for Playing " + name + "")
                
def show_header():

       pic = open("art/showcredits.txt", "r")
       contents = pic.read()
       print(contents)
       pic.close()
       print()      
    

    
 
 
                                

    
def show_result(solved,name,puzzle):
    
    if strikes < limit:
         print( "Way to go. " + name + " You can guess!")
         

    else:
         print( " Way to go, " + name + " you suck the word was " + str(puzzle) + ".")

        


  
def play():
   

    puzzle = get_puzzle()
    global strikes
    strikes = 0

    global limit
    limit = 6
    
    guesses = " " 
   
       
    solved = get_solved(puzzle,guesses)
    display_board(solved,guesses)
    while solved != puzzle and strikes < limit:
        letter = get_guess()
        
        

        if letter not in puzzle:
             strikes += 1
        guesses += letter
        
        if letter not in puzzle:
             playball(strikes)
        

            
        solved = get_solved(puzzle,guesses)
        display_board(solved,guesses)

    show_result(solved,name,puzzle)
        
        
    
show_header()
name = ask_name()
playing = True

while playing:
    play()
    playing = play_again(name) 

show_credits(name)
