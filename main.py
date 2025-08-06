import sqlite3
from tkinter import messagebox

class RegistrationSystem:
    def __init__(self):
        self.conn = sqlite3.connect('student.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                gender TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                address TEXT NOT NULL,
                course TEXT NOT NULL,
                picture TEXT NOT NULL
            )
        ''')

    def register_student(self, student):
        self.c.execute(
            "INSERT INTO students(name, email, phone, gender, birth_date, address, course, picture) VALUES (?,?,?,?,?,?,?,?)",
            student
        )
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Estudante registrado com sucesso!')

    def view_all_students(self):
        self.c.execute("SELECT * FROM students")
        dados = self.c.fetchall()
        return dados

    def search_student(self, id):
        try:
            self.c.execute("SELECT * FROM students WHERE id=?", (id,))
            dados = self.c.fetchone()
            if dados is None:
                messagebox.showwarning('Aviso', f'Nenhum estudante encontrado com ID: {id}')
            else:
                return dados
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao buscar estudante: {e}')

    def update_student(self, values_new):
        query = """
            UPDATE students
            SET name=?, email=?, phone=?, gender=? ,birth_date=?, address=?, course=?, picture=?
            WHERE id=?
        """
        self.c.execute(query, values_new)
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Estudante com ID:{values_new[8]} foi atualizado com sucesso!')

    def delete_student(self, id):
        self.c.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Estudante com ID:{id} foi deletado com sucesso!')