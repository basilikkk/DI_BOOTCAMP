"""This project allows users to take a quiz to test their Star Wars knowledge.
The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

Here is an array of dictionaries, containing those questions and answers
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
Create a function that informs the user of his number of correct/incorrect answers.
Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
If he had more then 3 wrong answers, ask him to play again."""


data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def quiz(data):
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []
    
    for item in data:
        print(item['question'])
        user_answer = input('Please enter your answer: ')
        
        if user_answer.strip().lower() == item['answer'].strip().lower():
            print('correct answer!')
            correct_answers += 1
        else:
            print('wrong answer!')
            incorrect_answers += 1
            wrong_answers.append({
                'question': item['question'],
                'your_answer': user_answer,
                'correct_answer': item['answer']
            })
    
    return correct_answers, incorrect_answers, wrong_answers

def display_results(name, correct, incorrect, wrong_answers):
    print(f"\n{name}, you got {correct} correct answers and {incorrect} incorrect answers.")
    
    if wrong_answers:
        print("\nHere are the questions you answered incorrectly:")
        for item in wrong_answers:
            print(f"Question: {item['question']}")
            print(f"Your Answer: {item['your_answer']}")
            print(f"Correct Answer: {item['correct_answer']}")
    
    if incorrect > 3:
        print(f"\n{name}, you had more than 3 wrong answers. Please try again!")

def main():
    name = input("Please enter your name: ")
    while True:
        correct, incorrect, wrong_answers = quiz(data)
        display_results(name, correct, incorrect, wrong_answers)
        
        if incorrect > 3:
            retry = input("Do you want to play again? type 'yes' or 'no': ")
            if retry.strip().lower() != 'yes':
                break
        else:
            break

main()        

