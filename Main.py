from tkinter import Tk, Frame, PhotoImage, Label, Button, Message

clicks=0
def check_button(r,c):
    global color_list,clicks
    clicks+=1
    btnList[r][c].config(highlightbackground=color_list[clicks])


def start():
    global attempts,active_row

    #add to attempts
    attempts+=1

    #make first row active
    for x in range(4):
        btnList[active_row][x].config(state='normal')
    active_row-=1

    #enable submit
    btnSubmit.config(state='normal')

    #disable start
    btnStart.config(state='disabled')


WINDOW_WIDTH, WINDOW_HEIGHT = 340, 915

root = Tk()
root.title('Mastermind')
root.geometry(f'{WINDOW_WIDTH:d}x{WINDOW_HEIGHT:d}+{root.winfo_screenwidth() // 2 - WINDOW_WIDTH // 2:d}+{root.winfo_screenheight() // 2 - WINDOW_HEIGHT // 2:d}')

attempts, color_index, active_row = 0, 0, 14
color_list = ('lightgray', 'red', 'blue', 'green', 'yellow', 'pink', 'cyan')

frame = Frame(root, padx=10, pady=20)
frame.pack()

imgLogo = PhotoImage(file='images/mastermind.png')
lblTitle = Label(frame, image=imgLogo, border=0)
lblTitle.grid(row=0,column=0,columnspan=5,pady=5)

btnList=[[0 for cols in range(4)]for rows in range(15)]
lblList=[0]*15

for r in range(len(btnList)):
    for c in range(len(btnList[r])+1):
        # print(c)
        if c<4:
            btnList[r][c]=Button(frame,state='disabled',command=lambda r=r, c=c: check_button(r,c),relief='sunken')
            btnList[r][c].grid(row=r+1,column=c,ipadx=25,ipady=10)
        elif c==4:
            lblList[r]=Label(frame, borderwidth=1, relief='ridge')
            lblList[r].grid(row=r+1,column=4,ipadx=25,ipady=9)

buttonFrame = Frame(frame, pady=15)
buttonFrame.grid(row=16,column=0,columnspan=5)

btnStart = Button(buttonFrame, text='START', width=10,height=2,command=start)
btnStart.pack(side='left')
btnSubmit = Button(buttonFrame, text='SUBMIT', width=10,height=2,state='disabled')
btnSubmit.pack(side='left')
btnQuit = Button(buttonFrame, text='QUIT', width=10,height=2)
btnQuit.pack(side='left')
lblMessage = Message(frame, text='Click START to begin!', font='TkDefaultFont 10 bold', width=300, anchor='c')
lblMessage.grid(row=17,column=0,columnspan=5)

root.mainloop()