from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# TODO: address user by name --> replace $$user$$ in yml files with username
# TODO: add games from previous bot
# TODO: tkinter GUI.

bot = ChatBot(
    'a', # Bot name
    logic_adapters=[
        {
            # if bot is anything less than 90% sure of it's answer, it will say it does not understand.
            'import_path': 'chatterbot.logic.BestMatch', 
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
        'chatterbot.logic.MathematicalEvaluation', #Allows bot to do basic maths e.g. 'what is 3 times 4'
        #'chatterbot.logic.TimeLogicAdapter', #Allows bot to give current time.
    ],
    preprocessors=[
        # Removes any consecutive whitespace characters from the statement text.
        'chatterbot.preprocessors.clean_whitespace'
    ]
)

# Train bot on included YAML files.
# Files consist of various conversations/questions and answers/prompts and responses.
trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    './data/ai.yml',
    './data/computers.yml',
    './data/conversations.yml',
    './data/emotion.yml',
    './data/greetings.yml',
    './data/money.yml',
    './data/profile.yml',
    './data/psychology.yml',
    './data/science.yml'
)


while True:
    try:
        bot_input = bot.get_response(input().lower())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break