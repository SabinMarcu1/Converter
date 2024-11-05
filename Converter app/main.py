from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="I am a label", font=("Arial", 16, "bold"))
my_label.config(text="New text")
my_label.grid(column=3, row=0)
my_label.config(padx=50, pady=50)

# Button


button = Button(text="Click me", command=button_clicked)
button.grid(column=0, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)
# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()
