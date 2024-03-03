import random
import tkinter as tk
import numpy as np
from typing import List
l:List[int] = []
root = tk.Tk()
def RandomNumberGenerating(limit:int):
    return random.randint(1, limit)

def TakeMean(L:List[int]):
    return np.mean(L)

class User:
    def __init__(self, entry:int|float):
        self.entry = entry
    def checkingSystem(self, itemCheck:int|float):
        return float((self.entry) - itemCheck)


def WaitVariableSetter(*vars:tk.BooleanVar):
    for var in vars:
        var.set(True)

def RunFuncs(*funcs):
    for func in funcs:
        func()
def delAll(target=root):
    for widget in target.winfo_children():
        widget.destroy()
def compare(var1:int|float, var2:int|float):
    if float(var1) > float(var2):
        return float(var1-var2)
    elif float(var2) > float(var1):
        return float(var2-var1)
    else:
        return 0
def compareAndReturnGreater(var1:int|float, var2:int|float) -> float:
    if float(var1) > float(var2):
        return float(var1)
    elif float(var2) > float(var1):
        return float(var2)
    else:
        return 0
def check(var1:int|float, var2:int|float) -> bool:
    if float(var1) == float(var2) or var1 == var2:
        return True
    else:
        return False
def P1CheckSys(target:tk.Entry, checkSys):
    User1 = User(int(target.get()))
    s1 = User1.checkingSystem(checkSys)
    return s1
def P2CheckSys(target:tk.Entry, checkSys):
    User2 = User(int(target.get()))
    s2 = User2.checkingSystem(checkSys)
    return s2
def MeanNumberGuessingGame(v:int):
    limitF = int(input("Enter the number generating limit: "))
    if limitF <= 10 or limitF > 100_000:
        print("Invalid input")
        root.destroy()
    l.append(RandomNumberGenerating(limitF))
    p1 = TakeMean(l)
    l2 = []
    var1 = tk.BooleanVar()
    var1.set(False)
    name = tk.Label(root, text="Player 1")
    Inp1 = tk.Entry()
    Button1 = tk.Button(root, text="Submit", command=lambda:[WaitVariableSetter(var1), l2.append(abs(P1CheckSys(Inp1, p1)))])
    name.pack(pady=10)
    Inp1.pack()
    Button1.pack()
    Button1.wait_variable(var1)

    delAll()
    name2 = tk.Label(root, text="Player 2")
    var2 = tk.BooleanVar()
    var2.set(False)
    Inp2 = tk.Entry()
    Button2 = tk.Button(root, text="Submit", command=lambda:[WaitVariableSetter(var2), l2.append(abs(P2CheckSys(Inp2, p1)))])
    name2.pack(pady=10)
    Inp2.pack()
    Button2.pack()
    Button2.wait_variable(var2)
    print(l2)
    if l2[0] < l2[1]:
        print("Player 1 wins")
        print("The correct number is: ",p1)
    elif l2[0] > l2[1]:
        print("Player 2 wins")
        print("The correct number is: ",p1)
    else:
        print("Tie")
        print("The correct number is: ",p1)
    if v > 1:
        print("Play again? (Y/N)")
        ans = input()
        if ans == "Y":
            delAll()
            MeanNumberGuessingGame(v-1)
        else:
            delAll()
            root.destroy()
    else:
        root.destroy()


if __name__ == "__main__":
    root.title("Mean Number Guessing Game")
    r = int(input("Turns: "))
    if r <= 0:
        r =1
    MeanNumberGuessingGame(r)
    root.mainloop()
