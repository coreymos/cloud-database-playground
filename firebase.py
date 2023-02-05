import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Reference to the Json key file
cred = credentials.Certificate('keys/cloud_key.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cloud-playground-e59e9-default-rtdb.firebaseio.com/'
})

# Default Data Structure
default = {
    'dhon': {
        'date_of_birth': 'August 17, 2000',
        'eye_color': 'Blue',
        'full_name': 'Derek Hon'
    },
    'tribano': {
        'date_of_birth': 'July 21, 2000',
        'eye_color': 'Green',
        'full_name': 'Tanner Banore',
        'height': '6 foot, 5 inches'
    },
    'derkon': {
        'date_of_birth': 'February 29, 2004',
        'eye_color': 'Brown',
        'full_name': 'Derek Henry',
        'hair_color': 'Blonde'
    }
}

# Save data
ref = db.reference('py/')
users_ref = ref.child('users')
users_ref.set(default)

# Interface loop
interacting = True
while (interacting):

    # Menu interface
    menu = int(input("1. Add a user\n2. Add a key value pair to a user\n3. Delete a user\n" +
    "4. Modify a username\n5. Delete all users\n6. Display all users and attributes\n7. Exit interface\n> "))

    # Adds a user to the data structure
    if menu == 1:
        hopper_ref = db.reference('py/users')
        new_user = input("Enter a new username: ")
        name = input("Enter full name: ")
        hopper_ref.update({
            new_user: {'full_name': name}
        })
    
    # Options 2, 3, 4 all require a user selection.
    elif (menu == 2) or (menu == 3) or (menu == 4):
        users_dict = ref.get('py/users/')

        count = 1
        array = []

        # Prints a list of all users.
        for user_key in users_dict[0]['users']:
            print(f"{count}. ", end='')
            print(user_key)
            array.append(user_key)
            count += 1

        selection = int(input("Select a user by typing in an integer: ")) - 1
        
        # Insert a key value pair into the selected user's dict.
        if menu == 2:
            print (users_dict[0]['users'][array[selection]])
            hopper_ref = users_ref.child(array[selection])
            update_key = input("Enter a key to add to this user: ")
            update_value = input("Enter a value to add to this key: ")
            hopper_ref.update({
                update_key: update_value
            })
        
        # Deletes selected user.
        elif menu == 3:
            delete_ref = users_ref.child(array[selection]).delete()
        
        # Selected username is deleted and replaced with new inputted username.
        elif menu == 4:
            modify_ref = db.reference('py/users/')
            attribute_ref = users_ref.child(array[selection])
            attributes = attribute_ref.get()
            delete_ref = users_ref.child(array[selection]).delete()
            update_user = input("Enter a new username for this user: ")
            modify_ref.update({
                update_user: attributes
            })
    
    # Deletes all of the users from the database.
    elif menu == 5:
        users_dict = db.reference('py/users/')
        users_dict.delete()

    # Displays all of the users and attributes to the screen.
    elif menu == 6:
        print(ref.get())

    # Exits the loop and ends the interface.
    elif menu == 7:
        interacting = False
