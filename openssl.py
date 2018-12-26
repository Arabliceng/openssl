#!/usr/bin/env python3
from tkinter import *
from PIL import Image,ImageTk
import subprocess
from subprocess import call
from tkinter import filedialog
from tkinter import messagebox

import sys
import os
if sys.version_info[0] < 3:
   import Tkinter as Tk
else:
   import tkinter as Tk

   folder=""
   file=""
   privatekey=""
   publickey=""
   orginalfile=""
   certificatefile=""
def get_privatekey():
    global privatekey
    privatekey = filedialog.askopenfilename(initialdir= "/" ,title='Please select a Private Key File')
    return privatekey
def get_publickey():
    global publickey
    publickey = filedialog.askopenfilename(initialdir= "/", title='Please select a Public Key File')
    return publickey

def encrypt(file,folder,password):
    command1="openssl enc -aes-256-cbc -salt -k "+password
    command2=" -in "+file
    encfile=os.path.basename(file)+".enc"
    command3=" -out "+folder+"/"+encfile
    com=command1+command2+command3
    p = call(com ,shell=True)
def genprivatekey(folder):
    command1="openssl genpkey -algorithm RSA -out  " + folder +"/private_key.pem -pkeyopt rsa_keygen_bits:2048"
    p = call(command1,shell=True)
    
def genpublickey(folder):
      command1="openssl rsa -pubout -in " + folder +"/private_key.pem -out " +folder +"/public_key.pem"
      p = call(command1,shell=True)

def sign(file,folder,privatekey):
        signedfile=os.path.basename(file)+".sha256 "
        command1="openssl dgst -sha256 -sign "+privatekey+" -out "+folder +"/"+signedfile +" " +file 
  #      command1="openssl rsautl -sign -in " + file +" -inkey "+privatekey+" -out " +folder +"/signedfile"
        p = call(command1,shell=True)
        print(command1)
   
