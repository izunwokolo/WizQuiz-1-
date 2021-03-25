import random 
def math_question():  
  math_questions = []
  math_questions.append('2 + 6')
  math_questions.append('10 + 5')
  math_questions.append('3 + 9')
  math_questions.append('3 * 9')
  math_questions.append('20 * 1')
  math_questions.append('8 * 4')
  math_questions.append('6 - 3')
  math_questions.append('3 - 3')
  math_questions.append('10 / 5')
  math_questions.append('15 / 5')
  return math_questions

def answer_dict():
  answers = {'2 + 6': 8,'10 + 5': 15, '3 + 9': 12, '3 * 9': 27, '20 * 1': 20, '8 * 4': 32, '6 - 3': 3, '3 - 3': 0, '10 / 5': 2, '15 / 5': 3}
  return answers

def failed_qs():
  failed = []
  return failed

def math_quiz():
  quiz_questions = math_question()
  quiz_answers = answer_dict()
  quiz_failed = failed_qs()

  # randomize questions
  random.shuffle(quiz_questions)
  score = 0
  finish = False
  while finish == False:
    for question in quiz_questions:
      print("Put in the correct value: " + question)
      player_answer = int(input("Enter an interger: "))   
      if player_answer == quiz_answers[question]:
        score += 1
      else:
        quiz_failed.append(question)
        score += 0 
    if quiz_failed == []:
      finish = True
    else: 
      quiz_questions = quiz_failed
      quiz_failed = []   

  return "You scored a " + str(score) + " out of 10" 

def main_screen():
  print("-----------------------------------")
  print("| Hello and welcome to WizQuiz    |")
  print("-----------------------------------")
  print("|                                 |")
  print("| To Begin:")
  print("| Press a to start the quiz       |")
  print("| Press b to stop the quiz        |")
  print("| Press c to see the Instructions |")
  print("-----------------------------------")
  user_choice = input("Select a, b, or c: ")
  if user_choice == "a":
    results = math_quiz()
  elif user_choice == "b":
    print("Come play again soon!")
    quit()
  elif user_choice == "c":
    with open("file_questions", "r") as my_files_handle:
      print(my_files_handle.read())

  
  return results

if __name__ == "__main__":
  print(main_screen())

