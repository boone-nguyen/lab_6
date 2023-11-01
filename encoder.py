#Made by Boone Nguyen
def encoder(password):
    val = []
    encoded = ""
    for i in password:
        val.append(i)
    for j in range(len(val)):
        val[j] = int(val[j]) + 3
    for e in range(len(val)):
        val[e] = str(val[e])
    for g in range(len(val)):
        val[g] = val[g][-1]
    for h in range(len(val)):
        encoded += val[h]
    return encoded


def print_menu():
    print("menu\n-------------\n1. Encode\n2. Decode\n3. Quit")

# added by Robert Iuhasz
def decoder(encoded):
    decoded_pass = ''
    for number in encoded:
        decoded_pass += str((int(number) - 3) % 10)
    return decoded_pass


if __name__ == '__main__':
    continue_run = True

    while continue_run:
        print_menu()
        option = input("Please enter an option: ")
        if option == "1":
            password = encoder(input("Please enter your password to encode:"))
            print("Your password has been encoded and stored!")
        elif option == "2":
            # added by Robert Iuhasz
            decoded_password = decoder(password)
            print("The encoded password is " + str(password) + ", and the original password is " + str(decoded_password))
        elif option == "3":
            continue_run = False
            break

    print("Thank you for using password encoder")
