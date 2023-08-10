class Question:
  def __init__(self,question,answer):
    print("Parameterised Constructor is called")
    self.question = question
    self.answer = answer
    

#Question Bank
question_data = [
  {"question":"What is India ?. ","answer":"Country"},
  {"question":"Is 3 Prime Number ?. ","answer":"yes"},
  {"question":"1960, Prime Number ?. ","answer":"yes"},
  {"question":"Google,was initially called as backrb?. ","answer":"yes"},
]

question_bank = []

for i in range(0,len(question_data)):
  question_bank.append(Question(question_data[i]["question"],question_data[i]["answer"]))

# for question in question_data:
#   question_obj.append(Question(question["question"],question["answer"]))


class QuizBrain:
  def __init__(self,q_list):
    print("Default constructor is called")
    self.question_number = 0
    self.question_list = q_list
    self.RightAnswer = 0

  def next_question(self):
    question_obj = self.question_list[self.question_number]
    user_ans = input(f"Q.{self.question_number}: {question_obj.question}").lower()
    if self.check_answer(question_obj.answer,user_ans):
      self.question_number += 1
      self.RightAnswer += 1
      print(f"Your Score is {self.RightAnswer}")
    else:
      self.question_number = len(self.question_list)
    

  def still_has_questions(self):
    if self.question_number < len(self.question_list):
      return True
    else:
      return False

  def check_answer(self,user_answer,correct_ans):
    if user_answer.lower() == correct_ans.lower():
      print("you are right!.")
      return True
    else:
      print("Wrong answer!.")
      return False

qb = QuizBrain(question_bank)
while qb.still_has_questions():
  qb.next_question()
