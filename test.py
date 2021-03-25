from main import *


def test_answer_dict():
  assert answer_dict()['2 + 6'] == 8
  assert len(answer_dict()) == 10
  print('test_answer_dict')
test_answer_dict()

def test_math_question():
  assert math_question()[0] == "2 + 6"
  print("test_math_question")
test_math_question()

def test_failed_qs():
  assert failed_qs()== []
  print("test_failed_qs")
test_failed_qs()
