#------------------importing tkinter------------------#
from tkinter import *
import random
import time

#------------------constants------------------#
THEME_COLOR = "#0366fc"
MYFONT = ("Times", 18, "italic")


#------------------60-item na trivia quiz------------------#
trivia_data = {
    "What is the capital of France?": "paris",
    "What gas do plants absorb?": "carbon dioxide",
    "Who painted the Mona Lisa?": "leonardo da vinci",
    "What planet is known as the Red Planet?": "mars",
    "How many days are in a leap year?": "366",
    "What is H2O commonly known as?": "water",
    "What is the largest animal on Earth?": "blue whale",
    "What is the fastest land animal?": "cheetah",
    "How many continents are there?": "7",
    "What is the tallest mountain?": "mount everest",
    "Who was the first person to walk in the moon?": "neil armstrong",
    "What is the boiling point of water in °C?": "100",
    "What galaxy do we live in?": "milky way",
    "What instrument has keys, pedals, and strings?": "piano",
    "What is the hardest natural substance?": "diamond",
    "How many bones does an adult have?": "206",
    "What is the largest ocean?": "pacific ocean",
    "What is the currency of Japan?": "yen",
    "What is the closest star to Earth?": "sun",
    "Which animal is known as the King of the Jungle?": "lion",
    "How many planets are in the solar system?": "8",
    "How many islands in the Philippines?": "7641",
    "What is the capital of Japan?": "tokyo",
    "What is the process that turns a caterpillar into a butterfly?": "metamorphosis",
    "What makes blood red?": "hemoglobin",
    "What part of the body pumps blood?": "heart",
    "Which river carries the most water in the world?": "amazon",
    "What is the smallest unit of matter?": "atom",
    "Where does the strongest earthquake ever recorded?": "chile",
    "What is the largest continent?": "asia",
    "What is the only flying mammal?": "bat",
    "What language is spoken in Spain?": "spanish",
    "What is the capital of Italy?": "rome",
    "What is a baby kangaroo?": "joey",
    "What animal gives us wool?": "sheep",
    "How many hearts does an octopus have?": "3",
    "What is the hottest planet in the solar system?": "venus",
    "How many days does it take for the earth to orbit the sun?": "365",
    "Who invented the telephone?": "alexander graham bell",
    "How many letters are in the English alphabet?": "26",
    "In Greek mithology, who is the god of the sea?": "poseidon",
    "What is the capital of Canada?": "ottawa",
    "Who is the king of the gods and the ruler of mount olympus?": "zues",
    "What is the longest river?": "nile",
    "How many elements are on the periodic table?": "118",
    "Which city is known as te summer capital of the Philippines?": "baguio",
    "What is the square root of 9?": "3",
    "How many legs do insects have?": "6",
    "What gas do humans inhale?": "oxygen",
    "What is the capital of the UK?": "london",
    "What is the main language in Brazil?": "portuguese",
    "Which ocean is the warmest?": "indian ocean",
    "What planet is closest to the sun?": "mercury",
    "What month has 28 days?": "february",
    "How many colors are in a rainbow?": "7",
    "What is the oldest city of the Philippines?": "cebu",
    "What organ allows us to breathe?": "lungs",
    "What is the only even prime number?": "2",
}



