from program_functions import *
from master_password_hasher import *

def main():
    print()
    print(f"- Hello {os.getlogin()}.")
    print("-" * 30)
    time.sleep(0.3)

    allowed_authentication_tries = 3

    if not os.path.isfile(f'C:\\Users\\{os.getlogin()}\\Desktop\\Python Password Manager in SQL\\hash_file'):
        print()
        print("[!] You are new here or the security file was deleted")
        if not os.path.isfile("secretkey.db"): 
            print()
        else:
            print("[!] Wiping existing database...")
            wipe_database()
            print("[!] Wiping is completed...")
        print()
        store_hash_file()
    else: 
        master_password = stdiomask.getpass("> Please enter your master password: ").strip()
        encoded_master_password = bytes(master_password, 'utf-8')
        while bcrypt.checkpw(encoded_master_password, read_hash_file()) is False:
            print()
            print(f"[!] Wrong Password!! Please try again, you still have {allowed_authentication_tries} time(s).")
            allowed_authentication_tries-=1
            master_password = stdiomask.getpass("> Please enter your master password: ").strip()
            encoded_master_password = bytes(master_password, 'utf-8')
            if allowed_authentication_tries == 0:
                print()
                choice = input("[?] Would you like to restart, but keep in mind that the data will be wipped!! [y/n]: ").strip().lower()
                if choice == "y":
                    os.remove(f'C:\\Users\\{os.getlogin()}\\Desktop\\Python Password Manager in SQL\\hash_file')
                    store_hash_file()
                    break
                else:
                    sys.exit()
    
    print()
    print("[!] Starting the connection to the database...")
    time.sleep(0.5)
    print("[!] The database is Connected!")

    
    menu = """
    1- Store a new password entry.
    2- Seach for an Entry.
    3- Update an Entry.
    4- Remove an Entry.
    5- Display All Entries.
    6- Wipe Data from Database.
    7- Change the Master Password
    8- Exit.
    """
    

    while True:
        print("-" * 50)
        print(menu)
        print("-" * 50)
        while True:
            print()
            choice = input("> What do you want to do?: ").strip()
            print()
            if choice == '8':
                print("[!] Closing connection to the database...")
                time.sleep(0.3)
                # closing the connection to the database
                connection.close()
                print("[!] Connection closed!")
                print(f"Goodbye {os.getlogin()}...")
                sys.exit()
            
            if choice == '1':
                insert_entry()
            
            if choice == '2':
                search_by_servicename()
            
            if choice == '3':
                print("""
    a- Update the username of an entry.
    b- Update the password of an entry.
            """)
                sub_choice_3 = input("> What do you choose? (a or b): ").strip()
                if sub_choice_3 == "a":
                        update_username()
                if sub_choice_3 == "b":
                        update_password()
                
            if choice == '4':
                remove_entry()

            if choice == '5':
                print_data()
            
            if choice == '6':
                wipe_database()
            
            if choice == '7':
                store_hash_file()
                print("[!] Master Password is changed.")
main()