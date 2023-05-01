from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
vis_timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global repetitions
    window.after_cancel(vis_timer)
    timer_lbl.config(text="Timer", foreground=GREEN)
    canvas.itemconfig(timer, text="00:00")
    check_lbl.config(text="")
    repetitions = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repetitions
    repetitions += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if repetitions == 8:
        timer_lbl.config(text="Break", foreground=RED)
        countdown(long_break_sec)
    elif repetitions % 2 == 1:
        timer_lbl.config(text="Work", foreground=GREEN)
        countdown(work_sec)
    else:
        timer_lbl.config(text="Break", foreground=PINK)
        countdown(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global vis_timer
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        vis_timer = window.after(5, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(repetitions // 2):
            marks += "✔"
        check_lbl.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_lbl = Label(text="Timer", font=(FONT_NAME, 40), foreground=GREEN, background=YELLOW)
timer_lbl.grid(row=0, column=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

check_lbl = Label(foreground=GREEN, background=YELLOW)
check_lbl.grid(row=3, column=1)


window.mainloop()