#------------------UI ng Trivia Quiz------------------#
class TriviaGame_UI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Trivia Quiz Game")
        self.window.config(bg=THEME_COLOR)
        self.window.geometry("500x520")

        self.questions =random.sample (list(trivia_data.keys()), 20)
        self.skipped = []
       
        self.index = 0
        self.score = 0

        self.build_front_page()
        self.window.mainloop()

    # -----------------FRONT PAGE------------------#
    def build_front_page(self):
        self.label_title = Label(text="Trivia Game", bg="#4e90ed", font=("Times", 35, "bold"))
        self.label_title.pack(pady=40)

        self.label_fname = Label(text="Enter first name:", bg="#4e90ed", font=("Times", 14))
        self.label_fname.pack()
        self.entry_fname = Entry(width=30, font=("Times", 14))
        self.entry_fname.pack(pady=5)

        self.label_lname = Label(text="Enter last name:", bg="#4e90ed", font=("Times", 14))
        self.label_lname.pack()
        self.entry_lname = Entry(width=30, font=("Times", 14))
        self.entry_lname.pack(pady=5)
        self.button_start = Button(text="Start Game", bg="#20e620", font=("Times", 15),
                                   command=self.start_game)
        self.button_start.pack(pady=20)

    # --------------------START GAME------------------#
    def start_game(self):
        self.first_name = self.entry_fname.get().strip()
        self.last_name = self.entry_lname.get().strip()

        if not self.first_name or not self.last_name:
            self.label_title.config(text="Enter your full name!", fg="#e82020")
            return

        if any(x.isdigit() for x in self.first_name + self.last_name):
            self.label_title.config(text="Name cannot contain digits!", fg="#e82020")
            return

        #-------------------------Remove front widgets-------------------------#
        self.label_title.pack_forget()
        self.label_fname.pack_forget()
        self.entry_fname.pack_forget()
        self.label_lname.pack_forget()
        self.entry_lname.pack_forget()
        self.button_start.pack_forget()

        #--------------------QUIZ WIDGETS-----------------------------#
        self.label_question = Label(text="", bg=THEME_COLOR, font=MYFONT, wraplength=500)
        self.label_question.pack(pady=40)

        self.entry_answer = Entry(width=30, font=MYFONT)
        self.entry_answer.pack()

        self.frame_buttons = Frame(self.window, bg=THEME_COLOR)
        self.frame_buttons.pack(pady=10)
        self.button_submit = Button(self.frame_buttons, text="Submit", width=10,
                                    bg="#20e620", font=("Times", 14), command=self.check_answer)
        self.button_submit.grid(row=0, column=0, padx=10)

        self.button_skip = Button(self.frame_buttons, text="Skip", width=10,
                                  bg="#e82020", font=("Times", 14), command=self.skip_question)
        self.button_skip.grid(row=0, column=1, padx=10)
        self.label_feedback = Label(text="", bg=THEME_COLOR, font=MYFONT)
        self.label_feedback.pack()
        self.label_score = Label(text=f"Score: {self.score}", bg=THEME_COLOR, font=MYFONT)
        self.label_score.pack()
        self.label_timer = Label(text="Time: 15", fg="#e82020", bg=THEME_COLOR, font=MYFONT)
        self.label_timer.pack()
        self.show_question()

    #-------------------------------SHOW QUESTION------------------------------#
    def show_question(self):
        if self.index >= len(self.questions):
            if self.skipped:
                self.questions = self.skipped
                self.skipped = []
                self.index = 0
            else:
                self.end_game()
                return
           
        q = self.questions[self.index]
        self.label_question.config(text=f"Q{self.index+1}: {q}")
        self.entry_answer.delete(0, END)
        self.label_feedback.config(text="")
        self.timer_seconds = 25
        self.update_timer()

    #------------------TIMER------------------------#
    def update_timer(self):
        self.label_timer.config(text=f"Time: {self.timer_seconds}")
        
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_id = self.window.after(1000, self.update_timer)
        else:
            self.flash_color("#e82020")
            self.label_feedback.config(text="Time's up!", fg="red")
            self.index += 1
            self.window.after(900, self.show_question)

    #------------------FLASH EFFECT (red or green)---------------#
    def flash_color(self, color):
        original = self.window.cget("bg")
        self.window.config(bg=color)
        self.window.after(300, lambda: self.window.config(bg=original))

    #-----------------CHECK ANSWER--------------#
    def check_answer(self):
        answer = self.entry_answer.get().lower().strip()

        if answer == "":
            self.label_feedback.config(text="Enter an answer!", fg="#e82020")
            return
       
        self.window.after_cancel(self.timer_id)
        correct = trivia_data[self.questions[self.index]]
        if answer == correct:
            self.score += 1
            self.label_feedback.config(text="Correct!", fg="#20e620")
            self.flash_color("#20e620")
        else:
            self.label_feedback.config(text=f"Wrong! Answer: {correct}", fg="#e82020")
            self.flash_color("#e82020")

        self.label_score.config(text=f"Score: {self.score}")
        self.index += 1
        self.window.after(900, self.show_question)

    #-----------------SKIP QUESTION-------------------#
    def skip_question(self):
        self.window.after_cancel(self.timer_id)
        self.skipped.append(self.questions[self.index])
        self.index += 1
        self.window.after(400, self.show_question)

    #-----------------END GAME-----------------#
    def end_game(self):
        self.label_question.pack_forget()
        self.entry_answer.pack_forget()
        self.frame_buttons.pack_forget()
        self.label_feedback.pack_forget()
        self.label_score.pack_forget()
        self.label_timer.pack_forget()

        percent = self.score / 20
        if percent >= 0.9:
            rating = "Excellent!"
            color = "green"
        elif percent >= 0.7:
            rating = "Very Good!"
            color = "green"
        elif percent >= 0.5:
            rating = "Good!"
            color = "orange"
        elif percent >= 0.3:
            rating = "Needs Improvement"
            color = "orange"
        else:
            rating = "Try Again"
            color = "red"

        Label(text=f"Well played {self.first_name}!",
              font=("Times", 38, "bold"), bg=THEME_COLOR).pack(pady=30)
        Label(text=f"Score: {self.score}/20",
              font=("Times", 25, "bold"), bg=THEME_COLOR).pack()
        Label(text=rating, font=("Times", 30, "bold"),
              fg=color, bg=THEME_COLOR).pack(pady=10)
       
        #-----------------------Save high score-----------------------#
        with open("scores.txt", "a") as f:
            f.write(f"{self.first_name} {self.last_name} - {self.score}/20\n")
        Label(text="High Scores:", font=("Times", 22, "bold"),
              bg=THEME_COLOR).pack(pady=10)
        try:
            with open("scores.txt", "r") as f:
                for line in f.readlines()[-5:]:
                    Label(text=line.strip(), font=("Times", 16),
                          bg=THEME_COLOR).pack()
        except:
            Label(text="No high scores yet.", bg=THEME_COLOR).pack()

        #----------------------PLAY AGAIN BUTTON-------------------------#
        Button(text="Play Again", bg="#20e620", font=("Times", 20),
               command=self.restart).pack(pady=20)
       
    def restart(self):
        self.window.destroy()
        TriviaGame_UI()

#------------------start ng main------------------#
game = TriviaGame_UI()