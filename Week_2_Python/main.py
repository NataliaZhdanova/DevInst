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

# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers


def quizzer() :
    correct = 0
    incorrect = 0
    quest_dic = dict()
    incorrect_list = []
    print("Welcome to our Star Wars quiz! \n")
    for index in range(0,6) :
        quest_dic = data[index]
        print(quest_dic["question"])
        user_answer = input("Your answer is: ")
        user_answer = user_answer.title()
        if user_answer == quest_dic["answer"] :
            correct += 1
        else :
            incorrect +=1
            incorrect_list.append(user_answer)
            quest_dic["user answer"] = user_answer
            data[index] = quest_dic
    return (correct, incorrect)

# Create a function that informs the user of his number of correct/incorrect answers.

def results() :
    correct_num, incorrect_num = quizzer()
    print(f"\nYou gave {correct_num} correct answers and {incorrect_num} wrong answers!\n")
    for index in range(0,6) :
        quest_dic = data[index]
        if "user answer" in quest_dic :
            print(f"For this question: '{quest_dic['question']}' the correct answer was '{quest_dic['answer']}', and your answer was '{quest_dic['user answer']}'. \n")
    if incorrect_num >= 3 :
        print("Please, take the quiz again!")
results()       