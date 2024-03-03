from random import *
import tkinter as tk
import time

root = tk.Tk()
my_dict = {i + 1: str(i) for i in range(10)}
my_dict.update({i + 1: chr(ord('a') + i) for i in range(26)})

# Create a list containing only the values from the dictionary
my_list = list(my_dict.values())
def CreateRandomItemKey(keyLength:int):
    uniqueKey:str = ""
    for i in range(keyLength):
        uniqueKey += choice(my_list)
    return uniqueKey

class User:
    def __init__(self, name:str, password:str):
        self.name = name
        self.password = password
    def checkSystem(self, playersInput:str, itemCheck:str):
        if playersInput == itemCheck:
            return True
        else:
            return False



def main():
    l = []
    s1 = str(input("Enter player1\'s name: "))
    s2 = str(input("Enter player2\'s name: "))
    l.append(s1)
    l.append(s2)
    l.append(0)
    l.append(0)
    publicKeyLength = 8
    randomKey1 = CreateRandomItemKey(publicKeyLength)
    randomKey2 = CreateRandomItemKey(publicKeyLength)
    randomKey3 = CreateRandomItemKey(publicKeyLength)
    def KEYCHOICEFORCE():
        global User1
        if keyChoice == 1:
            User1 = User(l[0], randomKey1)
        elif keyChoice == 2:
            User1 = User(l[0], randomKey2)
        else:
            User1 = User(l[0], randomKey3)

    def cartonmain():
        keyChoice = 0
        txt = tk.Label(root, text="p1\'s turn: ")
        var = tk.IntVar()
        var.set(0)
        def DestroyWindow():
            print("No input received after 5s. Destroying window.")
            root.destroy()
        def OnButtonClickHandler(nKey):
            global keyChoice
            keyChoice = nKey
            var.set(1)
            root.after_cancel(timeoutVar)
            ButtonClickActual()
        def initCheck(P:tk.Entry):
            print("Processing...")
            if User1.checkSystem(P.get(), User1.password) is False:
                delAll()
                print("You lose")
                root.destroy()
            else:
                delAll()
                print("You win")
                root.destroy()
        def delAll(target=root):
            for widget in target.winfo_children():
                widget.destroy()
        def OtherPlayer():

            delAll()
            txt = tk.Label(root, text="p2\'s turn: ")
            playersInput = tk.Entry(root)

            submitButton = tk.Button(root, text="Submit", command=lambda:[initCheck(playersInput)])
            txt.pack()
            playersInput.pack()
            submitButton.pack()
        def ButtonClickActual():
            KEYCHOICEFORCE()
            OtherPlayer()
        Button1 = tk.Button(root, text=randomKey1, command=lambda: OnButtonClickHandler(1))
        Button2 = tk.Button(root, text=randomKey2, command=lambda: OnButtonClickHandler(2))
        Button3 = tk.Button(root, text=randomKey3, command=lambda: OnButtonClickHandler(3))
        txt.pack()
        Button1.pack(pady=10)
        Button2.pack(pady=10)
        Button3.pack(pady=10)
        timeoutVar = root.after(5000, DestroyWindow)
        root.wait_variable(var)


    cartonmain()



if __name__ == "__main__":
    main()
    root.mainloop()

