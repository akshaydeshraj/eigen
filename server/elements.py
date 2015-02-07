"""
Audio elements with beats
"""

import time

bpms = [60, 30, 10]
pause = [0, 0, 0]

def play(channel, song, beat_id):
    """
    Play the given element.
    Open this in threads.
    """

    while True:
        if pause[beat_id] == 0:
            channel.play(song)
            time.sleep(60.0 / bpms[beat_id])
        else:
            continue