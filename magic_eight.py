def ask_question():
	question = str(input("What is your question? \n(Please end your quesiton with \"?\".\n Type \"quit\" to quit this step.)\n"))
	return question

def check_question(question):
	if (question[-1] == '?'):
		return True
	else:
		return False

question = ask_question()
while question != 'quit':
	if check_question(question):
		print("This is a question")
	else:
		print("I'm sorry, I can only answer questions. (Please end your question with \"?\")")
	question = str(input("What is your question?\n"))