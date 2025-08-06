from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from datetime import date
from main import RegistrationSystem
import os

# === Color Scheme ===
co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#e5e5e5"
co4 = "#403d3d"
co6 = "#146C94"
co9 = "#e9edf5"

class StudentRegistrationApp:
    def __init__(self, master):
        self.master = master
        self.picture = None
        self.picture_string = ""
        self.registration_system = RegistrationSystem()
        
        self.setup_window()
        self.create_frames()
        self.create_widgets()
        self.show_students()
    
    def setup_window(self):
        self.master.title("Student Registration System")
        self.master.geometry('810x535')
        self.master.configure(background=co1)
        self.master.resizable(width=False, height=False)
        style = ttk.Style(self.master)
        style.theme_use("clam")

    def create_frames(self):
        self.frame_logo = Frame(self.master, width=850, height=52, bg=co6)
        self.frame_logo.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        
        self.frame_button = Frame(self.master, width=100, height=200, bg=co1, relief=RAISED)
        self.frame_button.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)
        
        self.frame_details = Frame(self.master, width=800, height=100, bg=co1, relief=RAISED)
        self.frame_details.grid(row=1, column=1, padx=10, pady=1, sticky=NSEW)
        
        self.frame_table = Frame(self.master, width=800, height=100, bg=co2, relief=RAISED)
        self.frame_table.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

    def create_widgets(self):
        # Header
        app_lg = Image.open('pictures/logo.png').resize((50, 50))
        app_lg = ImageTk.PhotoImage(app_lg)
        app_logo = Label(self.frame_logo, image=app_lg, text="  Student Registration System",
                         compound=LEFT, anchor=NW, font=('Verdana', 15), bg=co6, fg=co1)
        app_logo.image = app_lg
        app_logo.place(x=5, y=0)
        
        # Student Photo
        img = Image.open('pictures/logo.png').resize((130, 130))
        self.picture = ImageTk.PhotoImage(img)
        self.l_picture = Label(self.frame_details, image=self.picture, bg=co1)
        self.l_picture.place(x=390, y=10)

        # Labels and Entries
        self.l_name = Label(self.frame_details, text="Name *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        self.l_name.place(x=4, y=10)
        self.e_name = Entry(self.frame_details, width=30, justify='left', relief='solid')
        self.e_name.place(x=7, y=40)
        
        self.l_email = Label(self.frame_details, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        self.l_email.place(x=4, y=70)
        self.e_email = Entry(self.frame_details, width=30, justify='left', relief='solid')
        self.e_email.place(x=7, y=100)
        
        self.l_phone = Label(self.frame_details, text="Phone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        self.l_phone.place(x=4, y=130)
        self.e_phone = Entry(self.frame_details, width=15, justify='left', relief='solid')
        self.e_phone.place(x=7, y=160)
        
        self.l_gender = Label(self.frame_details, text="Gender *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        self.l_gender.place(x=127, y=130)
        self.c_gender = ttk.Combobox(self.frame_details, width=7, font=('Ivy 8 bold'), justify='center')
        self.c_gender['values'] = ('M', 'F', 'T')
        self.c_gender.place(x=130, y=160)
        
        self.l_birth_date = Label(self.frame_details, text="Birth Date *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        self.l_birth_date.place(x=220, y=10)
        self.birth_date = DateEntry(self.frame_details, width=18, background='darkblue', foreground='white',
                                    borderwidth=2, year=2025)
        self.birth_date.place(x=224, y=40)
        
        self.l_address = Label(self.frame_details, text="Address *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        self.l_address.place(x=220, y=70)
        self.e_address = Entry(self.frame_details, width=20, justify='left', relief='solid')
        self.e_address.place(x=224, y=100)
        
        self.l_course = Label(self.frame_details, text="Course *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        self.l_course.place(x=220, y=130)
        self.c_course = ttk.Combobox(self.frame_details, width=20, font=('Ivy 8 bold'), justify='center')
        self.c_course['values'] = (
            "Business Administration", "Agronomy", "Architecture and Urbanism", "Visual Arts", "Biomedicine",
            "Computer Science", "Biological Sciences", "Accounting", "Economics", "Social Communication", 
            "Design", "Law", "Physical Education", "Nursing", "Environmental Engineering", "Civil Engineering",
            "Computer Engineering", "Control and Automation Engineering", "Production Engineering",
            "Electrical Engineering", "Mechanical Engineering", "Chemical Engineering", "Statistics",
            "Pharmacy", "Philosophy", "Physics", "Physiotherapy", "Geography", "Information Management",
            "Human Resources Management", "History", "Journalism", "Literature", "Logistics", "Marketing",
            "Mathematics", "Medicine", "Veterinary Medicine", "Fashion", "Music", "Nutrition", "Dentistry",
            "Pedagogy", "Psychology", "Advertising", "Chemistry", "International Relations",
            "Information Systems", "Social Work", "Information Technology", "Tourism", "Zootechnics"
        )
        self.c_course.place(x=224, y=160)
        
        # Search Section
        self.frame_to_search_for = Frame(self.frame_button, bg=co1, relief=RAISED)
        self.frame_to_search_for.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)
        Label(self.frame_to_search_for, text="Search Student [ID]", bg=co1, fg=co4, font=('Ivy 10')).grid(row=0, column=0)
        self.e_to_alter = Entry(self.frame_to_search_for, width=5, justify='center', relief='solid', font=('Ivy 10'))
        self.e_to_alter.grid(row=1, column=0, pady=10)
        Button(self.frame_to_search_for, command=self.search, text='Search', font=('Ivy 7 bold'), bg=co1, fg=co0).grid(row=2, column=0)
        
        # Photo Upload Button
        self.button_loading = Button(self.frame_details, command=self.choose_image, text='LOAD PHOTO', width=20,
                                     font=('Ivy 7 bold'), bg=co1, fg=co0)
        self.button_loading.place(x=390, y=160)
        
        # Action Buttons
        app_add = ImageTk.PhotoImage(Image.open('pictures/adicionar.png').resize((25, 25)))
        button_to_add = Button(self.frame_button, command=self.add, image=app_add, text=' Add', compound=LEFT,
                               font=('Ivy 11'), bg=co1, fg=co0)
        button_to_add.image = app_add
        button_to_add.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)
        
        app_update = ImageTk.PhotoImage(Image.open('pictures/atualizar.png').resize((25, 25)))
        button_to_update = Button(self.frame_button, command=self.update, image=app_update, text=' Update', compound=LEFT,
                                  font=('Ivy 11'), bg=co1, fg=co0)
        button_to_update.image = app_update
        button_to_update.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)
        
        app_delete = ImageTk.PhotoImage(Image.open('pictures/excluir.png').resize((25, 25)))
        button_to_delete = Button(self.frame_button, command=self.delete, image=app_delete, text=' Delete', compound=LEFT,
                                  font=('Ivy 11'), bg=co1, fg=co0)
        button_to_delete.image = app_delete
        button_to_delete.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

    def add(self):
        data = [
            self.e_name.get(), self.e_email.get(), self.e_phone.get(), self.c_gender.get(),
            self.birth_date.get(), self.e_address.get(), self.c_course.get(), self.picture_string
        ]
        if '' in data:
            messagebox.showerror('Error', 'Please fill in all fields.')
            return
        
        self.registration_system.register_student(data)
        self.clear_fields()
        self.show_students()
    
    def search(self):
        try:
            id_student = int(self.e_to_alter.get())
            dados = self.registration_system.search_student(id_student)
            
            self.e_name.delete(0, END)
            self.e_name.insert(END, dados[1])
            self.e_email.delete(0, END)
            self.e_email.insert(END, dados[2])
            self.e_phone.delete(0, END)
            self.e_phone.insert(END, dados[3])
            self.c_gender.set(dados[4])
            self.birth_date.set_date(dados[5])
            self.e_address.delete(0, END)
            self.e_address.insert(END, dados[6])
            self.c_course.set(dados[7])
            self.picture_string = dados[8]
            
            img = Image.open(self.picture_string).resize((130, 130))
            self.picture = ImageTk.PhotoImage(img)
            self.l_picture.config(image=self.picture)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to retrieve student: {e}")

    def update(self):
        try:
            id_student = int(self.e_to_alter.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid student ID to update.")
            return

        data = [
            self.e_name.get(), self.e_email.get(), self.e_phone.get(), self.c_gender.get(),
            self.birth_date.get(), self.e_address.get(), self.c_course.get(), self.picture_string,
            id_student
        ]
        
        if '' in data[:-1]:
            messagebox.showerror('Error', 'Please fill in all fields.')
            return

        self.registration_system.update_student(data)
        self.clear_fields()
        self.show_students()

    def delete(self):
        try:
            id_student = int(self.e_to_alter.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid student ID to delete.")
            return

        self.registration_system.delete_student(id_student)
        self.clear_fields()
        self.e_to_alter.delete(0, END)
        img = Image.open('pictures/logo.png').resize((130, 130))
        self.picture = ImageTk.PhotoImage(img)
        self.l_picture.config(image=self.picture)
        self.show_students()

    def choose_image(self):
        image_path = fd.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if image_path:
            self.picture_string = image_path
            img = Image.open(image_path).resize((130, 130))
            self.picture = ImageTk.PhotoImage(img)
            self.l_picture.config(image=self.picture)
            self.button_loading['text'] = 'Change Photo'

    def show_students(self):
        list_header = ['id', 'name', 'email', 'phone', 'gender', 'birth_date', 'address', 'course']
        df_list = self.registration_system.view_all_students()

        # Remove tabela antiga se existir
        if hasattr(self, 'tree_aluno'):
            self.tree_aluno.destroy()

        self.tree_aluno = ttk.Treeview(self.frame_table, selectmode="extended", columns=list_header, show="headings")
        vsb = ttk.Scrollbar(self.frame_table, orient="vertical", command=self.tree_aluno.yview)
        hsb = ttk.Scrollbar(self.frame_table, orient="horizontal", command=self.tree_aluno.xview)
        
        self.tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        
        hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center"]
        h = [40, 150, 150, 70, 70, 70, 120, 100]

        for i, col in enumerate(list_header):
            self.tree_aluno.heading(col, text=col.title(), anchor=NW)
            self.tree_aluno.column(col, width=h[i], anchor=hd[i])

        for item in df_list:
            self.tree_aluno.insert('', 'end', values=item)

    def clear_fields(self):
        self.e_name.delete(0, END)
        self.e_email.delete(0, END)
        self.e_phone.delete(0, END)
        self.c_gender.set('')
        self.birth_date.set_date(date.today())
        self.e_address.delete(0, END)
        self.c_course.set('')

if __name__ == "__main__":
    window = Tk()
    app = StudentRegistrationApp(window)
    window.mainloop()