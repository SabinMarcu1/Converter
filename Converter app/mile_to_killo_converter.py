from tkinter import *
from tkinter import messagebox  # Import pentru mesajele de eroare


# Funcția care convertește lungimea
def convert_length(event=None):  # Parametru `event` adăugat pentru a face funcția compatibilă cu bind
    try:
        value = float(length_input.get())
        if from_unit.get() == "Miles":
            km = value * 1.609
            m = value * 1609.34
            cm = value * 160934
            inche = value * 63360
            picioare = value * 5280
        elif from_unit.get() == "Kilometers":
            km = value
            m = value * 1000
            cm = value * 100000
            inche = value * 39370.1
            picioare = value * 3280.84
        elif from_unit.get() == "Meters":
            km = value / 1000
            m = value
            cm = value * 100
            inche = value * 39.3701
            picioare = value * 3.28084
        elif from_unit.get() == "Centimeters":
            km = value / 100000
            m = value / 100
            cm = value
            inche = value * 0.393701
            picioare = value * 0.0328084
        elif from_unit.get() == "Inches":
            km = value / 39370.1
            m = value / 39.3701
            cm = value * 2.54
            inche = value
            picioare = value / 12
        elif from_unit.get() == "Feet":
            km = value / 3280.84
            m = value / 3.28084
            cm = value * 30.48
            inche = value * 12
            picioare = value

        km_result_label.config(text=f"{km:.2f} Km")
        m_result_label.config(text=f"{m:.2f} m")
        cm_result_label.config(text=f"{cm:.2f} cm")
        inche_result_label.config(text=f"{inche:.2f} in")
        feet_result_label.config(text=f"{picioare:.2f} ft")

        length_input.delete(0, END)  # Curăță câmpul de input după calcul
    except ValueError:
        messagebox.showerror("Input Invalid", "Please enter a valid number.")  # Mesaj de eroare


# Creare fereastră principală
window = Tk()
window.title("Length Converter")
window.minsize(width=600, height=400)  # Lățime mai mare
window.config(padx=50, pady=50, bg="#B0E0E6")  # Fundal liniștitor

# Titlu cu font mai mare și bold
title_label = Label(text="Length Converter", font=("Arial", 24, "bold"), bg="#B0E0E6", fg="black")
title_label.grid(column=1, row=0, pady=(0, 20))  # Padding mai mare pentru titlu

# Input pentru lungime cu chenar negru, gros și text centrat
length_input = Entry(window, width=15, highlightthickness=2, highlightbackground="black", highlightcolor="black",
                     font=("Arial", 16), justify="center")
length_input.grid(column=1, row=1, padx=10, pady=10, sticky="EW")
length_input.focus()  # Pune focus pe câmpul de input când deschizi fereastra

# Label pentru lungime
length_label = Label(text="Length", font=("Arial", 16), bg="#B0E0E6", fg="black")
length_label.grid(column=2, row=1, padx=10, pady=10, sticky="W")

# Dropdown pentru unitatea de măsură de la care se face conversia
from_unit = StringVar(value="Miles")
unit_menu = OptionMenu(window, from_unit, "Miles", "Kilometers", "Meters", "Centimeters", "Inches", "Feet")
unit_menu.config(font=("Arial", 14), bg='#D3D3D3', fg='black')
unit_menu.grid(column=1, row=2, padx=10, pady=10)

# Buton pentru a calcula conversia
convert_button = Button(text="Convert", command=convert_length, font=("Arial", 16, "bold"), bg="#4caf50", fg="white",
                        relief="raised", bd=2)
convert_button.grid(column=1, row=3, padx=10, pady=10, sticky="EW")

# Labeluri pentru rezultatele conversiei aliniate vertical
result_frame = Frame(window, bg="#B0E0E6")  # Cadru pentru rezultate
result_frame.grid(column=1, row=4, pady=10)  # Plasare cadru rezultate

# Rezultate
km_result_label = Label(result_frame, text="0 Km", font=("Arial", 16), bg="#B0E0E6", fg="black")
km_result_label.grid(row=0, column=0, padx=10, pady=5, sticky="W")

m_result_label = Label(result_frame, text="0 m", font=("Arial", 16), bg="#B0E0E6", fg="black")
m_result_label.grid(row=1, column=0, padx=10, pady=5, sticky="W")

cm_result_label = Label(result_frame, text="0 cm", font=("Arial", 16), bg="#B0E0E6", fg="black")
cm_result_label.grid(row=2, column=0, padx=10, pady=5, sticky="W")

inche_result_label = Label(result_frame, text="0 in", font=("Arial", 16), bg="#B0E0E6", fg="black")
inche_result_label.grid(row=3, column=0, padx=10, pady=5, sticky="W")

feet_result_label = Label(result_frame, text="0 ft", font=("Arial", 16), bg="#B0E0E6", fg="black")
feet_result_label.grid(row=4, column=0, padx=10, pady=5, sticky="W")

# Adăugarea logo-ului "by Sabin" în colțul din dreapta
logo_label = Label(text="by Sabin", font=("Arial", 10, "italic"), bg="#B0E0E6", fg="black")
logo_label.grid(column=2, row=8, padx=10, pady=5, sticky="E")  # Poziționat în colțul din dreapta

# Bind pentru tasta Enter
window.bind('<Return>', convert_length)  # Asociază tasta Enter cu funcția

# Ajustare pentru ca toate coloanele să aibă dimensiuni egale
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Bucla principală
window.mainloop()
