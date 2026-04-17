#import tkinter for creating  GUI apps
import tkinter as tk

from tkinter import filedialog, messagebox
#main windo code
root= tk.Tk()
root.title(" NOTPAT BY HIMANSHU")
root.geometry("800x600")
# creat text area
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("helvetica",12)

)

text.pack( expand= True,fill=tk.BOTH)
# main loging starts now 
# function 1- to create a new file
def new_file():
    text.delete(1.0,  tk.END)
    #fuction 2- to open a new file

def open_file():
    #open file dialogue
    file_path=filedialog.askopenfilename(
         defaultextension=".txt",
         filetypes=(("text files","*.txt"))
    )
         # starts and keeps the window open
    if file_path:
    #open the selected file
     with open(file_path,"r") as file:
        text.delete(1.0, tk.END)
        text. insert(tk.END,file.read())

        #function 3 - save the filed

def save_file():
   #open save file dilogue
   file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("text files","*.txt")]
   )
   if file_path:
      with open(file_path,"w") as file:
         file.write(text.get(1.0,tk.END))

   messagebox.showinfo("info","file saved successfully")


#menu

menu= tk.Menu(root)
root.config(menu=menu)
file_Menu=tk.Menu(menu)

#new,open file save ,exit


menu.add_cascade(label="file", menu=file_Menu)
menu.add_cascade(label="help", menu=file_Menu)

file_Menu.add_command(label="new",command=new_file)
file_Menu.add_command(label="open", command=open_file)
file_Menu.add_command(label="save",command=save_file)
file_Menu.add_separator()
file_Menu.add_command(label="Exit",command=root.quit)



root.mainloop()