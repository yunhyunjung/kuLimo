import rospy
from std_msgs.msg import String

def main():
    rospy.init_mode('hello', anonymous=True)
    pub = rospy.Publisher('message', String, queue_size=10)
    data = String()
    i =0
    data.data = f"hello,ROS1 netic {i}"
    pub.publish()
    print("hello Ros")

if __name__ == "__main__":
    main()
