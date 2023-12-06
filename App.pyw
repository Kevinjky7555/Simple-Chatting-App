import socket, time
import string, secrets
from tkinter import *
from tkinter import messagebox
from threading import Thread

class MainWindow():
    def __init__(self) -> None:
        self.server = socket.socket();
        self.root = Tk();
        self.root.title("Simple Chatting - V1.1");
        self.root.resizable(0,0);

        self.var = {
            "v0": False,
            "v1": False,
            "v2": False,
            "v3": "127.0.0.1",
            "v4": "127.0.0.1",
            "v5": 5001,
            "v6": 5002,
            "v7": "#121212",
            "v8": "#ABB2B9",
            "v9": "#EAECEE",
            "v10": 60,
            "v11": "#2C3E50",
            "v12": 70,
            "v13": "Send", 
            "v14": 6, 
            "v15": 1, 
            "v16": "Join to chat!",
            "v17": "About",
            "v18": "Guest",
            "v19": 0,
            "v20": "Version 1.1 - Simple Chat Application\nJoin rooms with IDs and start chatting!",
        };


    def win(self):
        if (self.var['v0']):            
            self.txt = Text(self.root, bg = self.var['v7'], fg = self.var['v9'], width = self.var['v10']);
            self.txt.grid(row = 1, column = 0, columnspan = 2);

            self.a2 = Entry(self.root, bg = self.var['v11'], fg = self.var['v9'], width = self.var['v12']);
            self.a2.grid(row = 2, column = 0);

            self.a3 = Button(
                self.root,
                text = self.var['v13'],
                bg = self.var['v8'],
                command = self.sendMessage,
                width = self.var['v14'],
                height = self.var['v15']
            );
            self.a3.grid(row = 2, column = 1);
        else:
            self.a1 = Label(
                self.root,
                text = "Username:",
                fg = "WHITE",
                bg = self.var['v7'],
                width = 10
            );
            self.a1.grid(
                row = 0,
                column = 0
            );
            self.a2 = Entry(
                self.root,
                bg = self.var['v7'],
                fg = self.var['v9'],
                width = 50
            );
            self.a2.grid(
                row = 0,
                column = 1
            );
            self.a3 = Label(
                self.root,
                text = "Channel:",
                fg = "WHITE",
                bg = self.var['v7'],
                width = 10
            );
            self.a3.grid(
                row = 1,
                column = 0 
               );
            self.a4 = Entry(
                self.root,
                bg = self.var['v7'],
                fg = self.var['v9'],
                width = 50
            );
            self.a4.grid(
                row = 1,
                column = 1
            );
            self.a5 = Button(
                self.root,
                bg = self.var['v7'],
                fg = self.var['v9'],
                text = self.var['v16'],
                width = 42,
                height = 1,
                command = self.joinChannel
            );
            self.a5.grid(
                row = 2,
                column = 1
            );
            self.a6 = Button(
                self.root,
                bg = self.var['v7'],
                fg = self.var['v9'],
                text=self.var['v17'],
                width = 9,
                height = 1,
                command = self.aboutApp
            );
            self.a6.grid(
                row = 2,
                column = 0
            );

        if (not self.var['v2']):
            b1 = 0
            if (self.var['v1']):
                b1 = 1
            if (b1 == 0):
                if (self.checkAddress(b1)):
                    self.connectTo(b1);
            elif (b1 == 1):
                if (self.checkAddress(b1)):
                    self.connectTo(b1);

        t = Thread(target = self.listenServer)
        t.daemon = True
        t.start()

        self.root.mainloop();
    
    def msgBox(self, title, text):
        messagebox.showinfo(
        title,
        text
        );

    def errorBox(self, title, text):
        messagebox.showerror(
        title,
        text
        );
        
    def sendMessage(self):
        user_text = self.a2.get();
        text = f"{self.var['v18']} - {user_text}~{self.var['v19']}"

        if user_text != "":
            self.server.send(text.encode())
            self.a2.delete(0, END)

    def joinChannel(self):
        numbers = string.digits
        fname = "".join(secrets.choice(numbers) for i in range(4))
        
        i1 = self.a2.get().lower();
        i2 = self.a4.get().lower();

        if i1 == "":
            self.var['v18'] = f"Guest{fname}"
        else:
            self.var['v18'] = i1
        
        self.var['v19'] = i2
        data = f"/login~{self.var['v18']}~{i2}"
        self.server.send(data.encode())
        self.var['v0'] = True
        self.destroyElements()
        self.root.title(f"Simple Chatting - V1.1, username: {self.var['v18']}");
        self.msgBox("Welcome", "Have fun chatting!")
        self.win()

    def destroyElements(self):
        self.a1.destroy()
        self.a2.destroy()
        self.a3.destroy()
        self.a4.destroy()
        self.a5.destroy()
        self.a6.destroy()

    def aboutApp(self):
        messagebox.showinfo(
        "About Application",
        self.var['v20']
        );

    def connectTo(self, type=None):
        if (type == 0):
            try:
                self.server.connect((self.var['v3'], self.var['v5']));
            except Exception as error:
                messagebox.showerror("Connection error!", f"Error: {error}");
            else:
                self.var['v2'] = True
        elif(type == 1):
            try:
                self.server.connect((self.var['v4'], self.var['v6']));
            except Exception as error:
                messagebox.showerror("Connection error!", f"Error: {error}");
            else:
                self.var['v2'] = True
        else:
            if(self.var['v1']):
                try:
                    self.server.connect((self.var['v4'], self.var['v6']));
                except Exception as error:
                    messagebox.showerror("Connection error!", f"Error: {error}");
                else:
                    self.var['v2'] = True   
            else:
                try:
                    self.server.connect((self.var['v3'], self.var['v5']));
                except Exception as error:
                    messagebox.showerror("Connection error!", f"Error: {error}");
                else:
                    self.var['v2'] = True


    def checkAddress(self, type=None):
        if (type != None):
            if (type == 0):
                if (self.var['v3'] == "127.0.0.1"):
                    if (self.var['v5'] == 5001):
                        return True
                    else:
                        return False
                else:
                    return False
            elif (type == 1):
                if (self.var['v1']):
                    if (self.var['v4'] == "127.0.0.1"):
                        if(self.var['v6'] == 5002):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            if (self.var['v1']):
                if (self.var['v4'] == "127.0.0.1"):
                    if(self.var['v6'] == 5002):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                if (self.var['v3'] == "127.0.0.1"):
                    if (self.var['v5'] == 5001):
                        return True
                    else:
                        return False
                else:
                    return False

    def listenServer(self):
        while True:
            if (self.var['v2']):
                msg = self.server.recv(2048).decode()
                if (self.var['v0']):
                    try:
                        self.txt.insert(END, msg)
                        self.txt.see(END)
                    except:
                        pass
            else:
                self.connectTo(None);
                time.sleep(5);

    def checkName(self, name):
        pass

if __name__ == "__main__":
    MainWindow().win();
