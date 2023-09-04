from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
     global reps, marks, timer
     window.after_cancel(timer)
     canvas.itemconfig(timer_text, text="00:00")
     text.config(text="Timer")
     check.config(text="")
     reps = 0
     marks = ""
     timer = None
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
     global reps
     reps += 1
     work_sec = WORK_MIN * 60
     short_break_sec = SHORT_BREAK_MIN * 60
     long_break_sec = LONG_BREAK_MIN * 60
     if reps % 2 == 1:
          text.config(text="Working Time", fg=GREEN)
          count_down(work_sec)
     if  reps % 2 == 0:
          text.config(text="Short Break", fg=PINK) 
          count_down(short_break_sec)
     if reps % 8 == 0 and reps % 2 == 0:
          text.config(text="Long break", fg=RED)
          count_down(long_break_sec)
          

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
     global marks, reps, timer
     count_min = math.floor(count / 60)
     count_sec = math.floor(count % 60)
     if count_sec < 10:
          count_sec = f"0{count_sec}"

     canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
     if count > 0:
          timer = window.after(1000, count_down, count-1)
     else:
          start_timer()
          marks = "" 
          for _ in range(reps-1):
               marks += "✔"
          check.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
text.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



button_start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
button_reset.grid(row=2, column=2)

check = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28))
check.grid(row=3, column=1)

window.mainloop()