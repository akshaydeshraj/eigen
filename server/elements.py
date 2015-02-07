"""
Audio elements with beats
"""

import time
from audio import bpms, pause
from thread import start_new_thread as snt

def play(channel, song, beat_id):
    """
    Play the given element.
    Open this in threads.
    """

    while True:
        if pause[beat_id] == 0:
            snt(_play, (channel, song))
            # channel.play(song)
            time.sleep(60.0 / bpms[beat_id])
        else:
            continue


def _play(channel, song):
    channel.play(song)


def play_once(channel, song):
    """
    Play the given element once.
    """

    snt(_play, (channel, song))
