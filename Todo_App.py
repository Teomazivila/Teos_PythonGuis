from tkinter import *
import random
from tkinter import messagebox


fg='gold'
fg1='White'
fg2='White'
bg2='black'
bg ='Dark Slate Grey'
bg1 = 'black'

root = Tk()
root.title('Teomazivila ToDo')
root.config(bg='Dark Slate Grey')
root.geometry('650x500')

#========================================Functions========================
def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def Add_Task():
    task = txt_input.get()
    if task !="":

        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"] = "Please create a task."
    txt_input.delete(0, "end")

def del_all():
    confirm = messagebox.askyesno("DELETE ALL", "Do you Really want to delete all TASKS?")
    if confirm == True:
        global tasks
        tasks = []
        update_listbox()

def del_one():
    task= lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_dsc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def random_task():
    task = random.choice(tasks)
    lbl_display["text"]=task

def Number_tasks():
    number_of_tasks =len(tasks)
    msg = "Number of tasks : %s" %number_of_tasks
    lbl_display["text"]=msg

def iExit():
    op = messagebox.askyesno("Exit", "Do you really want to EXIT?")
    if op > 0:
        root.destroy()

#=====================================Labels & Entry==========================================
lbl_title = Label(root, text="Teo's_ToDo_List", font=('Baskerville Old Face', 20,'bold'), bg=bg, fg=fg)
lbl_title.grid(row=0, column=0)

lbl_display = Label(root, text="", font=('Baskerville Old Face', 15,'bold'), bg=bg, fg=fg2)
lbl_display.grid(row=0 , column=1)

txt_input = Entry(root, width=42, bd=7, font=('Baskerville Old Face',12,'bold'))
txt_input.grid(row=1, column=1, pady=7,padx=7)

#===============================Buttons===========================
btn_addTask = Button(root, width=12, text='Add Task', fg=fg1, font='Algerian 14 bold', bg=bg2, command=Add_Task)
btn_addTask.grid(row=1, column=0)

btn_Del_All = Button(root,width=12, text='Delete All', fg=fg1, font='Algerian 14 bold',bg=bg2, command=del_all)
btn_Del_All.grid(row=2 , column=0,pady=10, padx=7)

btn_Del_One = Button(root,width=12, text='Delete', fg=fg1, font='Algerian 14 bold',bg=bg2, command=del_one)
btn_Del_One.grid(row=3 , column=0, pady=10, padx=7)

btn_Sort_Asc = Button(root,width=12, text='Sort (ASC)', fg=fg1, font='Algerian 14 bold',bg=bg2, command=sort_asc)
btn_Sort_Asc.grid(row=4 , column=0, pady=10, padx=7)

btn_Sort_Dsc = Button(root,width=12, text='Sort (DSC)', fg=fg1, font='Algerian 14 bold',bg=bg2, command=sort_dsc)
btn_Sort_Dsc.grid(row=5 , column=0,pady=10, padx=7)

btn_Random = Button(root,width=12, text='Random T.', fg=fg1, font='Algerian 14 bold',bg=bg2, command=random_task)
btn_Random.grid(row=6 , column=0,pady=10, padx=7)

btn_totalTask = Button(root,width=12, text='Total_Tasks', fg=fg1, font='Algerian 14 bold',bg=bg2, command=Number_tasks)
btn_totalTask.grid(row=7 , column=0,pady=10, padx=7)

btn_Exit = Button(root,width=12, text='Exit', fg=fg1, font='Algerian 14 bold',bg=bg2, command=iExit)
btn_Exit.grid(row=8 , column=0,pady=10, padx=7)

lb_tasks = Listbox(root,height=10, width=50, font=('Baskerville Old Face',12))
lb_tasks.grid(row=2, column=1,pady=12, padx=12, rowspan=7)

#==============================creating a list=====================
tasks = []
#========Testing=======
#tasks = ["Drink Coffee", "Call My Wife", "Start Programming"]



root.mainloop()