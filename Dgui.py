WindowsConfig = {
    "windowTitle": "Driving School",
    "windowSize": (800, 600),
    "windowIcon": "Dgui.ico",
    "windowBackground": "white"
}
import pymysql
import tkinter as tk

class Dgui:
    def __init__(self):
        self.config =config={
                    "host":'localhost', # default host is localhost
                    "user":'root',      # default user is root
                    "password":'123456', 
                    "database":'DrivingSchool',      # if not exist, create a new database
                    "charset":'utf8mb4' # default charset is utf8mb4
                    }
        self.db=None
        self.windowTitle = WindowsConfig['windowTitle']
        self.windowSize = WindowsConfig['windowSize']
        self.windowIcon = WindowsConfig['windowIcon']
        self.windowBackground = WindowsConfig['windowBackground']
        self.root = tk.Tk()
        self.root.geometry(f"{self.windowSize[0]}x{self.windowSize[1]}")
        self.root.resizable(0,0)
        self.root.title(self.windowTitle)
        self.root.configure(bg=self.windowBackground)

        self.getDatebasePage()
        self.connectDatabaseFailLabel = tk.Label(self.root, text="Error connecting to database", fg="red", font=("Arial", 12), bg=self.windowBackground,heigh=2,width=38)
        self.createDatabaseFailLabel = tk.Label(self.root, text="Error creating database", fg="red", font=("Arial", 12), bg=self.windowBackground,heigh=2,width=38)

        self.root.protocol("WM_DELETE_WINDOW", self.rootClosing)
        self.root.mainloop()

    def rootClosing(self):
        self.db.close()
        self.root.destroy()
        print("Closing Dgui")

    def connectDatabase(self,host,user,password,database,charset):
    # connect to database
        try:
            db = pymysql.connect(host=host, 
                                user=user, 
                                password=password, )
        except:
            self.connectDatabaseFailLabel.place(x=200,y=550)
            print("Error connecting to database")
            return 
        self.config['host'] = host
        self.config['user'] = user
        self.config['password'] = password
        self.config['database'] = database
        self.config['charset'] = charset
        self.db=db
        # create a new database if not exist
        try:
            with self.db.cursor() as cursor:
                sql = "CREATE DATABASE IF NOT EXISTS "+self.config['database']
                cursor.execute(sql)
        except:
            self.createDatabaseFailLabel.place(x=200,y=550)
            print("Error creating database")
            return
        # use the database
        self.db.select_db(self.config['database'])
        # create a table if not exist
        with self.db.cursor() as cursor:
            sql = "CREATE TABLE IF NOT EXISTS Student (studentID INT PRIMARY KEY, name VARCHAR(50), gender VARCHAR(10), age INT, lessons json, unpaid INT)"
            cursor.execute(sql)
            sql = "CREATE TABLE IF NOT EXISTS Instructor (instructorID INT PRIMARY KEY, name VARCHAR(50), gender VARCHAR(10), age INT, lessons json, income INT)"
            cursor.execute(sql)
            sql = "CREATE TABLE IF NOT EXISTS Vehicle (vehicleID INT PRIMARY KEY, type VARCHAR(20), needMaintenance VARCHAR(10))"
            cursor.execute(sql)
            sql = "CREATE TABLE IF NOT EXISTS Lesson (lessonID INT PRIMARY KEY, type VARCHAR(20), studentID INT, instructorID INT, date DATE, time TIME, completed VARCHAR(20), canBeBooked VARCHAR(10), pay INT)"
            cursor.execute(sql)
            sql = "CREATE TABLE IF NOT EXISTS Payment (paymentID INT PRIMARY KEY, studentID INT, amount INT, lessonID INT, status VARCHAR(20))"
            cursor.execute(sql)
        self.db.commit()
        self.clear_widgets()
        self.page2()
    
    def getDatebasePage(self):
        hostLabel=tk.Label(self.root,text="host",font=("Arial"),width=10,height=2,bg=self.windowBackground)
        hostLabel.place(x=200,y=200)

        hostEntry=tk.Entry(self.root,width=20)
        hostEntry.insert(0,"localhost")
        hostEntry.place(x=400,y=210)
        #############
        userLabel=tk.Label(self.root,text="user",font=("Arial"),width=10,height=2,bg=self.windowBackground)
        userLabel.place(x=200,y=250)

        userEntry=tk.Entry(self.root,width=20)
        userEntry.insert(0,"root")
        userEntry.place(x=400,y=260)
        #############
        passwordLabel=tk.Label(self.root,text="password",font=("Arial"),width=10,height=2,bg=self.windowBackground)
        passwordLabel.place(x=200,y=300)

        passwordEntry=tk.Entry(self.root,width=20,show="*")
        passwordEntry.insert(0,"")
        passwordEntry.place(x=400,y=310)
        #############
        databaseLabel=tk.Label(self.root,text="database",font=("Arial"),width=10,height=2,bg=self.windowBackground)
        databaseLabel.place(x=200,y=350)

        databaseEntry=tk.Entry(self.root,width=20)
        databaseEntry.insert(0,"")
        databaseEntry.place(x=400,y=360)
        #############
        charsetLabel=tk.Label(self.root,text="charset",font=("Arial"),width=10,height=2,bg=self.windowBackground)
        charsetLabel.place(x=200,y=400)

        charsetEntry=tk.Entry(self.root,width=20)
        charsetEntry.insert(0,"utf8mb4")
        charsetEntry.place(x=400,y=410)

        #############
        PageTitle=tk.Label(self.root,text="MYSQL Database Configuration",font=("Arial"),width=40,height=2,bg=self.windowBackground)
        PageTitle.place(x=200,y=100)

        #########       
        Pagemore=tk.Label(self.root,text="if database not exist, create a new database",font=("Arial"),width=40,height=2,bg=self.windowBackground)
        Pagemore.place(x=200,y=450)

        #########
        ButtonConnectDatabase=tk.Button(self.root,text="Connect Database",font=("Arial"),
                                        width=20,height=2,bg="white",
                                        command=lambda:self.connectDatabase(hostEntry.get(),userEntry.get(),passwordEntry.get(),databaseEntry.get(),charsetEntry.get()))
        ButtonConnectDatabase.place(x=280,y=480)

    def page2(self):
        pass

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.connectDatabaseFailLabel = tk.Label(self.root, text="Error connecting to database", fg="red", font=("Arial", 12), bg=self.windowBackground,heigh=2,width=38)
        self.createDatabaseFailLabel = tk.Label(self.root, text="Error creating database", fg="red", font=("Arial", 12), bg=self.windowBackground,heigh=2,width=38)


Gui=Dgui()
