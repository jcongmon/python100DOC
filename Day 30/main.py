from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "1234567890"
    symbols = "~!@#$%^&*"
    pass_entry.delete(0, END)

    lower_chars = [choice(lowercase_letters) for _ in range(randint(5, 7))]
    upper_chars = [choice(uppercase_letters) for _ in range(randint(5, 7))]
    num_chars = [choice(nums) for _ in range(randint(2, 4))]
    special_chars = [choice(symbols) for _ in range(randint(2, 4))]
    pwd_list = lower_chars + upper_chars + num_chars + special_chars
    shuffle(pwd_list)
    new_pwd = "".join(pwd_list)
    pass_entry.insert(0, new_pwd)
    pyperclip.copy(new_pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def json_dump(data):
    with open("data.json", mode="w") as fp:
        json.dump(data, fp, indent=4)


def add_pwd():
    website = website_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website:
            {
                "email": user,
                "password": password,
            }
    }
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Missing data")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email/User: {user}\n"
                                                              f"Password: {password}\n"
                                                              f"Is that ok?")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                json_dump(new_data)
            else:
                data.update(new_data)
                json_dump(data)
            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)


# ----------------------------- SEARCH -------------------------------- #
def search():
    search_str = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data stored. Create and save first password.")
    else:
        try:
            rec_email = data[search_str]["email"]
            rec_pass = data[search_str]["password"]
            messagebox.showinfo(title=search_str, message=f"Email/User: {rec_email}\n"
                                                          f"Password: {rec_pass}")
        except KeyError:
            messagebox.showinfo(title="Error", message=f"There is no info stored for {search_str}.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=250, height=250, padx=20, pady=20)
canvas = Canvas(width=200, height=188)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=logo)
canvas.grid(row=0, column=1)

website_lbl = Label(text="Website:")
website_lbl.grid(row=1, column=0, sticky="E")

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="W")
website_entry.focus()

search_btn = Button(text="Search", width=13, command=search)
search_btn.grid(row=1 ,column=2, stick="W")

user_lbl = Label(text="Email/Username:")
user_lbl.grid(row=2, column=0, sticky="E")

user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2, sticky="W")
user_entry.insert(0, "test@email.com")

pass_lbl = Label(text="Password:")
pass_lbl.grid(row=3, column=0, sticky="E")

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, sticky="W")

gen_pass_btn = Button(text="Generate Password", command=generate_pwd)
gen_pass_btn.grid(row=3, column=2, sticky="W")

add_btn = Button(text="Add Password Information", width=36, command=add_pwd)
add_btn.grid(row=4, column=1, columnspan=2, sticky="W")


window.mainloop()
