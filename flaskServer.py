#Raspberry pi bell 

import os
from flask import Flask, render_template
from flask.ext.triangle import Triangle

app = Flask(__name__, static_path='/static')
Triangle(app)

@app.route('/')
def hello_world():
    return render_template('index.html') 

@app.route('/bell')
def play_bell():
    for x in range(5):
        #os.system('omxplayer -o local music/Old-fashioned-doorbell.mp3')	
    	#os.system('omxplayer -o local music/door-bell.mp3')	
    	os.system('omxplayer -o local music/ding-dong.mp3')	
    	os.system('omxplayer -o local music/match5.wav')	
    	os.system('omxplayer -o local music/match0.wav')	
    #os.system('omxplayer -o local music/match1.wav')	
    #os.system('omxplayer -o local music/match2.wav')	
    #os.system('omxplayer -o local music/match3.wav')	
    #os.system('omxplayer -o local music/match4.wav')	
    return 'Done' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug='True', use_reloader=True)
 
