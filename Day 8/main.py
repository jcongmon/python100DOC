alphabet = "abcdefghijklmnopqrstuvwxyz"


def find_idx(alphabet, c):
    for i in range(len(alphabet)):
        if c == alphabet[i]:
            return i


def cipher(task, msg, new_msg, shift):
    if task == "encode":
        for i in range(len(msg)):
            idx = find_idx(alphabet, msg[i])
            new_msg += alphabet[(idx + shift) % 26]
        print(f"Here is your encoded message: {new_msg}")
    elif task == "decode":
        for i in range(len(msg)):
            idx = find_idx(alphabet, msg[i])
            new_msg += alphabet[(idx - shift) % 26]
        print(f"Here is your decoded message: {new_msg}")


while True:
    task = input("Type 'encode' to encrypt, type 'decode' to decrypt.\n").lower()
    msg = input("Type your message:\n").lower()
    shift = int(input("Type the shift number.\n"))
    new_msg = ""

    cipher(task, msg, new_msg, shift)

    sentinel = input("Type 'yes' to continue or 'no' to quit.\n")
    if sentinel == "no":
        break


