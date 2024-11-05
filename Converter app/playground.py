from tkinter import *
from tkinter import messagebox

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

# Creare fereastră principală
window = Tk()
window.title("Temperature Converter")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)

# Setare fundal verde deschis
window.configure(bg='#A8E6CF')

# Dropdown pentru alegerea modului de conversie
conversion_mode = StringVar(value="Celsius to Fahrenheit")
conversion_menu = OptionMenu(window, conversion_mode, "Celsius to Fahrenheit", "Fahrenheit to Celsius")
conversion_menu.config(font=("Arial", 14), bg='#FFABAB', fg='black', highlightthickness=2)
conversion_menu.grid(column=1, row=0, padx=10, pady=10)

# Input pentru temperatura cu chenar negru și gros
celsius_input = Entry(window, width=10, highlightthickness=2, highlightbackground="black", highlightcolor="black", font=("Arial", 16), justify="center")
celsius_input.grid(column=1, row=1, padx=10, pady=10, sticky="EW")
celsius_input.focus()  # Pune focus pe câmpul de input când deschizi fereastra

# Label pentru Celsius cu font Arial, bold, 16
celsius_label = Label(text="Temperature", font=("Arial", 16, "bold"), bg='#A8E6CF', fg='black')
celsius_label.grid(column=2, row=1, padx=10, pady=10, sticky="W")

# Label "is equal to" cu font Arial, bold, 16
is_equal_label = Label(text="is equal to", font=("Arial", 16, "bold"), bg='#A8E6CF', fg='black')
is_equal_label.grid(column=0, row=2, padx=10, pady=10, sticky="E")

# Label pentru afișarea rezultatului cu font Arial, bold, 16
fahrenheit_result_label = Label(text="0 °F", font=("Arial", 16, "bold"), bg='#A8E6CF', fg='black')
fahrenheit_result_label.grid(column=1, row=2, padx=10, pady=10, sticky="EW")

# Label pentru Fahrenheit cu font Arial, bold, 16
fahrenheit_label = Label(text="°F", font=("Arial", 16, "bold"), bg='#A8E6CF', fg='black')
fahrenheit_label.grid(column=2, row=2, padx=10, pady=10, sticky="W")

# Buton pentru a calcula conversia
calculate_button = Button(text="Convert", command=convert_temperature, font=("Arial", 16, "bold"), bg='#FF6F61', fg='white')
calculate_button.grid(column=1, row=3, padx=10, pady=10, sticky="EW")

# Text pentru istoricul conversiilor
history = Text(window, width=40, height=10, font=("Arial", 12), wrap="word", bg='#FFABAB', fg='black')
history.grid(column=0, row=4, columnspan=3, padx=10, pady=10)

# Adăugarea logo-ului "by Sabin" în colțul din dreapta
logo_label = Label(text="by Sabin", font=("Arial", 10, "italic"), bg='#A8E6CF', fg='black')
logo_label.grid(column=2, row=8, padx=10, pady=5, sticky="E")  # Poziționat în colțul din dreapta

# Bind pentru tasta Enter
window.bind('<Return>', convert_temperature)  # Asociază tasta Enter cu funcția

# Ajustare pentru ca toate coloanele să aibă dimensiuni egale
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Bucla principală
window.mainloop()