def checksignatur(file,orginalfile,publickey):
          
  #        command1="openssl rsautl -verify -in " + file +" -inkey "+publickey+" -pubin"
        file1=os.path.basename(file)
        basefile=os.path.splitext(file1)[0]
        command1="openssl dgst -sha256 -verify "+publickey+" -signature "+file +" "+orginalfile
 #       p = call(command1,shell=True)
        proc = subprocess.Popen( command1, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        messagebox.showinfo("Verification Resualt", out)
        
        print(command1)
        
    
def selected_folder():
    global folder
    folder = filedialog.askdirectory(initialdir= "/", title='Please select a directory')
    print(folder)
    return folder
def browse_file():
    global file
    file = filedialog.askopenfilename(initialdir= "/", title='Please select a file')
    print(file)
    return file   
def selectcertificatefile():
   global certificatefile
   certificatefile= filedialog.askopenfilename(initialdir= "/", title='Please select a file')
   print(certificatefile)
   return certificatefile
def browse_ofile():
    global orginalfile
    orginalfile = filedialog.askopenfilename(initialdir= "/", title='Please select a file')
    print(orginalfile)
    return orginalfile    

def decrypt(encfile,folder,password):
    command1="openssl enc -aes-256-cbc -d -k "+password
    command2=" -in "+encfile
    file=os.path.basename(encfile)
    basefile=os.path.splitext(file)[0]
    command3=" -out "+folder+"/"+basefile
    com=command1+command2+command3
    p = call(com ,shell=True)
def helpgui():
       root = Tk.Tk()
       root.wm_title("help Window")
       info1="Documentation describe how script works \n"
       
       info1=info1+ "--------------------------------------------------------------\n"
       info="A- The steps for Encryption and Decryption process\n"
       info=info+ "-------------------------------------------------------\n"
       info=info+"1- Enter the password for Encryption and Decryption \n"
       info=info+"2- Select file to be encrypted or decrypted \n"
       info=info+"3- Select destination folder for encrypted or decrypted file \n"
       info=info+"4- Click encrypt file button for Encryption and decrypt file button for Decryption \n"
       info=info+ "\n"
       info=info+"B- The steps Generation of Public and Private Keys\n"
       info=info+ "-------------------------------------------------------\n"
       info=info+"1- Select the destination folder for Public or Private keys\n "
       info=info+"2- Click Generate Private key button for Private key and Click Generate Public Key for Public key "
       info=info+ "\n"
       info=info+"C- The steps Digital Signature process \n"
       info=info+"\n"
       info=info+" Signature of  the file\n "
       info=info+"--------------------------\n"
       info=info+"1- Select file to be signned by private key\n"
       info=info+"2- Select destination folder for signed file \n"
       info=info+"3- Select the Private Key file for the Signing process \n"
       info=info+ "\n"
       info=info+ "Verification of the  file \n "
       info=info+"-------------------------------\n"
       info=info+"1- Select  signned file to be verified by Public key \n"
       info=info+"2- Select the original file to be compared by verification process \n"
       info=info+"3- Select the Public key file for verification process\n"
       info=info+"4- the verification result will be Verified OK if the signned file is passed and verified failuer if the signned is not passed\n"
       info=info+"\n"
       info=info+"D- The steps of Certificate Generation process \n"
       info=info+"-------------------------------------------------\n"
      
       info=info+"1- Select destination folder for Certificate file and Private key file \n"
       info=info+"2- Enter the information of Certificate like country name(only two letters like 'US', city name ,company name, Email and the password for private key file  ) \n"
       info=info+ "\n"
       info=info+"E- The steps of Encryption/Decryption by Asymmetric keys \n"
       info=info+"----------------------------------------------------------\n"
       
       
       info=info+"1- Select file to be encrypted or decrypted \n"
       info=info+"2- Select Certificate file to be used in Encryption Process \n"
       info=info+"3- Select destination folder for encrypted or decrypted file \n"
       info=info+"4- Click encrypt file button for Encryption  \n"
       info=info+"5- Enter the Password that used in the generation of certificate and private key file for Decryption Process   \n"
       
       info=info+"2- Select Private key file for Decryption Process  \n"
       info=info+"4- Click decrypt file button for Decryption  \n"
       info=info+ "\n"
       
      

              
       
 ##########

 #  command1="openssl req -x509 -days 100000 -newkey rsa:1024 -passout pass:ahmad -subj '/c=sa' -keyout private_key.pem -out certificate.pem"

#command1="openssl smime -encrypt -binary -aes-256-cbc -in aa.mp4  -out eaa.mp4.enc -outform DER certificate.pem"
#command1="openssl smime -decrypt -binary -passin pass:ahmad  -in aa.mp4.enc -inform DER -out mam.mp4   -inkey private_key.pem"
 #command1="openssl smime -decrypt -binary -passin pass:ahmad  -in aa.mp4.enc -inform DER -out mam.mp4   -inkey private_key.pem"
       ###########
       
       



       
       ll=Label(root,justify=LEFT,  padx = 10, text=info1, font = "Helvetica 16 bold italic")
       
       ll.pack(side="top")
       ll1=Label(root,justify=LEFT,  padx = 10, text=info)
       ll1.pack(side="left")
       #ll.grid(row=0,column=0,padx=1)
def create_certificate(country,city,company,email,password,folder):
 #  messagebox.showinfo("Certificate Generation", "Please wait for Certificate Generation ")
   comm='export MYPASS={0}'.format(password)
   com='"/C={0}/ST={1}/O={2}/CN={3}"'.format(country ,city,company,email)
   command1="openssl req -x509 -days 100000 -newkey rsa:1024 -passout pass:"+password+" -subj "+com +" -keyout  "+folder +"/private_key.pem -out "+folder +"/certificate.pem"
   
   print(command1)

   proc = subprocess.Popen( command1, stdout=subprocess.PIPE, shell=True)
 
   (out, err) = proc.communicate()
   print(command1)

    
def asymmetricencrypt(file,folder,certificatefile):
   encfile=os.path.basename(file)+".enc"
   command1="openssl smime -encrypt -binary -aes-256-cbc -in "+file+"  -out " +folder +"/"+encfile+" -outform DER "+ certificatefile
   print(command1)

   proc = subprocess.Popen( command1, stdout=subprocess.PIPE, shell=True)
 
   (out, err) = proc.communicate()
   print(command1)

   
def asymmetricdecrypt(file,folder,password,privatekey):
      file1=os.path.basename(file)
      basefile=os.path.splitext(file1)[0]
      command1="openssl smime -decrypt -binary -passin pass:"+password +  " -in "+file +" -inform DER -out  "+ folder +"/"+ basefile+" -inkey "+ privatekey
      print(command1)
      proc = subprocess.Popen( command1, stdout=subprocess.PIPE, shell=True)
      (out, err) = proc.communicate()
      print(command1)
   
def certificategui():
       root = Tk.Tk()
       root.wm_title("Certificate  Generation Window")
       ll=Label(root, text="Select Folder for Certificate  ")
       ll.grid(row=0,column=0,pady=4,padx=1)
       broButton1 = Tk.Button(master = root, text = 'Select folder', width=10, command=selected_folder)
       broButton1.grid(row=0, column=1,pady=4,padx=15)
       
       ll33=Label(root, text="Enter Country Name for Certificate (just Two Letters) ")
       ll33.grid(row=1,column=0,pady=4,padx=1)
       e1 = Entry(root,width=12)
       e1.grid(row=1, column=1,pady=4,padx=1)
       
       ll1=Label(root, text="Enter The City name for Certificate  ")
       ll1.grid(row=2,column=0,pady=4,padx=1)
       e2 = Entry(root,width=12)
       e2.grid(row=2, column=1,pady=4,padx=15)
       
       ll1=Label(root, text="Enter The Company for Certificate ")
       ll1.grid(row=3,column=0,pady=4,padx=1)
       e3 = Entry(root,width=12)
       e3.grid(row=3, column=1,pady=4,padx=15)
       
       ll1=Label(root, text="Enter The Email  for Certificate ")
       ll1.grid(row=4,column=0,pady=4,padx=1)
       e4 = Entry(root,width=12)
       e4.grid(row=4, column=1,pady=4,padx=15)
       
       ll1=Label(root, text="Enter The Password  for Certificate")
       ll1.grid(row=5,column=0,pady=4,padx=1)
       e5 = Entry(root,show="*",width=12)
       e5.grid(row=5, column=1,pady=4,padx=15)
       
       broButton1 = Tk.Button(master = root, text = 'Create Certificate', width=15, command=lambda:create_certificate(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),folder))
       broButton1.grid(row=6, column=1,pady=4,padx=15)
   
