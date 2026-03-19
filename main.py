import random
import threading
import time
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 300
POMODORO_UNIT = 25*60

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
counting_down = False
reset = False
score = 0

def start_timer():
    global counting_down
    if not counting_down:
        count_down(POMODORO_UNIT)
        counting_down = True

def reset_timer():
    global reset
    reset = True

counting_down = False

timer = None
limit = 10
window = tkinter.Tk()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global counting_down, reset
    canvas.itemconfig(timer_txt, text=f"{int(count/60):02}:{count%60:02}")
    if count > 0 and not reset:
        window.after(1000, count_down, count-1)
    else:
        counting_down = False
        reset = False
        canvas.itemconfig(timer_txt, text=f"{int(POMODORO_UNIT/60):02}:{POMODORO_UNIT%60:02}")

# ---------------------------- UI SETUP ------------------------------- #
window.title("Pomodoro")
window.config(padx=50, pady=30, bg=YELLOW)

canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=tomato_img)
timer_txt = canvas.create_text(CANVAS_WIDTH*5/10, CANVAS_HEIGHT*5.5/10, font=(FONT_NAME, 30, "bold"), text=f"{int(POMODORO_UNIT/60):02}:{POMODORO_UNIT%60:02}", fill="white")
canvas.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=1)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column=2, row=1)

checkmark_label = tkinter.Label(text="This is old text")
checkmark_label.config(text="✔", font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=1)




window.mainloop()
