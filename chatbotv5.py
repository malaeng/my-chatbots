'''
chatbot using chatterbot library to implement Natural Language Processing
A conversation bot with training on various topics:
- greetings
- AI
- itself
- computers
- emotion
- money
- psychology
- science (limited knowledge at the moment)

Has 3 games which can be played using the following commands:
number guessing game: "play the number guessing game" | "play number guesser"
magic eight ball: "play the magic eight ball" | "play magic eight ball" | "play the magic 8 ball" | "play magic 8 ball"
scissors-paper-rock: "play scissors paper rock" | "play rock paper scissors"

'''
import tkinter as tk
from tkinter.constants import DISABLED
from random import randint, choice
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# TODO: address user by name --> replace $$user$$ in yml files with username

class chatbot:
    def __init__(self):
        self.bot = ChatBot(
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
        trainer = ChatterBotCorpusTrainer(self.bot)
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
    def get_response(self, input):
        bot_input = self.bot.get_response(input.lower())
        return(bot_input)
        
class application:
    def __init__(self):
        self.window = tk.Tk()
        self._setup_main_window()
        self.game = "none"
        self.ngg_record = 0
        self.spr_wins = 0
        self.spr_losses = 0
        self.spr_ties = 0
   
    def run(self):
        self.window.mainloop()
    
    def _setup_main_window(self):
        theme_colour = "#2e1f27"
        user_text_colour = "#3d405b"
        bot_text_colour = "#e07a5f"

        self.window.title("Chatbot App")
        #self.window.resizable(width=False, height=False)
        self.window.configure(width=600, height=800)

        # Header
        header = tk.Label(self.window, text="Chatbot using AI", pady=10, font=("Small Fonts", 20), bg="#ecf8f8")
        header.place(relwidth=1)

        # Div
        line = tk.Label(self.window, width=450, bg=theme_colour)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text widget
        self.text_widget = tk.Text(self.window, width=20, height=2, fg="#3d405b", bg="#f4f1de", padx=15, pady=10, 
                            wrap=tk.WORD, font=("Small Fonts", 14), relief=tk.FLAT)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        self.text_widget.tag_config('user', foreground=user_text_colour)
        self.text_widget.tag_config('bot', foreground=bot_text_colour)

        # Scrollbar
        scrollbar = tk.Scrollbar(self.window)
        scrollbar.place(relheight=0.72, relx=0.97, rely=0.09)
        scrollbar.configure(command=self.text_widget.yview)
        self.text_widget['yscrollcommand'] = scrollbar.set

        # Footer
        footer = tk.Label(self.window, height=75, bg=theme_colour)
        footer.place(relwidth=1, rely=0.825)

        # Message entry box
        self.msg_entry = tk.Entry(footer, bg="#ecf8f8", font=("Small Fonts", 18), relief=tk.FLAT, fg="#3d405b", justify="center")
        self.msg_entry.place(relwidth=0.74, relheight=0.085, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # Send button
        send_button = tk.Button(footer, text="SEND", width=20, command=lambda: self._on_enter_pressed(None), relief=tk.FLAT, bg="#ecf8f8", font=("Small Fonts", 22), fg="#3d405b")
        send_button.place(relx=0.77, rely=0.008, relheight=0.085, relwidth=0.22)

    def _on_enter_pressed(self, event):
        # event that happens after enter key is pressed (after user input)
        # Saves the input as msg, and displays it on screen from "you"
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        # If user has asked to play a game, start running the game instead of getting the chatbot response.
        if msg == "play the number guessing game" or msg == "play number guesser" or self.game == "numberguessinggame":
            if self.game != "numberguessinggame":
                self.print(150, "try and guess my number in the least amount of guesses. It is between 1 and 100")
                self.number = randint(0, 100)
                self.guesses = 0
            self.game = "numberguessinggame"
        elif msg == "play the magic eight ball" or msg == "play the magic 8 ball" or msg == "play magic 8 ball" or msg == "play magic eight ball" or self.game == "magic8ball":
            if self.game != "magic8ball":
                self.printt(150, "enter your yes/no question below. I will consult with the magic eight ball and give you a response.")
            self.game = "magic8ball"
        elif msg == "play scissors paper rock" or msg == "play rock paper scissors" or self.game == "scissorspaperrock" or self.game == "scissorspaperrock2":
            if self.game != "scissorspaperrock":
                self.printt(150, "please enter 'scissors'(1), 'paper'(2), or 'rock(3) to play.'")
            self.game = "scissorspaperrock"
        else:
            self.printt(150, bot.get_response(msg))

    def _insert_message(self, msg, sender):
        if not msg:
            # Nothing happens if user pressed enter without input
            return
        else:
            # Inserts message on the main text field
            self.msg_entry.delete(0, tk.END)

            msg1 = f"{sender}: {msg}\n\n"
            self.text_widget.configure(state=tk.NORMAL)
            self.text_widget.insert(tk.END, msg1, 'user')
            self.text_widget.configure(state=DISABLED)

            self.text_widget.see(tk.END)

        # Runs the appropriate game function for 'self.game'
        if self.game == "numberguessinggame":
            self.numberguessinggame(msg)
        elif self.game == "magic8ball":
            self.magic8ball(msg)
        elif self.game == "scissorspaperrock":
            self.scissorspaperrock(msg)
        elif self.game == "scissorspaperrock2":
            print("DEBUG: ScissorsPaperrock part 2 started")
            self.scissorspaperrock2(msg)
        
    def reply(self, msg):
        # Displays bot's response on screen from "bot", and stylised with the "bot" tag.
        msg = f"bot: {msg}\n\n"
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, msg, 'bot')
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(tk.END)

    def printt(self, ms, msg):
        # Function that calls 'reply' after the specified amount of milliseconds
        self.text_widget.after(ms, self.reply, msg)

    # ------------------------------------------------------------------------------------------------

    def numberguessinggame(self, msg):
        try:
            guess = int(msg)
            if guess > self.number:
                self.printt(150, "lower")
                self.guesses += 1
            elif guess < self.number:
                self.printt(150, "higher")
                self.guesses += 1
            elif guess == self.number: 
                self.printt(150, "you guessed it!")
                self.guesses += 1
                self.printt(200, ("You took " + str(self.guesses) + " guesses."))
                if self.ngg_record == 0 or self.ngg_record > self.guesses:
                    self.ngg_record = self.guesses
                self.printt(350, ("Your record is " + str(self.ngg_record) + " guesses."))

                self.game = "none"
        except ValueError:
            self.printt(150, "maybe try entering a number")

    def magic8ball(self, msg):
        print("DEBUG: magic8ball started")
        if msg == "q" or msg == "Q" or msg == "quit":
            self.game = "none"
        else:
            print("DEBUG: continuing with magic8ball")
            answers = ["It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes definitely.",
            "You may rely on it.",

            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",

            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",

            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
            answer = choice(answers)
            self.printt(150, answer)
            self.printt(300, "Enter your yes/no question below. If you wish to quit, enter 'Q'")
            
    def scissorspaperrock(self, msg):
        # First part is the main game loop
        print("DEBUG: scissors paper rock part 1")
        computeroptions = ["scissors", "paper", "rock"]
        computerselection = choice(computeroptions)
        if msg == "scissors" or msg == "1":
            self.printt(150, "scissors vs...")
            playerselection = "scissors"
        elif msg == "paper" or msg == "2":
            self.printt(150, "paper vs...")
            playerselection = "paper"
        elif msg == "rock" or msg == "3":
            self.printt(150, "rock vs...")
            playerselection = "rock"
        else:
            self.printt(150, "Please enter 'scissors', 'paper', 'rock', or their corresponding numbers.")
            playerselection = "none"
        
        if playerselection != "none":
            self.printt(1000, computerselection)

            if computerselection == playerselection:
                self.printt(1200, "It's a tie!")
                self.spr_ties += 1
            elif playerselection == 'rock' and computerselection == 'scissors':
                self.printt(1200, 'You win!')
                self.spr_wins += 1
            elif playerselection == 'paper' and computerselection == 'rock':
                self.printt(1200, 'You win!')
                self.spr_wins += 1
            elif playerselection == 'scissors' and computerselection == 'paper':
                self.printt(1200, 'You win!')
                self.spr_wins += 1
            elif playerselection == 'rock' and computerselection == 'paper':
                self.printt(1200, 'You lose!')
                self.spr_losses += 1
            elif playerselection == 'paper' and computerselection == 'scissors':
                self.printt(1200, 'You lose!')
                self.spr_losses += 1
            elif playerselection == 'scissors' and computerselection == 'rock':
                self.printt(1200, 'You lose!')
                self.spr_losses += 1

            self.printt(1500, ("wins: " + str(self.spr_wins)))
            self.printt(1500, ("losses: " + str(self.spr_losses)))
            self.printt(1500, ("ties: " + str(self.spr_ties)))

            self.printt(2500, "Do you want to play again?")
            self.game = "scissorspaperrock2"

    def scissorspaperrock2(self, msg):
        # Second part is to get response from "do you want to play again"
        print("DEBUG: scissorspaperrock part 2")
        if msg == "yes" or msg == "y":
            self.game = "scissorspaperrock"
            self.printt(300, "please enter 'scissors'(1), 'paper'(2), or 'rock(3) to play.'")
        elif msg == "no" or msg == "n":
            self.game = "none"
        else: 
            self.printt(150, "Please enter either 'yes' or 'no'")

if __name__ == "__main__":
    app = application()
    bot = chatbot()
    app.run()
