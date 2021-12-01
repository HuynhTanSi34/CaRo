from tkinter import *
from tkinter import messagebox
import random as r



def button(frame):          #Chức năng xác định một nút
    b=Button(frame,padx=1,bg="papaya whip",width=3,text=" ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b


def change_a():             #Chức năng chuyển sang người chơi khác
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break

def reset():                #Resets game
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])

def check():                #Kiểm tra chiến thắng hay hòa
    for i in range(3):
            #Kiểm tra chiều dọc hoặc ngang:
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Chức mừng!! Người chơi","'"+a+"' đã thắng")
                    reset()
    #Kiểm trad đường chéo:
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Chức mừng!! Người chơi","'"+a+"' đã thắng")
        reset()
    #Nếu ko thỏa cá dk trên thì kết quả hòa:
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Hòa!!","Trò chơi kết thúc với kết quả hòa")
        reset()
        
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
        label.config(text="Lượt của: "+a)
###############   Main Program #################
root=Tk()                   
root.title("Tic-Tac-Toe")   
a=r.choice(['O','X'])       
colour={'O':"blue",'X':"green"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label=Label(text="Lượt của: "+a,font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)
root.mainloop()
