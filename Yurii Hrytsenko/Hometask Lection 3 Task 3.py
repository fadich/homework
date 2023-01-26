# Task 3

first_question = '''Скільки нулів потрібно дописати праворуч від одиниці, ''' \
                 '''щоб отримати мільйон?'''
second_question = '''Підрахуйте результат: 3+3x3+3'''
third_question = '''Кільксть тупих кутів у рівносторонньому трикутнику?'''
fourth_question = '''Скільки метрів у кілометрі?'''
fifth_question = '''Скільки кілограмм у 1 тонні?'''

first_answer = "6"
second_answer = "15"
third_answer = "0"
fourth_answer = "1000"
fifth_answer = "1000"

questions = [first_question, second_question, third_question, fourth_question, fifth_question]
answers = [first_answer, second_answer, third_answer, fourth_answer, fifth_answer]

result = 0

for question, answer in zip(questions, answers):
    key = input(question + "\n")

    if key == answer:
        print("Вірно!")
        result += 1
    else:
        print("На жаль невірно!")

fin_result = int(100 / len(answers) * result)

print(f"Ви відповіли на всі запитання, Bаш результат: {fin_result} %")