Author: Supriya Bandal

YouTube link:  https://www.youtube.com/watch?v=28d6Xqf8evE&t=83s

## Real world example where we will create a `Song Playlist` in Python and implement a `Linked list` data structure.

# In this example, we have a `Song class` that represents a single song in the playlist. 
-> Each Song object has a `title` attribute to store the title of the song, an `artist` attribute to store the artist who performs the song. 
-> A `next_song` attribute to point to the next song in the playlist.

# The `Playlist class` represents the playlist itself. 
->It has a `head` attribute that points to the first song in the playlist, a `tail` attribute that points to the last song in the playlist.
-> A `current_song` attribute that points to the song currently being played. 
-> The `add_song` method adds a new song with the given title and artist to the end of the playlist.
-> The `play` method plays the current song. 
-> The `next` method moves to the next song in the playlist.
-> The `print_playlist` method prints out the titles and artists of all the songs in the playlist.
