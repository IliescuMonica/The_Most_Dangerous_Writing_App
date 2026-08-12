# ---------------------------- IMPORT LIBRARIES ------------------------------- #
from tkinter import *
from tkinter.ttk import Progressbar , Style

# ---------------------------- GLOBAL ------------------------------- #
timer = False
timer_id = None
decrease_id = None
timer_seconds = 0

# ---------------------------- FUNCTIONS ------------------------------- #
def start_timer(event): # triggered when user presses any key
    global timer, timer_id, timer_seconds, decrease_id
    # Get the timer duration based on the selected difficulty
    timer_seconds = set_difficulty()

    if not timer:
        timer = True
        # Reset the progress bar to the selected difficulty
        progress["maximum"] = timer_seconds
        progress["value"] = timer_seconds
        # Start decreasing the progress bar
        decrease_progress()
        # Delete the text if the user stops typing
        timer_id = window.after(timer_seconds * 1000, delete_text)

    else:
        # Reset the progress bar every time the user types
        progress["value"] = timer_seconds
        # Cancel the previous delete timer
        window.after_cancel(timer_id)
        # Cancel the previous progress countdown
        if decrease_id is not None:
            window.after_cancel(decrease_id)
        # Start the progress countdown again
        decrease_progress()
        # Start a new delete timer
        timer_id = window.after(timer_seconds * 1000, delete_text)


def delete_text():
    global timer, timer_id,decrease_id
    # Delete all text from the text box
    user_input_box.delete(1.0,"end")
    # Reset the timer state
    timer = False
    timer_id = None
    # Stop the progress bar countdown
    if decrease_id is not None:
        window.after_cancel(decrease_id)

    decrease_id = None

    # Reset the progress bar
    progress["value"] = timer_seconds

def decrease_progress():
    global decrease_id
    # Decrease the progress bar gradually
    if progress["value"] > 0:
        progress["value"] -= 0.1
        # Call this function again after 100 milliseconds
        decrease_id =window.after(100,decrease_progress)

def set_difficulty():
    # Set the timer duration based on the selected difficulty
    if difficulty.get() == "Chill":
        return 15
    elif difficulty.get() == "Dangerous":
        return 10
    elif difficulty.get() == "INSANE":
        return 5



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("The Most Dangerous Writing App")
window.config(padx=100,pady=50,bg="#1e1e1e")

# ---------------------------- TITLE ------------------------------- #
title = Label(
    window,
    text="THE MOST DANGEROUS WRITING APP",
    bg="#1e1e1e",
    fg="white",
    font=("Helvetica", 24, "bold")
)
title.grid(row=0, column=1, pady=(0, 10))

subtitle = Label(
    window,
    text="Keep writing. Don't stop.",
    bg="#1e1e1e",
    fg="#aaaaaa",
    font=("Helvetica", 11)
)
subtitle.grid(row=1, column=1, pady=(0, 20))

# ---------------------------- PROGRESS BAR ------------------------------- #
style = Style()
style.theme_use("clam")
style.configure(
    "Custom.Horizontal.TProgressbar",
    troughcolor="#333333",
    background="#e74c3c",
    bordercolor="#333333",
    lightcolor="#e74c3c",
    darkcolor="#e74c3c"
)

# ---------------------------- DIFFICULTY ------------------------------- #
difficulty_options = ["Chill", "Dangerous", "INSANE"]

difficulty = StringVar()
difficulty.set(difficulty_options[0])

difficulty_frame = Frame(window, bg="#1e1e1e")
difficulty_frame.grid(row=3, column=1, pady=10)


difficulty_label = Label(
    difficulty_frame,
    text="Difficulty:",
    bg="#1e1e1e",
    fg="white",
    font=("Helvetica", 11)
)
difficulty_label.pack(side="left", padx=5)


difficulty_button = OptionMenu(
    difficulty_frame,
    difficulty,
    *difficulty_options
)
difficulty_button.pack(side="left", padx=5)

# ---------------------------- PROGRESS BAR ------------------------------- #
progress = Progressbar(window,orient=HORIZONTAL,length=500,mode='determinate',style="Custom.Horizontal.TProgressbar")

timer_seconds = set_difficulty()

progress["maximum"] = timer_seconds
progress["value"] = timer_seconds

progress.grid(row=2,column=1,padx=10,pady=10)

# ---------------------------- TEXT BOX ------------------------------- #
user_input_box = Text(
    window,
    width=100,
    height=30,
    bg="#252526",
    fg="#f1f1f1",
    insertbackground="white",
    font=("Helvetica", 14),
    relief="flat",
    padx=15,
    pady=15
)
user_input_box.bind("<Key>", start_timer)
user_input_box.grid(row=4,column=1,columnspan=1,ipady=1)


window.mainloop()