# === Importing Required Libraries ===
from tkinter.ttk import *  # Import themed Tkinter widgets
from tkinter import *      # Import standard Tkinter widgets
from tkinter import ttk    # Additional ttk widgets (redundant with above imports)
from tkinter import messagebox  # Message dialogs
from tkinter import filedialog as fd  # File dialog for choosing files
from PIL import ImageTk, Image  # Image handling (Pillow library)
from tkcalendar import Calendar, DateEntry  # Calendar widget for date selection
from datetime import date
from main import *  # Import your own module, presumably with registration_system object

# === Color Scheme ===
co0 = "#2e2d2b"  # Dark gray (used for text)
co1 = "#feffff"  # White (background)
co2 = "#e5e5e5"  # Light gray (table background)
co3 = "#00a095"  # Teal (not used in this code snippet)
co4 = "#403d3d"  # Text color for labels
co6 = "#146C94"  # Blue (header background)
co7 = "#ef5350"  # Red (not used here)
co8 = "#263238"  # Dark green (not used here)
co9 = "#e9edf5"  # Light blue (not used here)

# === Global Variables for managing student image ===
picture = None           # The Tkinter-compatible photo image object
picture_string = ""      # Path to the image file

# === Main Application Window Setup ===
window = Tk()
window.title("Student Registration System")
window.geometry('810x535')   # Fixed window size
window.configure(background=co1)
window.resizable(width=False, height=False)  # Disable resizing

# Use 'clam' theme for better styling of ttk widgets
style = Style(window)
style.theme_use("clam")

# === Header Frame with Logo ===
frame_logo = Frame(window, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, columnspan=5, sticky=NSEW)

# Load and display logo image with text in the header
app_lg = Image.open('pictures/logo.png').resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="  Student Registration System",
                 compound=LEFT, anchor=NW, font=('Verdana', 15), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

# === Sidebar for Buttons ===
frame_button = Frame(window, width=100, height=200, bg=co1, relief=RAISED)
frame_button.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

# === Input Area for Student Information ===
frame_details = Frame(window, width=800, height=100, bg=co1, relief=RAISED)
frame_details.grid(row=1, column=1, padx=10, pady=1, sticky=NSEW)

# === Load Default Photo ===
img = Image.open('pictures/logo.png').resize((130, 130))
picture = ImageTk.PhotoImage(img)
l_picture = Label(frame_details, image=picture, bg=co1)
l_picture.place(x=390, y=10)

# === Function: Add Student to Database ===
def add():
    global picture, picture_string, l_picture

    # Collect data from input fields
    name = e_name.get()
    email = e_email.get()
    phone = e_phone.get()
    gender = c_gender.get()
    birth = birth_date.get()
    address = e_address.get()
    course = c_course.get()
    picture_path = picture_string

    data = [name, email, phone, gender, birth, address, course, picture_path]

    # Validate inputs - ensure no fields are empty
    if '' in data:
        messagebox.showerror('Error', 'Please fill in all fields.')
        return

    # Register student using external module function
    registration_system.register_student(data)

    # Clear all input fields after adding
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_phone.delete(0, END)
    c_gender.set('')
    birth_date.set_date(date.today())
    e_address.delete(0, END)
    c_course.set('')

    # Refresh the student list in the table
    show_students()

# === Function: Search Student by ID ===
def search():
    global picture, picture_string, l_picture

    try:
        id_student = int(e_to_alter.get())
        dados = registration_system.search_student(id_student)

        # Populate fields with retrieved student data
        e_name.delete(0, END)
        e_name.insert(END, dados[1])
        e_email.delete(0, END)
        e_email.insert(END, dados[2])
        e_phone.delete(0, END)
        e_phone.insert(END, dados[3])
        c_gender.set(dados[4])
        birth_date.set_date(dados[5])
        e_address.delete(0, END)
        e_address.insert(END, dados[6])
        c_course.set(dados[7])
        picture_string = dados[8]

        # Display the student's image
        img = Image.open(picture_string).resize((130, 130))
        picture = ImageTk.PhotoImage(img)
        l_picture.config(image=picture)

    except Exception as e:
        messagebox.showerror("Error", f"Unable to retrieve student: {e}")

