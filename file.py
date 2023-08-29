def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0
    for key in questions:
        print("-----------------------")
        print(key)
        for i in option[question_num]:
            print(i)
        guesse = input("Enter your answer (a/b/c): ")
        guesses.append(guesse)
        correct_guesses += check_answer(questions.get(key), guesse)
        question_num += 1
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses, guesses):
    print("-----------------")
    print("RESULTS")
    print("-----------------")
    print("Answers:", end=" ")
    for i in questions:
        print(questions[i], end=" ")
    print()
    print("Your Guesses:", end=" ")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is:", score, "%")

questions = {
    "1. What is the capital city of France?": "a",
    "2. Which planet is known as the Red Planet ?": "b",
    "3. Who wrote the play Romeo and Juliet ?": "c",
    "4. What is the chemical symbol for gold?": "a",
    "5. Which famous scientist developed the theory of general relativity?": "c",
    "6. What is the largest mammal in the world?": "b",
    "7. In which year did the Titanic sink?": "b",
    "8. Which country is known as the Land of the Rising Sun ?": "c",
    "9. What is the tallest mountain in the world?": "b",
    "10. Who painted the Mona Lisa?": "b"
}

option = [
    ["a) Paris", "b) London", "c) Berlin"],
    ["a) Venus", "b) Mars", "c) Jupiter"],
    ["a) Mark Twain", "b) Jane Austen", "c) William Shakespeare"],
    ["a) Au", "b) Ag", "c) Cu"],
    ["a) Isaac Newton", "b) Marie Curie", "c) Albert Einstein"],
    ["a) Elephant", "b) Blue whale", "c) Lion"],
    ["a) 1909", "b) 1912", "c) 1915"],
    ["a) China", "b) South Korea", "c) Japan"],
    ["a) Mount Kilimanjaro", "b) Mount Everest", "c) Mount Fuji"],
    ["a) Vincent van Gogh", "b) Leonardo da Vinci", "c) Pablo Picasso"]
]

new_game()
