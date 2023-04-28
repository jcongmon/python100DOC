with open("./Input/Names/invited_names.txt", mode='r') as data:
    names = data.readlines()

with open("./Input/Letters/starting_letter.txt", mode='r') as file:
    txt = file.read()
    replace_txt = "[name]"
    for name in names:
        txt = txt.replace(replace_txt, name.strip())
        replace_txt = name.strip()
        f = open(f"./Output/ReadyToSend/letter_to_{name.strip()}.txt", mode='w+')
        f.write(txt)
        f.close()
