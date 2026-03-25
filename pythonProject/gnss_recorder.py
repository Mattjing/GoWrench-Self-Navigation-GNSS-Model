{
 "cells": [
  {
   "cell_type": "code",
   "outputs": [],
   "source": [
    "#!/usr/bin/env python\n",
    "\n",
    "import rospy\n",
    "from sensor_msgs.msg import NavSatFix\n",
    "import rosbag\n",
    "\n",
    "class GNSSRecorder:\n",
    "    def __init__(self):\n",
    "        rospy.init_node('gnss_recorder', anonymous=True)\n",
    "        self.bag = rosbag.Bag('gnss_data.bag', 'w')\n",
    "        rospy.Subscriber('/piksi/navsatfix_best_fix', NavSatFix, self.callback)\n",
    "        rospy.loginfo(\"Recording GNSS data to gnss_data.bag\")\n",
    "\n",
    "    def callback(self, data):\n",
    "        rospy.loginfo(f\"Received GNSS data: {data}\")\n",
    "        self.bag.write('/piksi/navsatfix_best_fix', data)\n",
    "\n",
    "    def run(self):\n",
    "        rospy.spin()\n",
    "        self.bag.close()\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    try:\n",
    "        recorder = GNSSRecorder()\n",
    "        recorder.run()\n",
    "    except rospy.ROSInterruptException:\n",
    "        pass\n"
   ],
   "metadata": {
    "collapsed": false
   },
   "id": "d940a543805ab936"
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
