"""
Audio functions for eigen
"""

import pygame

N_CHN = 10

pygame.mixer.init()
pygame.mixer.set_num_channels(N_CHN)
channels = []

# Init songs
songs = []
SONGS = ["hisnare",
         "closehihat",
         "kick",
         "scratch",
         "distortedkick23",
         "bassdrum71"]

bpms = []
pause = []

for song in SONGS:
    songs.append(pygame.mixer.Sound("../sounds/" + song + ".wav"))
    bpms.append(30)
    pause.append(0)

# Init channels
for i in range(N_CHN):
    channels.append(pygame.mixer.Channel(i))


def pause_channel(channel_id):
    """Pause channel
    """

    channels[channel_id].pause()

    
def play_channel(channel_id):
    """Play channel
    """

    channels[channel_id].play()

    
def change_vol(channel_id, vol):
    """Change volume of channel
    """

    channels[channel_id].set_volume(vol)
