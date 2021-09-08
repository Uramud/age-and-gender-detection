from tkinter import *
from tkinter import ttk,filedialog
from tkinter import scrolledtext
from tkinter import messagebox
import os
from PIL import Image, ImageTk

window = Tk()
window.geometry("360x500")
window.resizable(0,0)
# window.wm_iconbitmap('icon.ico')
window.title('Age Prediction and Gender Detection')

style = ttk.Style()
style.theme_use('vista')
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

# global variables
is_recording = False

# heading
heading1 = Label(text='Age and Gender Classification',font=("Comic Sans MS",10,"normal"),width=40)
heading1.grid(column=0,row=0)

#display photo
dis_photo = PhotoImage(file='38260.png')
dis_photos = Button(image=dis_photo,borderwidth=1,relief=RIDGE,width=280,height=280)
dis_photos.grid(column=0,row=1)

# display gender and age
age_gender = ttk.Frame()
age_gender.columnconfigure(0,weight=1)
age_gender.grid(row=2,column=0)

mic_button = Button(age_gender,text='Gender',font=("Comic Sans MS",16,"normal"),fg="blue",bg="black",borderwidth=0,relief=RIDGE)
mic_button.grid(column=0,row=0,pady=5,padx=20)
mic_button = Button(age_gender,text='Age',padx=14,font=("Comic Sans MS",16,"normal"),borderwidth=0,relief=RIDGE)
mic_button.grid(column=1,row=0,pady=5,padx=20)

# capture and folder button
cap_fol = ttk.Frame()
cap_fol.columnconfigure(0,weight=1)
cap_fol.grid(row=3,column=0)

def switch_clicked():
    print('switch clicked')
    global is_recording
    if is_recording:
        is_recording = False
        folder_button.config(image=capture_icon)
        
    else:
        is_recording = True
        folder_button.config(image=folder_icon)
        
    
capture_icon = PhotoImage(file='camera.png')
switch_icon = PhotoImage(file='switch.png')
mic_button = Button(cap_fol,image=switch_icon,command=switch_clicked,width=40,height=40)
mic_button.grid(column=1,row=3)


def folder_clicked():
    files = filedialog.askopenfilenames(initialdir=os.getcwd(),title="Select Image File")
    # fil = files[0].split('/')[-1]
    # print(fil)
    # print('done')
    # dis_photoss = PhotoImage(file='38261.png',width=280,height=280)
    # dis_photos.config(image=dis_photoss)

    img=Image.open(files)
    img.thumbnail((350,350))
    img=ImageTk.PhotoImage(img)
    # dis_photos.configure(image=img)
    lbl.configure(image=img)
    lbl.image=img



folder_icon = PhotoImage(file='folder.png')
folder_button = Button(cap_fol,image=folder_icon,command=folder_clicked,width=40,height=40)
folder_button.grid(column=0,row=3,padx=10,pady=10)

frm=Frame(window)

lbl=Label(window)


window.mainloop()