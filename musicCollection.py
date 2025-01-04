class Song:  # Class to represent a song
    def __init__(self, title, artist):  # Initialize a song with title and artist
        self.title = title
        self.artist = artist

class User:  # Class to represent a user
    def __init__(self, name):  # Initialize a user with a name
        self.name = name
        self.collection = []   # Each user has a music collection, initialized as an empty list

    def add_song(self, title, artist):  # Method to add a song to the user's collection
        song = Song(title, artist)      # Create a new song instance
        self.collection.append(song)    # Add the song to the user's collection
        print(f"{title} by {artist} added to {self.name}'s collection")

    def retrieve_song(self, title):    # Method to retrieve song details by title
        for song in self.collection:
            if song.title.lower() == title.lower():    # Check if the song title matches
               return f" '{song.title}' is by {song.artist}."
        return "Song not found"

    def update_song(self, title, new_artist):   # Method to update the artist of a song
        for song in self.collection:
            if song.title.lower() == title.lower():   # Check if the song title matches
                song.artist = new_artist   # Update the artist for the song
                return f"Song '{song.title}' updated to artist {new_artist}."
        return "Song not found."

    def delete_song(self, title):  # Method to delete a song by title
        for song in self.collection:
            if song.title.lower() == title.lower():  # Check if the song title matches
                self.collection.remove(song)  # Remove the song from the collection
                return f"Song '{title}' deleted from {self.name}'s collection."
        return "Song not found."

    def display_songs(self):  # Method to display all songs in the user's collection
        if not self.collection:
            return f"No songs in {self.name}'s collection"

        result = f"List of songs in {self.name}'s collection:\n"
        for song in self.collection:
            result += f"- Title: {song.title}, Artist: {song.artist}\n"
        return result.strip()  # Return the list of songs as a formatted string


class MusicCollection:  # Class to manage the collection of users and songs
    def __init__(self):
        self.users = []  # Initialize an empty list of users
        self.current_user = None  # Initialize current user as None

    def add_user(self, name):  # Method to add a new user
        if any(user.name.lower() == name.lower() for user in self.users):  # Check if the user already exists
            print(f"User {name} already exists.")
            return

        user = User(name)  # Create a new User instance
        self.users.append(user)   # Add the new user to the list of users
        print(f"User {name} added")

        if not self.current_user:   # If no current user, set this one as current
            self.current_user = user

    def change_user(self):  # Method to change the current user
        # Check if there are any existing users
        if len(self.users) > 0:
            print("Select an existing user or type a new username to add.")

            for index, user in enumerate(self.users): #display existing users with their indicies
                print(f"{index + 1}) {user.name}")

            user_input = input(">>input (or type new username): ")

            if user_input.isdigit(): #if input is a number
                user_index = int(user_input) -1 #subtract 1 for zero based indexing
                if 0 <= user_index < len(self.users):   #check if user index is within range
                    selected_user = self.users[user_index]  #get current user

                    if selected_user.name.lower() == self.current_user.name.lower(): #check to see if you are already in the current user's selection
                        print(f"You're already in {self.current_user.name}'s collection")
                    else:
                        self.current_user = selected_user
                        print(f"User changed to user {self.current_user.name}") #change and inform user if
                    return

                else:   # If the input is a number but out of valid range, prompt again
                    print("Invalid user selection.")
                    return self.change_user()   # Recursively call the method to prompt again

            else:   # If input is not a number, assume it's a new username and add a new user
                return self.add_user(user_input)

        else:
            # If no users exist, prompt the user to add a new one
            user_input = input("No users found. Please add a new username: ")
            return self.add_user(user_input)


    def menu(self):  # Method to display the menu and handle user input
        while True:
            print("\n=== Menu ===")
            if self.current_user:
                print(f"== User {self.current_user.name} ==")

            print("1) Add user")   # Always show the option to add a user
            if len(self.users) > 1:
                print("2) Change User")  # Show change user option if multiple users exist

            if self.current_user:
                print("3) Add a song")   # Show add song option if a user is selected
            if self.current_user and self.current_user.collection:
                print("4) Retrieve song details")  # Show song management options if songs exist
                print("5) Update song details")
                print("6) Delete a song")
                print("7) Display all songs")

            print("0) Exit")   # Option to exit the program
            print("===============")

            try:
                choice = int(input(">>input: "))  # Get user choice

                if choice == 1:
                    name = input(">>input USerName: ")  # Input for new user name
                    self.add_user(name)

                elif choice == 2 and len(self.users) > 1:
                    self.change_user()

                elif choice == 3 and self.current_user:
                    title = input(">>input song title: ")  # Input for song title
                    artist = input(">>input song artist: ")  # Input for song artist
                    self.current_user.add_song(title, artist)

                elif choice == 4 and self.current_user and self.current_user.collection:
                    title = input("Enter a song title to retrieve: ")   # Input for retrieving song
                    print(self.current_user.retrieve_song(title))

                elif choice == 5 and self.current_user and self.current_user.collection:
                    title = input("Enter a song to update: ")  # Input for updating song
                    new_artist = input("Enter new Artist name: ")  # Input for new artist
                    print(self.current_user.update_song(title, new_artist))

                elif choice == 6 and self.current_user and self.current_user.collection:
                    title = input("Enter song title to delete: ")  # Input for deleting song
                    print(self.current_user.delete_song(title))

                elif choice == 7 and self.current_user  and self.current_user.collection:
                    print(self.current_user.display_songs())   # Display all songs


                elif choice == 0:
                    print("Exiting program.")  # Exit message
                    break

                else:
                    print("Invalid choice or no user selected.")   # Handle invalid choice
            except ValueError:
                print("Please enter a valid number.")  # Handle non-integer input




# Initialize the music collection and display the menu
music_collection = MusicCollection()
music_collection.menu()
