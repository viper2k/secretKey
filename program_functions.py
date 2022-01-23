from used_libraries import *
from web_automator import auto_login

# if the database file doesn't exist it will create one and create a table inside of it
if not os.path.isfile("secretkey.db"): 
        print("Database does not exist")
        print("Creating a new database file...")
        time.sleep(0.5)
        connection = sqlite3.connect('secretkey.db')
        command = connection.cursor()
        command.execute("""
        CREATE TABLE passwords(
        ServiceName TEXT,
        UserName TEXT,
        Password TEXT,
        URL TEXT) 
        """)
        print("File is created with the name 'secretkey.db'.")
        time.sleep(0.3)


# connect to the database file
connection = sqlite3.connect('secretkey.db')

# cursor allow us to execute sql commands
command = connection.cursor()


# Function 1: Generate a password randomly:
def generate_password(lengthOfPassword):
    # generating using built-in functions from the import string and random
    lower= string.ascii_lowercase
    upper= string.ascii_uppercase
    digit= string.digits
    # here it will put the character beside each other
    password = f"{lower}{upper}{digit}" # ABCabc012
    # we convert them to a list to use the shuffle function
    password = list(password) #[A,B,C,a,b,c,0,1,2]
    # randomaly shuffling the above created characters
    random.shuffle(password) #[B,c,A,0,b,8]
    finalPassword = random.choices(password, k= lengthOfPassword)
    finalPassword = "".join(finalPassword) #BcA0...
    return finalPassword


# Function 2: Insert a new password entry:
def insert_entry():
    service_name = input("~ Enter a service name: ").strip()
    user_name = input("~ Enter a user name: ").strip()
    # because password managers offers this feature we included it also where you can choose and enter your password or let the program generate and choose one for you but you can still choose the length of the password only.
    password_choice= input("[?] Do you want to enter the password manually or get a generated one? (m for manual or g for generated): ")
    while True:
        if password_choice != "m" and password_choice != "g":
            password_choice= input("[!?] Sorry you selected a non existing choice please try again (m for manual password store or g for generated password store): ")
        if password_choice == "m":
            password = stdiomask.getpass("~ Enter the password: ").strip()
            check_user_password = stdiomask.getpass("~ Please confirm the password to make sure: ").strip()
            while check_user_password != password:
                print()
                print("[!] Sorry the password you entered doesn't match the previuos one!!")
                password = stdiomask.getpass("~ Re-nter the password: ").strip()
                check_user_password = stdiomask.getpass("~ Please confirm the password to make sure: ").strip()
            break
        if password_choice == "g":
            lengthOfPassword = input("[?] How much do you want the length of the password? ")
            password = generate_password(int(lengthOfPassword))
            print(f"# The generated password is {password}")
            break
    url = input("~ Enter a url: ").strip()
    # with connection make us not need the connection.commit() to save the data into database each time
    with connection:
        command.execute("INSERT INTO passwords VALUES (:ServiceName, :UserName, :Password, :URL)",{'ServiceName': service_name, 'UserName': user_name, 'Password': password, 'URL': url})


# Function 3: Search for a password entry using the service name:
def search_by_servicename():
    wanted_service = input("> Enter a service name: ").strip()
    command.execute("SELECT * FROM passwords WHERE servicename = :ServiceName", {'ServiceName': wanted_service})
    result = command.fetchone()
    if result is None:
        print("Service is not Found!")
        choice = input("[?] Do you want to make an entry for it? [y/n]: ").strip().lower()
        if choice == "y":
            insert_entry()
    else:
        result_table = Texttable()
        result_table.add_row(result)
        print(result_table.draw())
        print()
        signin = input("[?] Do you want to sign in? [y/n]: ").strip().lower()
        if signin == "y":
            auto_login(result)


# Function 4: Update the username of a password entry: 
def update_username():
    print()
    service_name = input ("> What is the service that you want to change it's username? ").strip()
    new_username = input ("> What is the new username? ").strip()
    # with connection make us not need the connection.commit() to save the data into database each time
    with connection:
        command.execute("""
        UPDATE passwords SET username = :UserName
        WHERE servicename = :ServiceName""",
        {'ServiceName': service_name, 'UserName': new_username}
        )


# Function 5: Update the password of a password entry: 
def update_password():
    print()
    service_name = input ("> What is the service that you want to change it's password? ").strip()
    password_choice = input("[?] Do you want to enter the password manually or get a generated one? (m for manual or g for generated): ")
    while True:
        if password_choice != "m" and password_choice != "g":
            password_choice= input("[!?] Sorry you selected a non existing choice please try again (m for manual password store or g for generated password store): ")
        if password_choice == "m":
            new_password = stdiomask.getpass("~ Enter the new password: ").strip()
            check_new_password = stdiomask.getpass("~ Please confirm the password to make sure: ").strip()
            while check_new_password != new_password:
                print()
                print("[!] Sorry the password you entered doesn't match the previuos one!!")
                new_password = stdiomask.getpass("~ Re-nter the password: ").strip()
                check_new_password = stdiomask.getpass("~ Please confirm the password to make sure: ").strip()
            break
        if password_choice == "g":
            lengthOfPassword = input("[?] How much do you want the length of the password? ")
            new_password = generate_password(int(lengthOfPassword))
            print(f"# The generated password is {new_password}")
            break
    # with connection make us not need the connection.commit() to save the data into database each time
    with connection:
        command.execute("""
        UPDATE passwords SET password = :Password
        WHERE servicename = :ServiceName""",
        {'ServiceName': service_name, 'Password': new_password}
        )


# Function 6: Remove a password entry: 
def remove_entry():
    wanted_entry = input("> What is the entry (service) that you want to remove? ").strip()
    # with connection make us not need the connection.commit() to save the data into database each time
    with connection:
        command.execute("DELETE FROM passwords WHERE servicename= :ServiceName",{'ServiceName': wanted_entry})


# Function 7: Display all entries:
def print_data():
    command.execute("SELECT * FROM passwords ORDER BY ServiceName")
    entries = command.fetchall()
    header= ["Service Name", "User Name", "Password", "URL"]
    # we call Texttable in a variable called passwords_table 
    passwords_table = Texttable()
    # adding the headers
    passwords_table.add_row(header)
    # adding the passwords entries
    for entry in entries:
        passwords_table.add_row(entry)
    # printing the header and passwords entries in a tabular format
    print(passwords_table.draw())


# Function 8: Wipe and start over again with a new database:
def wipe_database():
    with connection:
        command.execute("DROP TABLE passwords")
    command.execute("""
        CREATE TABLE passwords(
        ServiceName TEXT,
        UserName TEXT,
        Password TEXT,
        URL TEXT) 
        """)
    print("[!] The table is now empty...")