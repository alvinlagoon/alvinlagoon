# Define main function
def main ():
    # declare varaible and give it a string
    answer_one = 'yes'
    answer_two = 'no'
    # Ask user for input
    ask = input("Would you like to do some math today? ").lower()
    
# check if the user response = to answer_one
    if ask == answer_one:
        print("\nLets do some mathamatics!")
        user = input("What mathamatical question do you want"
                    + " to do today? ").lower()
        # While all this condition is true, loop through each value 
        # and check if it matches the user input            
        while True:
            if user == 'add':
                print("Lets do some additions:")
                print("Input you're x and y values" )
                addition()
                return
            elif user == 'subtract':
                print("Let's do some subtraction:")
                print("Input you're x and y values" )
                subtraction()
                break
            elif user == 'multiply':
                print("Then lets do some multiplication:")
                print("Input you're x and y values" )
                multiplication()
                break
            elif user == "divide":
                print("Let's do some division")
                print("Input you're x and y values" )
                division()
                break
            else:
                print('Changed your mind? ')
                break  
    else:
        print("Next time then!")
        
        
#define function one_more to ask user if they want to do some more calculation              
def one_more():
    again = input("Do you want to do more math? ")
    while True:
        if again == "yes".lower():
            which_one = input("What would you like to do? ")
            if which_one == 'subtract':
                print("lets do some subtraction")
                subtraction()
                break
            elif which_one == 'add':
                print("lets do some addition")
                addition()
                break
            elif which_one == 'multiply':
                print('lets do some multiplication')
                multiplication()
                break
            elif which_one == 'division':
                print('lets do some division')
                division
                break
        else:
            print("See u soon")          
#define the mathmatical functions    
def subtraction():
    while True:
    #try to check if user inputed an int
    #if not tell user that the value they inputed is not an Integer
        try:
            question_one = int(input("what is x? "))
            break
        except ValueError:
            print("X is not an integer")
            continue
    while True:
        try:
            question_two = int(input("what is y? "))
            break
        except ValueError:
            print("Y is not an integer")
            continue
    answer = (question_one - question_two)
    print(f"You're answer is: {answer} ")
    one_more()
def multiplication():
    while True:
        try:
            question_one = int(input("what is x? "))
            break
        except ValueError:
            print("X is not an integer")
            continue
    while True:
        try:
            question_two = int(input("what is y? "))
            break
        except ValueError:
            print("Y is not an integer")
            continue
    answer = (question_one * question_two)
    print(f"You're answer is: {answer} ")   
    one_more()
def addition():

    while True:
        try:
            question_one = int(input("what is x? "))
            break
        except ValueError:
            print("X is not an integer")
            continue
    while True:
        try:
            question_two = int(input("what is y? "))
            break
        except ValueError:
            print("Y is not an integer")
            continue
    answer = (question_one + question_two)
    print(f"You're answer is: {answer} ")
    one_more()
def division():

    while True:
        try:
            question_one = int(input("what is x? "))
            break
        except ValueError:
            print("X is not an integer")
            continue
    while True:
        try:
            question_two = int(input("what is y? "))
            break
        except ValueError:
            print("Y is not an integer")
            continue
    answer = (question_one / question_two)
    print(f"You're answer is: {answer} ")
    one_more()


main()