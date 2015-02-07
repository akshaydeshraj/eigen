from flask import Flask, url_for , request
app = Flask(__name__)

@app.route('/')
def api_root():
	return 'Welcome'

# Deprecated

# @app.route('/toggle')
# def api_toggle():
#    # Toggle the state of the player
#    return 'state changed'    

# @app.route('/volume/<volume_value>')
# def api_volume(volume_value):
# 	# Adjusts volume of the player
# 	return 'Volume is now ' + volume_value

@app.route('/start/<tone_id>')
def api_start_tone(tone_id):
	# Start the tone 
	return 'Started Playing ' + tone_id

@app.route('/stop/<tone_id>')
def api_stop_tone(tone_id):
	# Stop the tone 
	return 'Stopped Playing ' + tone_id	

@app.route('/beat/<tone_id>' , methods=['POST'])
def api_change_beat(tone_id):
	return 'Changed beat of ' + tone_id + ' to ' + request.form['value']

@app.route('/volume/<tone_id>' , methods=['POST'])
def api_change_volume(tone_id):
	return 'Changed Volume of ' + tone_id + ' to ' + request.form['value']
		
if __name__ == '__main__':
    app.run(debug=True)