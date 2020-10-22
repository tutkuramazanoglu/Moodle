from tkinter import *
import pypyodbc
from tkinter import messagebox


class studentPanel:
    def __init__(self, window, rdAdmin, rdProf, rdStudent, userNameLbl, userPasswordLbl, passwordEntry, nameEntry,
                 btnExit, btnSignIn, userName, userPassword):
        self.window = window
        self.userName = userName
        self.userPassword = userPassword
        self.rdAdmin = rdAdmin
        self.rdProf = rdProf
        self.rdStudent = rdStudent
        self.window.title("Admin Panel")
        self.userNameLbl = userNameLbl
        self.userPasswordLbl = userPasswordLbl
        self.passwordEntry = passwordEntry
        self.nameEntry = nameEntry
        self.btnExit = btnExit
        self.btnSignIn = btnSignIn
        self.window.geometry("650x650")
        self.rdAdmin.configure(state=DISABLED)
        self.rdProf.configure(state=DISABLED)
        self.rdStudent.configure(state=DISABLED)
        self.window.title("Student Panel")
        self.userNameLbl.destroy()
        self.userPasswordLbl.destroy()
        self.passwordEntry.destroy()
        self.nameEntry.destroy()
        self.btnExit.destroy()
        self.btnSignIn.destroy()

    def displayStudent(self):
        connection = pypyodbc.connect \
            ('DRIVER={SQL Server};'
             'SERVER=LENOVO\SQLEXPRESS;'
             'DATABASE=schoolDb;'
             'Trusted_Connection=yes;')
        cursor = connection.cursor()
        result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                                   WHERE TABLE_NAME = N'courseStudent';""")
        if len(result.fetchall()) == 1:
            cursor = connection.cursor()
            strsql = "select * from users where userName=? AND userPassword=? "
            cursor.execute(strsql, (self.userName, self.userPassword,))
            result = cursor.fetchall()
            courseName = []
            grade = []
            if len(result) != 0:
                userID = result[0][0]
                self.lblStudentName = Label(self.window, text="Student Name", font=("Arial Bold", 15),
                                            foreground="#800000")
                self.lblStudentName.grid(column=0, row=1, padx=8, pady=8, sticky=W)
                self.lblName = Label(self.window, text=self.userName, font=("Arial Bold", 15), foreground="#800000")
                self.lblName.grid(column=1, row=1, padx=8, pady=8, sticky=W)
                self.lblCourseName = Label(self.window, text="COURSE NAME", font=("Arial Bold", 15),
                                           foreground="#800000")
                self.lblCourseName.grid(column=1, row=2, padx=8, pady=8, sticky=W)
                self.lblGrade = Label(self.window, text="GRADE", font=("Arial Bold", 15), foreground="#800000")
                self.lblGrade.grid(column=2, row=2, padx=8, pady=8, sticky=W)
                strsql = "select * from courseStudent where studentID=? "
                cursor.execute(strsql, (userID,))
                result = cursor.fetchall()
                if len(result) != 0:
                    for i in range(0, len(result)):
                        courseID = result[i][0]
                        strsql = "select * from course where courseID=? "
                        cursor.execute(strsql, (courseID,))
                        courseResult = cursor.fetchall()
                        courseName.append(courseResult)
                        grade.append(result[i][2])
                    for i in range(0, len(courseName)):
                        record = "{0} \t".format(courseName[i][0][1])
                        print(courseName)
                        record2 = "{0} \n".format(grade[i])
                        lbl1 = Label(self.window, text=record, font=("Arial Bold", 15), foreground="#800000")
                        lbl1.grid(column=1, row=3 + i)
                        lbl2 = Label(self.window, text=record2, font=("Arial Bold", 15), foreground="#800000")
                        lbl2.grid(column=2, row=3 + i)
                    self.btnExit = Button(self.window, text="Exit", command=self.window.destroy, foreground="#800000")
                    self.btnExit.grid(column=2, row=4 + i, padx=8, pady=8, sticky=W)


                else:
                    messagebox.showwarning("Warning", "Your grade has not entered yet.")

        else:
            messagebox.showerror("Error", "Information does not exist.")
