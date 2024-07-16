import speech_recognition as sr
import pyttsx3
import cv2
import time

# Function to be executed when "record" is recognized
def record_video(duration=5):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    out = cv2.VideoWriter(f'recorded_video_{timestamp}.avi', fourcc, 20.0, (640, 480))

    start_time = time.time()
    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            print("Error: Frame capture failed.")
            break
        out.write(frame)
        cv2.imshow('Recording...', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video recording saved as recorded_video_{timestamp}.avi")

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized: {text}")

            if "record" in text:
                record_video(duration=5)  # Record for 5 seconds (adjust as needed)

    except sr.UnknownValueError:
        print("Could not understand audio")
        continue
    except sr.RequestError as e:
        print(f"Error with the service; {e}")
        break
    except Exception as e:
        print(f"Error: {e}")
