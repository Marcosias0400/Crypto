import tkinter as tk
from tkinter import messagebox

class AdminLogin(tk.Tk):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.title("Inicio de Sesión de Administrador")
        self.geometry("300x150")

        self.label1 = tk.Label(self, text="ID de Administrador")
        self.label1.pack(pady=5)

        self.admin_id = tk.Entry(self)
        self.admin_id.pack(pady=5)

        self.label2 = tk.Label(self, text="Frase de Seguridad")
        self.label2.pack(pady=5)

        self.security_phrase = tk.Entry(self, show='*')
        self.security_phrase.pack(pady=5)

        self.login_button = tk.Button(self, text="Iniciar Sesión", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        admin_id = self.admin_id.get()
        security_phrase = self.security_phrase.get()

        # Verificar credenciales de administrador
        admins = self.db.query_admin()
        for admin in admins:
            if admin[0] == admin_id and self.db.C.verificado(admin[2], security_phrase):
                self.destroy()
                AdminInterface(self.db, admin_id).mainloop()
                return
        messagebox.showerror("Error", "ID o frase de seguridad incorrectos")

class AdminInterface(tk.Tk):
    def __init__(self, db, admin_id):
        super().__init__()
        self.db = db
        self.admin_id = admin_id
        self.title("Interfaz de Administrador")
        self.geometry("400x300")

        self.label = tk.Label(self, text=f"Bienvenido, {self.admin_id}")
        self.label.pack(pady=5)

        self.add_admin_button = tk.Button(self, text="Agregar Administrador", command=self.add_admin)
        self.add_admin_button.pack(pady=5)

        self.remove_admin_button = tk.Button(self, text="Eliminar Administrador", command=self.remove_admin)
        self.remove_admin_button.pack(pady=5)

        self.donors_interface_button = tk.Button(self, text="Interfaz de Donantes", command=self.open_donor_interface)
        self.donors_interface_button.pack(pady=5)

    def add_admin(self):
        AddAdminInterface(self.db).mainloop()

    def remove_admin(self):
        RemoveAdminInterface(self.db).mainloop()

    def open_donor_interface(self):
        self.destroy()
        DonorInterface(self.db).mainloop()

class AddAdminInterface(tk.Tk):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.title("Agregar Administrador")
        self.geometry("300x200")

        self.label1 = tk.Label(self, text="ID de Administrador")
        self.label1.pack(pady=5)

        self.admin_id = tk.Entry(self)
        self.admin_id.pack(pady=5)

        self.label2 = tk.Label(self, text="Frase de Seguridad")
        self.label2.pack(pady=5)

        self.security_phrase = tk.Entry(self, show='*')
        self.security_phrase.pack(pady=5)

        self.add_button = tk.Button(self, text="Agregar", command=self.add_admin)
        self.add_button.pack(pady=20)

    def add_admin(self):
        admin_id = self.admin_id.get()
        security_phrase = self.security_phrase.get()
        self.db.add_admin(admin_id, security_phrase)
        messagebox.showinfo("Éxito", "Administrador agregado exitosamente")
        self.destroy()

class RemoveAdminInterface(tk.Tk):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.title("Eliminar Administrador")
        self.geometry("300x200")

        self.label1 = tk.Label(self, text="ID de Administrador")
        self.label1.pack(pady=5)

        self.admin_id = tk.Entry(self)
        self.admin_id.pack(pady=5)

        self.remove_button = tk.Button(self, text="Eliminar", command=self.remove_admin)
        self.remove_button.pack(pady=20)

    def remove_admin(self):
        admin_id = self.admin_id.get()
        self.db.rm_admin(admin_id)
        messagebox.showinfo("Éxito", "Administrador eliminado exitosamente")
        self.destroy()

class DonorInterface(tk.Tk):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.title("Interfaz de Donantes")
        self.geometry("500x400")

        self.label1 = tk.Label(self, text="Agregar Donante")
        self.label1.pack(pady=5)

        self.donor_data = []
        self.labels = ["Cuenta Bancaria", "Nombre", "Apellido1", "Apellido2", "Concepto", "Tier", "Dirección"]
        for label in self.labels:
            lbl = tk.Label(self, text=label)
            lbl.pack(pady=2)
            entry = tk.Entry(self)
            entry.pack(pady=2)
            self.donor_data.append(entry)

        self.add_button = tk.Button(self, text="Agregar", command=self.add_donor)
        self.add_button.pack(pady=10)

        self.label2 = tk.Label(self, text="Buscar Donante")
        self.label2.pack(pady=5)

        self.search_entry = tk.Entry(self)
        self.search_entry.pack(pady=5)

        self.search_button = tk.Button(self, text="Buscar", command=self.search_donor)
        self.search_button.pack(pady=10)

        self.results = tk.Text(self, height=10, width=50)
        self.results.pack(pady=10)

    def add_donor(self):
        donor_info = [entry.get() for entry in self.donor_data]
        self.db.add_donantes(donor_info)
        messagebox.showinfo("Éxito", "Donante agregado exitosamente")
        for entry in self.donor_data:
            entry.delete(0, tk.END)

    def search_donor(self):
        search_term = self.search_entry.get()
        results = self.db.query_usr()
        self.results.delete('1.0', tk.END)
        for result in results:
            if search_term in result:
                self.results.insert(tk.END, f"{result}\n")

