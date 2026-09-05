import tkinter as tk

# ============================================================
# STRING DSA VISUALIZER
# ============================================================

window = tk.Tk()
window.title("String DSA Visualizer")
window.geometry("800x650")
window.configure(bg="#F5F7FA")
window.resizable(False, False)


# ============================================================
# STANDARD COLORS
# ============================================================

BG_COLOR = "#F5F7FA"
NAVY = "#1E3A5F"
BLUE = "#2563EB"
LIGHT_BLUE = "#EAF2F8"
WHITE = "#FFFFFF"
TEXT = "#263238"
BORDER = "#D5DDE5"
GREEN = "#198754"
RED = "#DC3545"


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    window,
    bg=NAVY,
    height=80
)
header.pack(fill="x")

title = tk.Label(
    header,
    text="STRING DSA VISUALIZER",
    bg=NAVY,
    fg=WHITE,
    font=("Arial", 24, "bold")
)
title.pack(pady=(15, 2))



# ============================================================
# INPUT SECTION
# ============================================================

input_frame = tk.Frame(
    window,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)
input_frame.pack(
    padx=50,
    pady=(25, 12),
    fill="x"
)

input_label = tk.Label(
    input_frame,
    text="Enter Your String",
    bg=WHITE,
    fg=TEXT,
    font=("Arial", 14, "bold")
)
input_label.pack(pady=(15, 8))

entry = tk.Entry(
    input_frame,
    font=("Arial", 16),
    width=40,
    justify="center",
    bg="#FAFBFC",
    fg=TEXT,
    relief="solid",
    bd=1
)
entry.pack(
    pady=(0, 18),
    ipady=6
)


# ============================================================
# RESULT BOX
# ============================================================

result_frame = tk.Frame(
    window,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)
result_frame.pack(
    padx=50,
    pady=6,
    fill="x"
)

result_heading = tk.Label(
    result_frame,
    text="RESULT",
    bg=LIGHT_BLUE,
    fg=NAVY,
    font=("Arial", 12, "bold"),
    anchor="w",
    padx=15
)
result_heading.pack(
    fill="x"
)

result = tk.Label(
    result_frame,
    text="Select an operation",
    bg=WHITE,
    fg=TEXT,
    font=("Arial", 15, "bold"),
    height=2
)
result.pack(
    fill="x",
    pady=5
)


# ============================================================
# LOGIC BOX
# ============================================================

logic_frame = tk.Frame(
    window,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)
logic_frame.pack(
    padx=50,
    pady=6,
    fill="x"
)

logic_heading = tk.Label(
    logic_frame,
    text="SHORT LOGIC",
    bg=LIGHT_BLUE,
    fg=NAVY,
    font=("Arial", 12, "bold"),
    anchor="w",
    padx=15
)
logic_heading.pack(
    fill="x"
)

logic = tk.Label(
    logic_frame,
    text="Operation logic will appear here",
    bg=WHITE,
    fg=TEXT,
    font=("Arial", 12),
    height=3,
    justify="left"
)
logic.pack(
    fill="x",
    pady=5
)


# ============================================================
# FUNCTION TO SHOW RESULT + LOGIC
# ============================================================

def show_result(result_text, logic_text, color=TEXT):

    result.config(
        text=result_text,
        fg=color
    )

    logic.config(
        text=logic_text,
        fg=TEXT
    )


# ============================================================
# REVERSE
# ============================================================

def reverse():

    s = entry.get()

    if s == "":
        show_result(
            "Please enter a string",
            "Logic: Enter a string first.",
            RED
        )
        return

    rev = s[::-1]

    show_result(
        rev,
        s + "  →  Reverse  →  " + rev,
        BLUE
    )


# ============================================================
# UPPERCASE
# ============================================================

def uppercase():

    s = entry.get()

    if s == "":
        show_result(
            "Please enter a string",
            "Logic: Enter a string first.",
            RED
        )
        return

    upper = s.upper()

    show_result(
        upper,
        s + "  →  Uppercase  →  " + upper,
        BLUE
    )


# ============================================================
# LOWERCASE
# ============================================================

def lowercase():

    s = entry.get()

    if s == "":
        show_result(
            "Please enter a string",
            "Logic: Enter a string first.",
            RED
        )
        return

    lower = s.lower()

    show_result(
        lower,
        s + "  →  Lowercase  →  " + lower,
        BLUE
    )


# ============================================================
# PALINDROME
# ============================================================

def palindrome():

    s = entry.get()

    if s == "":
        show_result(
            "Please enter a string",
            "Logic: Enter a string first.",
            RED
        )
        return

    rev = s[::-1]

    if s == rev:

        show_result(
            "✓ Palindrome",
            s + "  →  Reverse  →  " + rev +
            "\n" +
            s + " == " + rev +
            "  →  Palindrome",
            GREEN
        )

    else:

        show_result(
            "✗ Not Palindrome",
            s + "  →  Reverse  →  " + rev +
            "\n" +
            s + " != " + rev +
            "  →  Not Palindrome",
            RED
        )


# ============================================================
# COUNT CHARACTERS
# ============================================================

def count():

    s = entry.get()

    if s == "":
        show_result(
            "Please enter a string",
            "Logic: Enter a string first.",
            RED
        )
        return

    total = len(s)

    show_result(
        str(total) + " Characters",
        s + "  →  Count Characters  →  " + str(total),
        BLUE
    )


# ============================================================
# BUTTON SECTION
# ============================================================

button_frame = tk.Frame(
    window,
    bg=BG_COLOR
)
button_frame.pack(pady=15)


def create_button(text, command):

    return tk.Button(
        button_frame,
        text=text,
        command=command,
        width=13,
        height=2,
        bg=BLUE,
        fg=WHITE,
        activebackground=NAVY,
        activeforeground=WHITE,
        font=("Arial", 10, "bold"),
        relief="flat",
        cursor="hand2"
    )


create_button(
    "Reverse",
    reverse
).grid(row=0, column=0, padx=5)

create_button(
    "Uppercase",
    uppercase
).grid(row=0, column=1, padx=5)

create_button(
    "Lowercase",
    lowercase
).grid(row=0, column=2, padx=5)

create_button(
    "Palindrome",
    palindrome
).grid(row=0, column=3, padx=5)

create_button(
    "Count",
    count
).grid(row=0, column=4, padx=5)

window.mainloop()