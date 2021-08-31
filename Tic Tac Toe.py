import tkinter
from tkinter import *
from tkinter import messagebox

# Die folgende Funktion soll ausgeführt werden, wenn der Benutzer den Button 'Spielanleitung' anklickt
def button_action():
    text="Spielanleitung Tic Tac Toe\nTic Tac Toe wird auf einem 3x3 großem Spielfeld gespielt. Pro Zug dürfen sowohl der Spieler als auch der Computer abwechselnd Ihr Zeichen in ein freies Feld setzen. Der Spieler verwendet ein Kreuz, der Computer einen Kreis. Ziel des Spiels ist es, mit dem Kreuz eine Reihe,Spalte oder Diagonale zu setzen. Wer das zuerst schafft, gewinnt das Spiel."
    messagebox.showinfo(message=text, title="Spielanleitung")

from tkinter import *
from tkinter import messagebox
#Button klicken funktion
clicked= True
count= 0
# Die folgende Funktion soll ausgeführt werden, wenn der Benutzer den Button 'Spiel beginnen' anklickt
def tictactoe():
    root = Tk()
    root.title("Tic Tac Toe")

#Button klicken funktion
    clicked= True
    count= 0

# Alle Felder ausstellen
    def disable_buttons():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

# Hier wird geprüft ob einer der Spieler gewonnen hat
    def checkifwon():
         global winner
         winner = False

         if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
             b1.config(bg="blue")
             b2.config(bg="blue")
             b3.config(bg="blue")
             winner = True
             messagebox.showinfo("Tic Tac Toe", "Super, X gewinnt!")
             disable_buttons()

         elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
              b4.config(bg="blue")
              b5.config(bg="blue")
              b6.config(bg="blue")
              winner = True
              messagebox.showinfo("Tic Tac Toe", "Super, X gewinnt!")
              disable_buttons()

         elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
              b7.config(bg="blue")
              b8.config(bg="blue")
              b9.config(bg="blue")
              winner = True
              messagebox.showinfo("Tic Tac Toe", "Super, X gewinnt!")
              disable_buttons()

         elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
              b1.config(bg="blue")
              b4.config(bg="blue")
              b7.config(bg="blue")
              winner = True
              messagebox.showinfo("Tic Tac Toe", "Super, X gewinnt!")
              disable_buttons()

         elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
              b2.config(bg="blue")
              b5.config(bg="blue")
              b8.config(bg="blue")
              winner = True
              messagebox.showinfo("Tic Tac Toe", "Super, X gewinnt!")
              disable_buttons()

         elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
              b3.config(bg="blue")
              b6.config(bg="blue")
              b9.config(bg="blue")
              winner = True
              messagebox.showinfo("Tic Tac Toe", "Super, X gewinnt!")
              disable_buttons()

         elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.config(bg="blue")
            b5.config(bg="blue")
            b9.config(bg="blue")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Super, X gewinnt!")
            disable_buttons()

         elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3.config(bg="blue")
            b5.config(bg="blue")
            b7.config(bg="blue")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Super, X gewinnt!")
            disable_buttons()

#Es wird geprüft ob O gewonnen hat
         if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1.config(bg="blue")
            b2.config(bg="blue")
            b3.config(bg="blue")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Super, O hat gewonnen")
            disable_buttons()

         elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg="blue")
            b5.config(bg="blue")
            b6.config(bg="blue")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Super, O hat gewonnen")
            disable_buttons()

         elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg="blue")
            b8.config(bg="blue")
            b9.config(bg="blue")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Super, O hat gewonnen")
            disable_buttons()

         elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.config(bg="blue")
            b4.config(bg="blue")
            b7.config(bg="blue")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Super, O hat gewonnen")
            disable_buttons()

         elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg="blue")
            b5.config(bg="blue")
            b8.config(bg="blue")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Super, O hat gewonnen")
            disable_buttons()

         elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.config(bg="blue")
            b6.config(bg="blue")
            b9.config(bg="blue")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Super, O hat gewonnen")
            disable_buttons()

         elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg="blue")
            b5.config(bg="blue")
            b9.config(bg="blue")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Super, O hat gewonnen")
            disable_buttons()

         elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3.config(bg="blue")
            b5.config(bg="blue")
            b7.config(bg="blue")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Super, O hat gewonnen")
            disable_buttons()
#Es wird geprüft ob X gewonnen hat
    def b_click(b):
         global clicked, count

         if b["text"]== " " and clicked == True:
              b["text"]= "X"
              clicked = False
              count += 1
              checkifwon()
         elif b["text"]== " " and clicked == False:
              b["text"]= "O"
              clicked= True
              count += 1
              checkifwon()
         else:
              messagebox.showerror("Tic Tac Toe", "Das Feld wurde bereits belegt\n Wähle ein anderes Feld")

#Die Buttons für das Feld werden erstellt
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

# In der Ereignisschleife auf Eingabe des Benutzers warten.
    root.mainloop()

# Ein Fenster erstellen
fenster =Tk()
# Den Fenstertitle erstellen
fenster.title("Tic Tac Toe")
# Größe des Fensters wird definiert
fenster.geometry("500x450")

#Buttons erstellen.
change_button = Button(fenster, text="Spielanleitung", bg="light blue", font=('bold'), command=button_action)
test_button = Button(fenster, text="Spiel beginnen",bg="light green", font=("bold"), command=tictactoe)
exit_button = Button(fenster, text="Beenden",bg='brown',font=('bold'), command=fenster.quit)

#Label erstellen
info_label = Label(fenster)
anweisungs_label = Label(fenster)

#Die Komponenten werden in der gewünschten Reihenfolge angeordnet
anweisungs_label.pack()
info_label.pack()
change_button.pack()
test_button.pack()
exit_button.pack()

# Die absoluten Koordinaten werden definiert damit die Komponenten gesetzt und in ihrer Größe definiert werden
test_button.place(x=100, y=170, width=300, height=100)
change_button.place(x=100, y=50, width=300, height=100)
exit_button.place(x=100, y=290, width=300, height=100)

# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()