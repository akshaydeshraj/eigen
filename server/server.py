"""
Server for communicating with the sound module
"""

from flask import Flask, request
app = Flask(__name__)
from thread import start_new_thread
import elements as e
import audio as a


@app.route('/')
def api_root():
    return "I am working."


@app.route("/start/<tone_id>")
def api_start_loops(tone_id):
    tone_id = int(tone_id)
    start_new_thread(e.play, (a.channels[tone_id], a.songs[tone_id], tone_id))
    return "ok"


@app.route('/play/<tone_id>')
def api_play_tone(tone_id):
    a.play_channel(int(tone_id))
    e.pause[int(tone_id)] = 0
    return "ok"


@app.route('/pause/<tone_id>')
def api_pause_tone(tone_id):
    a.pause_channel(int(tone_id))
    e.pause[int(tone_id)] = 1
    return "ok"


@app.route('/beat/<tone_id>', methods=['POST'])
def api_change_beat(tone_id):
    # Change the beats per minute of given id.
    e.bpms[int(tone_id)] = int(request.form["value"])
    return "ok"


@app.route('/volume/<tone_id>', methods=['POST'])
def api_change_volume(tone_id):
    # Change the volume of given id.
    print float(request.form["value"])
    a.channels[int(tone_id)].set_volume(float(request.form["value"]))
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
