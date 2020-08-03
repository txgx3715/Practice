
from Question import Question

#Now we will learn how to build a multi-choice.
question_prompts = [
    "what color of apple ? \n (a)Red/Green\n(b)Megenta\n(c)Orange\n",
    "what color of banana ? \n (a)Yellow\n(b)Megenta\n(c)Blue\n",
    "what color of strawbeerries ? \n (a)Teal\n(b)Megenta\n(c)Red\n"
]



questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]
def run_test(questions):
    score = 0
    for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                    score +=1
print("You got" + str(score) + "/" + str(len(questions)))    

run_test(questions)