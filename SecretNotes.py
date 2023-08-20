from  tkinter import *
from  tkinter import messagebox
import base64

def encode(key,clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr(ord(clear[i]) + ord(key_c) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key,enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc.encode()).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c))%256)
        dec.append(dec_c)
    return "".join(dec)

def save_and_encrypt_notes():
    title = my_entry.get()
    message = text.get('1.0',END)
    master_secret = my_entry2.get()


    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showwarning(title='Error',message='Please Enter all info')

    else:
        #encryption
        message_encrypted = encode(master_secret,message)

        try:
            with open('mysecret.txt','a') as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            my_entry.delete(0, END)
            text.delete("1.0", END)
            my_entry2.delete(0, END)

def decrypt_notes():
    message_encrypted = text.get("1.0",END)
    master_secret = my_entry2.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showwarning(title="Error!",message="Please enter all info")

    else:
        try:
            decrypted_mesage = decode(master_secret,message_encrypted)
            text.delete("1.0",END)
            text.insert("1.0",decrypted_mesage)

        except:
            messagebox.showwarning(title="Error!", message="Please enter encrypted text")

window = Tk()
window.title("Secret Notes")
window.minsize(width=400,height=700)


# Resmi yüklemek için PhotoImage kullanılır
photo = PhotoImage(file='Adsız.png')
# Resmi görüntülemek için bir etiket oluşturulur
img_label = Label(window, image=photo)
img_label.pack()

#label
my_label = Label(text='Enter Your Tittle', font=('Arial', 10, 'bold'))
my_label.place(x=150,y=150)
my_label2 = Label(text='Enter Your Secret', font=('Arial', 10, 'bold'))
my_label2.place(x=150,y=200)
my_label3 = Label(text='Enter Master Key', font=('Arial', 10, 'bold'))
my_label3.place(x=150,y=555)



#Entry
my_entry= Entry(width=35)
my_entry.place(x=100,y=175)
my_entry2 = Entry(width=35)
my_entry2.place(x=100,y=578)

#TExt
text = Text(window,width=30,height=20)
text.place(x=90,y=230)


#Button
my_button = Button(text='Save & Encrypt',command=save_and_encrypt_notes)
my_button.place(x=150,y=600)
my_button2 = Button(text='Decrypt',command=decrypt_notes)
my_button2.place(x=170,y=635)

window.mainloop()