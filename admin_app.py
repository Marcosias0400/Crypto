import tkinter as tk
from tkinter import ttk, messagebox
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class AdminApp:
    def __init__(self, root, database_utils, crypto_utils):
        self.root = root
        self.database_utils = database_utils
        self.crypto_utils = crypto_utils
        self.setup_ui()

    def open_admin_login_window(self):
        login_window = tk.Toplevel(self.root)
        login_window.title("Admin Login")
        
        tk.Label(login_window, text="Admin ID:").grid(row=0, column=0, padx=10, pady=10)
        self.admin_id_entry = tk.Entry(login_window)
        self.admin_id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        self.admin_password_entry = tk.Entry(login_window, show='*')
        self.admin_password_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Button(login_window, text="Login", command=self.validate_admin_login).grid(row=2, columnspan=2, pady=10)

    def validate_admin_login(self):
        admin_id = self.admin_id_entry.get()
        password = self.admin_password_entry.get()
        valid, permission = self.database_utils.validate_admin_login(admin_id, password)
        if valid:
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            self.open_program_window(permission)
        else:
            messagebox.showerror("Error", "ID o contraseña incorrectos")

    def open_delete_admin_window():
      delete_admin_window = tk.Toplevel(root)
      delete_admin_window.title("Eliminar Admin")
    
      tk.Label(delete_admin_window, text="Admin ID:").grid(row=0, column=0, padx=10, pady=10)
      delete_admin_id_entry = tk.Entry(delete_admin_window)
      delete_admin_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
      def delete_admin_record():
        admin_id_to_delete = delete_admin_id_entry.get()
        if admin_id_to_delete != 'root':
            delete_admin(admin_id_to_delete)
            messagebox.showinfo("Exito", "Administrador eliminado con éxito")
            delete_admin_window.destroy()
        else:
            messagebox.showerror("Error", "No se puede eliminar el administrador root")

    def open_program_window(self, permission):
        program_window = tk.Toplevel(self.root)
        program_window.title("Transparencia de ONG")

        if permission == 1:
            tk.Button(program_window, text="Agregar Donante", command=self.open_add_donante_window).pack(pady=10)
        
        if permission == 0:
            tk.Button(program_window, text="Agregar Admin", command=self.open_add_admin_window).pack(pady=10)
            tk.Button(program_window, text="Eliminar Donante", command=self.open_delete_donante_window).pack(pady=10)
            tk.Button(program_window, text="Eliminar Admin", command=self.open_delete_admin_window).pack(pady=10)
    
    def open_add_admin_window(self):
      add_admin_window = tk.Toplevel(self.root)
      add_admin_window.title("Agregar Admin")
    
      tk.Label(add_admin_window, text="Admin ID:").grid(row=0, column=0, padx=10, pady=10)
      new_admin_id_entry = tk.Entry(add_admin_window)
      new_admin_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
      tk.Label(add_admin_window, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
      new_password_entry = tk.Entry(add_admin_window, show="*")
      new_password_entry.grid(row=1, column=1, padx=10, pady=10)
    
      tk.Label(add_admin_window, text="Permiso:").grid(row=2, column=0, padx=10, pady=10)
      permission_entry = tk.Entry(add_admin_window)
      permission_entry.grid(row=2, column=1, padx=10, pady=10)
    
      def add_new_admin():
        new_admin_id = new_admin_id_entry.get()
        new_password = new_password_entry.get()
        permission = int(permission_entry.get())
        if permission == 1:
            self.database_utils.add_admin(new_admin_id, new_password, self.crypto_utils.public_key, permission)
            messagebox.showinfo("Exito", "Administrador agregado con éxito")
            add_admin_window.destroy()
        else:
            messagebox.showerror("Error", "El permiso debe ser 0")
    
      tk.Button(add_admin_window, text="Agregar", command=add_new_admin).grid(row=3, columnspan=2, pady=10)
        
    def open_program_user(self):
        user_window = tk.Toplevel(self.root)
        user_window.title("Tranparencia ONG")
    
        tk.Label(user_window, text="Consulta a la Base de Datos").pack(padx=20, pady=20)
    
        query_label = tk.Label(user_window, text="Consulta:")
        query_label.pack(padx=10, pady=5)
    
        query_entry = tk.Entry(user_window, width=50)
        query_entry.pack(padx=10, pady=5)
    
        def run_query():
          query = query_entry.get()
          try:
            conn = sqlite3.connect('donantes.db')
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            result_text.delete(1.0, tk.END)
            for row in results:
                result_text.insert(tk.END, f"{row}\n")
          except Exception as e:
            messagebox.showerror("Error", f"Error ejecutando la consulta: {e}")

        query_button = tk.Button(user_window, text="Ejecutar Consulta", command=run_query)
        query_button.pack(padx=10, pady=5)
    
        result_text = tk.Text(user_window, width=80, height=20)
        result_text.pack(padx=10, pady=10)

    def open_add_donante_window(self):
        add_donante_window = tk.Toplevel(self.root)
        add_donante_window.title("Agregar Donante")
        
        tk.Label(add_donante_window, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
        self.nombre_entry = tk.Entry(add_donante_window)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_donante_window, text="Apellido1:").grid(row=1, column=0, padx=10, pady=10)
        self.apellido1_entry = tk.Entry(add_donante_window)
        self.apellido1_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(add_donante_window, text="Apellido2:").grid(row=2, column=0, padx=10, pady=10)
        self.apellido2_entry = tk.Entry(add_donante_window)
        self.apellido2_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(add_donante_window, text="Donación:").grid(row=3, column=0, padx=10, pady=10)
        self.donacion_entry = tk.Entry(add_donante_window)
        self.donacion_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(add_donante_window, text="Tier:").grid(row=4, column=0, padx=10, pady=10)
        self.tier_entry = tk.Entry(add_donante_window)
        self.tier_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(add_donante_window, text="Cuenta Bancaria:").grid(row=5, column=0, padx=10, pady=10)
        self.cuenta_bancaria_entry = tk.Entry(add_donante_window)
        self.cuenta_bancaria_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(add_donante_window, text="Dirección:").grid(row=6, column=0, padx=10, pady=10)
        self.direccion_entry = tk.Entry(add_donante_window)
        self.direccion_entry.grid(row=6, column=1, padx=10, pady=10)

        tk.Button(add_donante_window, text="Agregar", command=self.add_donante).grid(row=7, columnspan=2, pady=10)

    def add_donante(self):
        nombre = self.nombre_entry.get()
        apellido1 = self.apellido1_entry.get()
        apellido2 = self.apellido2_entry.get()
        donacion = self.donacion_entry.get()
        tier = self.tier_entry.get()
        cuenta_bancaria = self.cuenta_bancaria_entry.get()
        direccion = self.direccion_entry.get()

        self.database_utils.add_donante(nombre, apellido1, apellido2, donacion, tier, cuenta_bancaria, direccion)
        messagebox.showinfo("Éxito", "Donante agregado exitosamente")

    def open_delete_donante_window(self):
        delete_donante_window = tk.Toplevel(self.root)
        delete_donante_window.title("Eliminar Donante")

        tk.Label(delete_donante_window, text="ID del Donante:").grid(row=0, column=0, padx=10, pady=10)
        self.donante_id_entry = tk.Entry(delete_donante_window)
        self.donante_id_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(delete_donante_window, text="Eliminar", command=self.delete_donante(self.donante_id_entry.get())).grid(row=1, columnspan=2, pady=10)
        

    def delete_donante(self, text):
        donante_id = self.database_utils.get_donante_by_id(text)

    def setup_ui(self):
        self.root.title("Ventana Principal")

        admin_button = ttk.Button(self.root, text="Admin Login", command=self.open_admin_login_window)
        admin_button.pack(pady=10)

        user_button = ttk.Button(self.root, text="Usuario Genérico", command=self.open_program_user)
        user_button.pack(pady=10)

        self.root.mainloop()
    

   