def digitalsignaturegui():
       root = Tk.Tk()
       root.wm_title("Digital Signature Window")
       ll=Label(root, text="Select file to be signned  ")
       ll.grid(row=0,column=0,pady=4,padx=1)
       broButton1 = Tk.Button(master = root, text = 'Select file', width=10, command=browse_file)
       broButton1.grid(row=0, column=1,pady=4,padx=15)
       
       ll33=Label(root, text="Select folder for signned  file ")
       ll33.grid(row=1,column=0,pady=4,padx=1)
       broButton1 = Tk.Button(master = root, text = 'Select folder', width=10, command=selected_folder)
       broButton1.grid(row=1, column=1,pady=4,padx=15)
       
       ll1=Label(root, text="Select signned file for  verification  ")
       ll1.grid(row=2,column=0,pady=4,padx=1)
       broButton2 = Tk.Button(master = root, text = 'Select file', width=10, command=browse_file)
       broButton2.grid(row=2, column=1,pady=4,padx=15)
       
       ll1=Label(root, text="Select orginal  file for  verification  ")
       ll1.grid(row=3,column=0,pady=4,padx=1)
       broButton2 = Tk.Button(master = root, text = 'Select file', width=10, command=browse_ofile)
       broButton2.grid(row=3, column=1,pady=4,padx=15)
       


 
       
       ll2=Label(root, text="Select Private Key file for  signature ")
       ll2.grid(row=4,column=0,pady=4,padx=1)
       broButton22 = Tk.Button(master = root, text = 'Select Private Key', width=25, command=get_privatekey)
       broButton22.grid(row=4, column=1,pady=4,padx=15)
       
       ll=Label(root, text="Select Public Key file for  verfication ")
       ll.grid(row=5,column=0,pady=4,padx=1)
       broButton3 = Tk.Button(master = root, text = 'Select Public Key', width=25, command=get_publickey)
       broButton3.grid(row=5, column=1,pady=4,padx=15)
       
       broButton2 = Tk.Button(master = root, text = 'Sign File', width=30, command=lambda: sign(file,folder,privatekey))#lambda: encrypt(file,folder,e1.get())
       broButton2.grid(row=6, column=0,pady=4,padx=1)
       broButton3 = Tk.Button(master = root, text = 'Verify File', width=30, command=lambda:checksignatur(file,orginalfile,publickey))
       broButton3.grid(row=6, column=1,pady=4,padx=1)
def generationkeygui():
       root = Tk.Tk()
       root.wm_title("Generation Keys Window")
       ll=Label(root, text="Select folder for Public/Private Keys  ")
       ll.grid(row=0,column=0,pady=4,padx=1)
       broButton1 = Tk.Button(master = root, text = 'Select folder', width=10, command=selected_folder)
       broButton1.grid(row=0, column=1,pady=4,padx=15)
       broButton2 = Tk.Button(master = root, text = 'Generate Private Key', width=30, command=lambda: genprivatekey(folder))#lambda: encrypt(file,folder,e1.get())
       broButton2.grid(row=3, column=0,pady=4,padx=1)
       broButton3 = Tk.Button(master = root, text = 'Generate Public Key ', width=30, command=lambda:genpublickey(folder))
       broButton3.grid(row=3, column=1,pady=4,padx=1)
   
    
