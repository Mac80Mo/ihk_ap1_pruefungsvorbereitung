import tkinter as tk
import random

# Datenstruktur für Fragen und Antworten (Beispiel)
from fragen import fragen_pools # Importiert die Fragen aus der fragen.py

# Hauptanwendungsklasse
def starte_quiz_app():
    def aktualisiere_button():
        if aktuelle_frage_index == -1:
            haupt_button.config(text="Start", command=starte_quiz)
        elif aktuelle_frage_index < len(ausgewählte_fragen):
            haupt_button.config(text="Antwort anzeigen", command=zeige_antwort)
        elif aktuelle_frage_index == len(ausgewählte_fragen):
            haupt_button.config(text="Beenden", command=root.quit)

    def zeige_frage():
        if aktuelle_frage_index < len(ausgewählte_fragen):
            frage = ausgewählte_fragen[aktuelle_frage_index]
            text_widget_frage.config(state="normal")
            text_widget_frage.delete("1.0", tk.END)
            text_widget_frage.insert(tk.END, frage["Frage"])
            text_widget_frage.config(state="disabled")
            aktualisiere_button()
        else:
            text_widget_frage.config(state="normal")
            text_widget_frage.delete("1.0", tk.END)
            text_widget_frage.insert(tk.END, "Quiz beendet!")
            text_widget_frage.config(state="disabled")
            aktualisiere_button()

    def zeige_antwort():
        if aktuelle_frage_index < len(ausgewählte_fragen):
            antwort = ausgewählte_fragen[aktuelle_frage_index]["Antwort"]
            text_widget_frage.config(state="normal")
            text_widget_frage.insert(tk.END, f"\n\nAntwort:\n\n{antwort}")
            text_widget_frage.config(state="disabled")
            haupt_button.config(text="Nächste Frage", command=nächste_frage)

    def nächste_frage():
        nonlocal aktuelle_frage_index
        aktuelle_frage_index += 1
        zeige_frage()

    def starte_quiz():
        nonlocal ausgewählte_fragen, aktuelle_frage_index
        anzahl_fragen = 3  # Feste Anzahl von Fragen
        fragen = fragen_pools.get(aktuelle_kategorie.get(), [])
        ausgewählte_fragen = random.sample(fragen, min(anzahl_fragen, len(fragen)))
        aktuelle_frage_index = 0
        zeige_frage()

    def setze_kategorie(kategorie):
        aktuelle_kategorie.set(kategorie)
        kategorie_label.config(text=f"Sie haben \"{kategorie}\" gewählt.")

    # Hauptfenster erstellen
    global root
    root = tk.Tk()
    root.title("Vorbereitung IT AP1")
    root.geometry("450x600")
    root.resizable(True, True)  # Fenstergröße kann geändert werden
    root.config(bg="#2e2e2e")  # Dunkles Grau als Hintergrundfarbe

    # Stil des Fensters festlegen (dunkler Header)
    style = tk.Label(root, text="IT-Berufe\nGestreckte Abschlussprüfung Teil 1\nEinrichten eines IT-gestützten Arbeitsplatzes", bg="#2e2e2e", fg="white", font=("Arial", 14), pady=5)
    style.pack(fill="x")

    # Variablen
    aktuelle_kategorie = tk.StringVar(value=None)
    ausgewählte_fragen = []
    aktuelle_frage_index = -1  # -1 bedeutet, dass das Quiz noch nicht gestartet wurde

    # Menüleiste erstellen
    menüleiste = tk.Menu(root, bg="black", fg="white", tearoff=0)
    kategorie_menü = tk.Menu(menüleiste, bg="black", fg="white", tearoff=0, font=("Consolas", 10))

    for kategorie in fragen_pools.keys():
        kategorie_menü.add_command(label=kategorie, command=lambda k=kategorie: setze_kategorie(k), font=("Consolas", 10), foreground="#D19A66")

    menüleiste.add_cascade(label="Kategorien", menu=kategorie_menü)
    root.config(menu=menüleiste)

    # Hauptlayout
    main_frame = tk.Frame(root, padx=8, pady=8, bg="#2e2e2e")
    main_frame.pack(fill="both", expand=True)

    # Hinweistext
    hinweis_label = tk.Label(main_frame, text="Willkommen zur Vorbereitungs App!\nWählen oben eine Kategorie und drücke auf Start, um zu beginnen.", font=("Consolas", 12), wraplength=400, justify="center", bg="#2e2e2e", fg="#D19A66")
    hinweis_label.pack(pady=5)

    # Kategorieanzeige
    kategorie_label = tk.Label(main_frame, text="Noch keine Kategorie gewählt.", font=("Consolas", 12), fg="#569CD6", bg="#2e2e2e")
    kategorie_label.pack(pady=5)

    # Frageanzeige mit Scrollbar
    frame_frage = tk.Frame(main_frame, padx=8, pady=8, bg="#2e2e2e")
    frame_frage.pack(pady=5, fill="both", expand=True)

    text_widget_frage = tk.Text(frame_frage, wrap="word", font=("Consolas", 14), height=12, state="disabled", bg="black", fg="limegreen")
    text_widget_frage.pack(side="left", fill="both", expand=True)

    scrollbar_frage = tk.Scrollbar(frame_frage, command=text_widget_frage.yview, bg="black")
    scrollbar_frage.pack(side="right", fill="y")

    text_widget_frage.config(yscrollcommand=scrollbar_frage.set)

    # Button Frame
    button_frame = tk.Frame(root, padx=8, pady=8, bg="#2e2e2e")
    button_frame.pack(fill="x", pady=10)

    # Hauptbutton
    haupt_button = tk.Button(button_frame, text="Start", command=starte_quiz, bg="#d3d3d3", fg="black", font=("Arial", 16), height=3, width=20)
    haupt_button.pack()

    # Anwendung starten
    root.mainloop()

if __name__ == "__main__":
    starte_quiz_app()
