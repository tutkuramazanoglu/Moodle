from tkinter import *
from tkinter import messagebox

import pypyodbc


class profossorPanel:
    def __init__(self, window, rdAdmin, rdProf, rdStudent, userNameLbl, userPasswordLbl, passwordEntry, nameEntry,
                 btnExit, btnSignIn):
        self.window = window
        self.rdAdmin = rdAdmin
        self.rdProf = rdProf
        self.rdStudent = rdStudent
        self.userNameLbl = userNameLbl
        self.userPasswordLbl = userPasswordLbl
        self.passwordEntry = passwordEntry
        self.nameEntry = nameEntry
        self.btnExit = btnExit
        self.btnSignIn = btnSignIn
        self.window.geometry("650x300")
        self.rdAdmin.configure(state=DISABLED)
        self.rdProf.configure(state=DISABLED)
        self.rdStudent.configure(state=DISABLED)
        self.window.title("Professor Panel")
        self.userNameLbl.destroy()
        self.userPasswordLbl.destroy()
        self.passwordEntry.destroy()
        self.nameEntry.destroy()
        self.btnExit.destroy()
        self.btnSignIn.destroy()

    def displayProf(self):
        self.lblFrame=LabelFrame(self.window,text="Grade")
        self.lblCourseNumber = Label(self.lblFrame, text="Course Number", font=("Arial Bold", 15), foreground="blue")
        self.lblCourseNumber.grid(column=1, row=1, padx=8, pady=8, sticky=W)
        self.courseNumberEntry = Entry(self.lblFrame, width=20)
        self.courseNumberEntry.grid(column=2, row=1, padx=8, pady=8, sticky=W)
        self.lblStudentNumber = Label(self.lblFrame, text="Student Number", font=("Arial Bold", 15), foreground="blue")
        self.lblStudentNumber.grid(column=1, row=2, padx=8, pady=8, sticky=W)
        self.studentNumberEntry = Entry(self.lblFrame, width=20)
        self.studentNumberEntry.grid(column=2, row=2, padx=8, pady=8, sticky=W)
        self.lblGrade = Label(self.lblFrame, text="Grade", font=("Arial Bold", 15), foreground="blue")
        self.lblGrade.grid(column=1, row=3, padx=8, pady=8, sticky=W)
        self.gradeEntry = Entry(self.lblFrame, width=20)
        self.gradeEntry.grid(column=2, row=3, padx=8, pady=8, sticky=W)
        self.lblFrame.grid(column=1, row=2)
        def clearWidget():

            self.gradeEntry.delete(0, 'end')
            self.courseNumberEntry.delete(0, 'end')
            self.studentNumberEntry.delete(0, 'end')

        self.btnDelete = Button(self.lblFrame, text="Reset", foreground="#290066", command=clearWidget)
        self.btnDelete.grid(column=2, row=5, padx=8, pady=8, sticky=W)

        def submitGrade():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                       WHERE TABLE_NAME = N'courseStudent';""")
            if len(result.fetchall()) == 1:
                if self.gradeEntry.get() != "" and self.courseNumberEntry.get() != "" and self.studentNumberEntry.get() != "":
                    cursor = connection.cursor()
                    strsql = "select * from courseStudent where studentID=? AND courseID=?"
                    cursor.execute(strsql, (self.studentNumberEntry.get(), self.courseNumberEntry.get(),))
                    result = cursor.fetchall()
                    if len(result) != 0:
                        cursor.execute("UPDATE courseStudent SET grade='%s' WHERE studentID='%s' AND courseID='%s'" % (
                            self.gradeEntry.get(), self.studentNumberEntry.get(), self.courseNumberEntry.get()))
                        connection.commit()
                        messagebox.showinfo("Success", "Grade is submitted.")
                    else:
                        messagebox.showwarning("Warning", "The student does not enroll the course.")

            else:
                messagebox.showerror("Error",
                                     "The student or course does not exist. Please check course number and student number.")

        self.btnSubmit = Button(self.lblFrame, text="Submit", foreground="#290066", command=submitGrade)
        self.btnSubmit.grid(column=1, row=5, padx=8, pady=8, sticky=W)
        self.btnExit = Button(self.lblFrame, text="Exit", command=self.window.destroy, foreground="#290066")
        self.btnExit.grid(column=3, row=5, padx=8, pady=8, sticky=W)