def encryptionasymmetricgui():
     root = Tk.Tk()
     root.wm_title(" Asymmetric Encryption and Decryption Window")
     
     ll=Label(root, text="Enter Password for Decryption ")
     ll.grid(row=0,column=0,pady=4,padx=1)
     e1 = Entry(root, show="*",width=12)
     e1.grid(row=0, column=1,pady=4,padx=1)
     
     l1=Label(root, text="Select file to be encrypted/decrypted")
     l1.grid(row=1,column=0,pady=4,padx=1)
     broButton = Tk.Button(master = root, text = 'Select File ',  width=10,command=browse_file)
     broButton.grid(row=1, column=1,pady=4,padx=1)
     
     l1=Label(root, text="Select Certificate file  for Encryption ")
     l1.grid(row=2,column=0,pady=4,padx=1)
     broButton = Tk.Button(master = root, text = 'Select File ',  width=10,command=selectcertificatefile)
     broButton.grid(row=2, column=1,pady=4,padx=1)
     
     l2=Label(root, text="Select destination folder for  file ")
     l2.grid(row=3,column=0,pady=4,padx=1)
     broButton1 = Tk.Button(master = root, text = 'Select folder', width=10, command=selected_folder)
     broButton1.grid(row=3, column=1,pady=4,padx=15)
     
     l1=Label(root, text="Select Private Key  file  for Decryption ")
     l1.grid(row=4,column=0,pady=4,padx=1)
     broButton = Tk.Button(master = root, text = 'Select File ',  width=10,command=get_privatekey)
     broButton.grid(row=4, column=1,pady=4,padx=1)
     
     broButton2 = Tk.Button(master = root, text = 'Encrypt File ', width=10, command=lambda: asymmetricencrypt(file,folder,certificatefile))#lambda: encrypt(file,folder,e1.get())
     broButton2.grid(row=5, column=0,pady=4,padx=1)
     broButton3 = Tk.Button(master = root, text = 'Decrypt File', width=10, command=lambda:asymmetricdecrypt(file,folder,e1.get(),privatekey))
     broButton3.grid(row=5, column=1,pady=4,padx=1)

   
def encryptiongui():
     root = Tk.Tk()
     root.wm_title("Encryption and Decryption Window")
     ll=Label(root, text="Enter Password for Encryption/Decryption ")
     ll.grid(row=0,column=0,pady=4,padx=1)
     e1 = Entry(root, show="*",width=12)
     e1.grid(row=0, column=1,pady=4,padx=1)
     l1=Label(root, text="Select file to be encrypted/decrypted")
     l1.grid(row=1,column=0,pady=4,padx=1)
     broButton = Tk.Button(master = root, text = 'Select File ',  width=10,command=browse_file)
     broButton.grid(row=1, column=1,pady=4,padx=1)
     l2=Label(root, text="Select destination folder for  file ")
     l2.grid(row=2,column=0,pady=4,padx=1)

     broButton1 = Tk.Button(master = root, text = 'Select folder', width=10, command=selected_folder)
     broButton1.grid(row=2, column=1,pady=4,padx=15)
     broButton2 = Tk.Button(master = root, text = 'Encrypt File ', width=10, command=lambda: encrypt(file,folder,e1.get()))#lambda: encrypt(file,folder,e1.get())
     broButton2.grid(row=3, column=0,pady=4,padx=1)
     broButton3 = Tk.Button(master = root, text = 'Decrypt File', width=10, command=lambda:decrypt(file,folder,e1.get()))
     broButton3.grid(row=3, column=1,pady=4,padx=1)


root = Tk.Tk()
root.wm_title("Openssl Fucntions GUI ")


menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Encryption/Decryption Process", command = encryptiongui)
filemenu.add_command(label = "Generation Private and Public Key ", command = generationkeygui)
filemenu.add_command(label = "Digital Signature ", command = digitalsignaturegui)
filemenu.add_command(label = "Generation Certificate ", command = certificategui)
filemenu.add_command(label = "Encryption and Decryption by Asymmetric Key", command = encryptionasymmetricgui)

filemenu.add_separator()

filemenu.add_command(label = "Help about using Script's functions ", command = helpgui)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = exit)
menubar.add_cascade(label = "File", menu = filemenu)


root.config(menu = menubar)
imagefile = "./toto.jpg"
img = ImageTk.PhotoImage(Image.open(imagefile))
lbl = Label(root, image = img).pack()

root.mainloop()
