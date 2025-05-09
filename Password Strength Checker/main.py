from tkinter import *

import string

# GUI Init

window = Tk()
window.geometry("400x200")
window.title("Password Strength Checker By Zeyrian")
window.config(background="white")

label = Label(window, text="Enter Password",
              font=('Lexend', 25, 'bold'))

label2 = Label(window, text="No Password Detected.",
              font=('Lexend', 15, 'bold'))
entry = Entry(window)

result_message = ""

def submit():
    password = entry.get()

    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in string.ascii_uppercase])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in string.ascii_uppercase])
    special = any([1 if c in string.punctuation else 0 for c in string.ascii_uppercase])
    digits = any([1 if c in string.digits else 0 for c in string.ascii_uppercase])
    length = len(password)

    characters = [upper_case, lower_case, special, digits]

    score = 0

    with open('common.txt', 'r') as file:
        common = file.read().splitlines()

    if password in common:
        score -= 1

    if length > 8:
        score += (length-8)/2
        score += sum(characters)
    else:
        score = 1

    if score < 5:
        result_message = "Password is weak"
        label2.config(fg="red")
    if score == 5:
        result_message = "Password is moderately strong"
        label2.config(fg="black")
    if score > 5:
        result_message = "Password is strong!"
        label2.config(fg="green")

    label2.config(text=result_message)

submit = Button(window, text="Submit",command=submit)

submit.place(x=100, y=100)

label.place(x=10, y=0)
label.config(background="white")

label2.place(x=10, y=130)
label2.config(background="white")

entry.config(background="white",
             font=('Lexend', 20, 'bold'))
entry.place(x=10,y=50)

window.mainloop()
