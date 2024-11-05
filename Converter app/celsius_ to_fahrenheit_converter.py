from tkinter import *
from tkinter import messagebox
import pyperclip  # Asigură-te că ai instalat biblioteca pyperclip

# Funcția de conversie a temperaturilor
def convert_temperature(event=None):
    try:
        if conversion_mode.get() == "Celsius to Fahrenheit":
            celsius = float(celsius_input.get())
            fahrenheit = (celsius * 9/5) + 32
            fahrenheit_result_label.config(text=f"{fahrenheit:.2f} °F")
            history.insert(END, f"{celsius:.2f} °C = {fahrenheit:.2f} °F\n")
        else:
            fahrenheit = float(celsius_input.get())
            celsius = (fahrenheit - 32) * 5/9
            fahrenheit_result_label.config(text=f"{celsius:.2f} °C")
            history.insert(END, f"{fahrenheit:.2f} °F = {celsius:.2f} °C\n")

        celsius_input.delete(0, END)
    except ValueError:
        messagebox.showerror("Input Invalid", "Please enter a valid number.")

# Funcție pentru copierea rezultatului
def copy_result():
    result_text = fahrenheit_result_label.cget("text")
    pyperclip.copy(result_text)
    messagebox.showinfo("Copied", "Result copied to clipboard!")

# Creare fereastră principală
window = Tk()
window.title("Temperature Converter")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)

# Setare fundal colorat
window.configure(bg='#2ECC71')  # Fundal verde deschis

# Dropdown pentru alegerea modului de conversie
conversion_mode = StringVar(value="Celsius to Fahrenheit")
conversion_menu = OptionMenu(window, conversion_mode, "Celsius to Fahrenheit", "Fahrenheit to Celsius")
conversion_menu.config(font=("Arial", 14), bg='#34495E', fg='white', highlightthickness=2)
conversion_menu.grid(column=1, row=0, padx=10, pady=10)

# Input pentru temperatura cu chenar negru și gros
celsius_input = Entry(window, width=10, highlightthickness=2, highlightbackground="black", highlightcolor="black", font=("Arial", 16), justify="center")
celsius_input.grid(column=1, row=1, padx=10, pady=10, sticky="EW")
celsius_input.focus()  # Pune focus pe câmpul de input când deschizi fereastra

# Label pentru Celsius cu font Arial, bold, 16
celsius_label = Label(text="Temperature", font=("Arial", 16, "bold"), bg='#2ECC71', fg='white')
celsius_label.grid(column=2, row=1, padx=10, pady=10, sticky="W")

# Label "is equal to" cu font Arial, bold, 16
is_equal_label = Label(text="is equal to", font=("Arial", 16, "bold"), bg='#2ECC71', fg='white')
is_equal_label.grid(column=0, row=2, padx=10, pady=10, sticky="E")

# Label pentru afișarea rezultatului cu font Arial, bold, 16
fahrenheit_result_label = Label(text="0 °F", font=("Arial", 16, "bold"), bg='#2ECC71', fg='white')
fahrenheit_result_label.grid(column=1, row=2, padx=10, pady=10, sticky="EW")

# Label pentru Fahrenheit cu font Arial, bold, 16
fahrenheit_label = Label(text="°F", font=("Arial", 16, "bold"), bg='#2ECC71', fg='white')
fahrenheit_label.grid(column=2, row=2, padx=10, pady=10, sticky="W")

# Buton pentru a calcula conversia
calculate_button = Button(text="Convert", command=convert_temperature, font=("Arial", 16, "bold"), bg='#E74C3C', fg='white')
calculate_button.grid(column=1, row=3, padx=10, pady=10, sticky="EW")

# Buton de copiere
copy_button = Button(text="Copy Result", command=copy_result, font=("Arial", 16, "bold"), bg='#2980B9', fg='white')
copy_button.grid(column=1, row=4, padx=10, pady=10, sticky="EW")

# Text pentru istoricul conversiilor
history = Text(window, width=40, height=10, font=("Arial", 12), wrap="word", bg='#34495E', fg='white')
history.grid(column=0, row=5, columnspan=3, padx=10, pady=10)

# Bind pentru tasta Enter
window.bind('<Return>', convert_temperature)  # Asociază tasta Enter cu funcția

# Ajustare pentru ca toate coloanele să aibă dimensiuni egale
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Funcție pentru a salva istoricul într-un fișier
def save_history():
    with open("conversion_history.txt", "w") as file:
        file.write(history.get("1.0", END))
    messagebox.showinfo("Saved", "History saved to conversion_history.txt")

# Buton pentru a salva istoricul
save_button = Button(text="Save History", command=save_history, font=("Arial", 16, "bold"), bg='#8E44AD', fg='white')
save_button.grid(column=1, row=6, padx=10, pady=10, sticky="EW")

# Bucla principală
window.mainloop()
