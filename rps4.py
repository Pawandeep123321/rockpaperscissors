import cv2
import numpy as np

app= Flask(__name__)

# Load the cascade for hand gesture recognition
hand_cascade = cv2.CascadeClassifier('hand.xml')

# Define the choices for the game
choices = {0: 'rock', 1: 'paper', 2: 'scissors'}

# Start the webcam
cap = cv2.VideoCapture(0)

def generate_frames():
        while True:
            
            # Read a frame from the webcam
            success, frame = cap.read()
            if not success:
                break:

            else:
                ret,buffer=cv2.imencode('.jpg',frame)
                frame=buffer.tobytes()

            yield((b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect hands in the frame
            hands = hand_cascade.detectMultiScale(gray, 1.1, 5)

            # Draw a rectangle around the hand
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Show the webcam feed
            cv2.imshow('Webcam', frame)

            # Check if the user has made a gesture
            if len(hands) > 0:
                # Get the user's choice
                choice = np.random.randint(0, 3)

                # Print the user's choice
                print(f'You chose {choices[choice]}')

                # Compare the user's choice to the computer's choice
                computer_choice = np.random.randint(0, 3)
                if choice == computer_choice:
                    print("It's a tie!")
                elif (choice == 0 and computer_choice == 2) or \
                     (choice == 1 and computer_choice == 0) or \
                     (choice == 2 and computer_choice == 1):
                    print('You win!')
                else:
                    print('You lose!')

            # Check if the user wants to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)


# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
