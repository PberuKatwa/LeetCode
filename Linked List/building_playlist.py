class Song:
    def __init__(self,title):
        self.title = title
        self.next_song = None
        pass

song_1 = Song("Oath")
song_2 = Song("Mpishi")
song_3 = Song("Get Busy")
song_4 = Song("Bembeleza")

song_1.next_song = song_2
song_2.next_song = song_3
song_3.next_song = song_4

current_song = song_1

while current_song:
    print(f'Now Playing : {current_song.title} ')
    current_song = current_song.next_song