import cv2


def getFrame(videoPath, svPath):
    cap = cv2.VideoCapture(videoPath)
    numFrame = 0
    n = 0
    while True:
        if cap.grab():
            flag, frame = cap.retrieve()
            if not flag:
                continue
            else:
                # cv2.imshow('video', frame)
                numFrame += 1
                if (numFrame % 10 == 0):
                    n = n + 1
                    if (n < 10):
                        newPath = svPath + "0000" + str(n) + ".png"
                    elif (n > 10 and n <= 99):
                        newPath = svPath + "000" + str(n) + ".png"
                    elif (n > 99 and n <= 999):
                        newPath = svPath + "00" + str(n) + ".png"
                    elif (n > 999 and n<=9999):
                        newPath = svPath + "0" + str(n) + ".png"
                    elif (n > 9999):
                        newPath = svPath + "" + str(numFrame) + ".png"
                    print(newPath)
                    cv2.imencode('.png', frame)[1].tofile(newPath)
        if cv2.waitKey(10) == 27:
            break


if __name__ == '__main__':
    getFrame("/Users/shencheng/PycharmProjects/graduationDesign/video/15.mp4",
             "/Users/shencheng/PycharmProjects/graduationDesign/img1/")
