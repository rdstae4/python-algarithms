import math
import time

import cv2
import mediapipe as mp


class posedetector:
    def __init__(
        self, mode=False, upbody=False, smooth=True, detectioncon=0.5, trackCon=0.5
    ):
        self.mode = mode
        self.upbody = upbody
        self.smooth = smooth
        self.detectioncon = detectioncon
        self.trackCon = trackCon
        self.mpdraw = mp.solutions.drawing_utils
        self.mppose = mp.solutions.pose
        self.pose = self.mppose.Pose(
            self.mode, self.upbody, self.smooth, self.detectioncon, self.trackCon
        )

    def findpose(self, img, draw=True):
        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgrgb)
        if self.results.pose_landmarks:
            if draw:
                self.mpdraw.draw_landmarks(
                    img, self.results.pose_landmarks, self.mppose.POSE_CONNECTIONS
                )
        return img

    def findposition(self, img, draw=True):
        self.imlist = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.imlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.imlist


def main():
    cap = cv2.VideoCapture("PoseVideos/1.mp4")
    ptime = 0
    detector = posedetector()
    while True:
        success, img = cap.read()
        img = detector.findpose(img)
        imlist = detector.findposition(img, draw=False)
        if len(imlist) != 0:
            print(imlist[14])
            cv2.circle(img, (imlist[14][1], imlist[14][2]), 15, (0, 0, 255), cv2.FILLED)
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(
            img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3
        )
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
