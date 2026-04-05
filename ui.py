import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import generator
import password_strength
from datetime import datetime


def run_app():
    root = tk.Tk()
    root.title("Secure Password Generator")
    root.geometry("620x720")
    root.resizable(False, False)
    root.configure(bg="gray")

    # ==============================
    # Fonctions utilitaires
    # ==============================

    def save_password(password):
        with open("password_history.txt", "a") as file:
            time = datetime.now().strftime("%Y-%m-%d %H:%M")
            file.write(f"{time} : {password}\n")

    def show_history():
        try:
            with open("password_history.txt", "r") as file:
                history = file.read()
        except:
            history = "Aucun mot de passe sauvegardé."

        messagebox.showinfo("Historique des mots de passe", history)

    def clear_fields():
        result_var.set("")
        test_entry.delete(0, tk.END)
        strength_var.set("")
        progress['value'] = 0

    # ==============================
    # Génération et copie
    # ==============================

    def generate_password_gui():
        try:
            length = int(length_entry.get())

            if length < 12:
                messagebox.showerror("Erreur", "La longueur doit être au moins 12")
                return

        except:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide")
            return

        include_uppercase = upper_var.get()
        include_lowercase = lower_var.get()
        include_digits = digit_var.get()
        include_special = special_var.get()

        if not (include_uppercase or include_lowercase or include_digits or include_special):
            messagebox.showerror("Erreur", "Choisissez au moins un type de caractère")
            return

        password = generator.generate_password(
            length,
            include_uppercase,
            include_lowercase,
            include_digits,
            include_special
        )

        result_var.set(password)
        save_password(password)

    def copy_password():
        password = result_var.get()

        if password == "":
            messagebox.showwarning("Attention", "Aucun mot de passe à copier")
            return

        root.clipboard_clear()
        root.clipboard_append(password)

        messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papier")

    # ==============================
    # Test de sécurité
    # ==============================

    def check_password_gui():
        password = test_entry.get()

        if password == "":
            messagebox.showerror("Erreur", "Veuillez entrer un mot de passe")
            return

        strength = password_strength.check_password_strength(password)
        strength_var.set(strength)

        if strength == "Mot de passe très sécurisé":
            progress['value'] = 100
            strength_label.config(fg="green")
        elif strength == "Mot de passe sécurisé":
            progress['value'] = 75
            strength_label.config(fg="blue")
        elif strength == "Mot de passe moyen":
            progress['value'] = 50
            strength_label.config(fg="orange")
        else:
            progress['value'] = 25
            strength_label.config(fg="red")

    # ==============================
    # Aide
    # ==============================

    def show_help():
        messagebox.showinfo(
            "Aide",
            "Secure Password Generator\n\n"
            "1. Entrez la longueur du mot de passe (minimum 12).\n"
            "2. Choisissez les types de caractères.\n"
            "3. Cliquez sur 'Générer'.\n\n"
            "Vous pouvez aussi tester un mot de passe."
        )

    def show_about():
        messagebox.showinfo(
            "À propos",
            "Secure Password Generator\n\n"
            "Application Python avec interface Tkinter."
        )

    # ==============================
    # Interface graphique
    # ==============================

    # Menu
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Fichier", menu=file_menu)
    file_menu.add_command(label="Générer", command=generate_password_gui)
    file_menu.add_command(label="Copier", command=copy_password)
    file_menu.add_command(label="Effacer", command=clear_fields)
    file_menu.add_separator()
    file_menu.add_command(label="Quitter", command=root.quit)

    tools_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Outils", menu=tools_menu)
    tools_menu.add_command(label="Tester mot de passe", command=check_password_gui)
    tools_menu.add_command(label="Historique", command=show_history)

    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Aide", menu=help_menu)
    help_menu.add_command(label="Comment utiliser", command=show_help)
    help_menu.add_command(label="À propos", command=show_about)

    # Titre
    tk.Label(
        root,
        text="SECURE PASSWORD GENERATOR",
        font=("Arial", 16, "bold"),
        fg="#22c55e",
        bg="#0f172a"
    ).pack(pady=10)

    # ==============================
    # Frame générateur
    # ==============================

    generator_frame = tk.LabelFrame(
        root,
        text="Générateur de mot de passe",
        bg="#1e293b",
        fg="white",
        padx=10,
        pady=10
    )
    generator_frame.pack(padx=15, pady=10, fill="both")

    tk.Label(generator_frame, text="Longueur :", bg="#1e293b", fg="white").pack()

    length_entry = tk.Entry(generator_frame, justify="center")
    length_entry.insert(0, "12")
    length_entry.pack(pady=5)

    # Options
    options_frame = tk.Frame(generator_frame, bg="#374151")
    options_frame.pack(pady=10)

    upper_var = tk.BooleanVar()
    lower_var = tk.BooleanVar()
    digit_var = tk.BooleanVar()
    special_var = tk.BooleanVar()

    tk.Checkbutton(options_frame, text="Majuscules", variable=upper_var, bg="#374151", fg="white", selectcolor="#374151").pack(anchor="w", padx=20)
    tk.Checkbutton(options_frame, text="Minuscules", variable=lower_var, bg="#374151", fg="white", selectcolor="#374151").pack(anchor="w", padx=20)
    tk.Checkbutton(options_frame, text="Chiffres", variable=digit_var, bg="#374151", fg="white", selectcolor="#374151").pack(anchor="w", padx=20)
    tk.Checkbutton(options_frame, text="Symboles", variable=special_var, bg="#374151", fg="white", selectcolor="#374151").pack(anchor="w", padx=20)

    tk.Button(
        generator_frame,
        text="Générer",
        command=generate_password_gui,
        bg="#38bdf8",
        fg="black"
    ).pack(pady=10)

    result_var = tk.StringVar()

    tk.Entry(generator_frame, textvariable=result_var, width=30).pack(pady=5)

    tk.Button(generator_frame, text="Copier", command=copy_password).pack(pady=5)

    # ==============================
    # Frame test
    # ==============================

    test_frame = tk.LabelFrame(
        root,
        text="Tester la sécurité",
        bg="#1e293b",
        fg="white",
        padx=10,
        pady=10
    )
    test_frame.pack(padx=15, pady=10, fill="both")

    test_entry = tk.Entry(test_frame)
    test_entry.pack(pady=5)

    tk.Button(test_frame, text="Vérifier", command=check_password_gui).pack(pady=5)

    strength_var = tk.StringVar()

    strength_label = tk.Label(test_frame, textvariable=strength_var)
    strength_label.pack(pady=5)

    progress = ttk.Progressbar(test_frame, length=250)
    progress.pack(pady=5)

    root.mainloop()