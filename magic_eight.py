import random
def ask_question():
	question = str(input("What is your question? \n(Please end your quesiton with \"?\".\n Type \"quit\" to quit this step.)\n"))
	return question

def check_question(question):
	if (question[-1] == '?'):
		return True
	else:
		return False

def returnAnswer():
    possibleAnswers = ["It is certain", "It is decidely so", "Without a doubt", "Yes - definitely",
    "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
    "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now",
    "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no",
    "Outlook not so good", "Very doubtful"]
    Answer = possibleAnswers[random.randint(0,19)]
    return Answer

question = ask_question()
while question != 'quit':
	if check_question(question):
		print(returnAnswer())
	else:
		print("I'm sorry, I can only answer questions. (Please end your question with \"?\")")
	question = str(input("What is your question?\n"))
	

