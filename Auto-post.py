from selenium import webdriver

from tkinter import *
from tkinter import filedialog,ttk
import tkinter.ttk
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoAlertPresentException
import time
import random
import bs4




PATH = os.path.join(os.environ["HOMEPATH"],'desktop')
def Upload():
    global filename
    filename = filedialog.askopenfilename(initialdir = PATH, title = "Choose an image to upload")
    labfile.config(text=filename)
    cor = open("FileName.txt", "w")
    cor.write(filename)
    cor.close()

def Add():
    global liste
    op2 = open("WebsitesBot.txt","a")
    op2.write("\n" + websitesdeg.get())
    op2.close()
    liste.append(websitesdeg.get())
    ComboWeb.config(values=liste)

def POST():
    global drive
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver,20)
    CurrentURL = driver.current_url
    Commentaire = CommentField.get()
    Sujet = SubjectField.get()
    for i in liste:
        xx = random.randrange(1000,99999999999999999)
        xx = str(xx)
        Le_Message = Commentaire + "\n" + xx
        driver.get(i)
        wait.until(EC.presence_of_element_located((By.NAME, "subject")))
        CurrentURL = driver.current_url
        driver.find_element_by_name("subject").send_keys(Sujet)
        driver.find_element_by_name("body").send_keys(Le_Message)
        driver.find_element_by_name("file").send_keys(filename)
        driver.find_element_by_name("post").click()
        try:
            driver.find_element_by_name("post").submit()
        except:
            pass
        z = 0
        while 1:
            time.sleep(1)
            Source = driver.page_source
            xb = re.search(xx, Source)
            if xb is not None:
                break
            else:
                pass
            if z >= 45:
                break
            else:
                pass
            
        
        
        
        
    

    
fenetre = Tk()
frame = Frame(fenetre, bg="dark grey")
frame.grid(row=0,column=0)
NameField = Entry(frame, width = 20)
SubjectField = Entry(frame, width = 20)
CommentField = Entry(frame, width = 20)
UploadBut = Button(frame, text = "Upload", fg ="blue", bg="dark grey", width = 10,command=Upload)
PostBut = Button(frame,text = "POST", fg = "dark red", bg ="dark grey", width = 10,command=POST)
AddWebsite = Button(frame, text="Add website", fg ="blue", bg="dark grey", width = 10,command = Add)
websitesdeg = StringVar()
ComboWeb = tkinter.ttk.Combobox(frame, textvariable = websitesdeg, width = 20)
op = open("WebsitesBot.txt","r")
rop = op.readlines()
op.close()
liste = rop
ComboWeb["value"] = liste
ComboWeb.current(0)




Label(frame, bg="dark grey", fg="red", text = "Name").grid(row=0,column=0,sticky =NW)
Label(frame, bg="dark grey", fg="red", text = "Subject").grid(row=1,column=0,sticky =NW)
Label(frame, bg="dark grey", fg="red", text = "Comment").grid(row=2,column=0,sticky =NW)
Label(frame, bg="dark grey",text="").grid(row=3,column=2,sticky=NW)
labfile = Label(frame,bg="dark grey", text="", fg="red")
labfile.grid(row=4,column=1,sticky=NW)
PostBut.grid(row=5,column=0,sticky=NW, pady=7)
AddWebsite.grid(row=6, column=0,sticky=NW,pady=6)
ComboWeb.grid(row=6,column=1,sticky=NW,pady=8)



NameField.grid(row=0,column=1,sticky =NW)
SubjectField.grid(row=1,column=1,sticky =NW)
CommentField.grid(row=2,column=1,sticky =NW)
UploadBut.grid(row=4,column=0,columnspan =1 ,sticky = NW)



fenetre.mainloop()
