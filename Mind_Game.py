import random
import time

def ask_question(question, correct_answer, options=None):
    """
    Function to ask a question, check the answer, and return whether the answer was correct.
    Optionally, a list of multiple choice options can be provided.
    """
    print(question)
    if options:
        print("Options: " + ', '.join(options))
    
    start_time = time.time()
    answer = input("Your answer: ").strip().lower()
    end_time = time.time()
    
    time_taken = round(end_time - start_time, 2)
    if answer == correct_answer.lower():
        print(f"Correct! Time taken: {time_taken} seconds\n")
        return True, time_taken
    else:
        print(f"Wrong! The correct answer is: {correct_answer}. Time taken: {time_taken} seconds\n")
        return False, time_taken

def play_quiz():
    """
    Function to run the quiz game with multiple questions and score tracking.
    """
    print("Welcome to the Advanced Quiz Game\nLet's test your knowledge!")
    
    # Player greeting
    player_name = input("Enter Your Name: ")
    print(f"Hello, {player_name}! Let's begin the quiz.\n")

    score = 0
    total_time = 0
    question_bank = [
        ("What does CPU stand for?", "Central Processing Unit"),
        ("What does GPU stand for?", "Graphical Processing Unit"),
        ("What does RAM stand for?", "Random Access Memory"),
        ("What does ROM stand for?", "Read Only Memory"),
        ("Is a mouse an input device or output device?", "input device")
    ]
    
    # Shuffle questions to randomize order
    random.shuffle(question_bank)

    for question, correct_answer in question_bank:
        is_correct, time_taken = ask_question(question, correct_answer)
        total_time += time_taken
        if is_correct:
            score += 1

    # Display final results
    print(f"\nQuiz Over! You got {score} correct answers out of {len(question_bank)}.")
    accuracy = (score / len(question_bank)) * 100
    print(f"Your accuracy: {accuracy:.2f}%")
    print(f"Total time taken: {round(total_time, 2)} seconds")

    # Offer a retry
    retry = input("Would you like to play again? (yes/no): ").lower()
    if retry == 'yes':
        play_quiz()
    else:
        print("Thank you for playing! Goodbye.")

# Start the quiz game
play_quiz()
