from tkinter import *
from tkinter import messagebox
import pypyodbc


class adminPanel:
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
        self.window.geometry("1000x1000")
        self.rdAdmin.configure(state=DISABLED)
        self.rdProf.configure(state=DISABLED)
        self.rdStudent.configure(state=DISABLED)
        self.window.title("Admin Panel")
        self.userNameLbl.destroy()
        self.userPasswordLbl.destroy()
        self.passwordEntry.destroy()
        self.nameEntry.destroy()
        self.btnExit.destroy()
        self.btnSignIn.destroy()

    def displayAdmin(self):
        self.studentFrame = LabelFrame(self.window, text="Student", font=("Arial Bold", 18), foreground="black")
        self.lblStudentName = Label(self.studentFrame, text="Student Name", font=("Arial Bold", 15), foreground="red")
        self.lblStudentName.grid(column=0, row=1, padx=8, pady=8, sticky=W)
        self.studentNameEntry = Entry(self.studentFrame, width=20)
        self.studentNameEntry.grid(column=1, row=1, padx=8, pady=8, sticky=W)
        self.lblStudentNumber = Label(self.studentFrame, text="Student Number", font=("Arial Bold", 15),
                                      foreground="red")
        self.lblStudentNumber.grid(column=0, row=2, padx=8, pady=8, sticky=W)
        self.studentNumberEntry = Entry(self.studentFrame, width=20)
        self.studentNumberEntry.grid(column=1, row=2, padx=8, pady=8, sticky=W)
        self.studentFrame.grid(column=0, row=1)

        def updateStudent():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                   WHERE TABLE_NAME = N'student';""")
            if len(result.fetchall()) == 1:
                cursor = connection.cursor()
                strsql = "select * from student where studentID=? "
                cursor.execute(strsql, (self.studentNumberEntry.get(),))
                result = cursor.fetchall()
                if len(result) != 0:
                    if self.studentNameEntry.get() != "":
                        cursor.execute("UPDATE student SET studentName='%s' WHERE studentID='%s'" % (
                            self.studentNameEntry.get(), self.studentNumberEntry.get()))
                        cursor.execute("UPDATE users SET userName='%s' WHERE userID='%s'" % (
                            self.studentNameEntry.get(), self.studentNumberEntry.get()))
                        messagebox.showinfo("Error", "Student is updated.")
                        connection.commit()

                    connection.close()
                else:
                    messagebox.showerror("Error", "Student does not exist in database.")
            else:
                messagebox.showerror("Error", "Please first enter student's information.")

        self.btnUpdate = Button(self.studentFrame, text="Update Student", foreground="#ff1a1a", command=updateStudent)
        self.btnUpdate.grid(column=2, row=2, padx=8, pady=8, sticky=W)

        def deleteStudent():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                               WHERE TABLE_NAME = N'student';""")
            if len(result.fetchall()) == 1:
                cursor = connection.cursor()
                strsql = "select * from student where studentID=? "
                cursor.execute(strsql, (self.studentNumberEntry.get(),))
                result = cursor.fetchall()
                if len(result) != 0:
                    cursor.execute("DELETE student WHERE studentID='%s'" % (self.studentNumberEntry.get()))
                    cursor.execute("DELETE users WHERE userID='%s'" % (self.studentNumberEntry.get()))
                    cursor.execute("DELETE courseStudent WHERE studentID='%s'" % (self.studentNumberEntry.get()))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Success", "Student is deleted succesfully.")
                else:
                    messagebox.showerror("Unsuccess", "The student does not exist in database.")

        self.btnUpdate = Button(self.studentFrame, text="Delete Student", foreground="#ff1a1a", command=deleteStudent)
        self.btnUpdate.grid(column=2, row=1, padx=8, pady=8, sticky=W)

        self.courseFrame = LabelFrame(self.window, text="Course", font=("Arial Bold", 18), foreground="black")
        self.lblCourseName = Label(self.courseFrame, text="Course Name", font=("Arial Bold", 15), foreground="red")
        self.lblCourseName.grid(column=0, row=4, padx=8, pady=8, sticky=W)
        self.courseNameEntry = Entry(self.courseFrame, width=20)
        self.courseNameEntry.grid(column=1, row=4, padx=8, pady=8, sticky=W)
        self.lblCourseNumber = Label(self.courseFrame, text="Course Number", font=("Arial Bold", 15), foreground="red")
        self.lblCourseNumber.grid(column=0, row=6, padx=8, pady=8, sticky=W)
        self.CourseNumberEntry = Entry(self.courseFrame, width=20)
        self.CourseNumberEntry.grid(column=1, row=6, padx=8, pady=8, sticky=W)
        self.lblProfCourse = Label(self.courseFrame, text="Professor ID", font=("Arial Bold", 15), foreground="red")
        self.lblProfCourse.grid(column=0, row=5, padx=8, pady=8, sticky=W)
        self.profCourseEntry = Entry(self.courseFrame, width=20)
        self.profCourseEntry.grid(column=1, row=5, padx=8, pady=8, sticky=W)
        self.courseFrame.grid(column=0, row=2)

        def updateCourse():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                   WHERE TABLE_NAME = N'course';""")
            if len(result.fetchall()) == 1:
                cursor = connection.cursor()
                strsql = "select * from course where courseID=? "
                cursor.execute(strsql, (self.CourseNumberEntry.get(),))
                result = cursor.fetchall()
                if len(result) != 0:
                    if self.courseNameEntry.get() != "":
                        cursor.execute("UPDATE course SET courseName='%s' WHERE courseID='%s'" % (
                            self.courseNameEntry.get(), self.CourseNumberEntry.get()))
                        connection.commit()
                        messagebox.showinfo("Success", "Course name is updated succussfully.")
                    if self.profCourseEntry.get() != "":
                        strsql = "select * from professor where professorID=? "
                        cursor.execute(strsql, (self.profCourseEntry.get(),))
                        result = cursor.fetchall()
                        if len(result) != 0:
                            cursor.execute("UPDATE professorCourse SET professor='%s' WHERE courseID='%s'" % (
                                self.profCourseEntry.get(), self.CourseNumberEntry.get()))
                            connection.commit()
                            messagebox.showinfo("Success", "Professor is changed.")
                        else:
                            messagebox.showwarning("Error", "The professor number does not exist in database.")
                    connection.close()
                else:
                    messagebox.showerror("Error", "Course does not exist in database.")
            else:
                messagebox.showerror("Error", "Please first enter course's information.")

        self.btnUpdate = Button(self.courseFrame, text="Update Course", foreground="#ff1a1a", command=updateCourse)
        self.btnUpdate.grid(column=2, row=5, padx=8, pady=8, sticky=W)

        def deleteCourse():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                                     WHERE TABLE_NAME = N'course';""")
            if len(result.fetchall()) == 1:
                cursor = connection.cursor()
                strsql = "select * from course where courseID=? "
                cursor.execute(strsql, (self.CourseNumberEntry.get(),))
                result = cursor.fetchall()
                if len(result) != 0:
                    cursor.execute("DELETE course WHERE courseID='%s'" % (self.CourseNumberEntry.get()))
                    cursor.execute("DELETE professorCourse WHERE courseID='%s'" % (self.CourseNumberEntry.get()))
                    cursor.execute("DELETE courseStudent WHERE courseID='%s'" % (self.CourseNumberEntry.get()))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Success", "Course is deleted succesfully.")
                else:
                    messagebox.showerror("Unsuccess", "The course does not exist in database.")
            else:
                messagebox.showerror("Unsuccess", "Invalid entering.")

        self.btnUpdate = Button(self.courseFrame, text="Delete Course", foreground="#ff1a1a", command=deleteCourse)
        self.btnUpdate.grid(column=2, row=6, padx=8, pady=8, sticky=W)

        def submitCourse():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                               WHERE TABLE_NAME = N'professor';""")
            if len(result.fetchall()) == 1:
                if self.CourseNumberEntry.get() != "" and self.courseNameEntry.get() != "" and self.profCourseEntry.get() != "":
                    cursor = connection.cursor()
                    strsql = "select * from professor where professorID=? "
                    cursor.execute(strsql, (self.profCourseEntry.get(),))
                    result = cursor.fetchall()
                    if len(result) != 0:
                        cursor.execute("INSERT INTO course VALUES (?, ?)",
                                       (self.CourseNumberEntry.get(), self.courseNameEntry.get()))
                        cursor.execute("INSERT INTO professorCourse VALUES (?, ?)",
                                       (self.CourseNumberEntry.get(), self.profCourseEntry.get()))
                        connection.commit()
                        messagebox.showinfo("Success", "Course is saved succussfully.")
                    else:
                        messagebox.showwarning("Warning", "Please check professor number.")
                else:
                    messagebox.showerror("Error", "Please enter all informaiton for course..")

        self.btnSubmit = Button(self.courseFrame, text="Submit Course", foreground="#ff1a1a", command=submitCourse)
        self.btnSubmit.grid(column=2, row=4, padx=8, pady=8, sticky=W)

        # PROF
        self.professorFrame = LabelFrame(self.window, text="Professor", font=("Arial Bold", 18), foreground="black")
        self.lblProfessorName = Label(self.professorFrame, text="Professor Name", font=("Arial Bold", 15),
                                      foreground="red")
        self.lblProfessorName.grid(column=0, row=6, padx=8, pady=8, sticky=W)
        self.professorNameEntry = Entry(self.professorFrame, width=20)
        self.professorNameEntry.grid(column=1, row=6, padx=8, pady=8, sticky=W)
        self.lblProfessorNumber = Label(self.professorFrame, text="Professor Number", font=("Arial Bold", 15),
                                        foreground="red")
        self.lblProfessorNumber.grid(column=0, row=7, padx=8, pady=8, sticky=W)
        self.professorNumberEntry = Entry(self.professorFrame, width=20)
        self.professorNumberEntry.grid(column=1, row=7, padx=8, pady=8, sticky=W)
        self.lblCourseProfessor = Label(self.professorFrame, text="Course ID", font=("Arial Bold", 15),
                                        foreground="red")
        self.lblCourseProfessor.grid(column=0, row=6, padx=8, pady=8, sticky=W)
        self.CourseProfessorEntry = Entry(self.professorFrame, width=20)
        self.CourseProfessorEntry.grid(column=1, row=6, padx=8, pady=8, sticky=W)
        self.professorFrame.grid(column=1, row=1)

        def updateProfessor():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                               WHERE TABLE_NAME = N'professor';""")
            if len(result.fetchall()) == 1:
                strsql = "select * from professor where professorID=? "
                cursor.execute(strsql, (self.professorNumberEntry.get(),))
                result = cursor.fetchall()
                if len(result) != 0:
                    if self.professorNameEntry.get() != "":
                        cursor.execute("UPDATE professor SET professorName='%s' WHERE professorID='%s'" % (
                            self.professorNameEntry.get(), self.professorNumberEntry.get()))
                        cursor.execute("UPDATE users SET userName='%s' WHERE userID='%s'" % (
                            self.professorNameEntry.get(), self.professorNumberEntry.get()))
                        connection.commit()
                        messagebox.showinfo("Success", "Professor name is updated succussfully.")
                    connection.close()
                else:
                    messagebox.showerror("Error", "Professor does not exist in database.")
            else:
                messagebox.showerror("Error", "Please first enter professor's information.")

        self.btnUpdate = Button(self.professorFrame, text="Update Professor", foreground="#ff1a1a",
                                command=updateProfessor)
        self.btnUpdate.grid(column=2, row=6, padx=8, pady=8, sticky=W)

        def deleteProfessor():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                                                         WHERE TABLE_NAME = N'course';""")
            if len(result.fetchall()) == 1:
                cursor = connection.cursor()
                strsql = "select * from professor where professorID=? "
                cursor.execute(strsql, (self.professorNumberEntry.get(),))
                result = cursor.fetchall()
                if len(result) != 0:
                    cursor.execute("DELETE professor WHERE professorID='%s'" % (self.professorNumberEntry.get()))
                    cursor.execute("DELETE users WHERE userID='%s'" % (self.professorNumberEntry.get()))
                    cursor.execute("DELETE professorCourse WHERE professor='%s'" % (self.professorNumberEntry.get()))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Success", "Professor is deleted succesfully.")
                else:
                    messagebox.showerror("Unsuccess", "The professor does not exist in database.")
            else:
                messagebox.showerror("Unsuccess", "Invalid entering.")

        self.btnUpdate = Button(self.professorFrame, text="Delete Professor", foreground="#ff1a1a",
                                command=deleteProfessor)
        self.btnUpdate.grid(column=2, row=7, padx=8, pady=8, sticky=W)
        # User Information
        self.userFrame = LabelFrame(self.window, text="User", font=("Arial Bold", 18), foreground="black")
        self.lblUserName = Label(self.userFrame, text="User Name", font=("Arial Bold", 15), foreground="red")
        self.lblUserName.grid(column=0, row=8, padx=8, pady=8, sticky=W)
        self.userNameEntry = Entry(self.userFrame, width=20)
        self.userNameEntry.grid(column=1, row=8, padx=8, pady=8, sticky=W)
        self.lblUserPassword = Label(self.userFrame, text="User Password", font=("Arial Bold", 15), foreground="red")
        self.lblUserPassword.grid(column=0, row=9, padx=8, pady=8, sticky=W)
        self.passwordEntry = Entry(self.userFrame, width=20)
        self.passwordEntry.grid(column=1, row=9, padx=8, pady=8, sticky=W)
        self.lblIDName = Label(self.userFrame, text="User ID", font=("Arial Bold", 15), foreground="red")
        self.lblIDName.grid(column=0, row=10, padx=8, pady=8, sticky=W)
        self.userIDEntry = Entry(self.userFrame, width=20)
        self.userIDEntry.grid(column=1, row=10, padx=8, pady=8, sticky=W)
        self.lblUserType = Label(self.userFrame, text="User Type", font=("Arial Bold", 15),
                                 foreground="red")
        self.lblUserType.grid(column=0, row=11, padx=8, pady=8, sticky=W)
        self.userTypeEntry = Entry(self.userFrame, width=20)
        self.userTypeEntry.grid(column=1, row=11, padx=8, pady=8, sticky=W)
        self.userFrame.grid(column=1, row=2)

        def submitUser():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                               WHERE TABLE_NAME = N'users';""")
            if len(result.fetchall()) == 1:

                if self.userIDEntry.get() != "" and self.passwordEntry.get() != "" and self.userNameEntry.get() != "" \
                        and self.userTypeEntry.get() != "":
                    cursor = connection.cursor()
                    strsql = "select * from users where userID=? "
                    cursor.execute(strsql, (self.userIDEntry.get(),))
                    result = cursor.fetchall()
                    if len(result) == 0:
                        try:
                            sql_command = """CREATE TABLE users (userID INTEGER PRIMARY KEY, userName VARCHAR(20),
                                    useRPassword VARCHAR(20), userType INTEGER );"""
                            cursor.execute(sql_command)
                            cursor.commit()
                            connection.commit()
                            cursor.execute("INSERT INTO users VALUES (?, ?, ?,?)", (
                                self.userIDEntry.get(), self.userNameEntry.get(), self.passwordEntry.get(),
                                self.userTypeEntry.get()))
                            connection.commit()
                            messagebox.showinfo("Success", "User is saved succussfully.")
                        except:
                            cursor.execute("INSERT INTO users VALUES (?, ?, ?,?)", (
                                self.userIDEntry.get(), self.userNameEntry.get(), self.passwordEntry.get(),
                                self.userTypeEntry.get()))
                            connection.commit()
                            messagebox.showinfo("Success", "User is saved succussfully.")

                        if (self.userTypeEntry.get() == '1'):  # admin
                            try:
                                sql_command = """CREATE TABLE admin (  
                                        adminID INTEGER PRIMARY KEY,  
                                        adminName VARCHAR(20));"""
                                cursor.execute(sql_command)
                                cursor.commit()
                                connection.commit()
                                cursor.execute("INSERT INTO admin VALUES (?,?)",
                                               (self.userIDEntry.get(), self.userNameEntry.get()))
                                cursor.commit()
                            except:
                                cursor = connection.cursor()
                                cursor.execute("INSERT INTO admin VALUES (?,?)",
                                               (self.userIDEntry.get(), self.userNameEntry.get()))
                                connection.commit()
                        elif (self.userTypeEntry.get() == '2'):  # professor
                            try:
                                sql_command = """CREATE TABLE professor (  
                                        professorID INTEGER PRIMARY KEY,  
                                        prosessorName VARCHAR(20));"""
                                cursor.execute(sql_command)
                                cursor.commit()
                                connection.commit()
                                cursor.execute("INSERT INTO professor VALUES (?,?)",
                                               (self.userIDEntry.get(), self.userNameEntry.get()))
                                cursor.commit()
                            except:
                                cursor = connection.cursor()
                                cursor.execute("INSERT INTO professor VALUES (?,?)",
                                               (self.userIDEntry.get(), self.userNameEntry.get()))
                                connection.commit()

                        else:  # student
                            try:
                                sql_command = """CREATE TABLE student (  
                                                                       studentID INTEGER PRIMARY KEY,  
                                                                       studentName VARCHAR(20));"""
                                cursor.execute(sql_command)
                                cursor.commit()
                                connection.commit()
                                cursor.execute("INSERT INTO student VALUES (?,?)",
                                               (self.userIDEntry.get(), self.userNameEntry.get()))
                                connection.commit()
                            except:
                                cursor.execute("INSERT INTO student VALUES (?,?)",
                                               (self.userIDEntry.get(), self.userNameEntry.get()))
                                connection.commit()

                    else:
                        messagebox.showerror("Warning", "The user already exists in database.")

                else:
                    messagebox.showerror("Error", "Please enter fieds.")

        self.btnSubmit = Button(self.userFrame, text="Submit User", command=submitUser, foreground="#ff1a1a")
        self.btnSubmit.grid(column=2, row=8, padx=8, pady=8, sticky=W)

        def updateUser():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                                       WHERE TABLE_NAME = N'users';""")
            if len(result.fetchall()) == 1:
                cursor = connection.cursor()
                strsql = "select * from users where userID=? "
                cursor.execute(strsql, (self.userIDEntry.get(),))
                result = cursor.fetchall()
                if result != 0:
                    if self.userNameEntry.get() != "":
                        cursor.execute("UPDATE users SET userName='%s' WHERE userID='%s'" % (
                            self.userNameEntry.get(), self.userIDEntry.get()))
                        connection.commit()
                        if self.userTypeEntry.get() == "1":  # admin
                            cursor.execute("UPDATE admin SET adminName='%s' WHERE adminID='%s'" % (
                                self.userNameEntry.get(), self.userIDEntry.get()))
                            connection.commit()
                        elif self.userTypeEntry.get() == "2":  # prof
                            cursor.execute("UPDATE professor SET professorName='%s' WHERE professorID='%s'" % (
                                self.userNameEntry.get(), self.userIDEntry.get()))
                            connection.commit()
                            messagebox.showinfo("Success", "User name is changed successfully.")
                        elif self.userTypeEntry.get() == "3":
                            cursor.execute("UPDATE student SET studentName='%s' WHERE studentID='%s'" % (
                                self.userNameEntry.get(), self.userIDEntry.get()))
                            connection.commit()
                            messagebox.showinfo("Success", "User name is changed successfully.")

                        else:
                            messagebox.showwarning("Warning", "Please enter user type.")

                    if self.passwordEntry.get() != "":
                        cursor.execute("UPDATE users SET userPassword='%s' WHERE userID='%s'" % (
                            self.passwordEntry.get(), self.userIDEntry.get()))
                        connection.commit()
                        messagebox.showinfo("Success", "User password is changed successfully.")
                    if self.userTypeEntry.get():
                        pass
                    connection.close()
                else:
                    messagebox.showwarning("Warning", "This user does not exist in database.")
            else:
                messagebox.showwarning("Warning", "Please first enter user's information.")

        def deleteUser():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                 WHERE TABLE_NAME = N'users';""")
            if len(result.fetchall()) == 1:
                cursor = connection.cursor()
                strsql = "select * from users where userID=? "
                cursor.execute(strsql, (self.userIDEntry.get(),))
                result = cursor.fetchall()
                print("1")
                print(result)
                if len(result) != 0 and self.userTypeEntry.get() != "":
                    cursor.execute("DELETE users WHERE userID='%s'" % (self.userIDEntry.get()))
                    if self.userTypeEntry.get() == "1":
                        cursor.execute("DELETE admin WHERE adminID='%s'" % (self.userIDEntry.get()))
                        messagebox.showinfo("Success", "Admin is deleted succesfully.")
                    elif self.userTypeEntry.get() == "2":
                        cursor.execute("DELETE professor WHERE professorID='%s'" % (self.userIDEntry.get()))
                        cursor.execute("DELETE professorCourse WHERE professor='%s'" % (self.userIDEntry.get()))
                        messagebox.showinfo("Success", "Professor is deleted succesfully.")
                    elif self.userTypeEntry.get() == "3":
                        cursor.execute("DELETE student WHERE studentID='%s'" % (self.userIDEntry.get()))
                        cursor.execute("DELETE courseStudent WHERE studentID='%s'" % (self.userIDEntry.get()))
                        messagebox.showinfo("Success", "Student is deleted succesfully.")
                    else:
                        messagebox.showwarning("The user does not exist.")
                    connection.commit()
                    connection.close()

                else:
                    messagebox.showerror("Unsuccess", "Please enter user type.")
            else:
                messagebox.showerror("Error", "The information does not exist.")

        self.btnUpdate = Button(self.userFrame, text="Update User", foreground="#ff1a1a", command=updateUser)
        self.btnUpdate.grid(column=2, row=9, padx=8, pady=8, sticky=W)
        self.btnDelete = Button(self.userFrame, text="Delete User", foreground="#ff1a1a", command=deleteUser)
        self.btnDelete.grid(column=2, row=10, padx=8, pady=8, sticky=W)
        # Grade
        self.gradeFrame = LabelFrame(self.window, text="Grade", font=("Arial Bold", 18), foreground="black")
        self.lblGrade = Label(self.gradeFrame, text="Grade", font=("Arial Bold", 15), foreground="red")
        self.lblGrade.grid(column=0, row=11, padx=8, pady=8, sticky=W)
        self.gradeEntry = Entry(self.gradeFrame, width=20)
        self.gradeEntry.grid(column=1, row=11, padx=8, pady=8, sticky=W)
        self.lblStudentGrade = Label(self.gradeFrame, text="Student ID", font=("Arial Bold", 15), foreground="red")
        self.lblStudentGrade.grid(column=0, row=13, padx=8, pady=8, sticky=W)
        self.studentGradeEntry = Entry(self.gradeFrame, width=20)
        self.studentGradeEntry.grid(column=1, row=13, padx=8, pady=8, sticky=W)
        self.lblCourseGrade = Label(self.gradeFrame, text="Course ID", font=("Arial Bold", 15), foreground="red")
        self.lblCourseGrade.grid(column=0, row=12, padx=8, pady=8, sticky=W)
        self.courseGradeEntry = Entry(self.gradeFrame, width=20)
        self.courseGradeEntry.grid(column=1, row=12, padx=8, pady=8, sticky=W)
        self.gradeFrame.grid(column=0, row=4)

        def submitGrade():
            if int(self.gradeEntry.get()) >= 0 and int(self.gradeEntry.get()) <= 100:
                if self.studentGradeEntry.get() != "" and self.courseGradeEntry.get() != "":
                    connection = pypyodbc.connect \
                        ('DRIVER={SQL Server};'
                         'SERVER=LENOVO\SQLEXPRESS;'
                         'DATABASE=schoolDb;'
                         'Trusted_Connection=yes;')
                    cursor = connection.cursor()
                    result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                                       WHERE TABLE_NAME = N'student';""")
                    result1 = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                                        WHERE TABLE_NAME = N'course';""")
                    if len(result.fetchall()) == 1 and len(result1.fetchall()) == 1:
                        cursor = connection.cursor()
                        strsql = "select * from student where studentID=? "
                        cursor.execute(strsql, (self.studentGradeEntry.get(),))
                        result = cursor.fetchall()
                        strsql = "select * from course where courseID=? "
                        cursor.execute(strsql, (self.courseGradeEntry.get(),))
                        result2 = cursor.fetchall()
                        if len(result) != 0 and len(result2) != 0:
                            cursor.execute("INSERT INTO courseStudent VALUES (?,?,?)", (
                                self.gradeEntry.get(), self.studentGradeEntry.get(), self.courseGradeEntry.get()))
                            connection.commit()
                            messagebox.showinfo("Success", "The grade is saved successfully.")
                        elif len(result) == 0:
                            messagebox.showerror("Error", "The student does not exists in database.")
                        else:
                            messagebox.showerror("Error", "The course does not exists in database.")
                else:
                    messagebox.showwarning("Warning", "Grade should be between 0 and 100.")

        self.btnSubmit = Button(self.gradeFrame, text="Submit Grade", command=submitGrade, foreground="#ff1a1a")
        self.btnSubmit.grid(column=2, row=12, padx=8, pady=8, sticky=W)

        def updateGrade():
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
                strsql = "select * from courseStudent where studentID=? and courseID=?"
                cursor.execute(strsql, (self.studentGradeEntry.get(), self.courseGradeEntry.get(),))
                result = cursor.fetchall()
                if result != 0:
                    if self.gradeEntry.get() != "":
                        if int(self.gradeEntry.get()) >= 0 and int(self.gradeEntry.get()) <= 100:
                            cursor.execute("UPDATE courseStudent SET grade='%s' WHERE courseID='%s' and studentID='%s'" % (
                                self.gradeEntry.get(), self.courseGradeEntry.get(), self.studentGradeEntry.get()))
                            connection.commit()
                        else:
                            messagebox.showwarning("Warning", "Grade must be between 0 and 100.")
                    else:
                        messagebox.showwarning("Warning", "Please enter grade.")
                    connection.close()
                else:
                    messagebox.showerror("Error", "Please enter correct ID for student or course")

        self.btnUpdate = Button(self.gradeFrame, text="Update Grade", command=updateGrade, foreground="#ff1a1a")
        self.btnUpdate.grid(column=2, row=11, padx=8, pady=8, sticky=W)

        def deleteGrade():
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
                strsql = "select * from courseStudent WHERE studentID=? and courseID=? "
                cursor.execute(strsql, (self.studentGradeEntry.get(), self.courseGradeEntry.get(),))
                result = cursor.fetchall()
                if len(result) != 0:
                    cursor.execute("DELETE courseStudent WHERE  studentID='%s' and courseID='%s'" % (
                        self.studentGradeEntry.get(), self.courseGradeEntry.get()))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Success", "Grade is deleted succesfully.")
                else:
                    messagebox.showerror("Unsuccess", "The course or the student do not exist in database.")

        self.btnDelete = Button(self.gradeFrame, text="Delete Grade", command=deleteGrade, foreground="#ff1a1a")
        self.btnDelete.grid(column=2, row=13, padx=8, pady=8, sticky=W)

        # Admin
        self.adminFrame = LabelFrame(self.window, text="Admin", font=("Arial Bold", 18), foreground="black")
        self.lblAdminName = Label(self.adminFrame, text="Admin Name", font=("Arial Bold", 15), foreground="red")
        self.lblAdminName.grid(column=0, row=13, padx=8, pady=8, sticky=W)
        self.adminNameEntry = Entry(self.adminFrame, width=20)
        self.adminNameEntry.grid(column=1, row=13, padx=8, pady=8, sticky=W)
        self.lblAdminNumber = Label(self.adminFrame, text="Admin Number", font=("Arial Bold", 15),
                                    foreground="red")
        self.lblAdminNumber.grid(column=0, row=14, padx=8, pady=8, sticky=W)
        self.adminNumberEntry = Entry(self.adminFrame, width=20)
        self.adminNumberEntry.grid(column=1, row=14, padx=8, pady=8, sticky=W)
        self.adminFrame.grid(column=0, row=3)

        def updateAdmin():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                                   WHERE TABLE_NAME = N'admin';""")
            if len(result.fetchall()) == 1:
                cursor = connection.cursor()
                strsql = "select * from admin where adminID=? "
                cursor.execute(strsql, (self.adminNumberEntry.get(),))
                result = cursor.fetchall()
                if len(result) != 0:
                    if self.adminNameEntry.get() != "":
                        cursor.execute("UPDATE admin SET adminName='%s' WHERE adminID='%s'" % (
                            self.adminNameEntry.get(), self.adminNumberEntry.get()))
                        cursor.execute("UPDATE users SET userName='%s' WHERE userID='%s'" % (
                            self.adminNameEntry.get(), self.adminNumberEntry.get()))
                        messagebox.showinfo("Success", "Admin is updated.")
                        connection.commit()

                    connection.close()
                else:
                    messagebox.showerror("Error", "Admin does not exist in database.")
            else:
                messagebox.showerror("Error", "Please first enter admin's information.")

        self.btnUpdate = Button(self.adminFrame, text="Update Admin", foreground="#ff1a1a", command=updateAdmin)
        self.btnUpdate.grid(column=2, row=14, padx=8, pady=8, sticky=W)

        def deleteAdmin():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                                                           WHERE TABLE_NAME = N'admin';""")
            if len(result.fetchall()) == 1:
                cursor = connection.cursor()
                strsql = "select * from admin where adminID=? "
                cursor.execute(strsql, (self.adminNumberEntry.get(),))
                result = cursor.fetchall()
                if len(result) != 0:
                    cursor.execute("DELETE admin WHERE adminID='%s'" % (self.adminNumberEntry.get()))
                    cursor.execute("DELETE users WHERE userID='%s'" % (self.adminNumberEntry.get()))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Success", "Admin is deleted succesfully.")
                else:
                    messagebox.showerror("Unsuccess", "The admin does not exist in database.")

        self.btnUpdate = Button(self.adminFrame, text="Delete Admin", foreground="#ff1a1a", command=deleteAdmin)
        self.btnUpdate.grid(column=2, row=13, padx=8, pady=8, sticky=W)

        self.btnExit = Button(self.window, text="Exit", command=self.window.destroy, foreground="#ff1a1a")
        self.btnExit.grid(column=2, row=4, padx=8, pady=8, sticky=W)

        def cleanEntry():
            self.userNameEntry.delete(0, 'end')
            self.passwordEntry.delete(0, 'end')
            self.userTypeEntry.delete(0, 'end')
            self.userIDEntry.delete(0, 'end')
            self.studentNameEntry.delete(0, 'end')
            self.studentNumberEntry.delete(0, 'end')
            self.professorNumberEntry.delete(0, 'end')
            self.professorNameEntry.delete(0, 'end')
            self.courseNameEntry.delete(0, 'end')
            self.CourseNumberEntry.delete(0, 'end')
            self.profCourseEntry.delete(0, 'end')

        self.btnExit = Button(self.window, text="Clean Entry", command=cleanEntry, foreground="#ff1a1a")
        self.btnExit.grid(column=1, row=4, padx=8, pady=8, sticky=W)

        # enroll course
        self.enrollFrame = LabelFrame(self.window, text="Enrol", font=("Arial Bold", 18), foreground="black")
        self.lblenrollCourse = Label(self.enrollFrame, text="Course Name", font=("Arial Bold", 15), foreground="red")
        self.lblenrollCourse.grid(column=0, row=1, padx=8, pady=8, sticky=W)
        self.enrollCourseEntry = Entry(self.enrollFrame, width=20)
        self.enrollCourseEntry.grid(column=1, row=1, padx=8, pady=8, sticky=W)
        self.lblenrollStudent = Label(self.enrollFrame, text="Student Number", font=("Arial Bold", 15),
                                      foreground="red")
        self.lblenrollStudent.grid(column=0, row=2, padx=8, pady=8, sticky=W)
        self.enrollStudentEntry = Entry(self.enrollFrame, width=20)
        self.enrollStudentEntry.grid(column=1, row=2, padx=8, pady=8, sticky=W)
        self.enrollFrame.grid(column=1, row=3)

        def submitCourseForStudent():
            connection = pypyodbc.connect \
                ('DRIVER={SQL Server};'
                 'SERVER=LENOVO\SQLEXPRESS;'
                 'DATABASE=schoolDb;'
                 'Trusted_Connection=yes;')
            cursor = connection.cursor()
            result = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                        WHERE TABLE_NAME = N'course';""")
            result1 = cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES 
                                                                    WHERE TABLE_NAME = N'student';""")
            if len(result.fetchall()) == 1 and len(result1.fetchall()) == 1:
                if self.enrollCourseEntry.get() != "" and self.enrollStudentEntry.get() != "":
                    cursor = connection.cursor()
                    strsql = "select * from course where courseID=?"
                    cursor.execute(strsql, (self.enrollCourseEntry.get(),))
                    result = cursor.fetchall()
                    strsql1 = "select * from student where studentID=?"
                    cursor.execute(strsql1, (self.enrollStudentEntry.get(),))
                    result1 = cursor.fetchall()
                    if len(result) != 0 and len(result1) != 0:
                        cursor.execute("INSERT INTO courseStudent VALUES (?, ?,?)",
                                       (self.enrollCourseEntry.get(), self.enrollStudentEntry.get(), 0))
                        connection.commit()
                        messagebox.showinfo("Success", "Student is enrolled course succussfully.")
                    else:
                        messagebox.showwarning("Warning", "Please enter student number or course number.")
                else:
                    messagebox.showerror("Error", "Please enter all information for enrolling course.")

        self.btnSubmit = Button(self.enrollFrame, text="Enrol Course", foreground="#ff1a1a",
                                command=submitCourseForStudent)
        self.btnSubmit.grid(column=2, row=1, padx=8, pady=8, sticky=W)
