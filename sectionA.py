from tkinter import *
from tkinter import messagebox
import AdminPanel
import ProfessorPanel
import StudentPanel
import pypyodbc


class formSignIn:
    def __init__(self):
        self.window = Tk()
        self.userName = ""
        self.userPassword = ""
        self.selected = IntVar()
        self.window.geometry("500x250")
        self.window.title("Welcome")
        self.userTypeLbl = Label(self.window, text="User Type", font=("Arial Bold", 15), foreground="green")
        self.userTypeLbl.grid(column=0, row=0, padx=8, pady=8, sticky=W)
        self.rdAdmin = Radiobutton(self.window, text="Admin", value=1, font=("Arial", 10), variable=self.selected,
                                   foreground="brown")
        self.rdAdmin.grid(column=1, row=0, padx=8, pady=8, sticky=W)
        self.rdProf = Radiobutton(self.window, text="Professor", value=2, font=("Arial", 10), variable=self.selected,
                                  foreground="brown")
        self.rdProf.grid(column=2, row=0, padx=8, pady=8, sticky=W)
        self.rdStudent = Radiobutton(self.window, text="Student", value=3, font=("Arial", 10), variable=self.selected,
                                     foreground="brown")
        self.rdStudent.grid(column=3, row=0, padx=8, pady=8, sticky=W)
        self.userNameLbl = Label(self.window, text="User Name", font=("Arial Bold", 15), foreground="green")
        self.userNameLbl.grid(column=0, row=1, padx=8, pady=8, sticky=W)
        self.nameEntry = Entry(self.window, width=20, foreground="brown", font=("bold", 10))
        self.nameEntry.grid(column=1, row=1, padx=8, pady=8, sticky=W)
        self.userPasswordLbl = Label(self.window, text="Password", font=("Arial Bold", 15), foreground="green")
        self.userPasswordLbl.grid(column=0, row=2, padx=8, pady=8, sticky=W)
        self.passwordEntry = Entry(self.window, width=20, foreground="brown", font=("bold", 10))
        self.passwordEntry.grid(column=1, row=2, padx=8, pady=8, sticky=W)

        connection = pypyodbc.connect \
            ('DRIVER={SQL Server};'
             'SERVER=LENOVO\SQLEXPRESS;'
             'DATABASE=schoolDb;'
             'Trusted_Connection=yes;')

        def clickedSingIn():
            cursor = connection.cursor()
            strsql = "select * from users where userName=? and userPassword=? and userType=?"
            cursor.execute(strsql, (self.nameEntry.get(), self.passwordEntry.get(), self.selected.get(),))
            result = cursor.fetchall()
            if len(result) > 0:
                if result[0][3] == 1:
                    AdminPanel.adminPanel(self.window, self.rdAdmin, self.rdProf, self.rdStudent, self.userNameLbl,
                                          self.userPasswordLbl, self.passwordEntry, self.nameEntry, self.btnExit,
                                          self.btnSignIn)
                    AdminPanel.adminPanel.displayAdmin(self)
                elif result[0][3] == 2:
                    ProfessorPanel.profossorPanel(self.window, self.rdAdmin, self.rdProf, self.rdStudent,
                                                  self.userNameLbl,
                                                  self.userPasswordLbl, self.passwordEntry, self.nameEntry,
                                                  self.btnExit,
                                                  self.btnSignIn)
                    ProfessorPanel.profossorPanel.displayProf(self)
                    ProfessorPanel.profossorPanel.displayProf(self)
                else:
                    self.userName = self.nameEntry.get()
                    self.userPassword = self.passwordEntry.get()
                    StudentPanel.studentPanel(self.window, self.rdAdmin, self.rdProf, self.rdStudent,
                                              self.userNameLbl,
                                              self.userPasswordLbl, self.passwordEntry, self.nameEntry,
                                              self.btnExit,
                                              self.btnSignIn, self.userName, self.userPassword)
                    StudentPanel.studentPanel.displayStudent(self)
            else:
                strsql = "select * from users where userName=?"
                strsql1 = "select * from users where  userPassword=? "
                strsql2 = "select * from users where  userName=? and userPassword=? and userType=?"
                cursor.execute(strsql, (self.nameEntry.get(),))
                a = cursor.fetchall()
                cursor.execute(strsql1, (self.passwordEntry.get(),))
                b = cursor.fetchall()
                cursor.execute(strsql2, (self.nameEntry.get(), self.passwordEntry.get(), self.selected.get(),))
                c = cursor.fetchall()
                print(c)
                if len(a) == 0:
                    messagebox.showwarning("Warning", "User name is entered wrong.")
                elif len(b) == 0:
                    messagebox.showwarning("Warning", "Password is entered wrong.")
                elif len(c) == 0:
                    messagebox.showwarning("Warning", "User Type is entered wrong.")
                else:
                    messagebox.showwarning("Warning", "The user does not exist in database.")

        self.btnSignIn = Button(self.window, text="Sing In", command=clickedSingIn, foreground="brown",
                                font=("bold", 11))
        self.btnSignIn.grid(column=1, row=3, padx=8, pady=8, sticky=W)
        self.btnExit = Button(self.window, text="Exit", command=self.window.destroy, foreground="brown",
                              font=("bold", 11))
        self.btnExit.grid(column=2, row=3, padx=8, pady=8, sticky=W)

        mainloop()


formSignIn()
