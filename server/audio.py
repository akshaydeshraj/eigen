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
SONGS = ["../sounds/hisnare.wav", "../sounds/mono.wav"]

for song in SONGS:
    songs.append(pygame.mixer.Sound(song))

# Init channels
for i in range(N_CHN):
    channels.append(pygame.mixer.Channel(0))


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
