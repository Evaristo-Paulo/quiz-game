questions ={
    'What is the capital of France?': 'D',
    'Who is the writer of "Le Prénom" movie?': 'D',
    'Who painted the Mona Lisa?': 'C',
    'In what year did World War II end?': 'B',
    'Which ancient civilization built the Great Wall of China?': 'A',
    'What is the largest planet in our solar system?': 'B',
    'Who won the FIFA World Cup in 2022?': 'A',
    'Who is considered the greatest basketball player of all time?': 'A',
    'Which African country is famous for its pyramids?': 'C',
    'Who is considered the greatest football player of all time?': 'D'
}

answers = [
    ['A. Brussels', 'B. Madrid', 'C.Lyon', 'D. Paris'],
    ['A. Vincent Dieutre', 'B. Olivier Assayas', 'C. Mel Gibson', 'D.Alexandre de La Patellièr'],
    ['A. Miguelangelo', 'B. Bennedith patietoi', 'C. Leonardo da Vinci', 'D. CLAUDE MONET'],
    ['A. May 8, 1945', 'B. September 2, 1945', 'C. November 11, 1918', 'D. September 3, 1945'],
    ['A. Ancient China', 'B. Ancient India', 'C. Ancient Egypt', 'D. Mesoamerica'],
    ['A. Saturn', 'B. Jupiter', 'C. Uranus', 'D. Neptune'],
    ['A. Argentina', 'B. Brazil', 'C. France', 'D. Croatia'],
    ['A. Michael Jordan', 'B. Kareem Abdul-Jabar', 'C. Magic Johnson', 'D. LeBron James'],
    ['A. South Africa', 'B. Sudan', 'C. Egypt', 'D. Madagascar'],
    ['A. Maradona', 'B. Cristiano Ronaldo', 'C. Pelé', 'D. Messi'],
]

def new_game():
    question_number = 1
    total_score = 0
    guesses = []

    for question in questions:
        print('\n')
        print(f'{question_number}. {question}')
        for answer in answers[question_number - 1]:
            print(answer)
        question_number += 1
        guess = input('Enter the right answer (A, B, C or D): ')
        guess = guess.upper()
        guesses.append(guess)
        key = questions.get(question)

        print("--------------------------------------")
        total_score += check_answer(key, guess)
        print("--------------------------------------")

    display_score(questions, guesses, total_score)

def check_answer(answer, question ):
    if answer == question:
        print('CORRECT!')
        return 1
    else:
        print('WRONG!')
        return 0

def display_score (questions, guesses, total_score):
    print('\n')
    print("--------------------------------------")
    print('RESULT')
    print("--------------------------------------")
    print('Answers: ', end="")
    for value in questions.values():
        print(value, end=" ")
    print('')
    print('Guesses: ', end="")
    for guess in guesses:
        print(guess, end=" ")
    print('')
    score = int((total_score/len(questions)) * 100)
    print(f'Score: {score}%' )
    print('\n')

    print("--------------------------------------")
    if score > 50:
        print('PARABÉNS!')
    else:
        print('PRECISA LER MAIS!')
    print("--------------------------------------")

def play_again():
    op = input('Do you want to play again? (Y or N)\nR: ')
    op = op.upper()

    if op == 'Y':
        return True

    return False

new_game()

while play_again():
    new_game()

print('bye!...')

