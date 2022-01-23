from used_libraries import bcrypt, os, stdiomask, sys

def store_hash_file():
    master_password = stdiomask.getpass("> Please enter a new master password: ").strip()
    check_master_password = stdiomask.getpass("> Please confirm the password to make sure: ").strip()
    while check_master_password != master_password:
                print()
                print("[!] Sorry the password you entered doesn't match the previuos one!!")
                master_password = stdiomask.getpass("> Re-nter the password: ").strip()
                check_master_password = stdiomask.getpass("> Please confirm the password to make sure: ").strip()
    encoded_master_password = bytes(master_password, 'utf-8')
    hashed_password = bcrypt.hashpw(encoded_master_password, bcrypt.gensalt())
    hash_file = open(f'C:\\Users\\{os.getlogin()}\\Desktop\\Python Password Manager in SQL\\hash_file', 'wb')
    hash_file.write(hashed_password)
    hash_file.close()

def read_hash_file():
    hash_file = open(f'C:\\Users\\{os.getlogin()}\\Desktop\\Python Password Manager in SQL\\hash_file', 'rb')
    data = hash_file.read()
    hash_file.close()
    return data