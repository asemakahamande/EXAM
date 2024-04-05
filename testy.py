from question import question

question_prompts = [
    "1. The outcome of a processed data in a computer is known as  \n (a) raw fact \n (b) information \n (c) database\n (d) computer result \n\n",
    "2. which of the following computing device did not exist in pre computing age to the 19th century \n (a) Napier's Bones \n (b) Abacus \n (c) ENIAC\n(d) SLide Rule \n\n",
    "3. The combination of different parts of the computer to help achieve a task best describe ....  \n (a) computer \n (b) computer system \n (c) hardware\n (d) Software \n\n",
    "4. In a computer, the sets of instruction that direct it in performing a particular task is called \n (a) information\n (b) program \n (c) data\n (d) Abacus\n\n",
    "5. What is the Nationality of John Napier \n (a) England\n (b) Scotland \n (c) France\n (d) Germany \n\n",
]

question = [
    question(question_prompts[0], "b"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b"),
    question(question_prompts[3], "b"),
    question(question_prompts[4], "b"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompts)
        if answer == question.answer:
            score+= 1
    print("you got "+str(score) + "/"  + str(len(questions)) +" correct")
run_test(question)