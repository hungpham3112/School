import cv2
from fer import FER

detector = FER()

def detect_expression(image):
    face_info = detector.detect_emotions(image)
    if face_info:
        bounding_box = face_info[0]["box"]
        cv2.rectangle(image, (
            bounding_box[0], bounding_box[1]),
            (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
            (0, 155, 255), 2)

        emotion_name = detector.top_emotion(image)[0]

        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size, _ = cv2.getTextSize(emotion_name, font, 0.5, 1)

        cv2.putText(image, emotion_name,
                    (bounding_box[0], bounding_box[1] - 10),
                    font, 0.9, (0, 255, 0), 2)

    return image
