import mediapipe as mp
import cv2


class Controller:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.mp_holistic = mp.solutions.holistic
        self.cap = cv2.VideoCapture(0)
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5,
                                      min_tracking_confidence=0.5)

    def formatImage(self, image):
        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        return image

    def classifyPose(self, results):
        def getJoint(joint_name):
            return results.pose_landmarks.landmark[self.mp_pose.PoseLandmark[joint_name]]
        if(getJoint("NOSE").y < 0.1):
            print("jump")
            return -1
        elif(getJoint("NOSE").y > 0.7):
            print("duck")
            return -2

        if(getJoint("LEFT_HIP").x < 0.4):
            print("left")
            return 0
        elif(getJoint("LEFT_HIP").x < 0.7):
            print("middle")
            return 1
        else:
            print("right")
            return 2
        return 1

    def renderFeedback(self, image, results):
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        self.mp_drawing.draw_landmarks(
            image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        cv2.imshow('camera', image)
        cv2.waitKey(3)
