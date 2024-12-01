def quiz():
    print("Welcome to the Quiz!")
    score = 0

    # Question 1
    print("\n1. What is the capital of india?")
    print("a) London\n b) Paris\n c) Rome\n d) delhi")
    answer = input("Your answer: ")
    if answer == "d":
        score += 1
        print("Correct Answer!!!")
    else:
        print("Wrong Answer")    

    # Question 2
    print("\n2. Which planet is known as the biggest Planet?")
    print("a) Venus\n b) Jupiter\n c) Mars\n d) Saturn")
    answer = input("Your answer: ")
    if answer == "b":
        score += 1
        print("Correct Answer!!!")
    else:
        print("wrong answer")      

    # Question 3
    print("\n3. how many colors a rainbow has?")
    print("a) 1\n b) 7\n c) 3\n d) 5")
    answer = input("Your answer: ")
    if answer == "b":
        print("Correct Answer!!!")
        score += 1

    else:
        print("wrong answer") 
        # Final Score
    print("\nYou scored ",score ," Thanks for playing!")

# Run the quiz
quiz()
