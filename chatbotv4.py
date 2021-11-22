import tkinter as tk
from tkinter.constants import DISABLED
from random import randint, choice
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# TODO: address user by name --> replace $$user$$ in yml files with username
# TODO: add games from previous bot

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
   
    def run(self):
        self.window.mainloop()
    
    def _setup_main_window(self):
        theme_colour = "#2e1f27"
        user_text_colour = "#3d405b"
        bot_text_colour = "#e07a5f"
        mainfont = "consolas"

        self.window.title("Chatbot App")
        #self.window.resizable(width=False, height=False)
        self.window.configure(width=600, height=800)

        # Header
        header = tk.Label(self.window, text="Chatbot using AI", pady=10, font=(mainfont, 20), bg="#ecf8f8")
        header.place(relwidth=1)

        # Div
        line = tk.Label(self.window, width=450, bg=theme_colour)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text widget
        self.text_widget = tk.Text(self.window, width=20, height=2, fg="#3d405b", bg="#f4f1de", padx=15, pady=10, 
                            wrap=tk.WORD, font=(mainfont, 14), relief=tk.FLAT)
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
        self.msg_entry = tk.Entry(footer, bg="#ecf8f8", font=(mainfont, 18), relief=tk.FLAT, fg="#3d405b", justify="center")
        self.msg_entry.place(relwidth=0.74, relheight=0.085, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # Send button
        send_button = tk.Button(footer, text="SEND", width=20, command=lambda: self._on_enter_pressed(None), relief=tk.FLAT, bg="#ecf8f8", font=(mainfont, 22), fg="#3d405b")
        send_button.place(relx=0.77, rely=0.008, relheight=0.085, relwidth=0.22)

    def _on_enter_pressed(self, event):
        # event that happens after enter key is pressed (after user input)
        # Saves the input as msg, and displays it on screen from "you"
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        self.printt(150, bot.get_response(msg))

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

        
    def reply(self, msg):              
        msg = f"bot: {msg}\n\n"
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, msg, 'bot')
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(tk.END)

    def printt(self, ms, msg):
        self.text_widget.after(ms, self.reply, msg)

if __name__ == "__main__":
    app = application()
    bot = chatbot()
    app.run()




