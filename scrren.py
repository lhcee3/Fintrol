#pip install opencv-python mediapipe screen-brightness-control
import cv2
import mediapipe as mp
import screen_brightness_control as sbc


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)


prev_distance = None
brightness_change_threshold = 0.02

def calculate_finger_distance(landmarks):
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    return ((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)**0.5

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    
    image = cv2.flip(image, 1)

    
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    
    results = hands.process(rgb_image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            
            current_distance = calculate_finger_distance(hand_landmarks)

            if prev_distance is not None:
            
                distance_change = current_distance - prev_distance

                
                if abs(distance_change) > brightness_change_threshold:
                    current_brightness = sbc.get_brightness()[0]
                    new_brightness = current_brightness + (distance_change * 100)
                    new_brightness = max(0, min(100, new_brightness))
                    sbc.set_brightness(new_brightness)

            prev_distance = current_distance

    
    cv2.imshow('Hand Tracking', image)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()