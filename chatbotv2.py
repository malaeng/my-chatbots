import tkinter as tk
from tkinter.constants import DISABLED
from random import randint, choice

class chatbotapp:
    def __init__(self):
        self.window = tk.Tk()
        self._setup_main_window()
        self.game = "startup"
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
        header = tk.Label(self.window, text="Gamebot", pady=10, font=("Small Fonts", 20), bg="#ecf8f8")
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

    def _insert_message(self, msg, sender):
        if not msg:
            # Nothing happens if user pressed enter without input
            return
        elif msg == "!@#skipstart!@#" and sender == "skip":
            # Eliminates an issue where bot asks for input twice before game select.
            self.msg_entry.delete(0, tk.END)
        else:
            # Inserts message on the main text field
            self.msg_entry.delete(0, tk.END)

            msg1 = f"{sender}: {msg}\n\n"
            self.text_widget.configure(state=tk.NORMAL)
            self.text_widget.insert(tk.END, msg1, 'user')
            self.text_widget.configure(state=DISABLED)

            self.text_widget.see(tk.END)

        if self.game == "startup":
            greetings = ["hi.", "hey!", "hi there.", "Hello!", "greetings."]
            self.printt(150, choice(greetings))
            self.printt(300, "What is your name?")
            self.game = "startup2"
        elif self.game == "startup2":
            self.startup2(msg)
        elif self.game == "startup3":
            self.startup3(msg)
        elif self.game == "gameselect":

            self.printt(450, "What game would you like to play, " + self.name + "?")
            self.printt(600, "Currently I am programmed with 3 options:")

            self.printt(700, "enter (1) to play the number guessing game")
            self.printt(800, "enter (2) to play the magic 8 ball")
            self.printt(900, "enter (3) to play scissors paper rock")
            #self.printt(1000, "enter (4) to play gambling games.")
            self.game = "gameselect2"
        elif self.game == "gameselect2":
            self.gameselect2(msg)
        elif self.game  == "gambleselect":
            self.gambleselect(msg)


            self.gambleselect(msg)
        elif self.game == "numberguessinggame":
            self.numberguessinggame(msg)
        elif self.game == "magic8ball":
            self.magic8ball(msg)
        elif self.game == "scissorspaperrock":
            self.scissorspaperrock(msg)
        elif self.game == "scissorspaperrock2":
            print("DEBUG: ScissorsPaperrock part 2 initiated")
            self.scissorspaperrock2(msg)
        #print("DEBUG: ran _insert_message")
        
    def reply(self, msg):              
        msg = f"bot: {msg}\n\n"
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, msg, 'bot')
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(tk.END)

    def printt(self, ms, msg):
        self.text_widget.after(ms, self.reply, msg)

    # ------------------------------------------------------------------------------------------------

    def startup2(self, msg):
        print("DEBUG: Running startup2")
        self.name = msg
        self.printt(150, ("Hello, " + self.name + "!"))
        self.printt(300, "It's lovely to meet you.")
        self.printt(450, "How old are you, " + self.name + "?")
        self.game = "startup3"

    def startup3(self, msg):
        print("DEBUG: Running startup3")
        try:
            # bot comments on users age
            self.age = int(msg)
            if self.age <= 3:
                self.printt(150, "Really? They're sending me babies?")
            elif self.age > 3 and self.age < 18:
                self.printt(150, "Ah. A child.")
            elif self.age >= 18 and self.age < 60:
                self.printt(150, "So you're an adult. Interesting.")
            elif self.age >= 60 and self.age < 100:
                self.printt(150, "You're an old man lol")
            elif self.age >= 100:
                self.printt(150, "I'm impressed. That's pretty old. Or you're lying. That wouldn't be very cool.")
            else:
                self.printt(("I'm no expert on how the world works, but I don't think that's possible."))


            self.printt(300, "I am not really advanced enough to have an actual conversation with you.")
            self.printt(450, "So instead, I thought we could play some fun games together.")

            self.game = "gameselect"
            self._insert_message("!@#skipstart!@#", "skip")
        except ValueError:
            # If user doesn't enter a number, ask them to try again.
            self.printt(150, "That's not a number! try again")

    def gameselect2(self, msg):
        print("DEBUG: running gameselect2")
        # Ask user what game they would like to play.
        if msg == "1":
            self.game = "numberguessinggame"
            print("you chose 1")
            self.printt(150, "You chose the number guessing game.") 
            self.printt(200, "The aim of this game is to guess the number (1-100) in the least amount of tries")
            self.printt(200, "As you guess, I will give you hints.")
            self.printt(200, "Enter your guesses below:")
            self.number = randint(0, 100)
            self.guesses = 0
        elif msg == "2":
            self.game = "magic8ball"
            self.printt(150, "Enter your yes/no question below. If you wish to quit, enter 'Q'")
        elif msg == "3":
            self.game = "scissorspaperrock"
            self.printt(150, "You chose scissors paper rock.")
            self.printt(300, "please enter 'scissors'(1), 'paper'(2), or 'rock(3) to play.'")
        else: 
            self.printt(150, "Please enter 1, 2, or 3.")
        '''
        elif msg == "4":
            self.game = "gambleselect"
            self.printt(150, "So you want to gamble?")
            if self.age < 18:
                self.printt(300, "Sorry, you are not old enough to gamble")
                self.game = "gameselect"
                self._insert_message("!@#skipstart!@#", "skip")
            else:
                self.printt(300, "I was just joking!")
                self.printt(300, "I don't condone gambling")
                self.game = "gameselect"
                self._insert_message("!@#skipstart!@#", "skip")
                #self.printt(300, "Great! I love gambling")
                #self.printt(450, "currently, I am programmed with 2 gambling games:")

                #self.printt(600, "Enter (1) to play Chō-Han")
                #self.printt(700, "Enter (2) to play the coin toss")
                # Other ideas: blackjack
        '''

    def gambleselect(self, msg):
        print("DEBUG: running gambleselect...")
        if msg == "1":
            self.game = "cho-han"
        elif msg == "2":
            self.game = "cointoss"

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

                self.game = "gameselect"
                self._insert_message("!@#skipstart!@#", "skip")
        except ValueError:
            self.printt(150, "maybe try entering a number")

    def magic8ball(self, msg):
        print("DEBUG: magic8ball started")
        if msg == "q" or msg == "Q" or msg == "quit":
            self.game = "gameselect"
            self._insert_message("!@#skipstart!@#", "skip")
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
        print("DEBUG: scissorspaperrock part 2")
        if msg == "yes" or msg == "y":
            self.game = "scissorspaperrock"
            self.printt(300, "please enter 'scissors'(1), 'paper'(2), or 'rock(3) to play.'")
        elif msg == "no" or msg == "n":
            self.game = "gameselect"
            self._insert_message("!@#skipstart!@#", "skip")
        else: 
            self.printt(150, "Please enter either 'yes' or 'no'")

if __name__ == "__main__":
    app = chatbotapp()
    app.run()