# === Function: Update Student Data ===
def update():
    global picture, picture_string, l_picture

    try:
        id_student = int(e_to_alter.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid student ID to update.")
        return

    # Collect data from fields
    name = e_name.get()
    email = e_email.get()
    phone = e_phone.get()
    gender = c_gender.get()
    birth = birth_date.get()
    address = e_address.get()
    course = c_course.get()
    picture_path = picture_string

    data = [id_student, name, email, phone, gender, birth, address, course, picture_path]

    # Validate inputs
    if '' in data[1:]:  # exclude id_student from validation
        messagebox.showerror('Error', 'Please fill in all fields.')
        return

    # Update student in external system
    registration_system.update_student(data)

    # Clear fields after update
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_phone.delete(0, END)
    c_gender.set('')
    birth_date.set_date(date.today())
    e_address.delete(0, END)
    c_course.set('')

    # Refresh the image display (optional, since the image path should be unchanged)
    img = Image.open(picture_string).resize((130, 130))
    picture = ImageTk.PhotoImage(img)
    l_picture.config(image=picture)

    # Refresh the student list
    show_students()

# === Function: Delete Student ===
def delete():
    global picture, picture_string, l_picture

    try:
        id_student = int(e_to_alter.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid student ID to delete.")
        return

    registration_system.delete_student(id_student)

    # Clear all input fields after deletion
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_phone.delete(0, END)
    c_gender.set('')
    birth_date.set_date(date.today())
    e_address.delete(0, END)
    c_course.set('')
    e_to_alter.delete(0, END)

    # Reset the image to default (logo)
    img = Image.open('pictures/logo.png').resize((130, 130))
    picture = ImageTk.PhotoImage(img)
    l_picture.config(image=picture)

    # Refresh the student list
    show_students()

# === Labels and Entry Fields for Student Info ===
l_name = Label(frame_details, text="Name *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_name.place(x=4, y=10)
e_name = Entry(frame_details, width=30, justify='left', relief='solid')
e_name.place(x=7, y=40)

l_email = Label(frame_details, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_phone = Label(frame_details, text="Phone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_phone.place(x=4, y=130)
e_phone = Entry(frame_details, width=15, justify='left', relief='solid')
e_phone.place(x=7, y=160)

l_gender = Label(frame_details, text="Gender *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_gender.place(x=127, y=130)
c_gender = ttk.Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify='center')
c_gender['values'] = ('M', 'F', 'T')
c_gender.place(x=130, y=160)

l_birth_date = Label(frame_details, text="Birth Date *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_birth_date.place(x=220, y=10)
birth_date = DateEntry(frame_details, width=18, background='darkblue', foreground='white',
                       borderwidth=2, year=2025)
birth_date.place(x=224, y=40)

l_address = Label(frame_details, text="Address *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_address.place(x=220, y=70)
e_address = Entry(frame_details, width=20, justify='left', relief='solid')
e_address.place(x=224, y=100)

l_course = Label(frame_details, text="Course *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_course.place(x=220, y=130)
c_course = ttk.Combobox(frame_details, width=20, font=('Ivy 8 bold'), justify='center')
c_course['values'] = (
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
c_course.place(x=224, y=160)

# === Frame to Display Student Records in Table ===
frame_table = Frame(window, width=800, height=100, bg=co2, relief=RAISED)
frame_table.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

# === Function: Display All Students in Treeview Table ===
def show_students():
    list_header = ['id', 'name', 'email', 'phone', 'gender', 'birth_date', 'address', 'course']
    df_list = registration_system.view_all_students()

    # Clear existing treeview if any to avoid duplicates
    for widget in frame_table.winfo_children():
        widget.destroy()

    tree_aluno = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree_aluno.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')

    hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center"]
    h = [40, 150, 150, 70, 70, 70, 120, 100]

    for i, col in enumerate(list_header):
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        tree_aluno.column(col, width=h[i], anchor=hd[i])

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)

# === Student Search Section ===
frame_to_search_for = Frame(frame_button, bg=co1, relief=RAISED)
frame_to_search_for.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

Label(frame_to_search_for, text="Search Student [ID]", bg=co1, fg=co4, font=('Ivy 10')).grid(row=0, column=0)
e_to_alter = Entry(frame_to_search_for, width=5, justify='center', relief='solid', font=('Ivy 10'))
e_to_alter.grid(row=1, column=0, pady=10)

button_to_alter = Button(frame_to_search_for, command=search, text='Search', font=('Ivy 7 bold'), bg=co1, fg=co0)
button_to_alter.grid(row=2, column=0)

# === Function: Choose Image from File ===
def choose_image():
    global picture, picture_string, l_picture
    image_path = fd.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
    if image_path:
        picture_string = image_path
        img = Image.open(image_path).resize((130, 130))
        picture = ImageTk.PhotoImage(img)
        l_picture.config(image=picture)
        button_loading['text'] = 'Change Photo'

# === Photo Upload Button ===
button_loading = Button(frame_details, command=choose_image, text='LOAD PHOTO', width=20,
                        font=('Ivy 7 bold'), bg=co1, fg=co0)
button_loading.place(x=390, y=160)

# === Action Buttons: Add, Update, Delete with Icons ===
app_add = ImageTk.PhotoImage(Image.open('pictures/adicionar.png').resize((25, 25)))
button_to_add = Button(frame_button, command=add, image=app_add, text=' Add', compound=LEFT,
                       font=('Ivy 11'), bg=co1, fg=co0)
button_to_add.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_update = ImageTk.PhotoImage(Image.open('pictures/atualizar.png').resize((25, 25)))
button_to_update = Button(frame_button, command=update, image=app_update, text=' Update', compound=LEFT,
                          font=('Ivy 11'), bg=co1, fg=co0)
button_to_update.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_delete = ImageTk.PhotoImage(Image.open('pictures/excluir.png').resize((25, 25)))
button_to_delete = Button(frame_button, command=delete, image=app_delete, text=' Delete', compound=LEFT,
                          font=('Ivy 11'), bg=co1, fg=co0)
button_to_delete.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# === Initialize the table with current students when app starts ===
show_students()

# === Start the GUI main loop ===
window.mainloop()
