import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox


class Reg_App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 230
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_RegLogin = tk.Entry(root)
        GLineEdit_RegLogin["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_RegLogin["font"] = ft
        GLineEdit_RegLogin["fg"] = "#333333"
        GLineEdit_RegLogin["justify"] = "center"
        GLineEdit_RegLogin["text"] = "Entry"
        GLineEdit_RegLogin.place(x=230, y=60, width=100, height=25)
        self.GLineEdit_RegLogin = GLineEdit_RegLogin

        GLineEdit_RegPassword = tk.Entry(root)
        GLineEdit_RegPassword["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_RegPassword["font"] = ft
        GLineEdit_RegPassword["fg"] = "#333333"
        GLineEdit_RegPassword["justify"] = "center"
        GLineEdit_RegPassword["text"] = "Entry"
        GLineEdit_RegPassword.place(x=230, y=110, width=100, height=25)
        self.GLineEdit_RegPassword = GLineEdit_RegPassword

        GLineEdit_RegPassword1 = tk.Entry(root)
        GLineEdit_RegPassword1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_RegPassword1["font"] = ft
        GLineEdit_RegPassword1["fg"] = "#333333"
        GLineEdit_RegPassword1["justify"] = "center"
        GLineEdit_RegPassword1["text"] = "Entry"
        GLineEdit_RegPassword1.place(x=230, y=150, width=100, height=25)
        self.GLineEdit_RegPassword2 = GLineEdit_RegPassword1

        GMessage_Login = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_Login["font"] = ft
        GMessage_Login["fg"] = "#333333"
        GMessage_Login["justify"] = "center"
        GMessage_Login["text"] = "Login"
        GMessage_Login.place(x=110, y=60, width=110, height=25)

        GMessage_Password = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_Password["font"] = ft
        GMessage_Password["fg"] = "#333333"
        GMessage_Password["justify"] = "center"
        GMessage_Password["text"] = "Password"
        GMessage_Password.place(x=110, y=110, width=110, height=25)

        GMessage_Password1 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_Password1["font"] = ft
        GMessage_Password1["fg"] = "#333333"
        GMessage_Password1["justify"] = "center"
        GMessage_Password1["text"] = "Password"
        GMessage_Password1.place(x=110, y=150, width=110, height=25)

        GMessage_AccReg = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_AccReg["font"] = ft
        GMessage_AccReg["fg"] = "#333333"
        GMessage_AccReg["justify"] = "center"
        GMessage_AccReg["text"] = "Account registration"
        GMessage_AccReg.place(x=210, y=10, width=150, height=25)

        GButton_Register = tk.Button(root)
        GButton_Register["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_Register["font"] = ft
        GButton_Register["fg"] = "#000000"
        GButton_Register["justify"] = "center"
        GButton_Register["text"] = "Reg"
        GButton_Register.place(x=180, y=190, width=100, height=25)
        GButton_Register["command"] = self.GButton_Register

        GButton_Cancel = tk.Button(root)
        GButton_Cancel["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_Cancel["font"] = ft
        GButton_Cancel["fg"] = "#000000"
        GButton_Cancel["justify"] = "center"
        GButton_Cancel["text"] = "Cancel"
        GButton_Cancel.place(x=290, y=190, width=100, height=25)
        GButton_Cancel["command"] = self.GButton_CancelRegister

    def GButton_Register(self):
        login = self.GLineEdit_RegLogin.get()
        password = self.GLineEdit_RegPassword.get()
        password1 = self.GLineEdit_RegPassword1.get()
        if password != password1:
            messagebox.showerror("Password != Password1")

    def GButton_CancelRegister(self):
        messagebox.showerror("Password != Password1")


if __name__ == "__main__":
    root = tk.Tk()
    app = Reg_App(root)
    root.mainloop()