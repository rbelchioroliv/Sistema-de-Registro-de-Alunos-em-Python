import sqlite3
from tkinter import messagebox

# Classe responsável pelo sistema de registro de estudantes
# Class responsible for the student registration system
class RegistrationSystem:
    def __init__(self):
        # Conecta ao banco de dados (ou cria se não existir)
        # Connects to the database (or creates it if it doesn't exist)
        self.conn = sqlite3.connect('student.db')
        self.c = self.conn.cursor()
        
        # Cria a tabela de estudantes, se ainda não existir
        # Creates the students table if it doesn't already exist
        self.create_table()

    # Função para criar a tabela no banco de dados
    # Function to create the students table in the database
    def create_table(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID único e automático para cada estudante
                                                      -- Unique and auto-incremented ID for each student
                name TEXT NOT NULL,                    -- Nome do estudante
                                                      -- Student's name
                email TEXT NOT NULL,                   -- E-mail do estudante
                                                      -- Student's email
                phone TEXT NOT NULL,                   -- Telefone do estudante
                                                      -- Student's phone number
                gender TEXT NOT NULL,                  -- Gênero do estudante
                                                      -- Student's gender
                birth_date TEXT NOT NULL,              -- Data de nascimento do estudante
                                                      -- Student's birth date
                address TEXT NOT NULL,                 -- Endereço do estudante
                                                      -- Student's address
                course TEXT NOT NULL,                  -- Curso matriculado
                                                      -- Enrolled course
                picture TEXT NOT NULL                  -- Caminho para a imagem (foto) do estudante
                                                      -- Path to student's image (photo)
            )
        ''')

    # Função para registrar um novo estudante
    # Function to register a new student
    def register_student(self, student):
        self.c.execute(
            "INSERT INTO students(name, email, phone, gender, birth_date, address, course, picture) VALUES (?,?,?,?,?,?,?,?)",
            student  # A tupla com os dados do estudante / Tuple with student data
        )
        self.conn.commit()  # Salva as alterações no banco de dados / Saves changes to the database

        # Mostrando mensagem de sucesso
        # Displaying success message
        messagebox.showinfo('Sucesso', 'Estudante registrado com sucesso!')

    # Função para visualizar todos os estudantes
    # Function to view all students
    def view_all_students(self):
        self.c.execute("SELECT * FROM students")
        dados = self.c.fetchall()  # Busca todos os registros / Fetches all records
        return dados

   # Função para buscar um estudante por ID
    # Function to search for a student by ID
    def search_student(self, id):
        try:
            self.c.execute("SELECT * FROM students WHERE id=?", (id,))
            dados = self.c.fetchone()  # Busca um único registro / Fetches a single record

            if dados is None:
                # Se não encontrar nenhum registro com esse ID
                messagebox.showwarning('Aviso', f'Nenhum estudante encontrado com ID: {id}')
            else:
                return dados
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao buscar estudante: {e}')

    # Função para atualizar os dados de um estudante
    # Function to update a student’s data
    def update_student(self, values_new):
        query = """
            UPDATE students 
            SET name=?, email=?, phone=?, gender=? ,birth_date=?, address=?, course=?, picture=? 
            WHERE id=?
        """
        self.c.execute(query, values_new)  # Executa a atualização / Executes the update
        self.conn.commit()  # Salva as alterações / Saves changes

        # Mostrando mensagem de sucesso
        # Displaying success message
        messagebox.showinfo('Sucesso', f'Estudante com ID:{values_new[8]} foi atualizado com sucesso!')

    # Função para deletar um estudante pelo ID
    # Function to delete a student by ID
    def delete_student(self, id):
        self.c.execute("DELETE FROM students WHERE id=?", (id,))  # Executa a exclusão / Executes deletion
        self.conn.commit()  # Salva as alterações / Saves changes
        messagebox.showinfo('Sucesso', f'Estudante com ID:{id} foi deletado com sucesso!')


# Criando uma instância do sistema de registro
# Creating an instance of the registration system
registration_system = RegistrationSystem()




