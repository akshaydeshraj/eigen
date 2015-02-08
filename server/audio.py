"""
Audio functions for eigen
"""

import pygame

N_CHN = 15

pygame.mixer.init()
pygame.mixer.set_num_channels(N_CHN)
channels = []

# Init songs
songs = []
SONGS = ["hisnare",
         "closehihat",
         "hihat4",
         "kick",
         "distortedkick23",
         "bassdrum71",
         "cymbal",
         "effect",
         "",
         "background",
         "background2"]

bpms = []
pause = []

for song in SONGS:
    songs.append(pygame.mixer.Sound("../sounds/" + song + ".wav"))
    bpms.append(90)
    pause.append(0)

# Init channels
for i in range(N_CHN):
    channels.append(pygame.mixer.Channel(i))


# Initialize first song
# def play_background():
#    channels[10].play(songs[10])

    
def pause_channel(channel_id):
    """Pause channel
    """

    channels[channel_id].pause()

    
def play_channel(channel_id):
    """Play channel
    """

    channels[channel_id].play(songs[channel_id])

    
def change_vol(channel_id, vol):
    """Change volume of channel
    """

    channels[channel_id].set_volume(vol)
