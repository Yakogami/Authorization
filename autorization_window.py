import tkinter
import tkinter as tk
import tkinter.font as tkFont
import tkinter as ttk
from tkinter import messagebox
from database import Database
import datetime
from registration_window import Reg_App
import time


# import getpass
# pswd = getpass.getpass('Password:')

class App:
    def __init__(self, root):
        self.root = root
        self.database = Database("database.db")

        # setting title
        root.title("Authorization")
        # setting window size
        width = 600
        height = 230
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        GButton_login = tk.Button(root)
        GButton_login["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_login["font"] = ft
        GButton_login["fg"] = "#000000"
        GButton_login["justify"] = "center"
        GButton_login["text"] = "Login"
        GButton_login.place(x=200, y=110, width=100, height=30)
        GButton_login["command"] = self.login

        GButton_register = tk.Button(root)
        GButton_register["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_register["font"] = ft
        GButton_register["fg"] = "#000000"
        GButton_register["justify"] = "center"
        GButton_register["text"] = "Register"
        GButton_register.place(x=300, y=110, width=100, height=30)
        GButton_register["command"] = self.GButton_reg_command

        GMessage_1 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_1["font"] = ft
        GMessage_1["fg"] = "#333333"
        GMessage_1["justify"] = "center"
        GMessage_1["text"] = "Login"
        GMessage_1.place(x=100, y=40, width=100, height=30)

        GMessage_2 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_2["font"] = ft
        GMessage_2["fg"] = "#333333"
        GMessage_2["justify"] = "center"
        GMessage_2["text"] = "Password"
        GMessage_2.place(x=100, y=70, width=110, height=30)

        GLineEdit_login = tk.Entry(root)
        GLineEdit_login["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_login["font"] = ft
        GLineEdit_login["fg"] = "#333333"
        GLineEdit_login["justify"] = "center"
        GLineEdit_login["text"] = ""
        GLineEdit_login.place(x=200, y=40, width=200, height=30)
        self.GLineEdit_login = GLineEdit_login

        GLineEdit_password = tk.Entry(root, show="*")
        GLineEdit_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_password["font"] = ft
        GLineEdit_password["fg"] = "#333333"
        GLineEdit_password["justify"] = "center"
        GLineEdit_password["text"] = ""
        GLineEdit_password.place(x=200, y=70, width=200, height=30)
        self.GLineEdit_password = GLineEdit_password

    # Хуй знает что делать после этого логина... Нужно придумать какую-то дальнейшую реализацию
    def login(self):
        login = self.GLineEdit_login.get()
        password = self.GLineEdit_password.get()
        # huy = [login, password]
        pizda = self.database.all_users()
        print(pizda)


    def GButton_reg_command(self):
        new_root = tkinter.Toplevel(root)
        registration_window = Reg_App(new_root)  # Создаем экземпляр класса MyWindow
        new_root.title("Registration")
        new_root.transient(root)
        new_root.grab_set()
        new_root.focus_set()
        new_root.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("Exit", "Cancel authorization?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
