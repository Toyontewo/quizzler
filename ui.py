from tkinter import *
from quiz_brain import QuizBrain
from data import question_data

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        self.exit_btn = Button(text="Exit", highlightbackground=THEME_COLOR, command=self.end_window)
        self.exit_btn.grid(row=0, column=0)

        self.score_title = Label(text=f"Score:{self.score}", bg=THEME_COLOR, fg="white")
        self.score_title.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="All is well",
                                                     fill=THEME_COLOR,
                                                     font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_img = PhotoImage(file="images/true.png")
        self.check_btn = Button(image=check_img, highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.check_btn.grid(row=2, column=1)

        wrong_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=wrong_img, highlightbackground=THEME_COLOR, command=self.false_pressed)
        self.false_btn.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def end_window(self):
        self.window.destroy()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_title.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the Quiz, Your score is {self.quiz.score}")
            self.check_btn.config(state="disabled")
            self.false_btn.config(state="disabled")


    def true_pressed(self):
        # self.score += 1
        # self.score_title.config(text=f"Score:{self.score}")
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

