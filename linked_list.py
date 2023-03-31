# Author: Supriya Bandal

# pylint: disable=too-few-public-methods
# Define a Song class to represent a single song in the playlist
class Song:
    """
    A class representing a song.

    Attributes:
        title (str): The title of the song.
        artist (str): The name of the artist who performed the song.
        next_song (Song): A reference to the next song in a playlist, if any.

    Methods:
        __init__(title, artist): Initializes a new Song object with the given title and artist.
    """

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next_song = None  # Reference to the next song in the playlist


# Define a Playlist class to represent the playlist
class Playlist:
    """
    A class representing a playlist of songs.

    Attributes:
        head (Song): A reference to the first song in the playlist.
        tail (Song): A reference to the last song in the playlist.
        current_song (Song): A reference to the song currently being played, or None if the playlist is not currently playing.

    Methods:
        add_song(title, artist): Adds a new song to the playlist with the given title and artist.
        play(): Plays the current song in the playlist.
        next(): Advances to the next song in the playlist.
        print_playlist(): Prints the list of songs in the playlist.
    """

    def __init__(self):
        self.head = None  # Reference to the first song in the playlist
        self.tail = None  # Reference to the last song in the playlist
        self.current_song = None  # Reference to the currently playing song

    # Method to add a new song to the end of the playlist
    def add_song(self, title, artist):
        """
        Adds a new song to the playlist with the given title and artist.

        Args:
            title (str): The title of the song.
            artist (str): The name of the artist who performed the song.

        Returns:
            None
        """
        new_song = Song(title, artist)  # Create a new Song object
        if self.head is None:  # If the playlist is empty
            self.head = new_song  # Set head to the new song
            self.tail = new_song  # Set tail to the new song
        else:  # Otherwise
            # Set the next_song reference of the current tail to the new song
            self.tail.next_song = new_song
            self.tail = new_song  # Set tail to the new song

    # Method to play the current song
    def play(self):
        """
        Plays the current song in the playlist. If no song is currently playing,
        the first song in the playlist will be played.

        Args:
            None

        Returns:
            None
            """
        if self.current_song is None:  # If no song is currently playing
            self.current_song = self.head  # Set current_song to the head of the playlist
        print("Playing:", self.current_song.title,
              "by", self.current_song.artist)

    # Method to move to the next song in the playlist
    def next(self):
        """
        Plays the next song in the playlist.

        Args:
            None

        Returns:
            None
        """
        if self.current_song is None:  # If no song is currently playing
            return
        # Set current_song to the next song in the playlist
        self.current_song = self.current_song.next_song

    # Method to print all the songs in the playlist
    def print_playlist(self):
        """
        Prints the title and artist of each song in the playlist.

        Args:
            None

        Returns:
            None
        """
        if self.head is None:  # If the playlist is empty
            print("Playlist is empty")
            return
        current = self.head  # Start at the head of the playlist
        while current is not None:  # While there are still songs in the playlist
            # Print the current song
            print(current.title, "by", current.artist)
            current = current.next_song  # Move to the next song in the playlist


# Creating a playlist
playlist = Playlist()

# Adding songs to the playlist
playlist.add_song("Stairway to Heaven", "Led Zeppelin")
playlist.add_song("Bohemian Rhapsody", "Queen")
playlist.add_song("Hotel California", "The Eagles")
playlist.add_song("November Rain", "Guns N' Roses")

# Playing the first song
playlist.play()

# Skipping to the next song
playlist.next()

# Printing the playlist
playlist.print_playlist()
