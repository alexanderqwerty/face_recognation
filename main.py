import cv2
import face_recognition

n = 8
n_by = 1 / n

if __name__ == '__main__':
    capture = cv2.VideoCapture("http://192.168.0.16:8080/video")
    while True:
        frame = capture.read()[1]
        rgb_frame = frame[:, :, ::-1]
        small_frame = cv2.resize(frame, (0, 0), fx=n_by, fy=n_by)
        rgb_small_frame = small_frame[:, :, ::-1]
        faces = face_recognition.face_locations(rgb_small_frame)
        for face_location in faces:
            top, right, bottom, left = face_location
            top *= n
            right *= n
            bottom *= n
            left *= n
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()
