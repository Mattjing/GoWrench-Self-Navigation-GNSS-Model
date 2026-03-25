#!/usr/bin/env python
import rospy
from sensor_msgs.msg import NavSatFix
import json
from flask import Flask, render_template

app = Flask(__name__)
coordinates = {'latitude': 0.0, 'longitude': 0.0}

@app.route('/')
def index():
    return render_template('index.html', api_key='AIzaSyBJXqeYsRZaNtO2B5YilmMUBG30cdT0JfQ', lat=coordinates['latitude'], lon=coordinates['longitude'])

def callback(data):
    global coordinates
    coordinates['latitude'] = data.latitude
    coordinates['longitude'] = data.longitude

def listener():
    rospy.init_node('gnss_listener', anonymous=True)
    rospy.Subscriber("/piksi_rover/navsatfix_best_fix", NavSatFix, callback)
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    listener()