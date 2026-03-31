import tkinter as tk
import tkinter.messagebox as tk_msgbox

# ---------------------------- KONFIGURACJA ---------------------------- #
COLOR_PINK = "#e2979c"
COLOR_RED = "#e7305b"
COLOR_GREEN = "#9bdeac"
COLOR_YELLOW = "#f7f5dd"

FONT_NAME = "Courier"

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 300

SECONDS_IN_MINUTE = 60
WORK_DURATION = 25 * SECONDS_IN_MINUTE
SHORT_BREAK_DURATION = 5 * SECONDS_IN_MINUTE
LONG_BREAK_DURATION = 20 * SECONDS_IN_MINUTE

POMODORO_STAGES = [
    ("PRACA", WORK_DURATION),
    ("KRÓTKA PRZERWA", SHORT_BREAK_DURATION),
    ("PRACA", WORK_DURATION),
    ("KRÓTKA PRZERWA", SHORT_BREAK_DURATION),
    ("PRACA", WORK_DURATION),
    ("KRÓTKA PRZERWA", SHORT_BREAK_DURATION),
    ("PRACA", WORK_DURATION),
    ("DŁUGA PRZERWA", LONG_BREAK_DURATION),
]

# ---------------------------- STAN APLIKACJI ---------------------------- #
current_stage_index = 0
after_job_id = None


# ---------------------------- FUNKCJE POMOCNICZE ---------------------------- #
def update_canvas_text(text_id, value):
    canvas.itemconfig(text_id, text=value)


def format_time(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes:02}:{remaining_seconds:02}"


def update_timer_display(seconds):
    update_canvas_text(timer_text_id, format_time(seconds))


def update_status_display(status):
    update_canvas_text(status_text_id, status)


def show_stage_finished_popup():
    tk_msgbox.showinfo("Pomodoro", "Czas uplynal")


def move_to_next_stage():
    global current_stage_index
    current_stage_index = (current_stage_index + 1) % len(POMODORO_STAGES)


# ---------------------------- OBSŁUGA TIMERA ---------------------------- #
def start_timer():
    global after_job_id

    if after_job_id is not None:
        return

    stage_name, stage_duration = POMODORO_STAGES[current_stage_index]
    update_status_display(stage_name)
    countdown(stage_duration)


def reset_timer():
    global after_job_id, current_stage_index

    if after_job_id is not None:
        window.after_cancel(after_job_id)
        after_job_id = None

    current_stage_index = 0
    update_status_display("POMODORO")
    update_timer_display(WORK_DURATION)


def countdown(seconds_left):
    global after_job_id

    update_timer_display(seconds_left)

    if seconds_left > 0:
        after_job_id = window.after(1000, countdown, seconds_left - 1)
    else:
        after_job_id = None
        show_stage_finished_popup()
        move_to_next_stage()
        start_timer()


# ---------------------------- UI ---------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=30, bg=COLOR_YELLOW)

canvas = tk.Canvas(
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
    bg=COLOR_YELLOW,
    highlightthickness=0,
)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=tomato_image)

timer_text_id = canvas.create_text(
    CANVAS_WIDTH / 2,
    CANVAS_HEIGHT * 0.55,
    font=(FONT_NAME, 30, "bold"),
    text=format_time(WORK_DURATION),
    fill="white",
)

status_text_id = canvas.create_text(
    CANVAS_WIDTH * 0.525,
    CANVAS_HEIGHT * 0.05,
    font=(FONT_NAME, 30, "bold"),
    text="POMODORO",
    fill=COLOR_PINK,
)

canvas.grid(column=1, row=0)

start_button = tk.Button(
    text="Start",
    font=(FONT_NAME, 10, "bold"),
    command=start_timer,
)
start_button.grid(column=0, row=1)

reset_button = tk.Button(
    text="Reset",
    font=(FONT_NAME, 10, "bold"),
    command=reset_timer,
)
reset_button.grid(column=2, row=1)

window.mainloop()
