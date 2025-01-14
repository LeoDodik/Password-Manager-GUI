from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)





    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()  # Get the text from the website entry
    email = email_entry.get()      # Get the text from the email entry
    password = password_entry.get()# Get the text from the password entry


    if int(len(website)) == 0 or int(len(email))  == 0 or int(len(password)) == 0 :
         messagebox.showinfo(title="Error",message="Please fill out the empty fields")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}"
                                                      f"\n Password: {password} \n Is it ok to save?")
        if is_ok:
         with open("data.txt", "a") as f:
            f.write(f"Website: {website} | Email: {email} | Password: {password}\n")




    website_entry.delete(0,END)
    email_entry.delete(0,END)
    password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.geometry("300x300")  # Adjust the window size here
window.title("Password Manager")

# LOGO SETUP
canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

# LABELS
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


#ENTRIES
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"mesttest71@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1,columnspan=2)

#BUTTONS
add_button = Button(text="Add",command=save)
add_button.grid(row=4,column=1,columnspan=2)

password_button = Button(text="Generate Password",command=password_generator)
password_button.grid(column=2,row=3)

window.mainloop()
