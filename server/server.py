from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
	return 'Welcome'

@app.route('/toggle')
def api_toggle():
   # Toggle the state of the player
   return 'state changed'    

@app.route('/volume/<volume_value>')
def api_volume(volume_value):
	# Adjusts volume of the player
	return 'Volume is now ' + volume_value

if __name__ == '__main__':
    app.run(debug=True)