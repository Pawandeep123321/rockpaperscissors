import cv2
import numpy as np

app= Flask(__name__)
def generate_frames():
        cap = cv2.VideoCapture(0)
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


def play_game():
    # Open the webcam
    #cap = cv2.VideoCapture(0)

    while True:
        # Capture an image from the webcam
        #success, frame = cap.read()
        

        # Convert the image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Identify the hand gesture
        hand_gesture = identify_gesture(gray)

        # Determine the move based on the hand gesture
        move = determine_result(hand_gesture)

        if move == 'rock' or move == 'paper' or move == 'scissors':
            # Play the game
            result = play(move)
            print(f'You chose {move}. The computer chose {result["computer"]}. {result["winner"]}')
            break
        else:
            print("Invalid move. Please show either 'rock', 'paper', or 'scissors'.")

def identify_gesture(image):
    # Use image processing techniques to identify the hand gesture
    # ...
    return hand_gesture

def determine_result(hand_gesture):
    # Determine the move based on the hand gesture
    if hand_gesture == 'rock':
        return 'rock'
    elif hand_gesture == 'paper':
        return 'paper'
    elif hand_gesture == 'scissors':
        return 'scissors'
    else:
        return None

def play(player_move):
    # Play the game and determine the winner
    computer_move = random.choice(['rock', 'paper', 'scissors'])
    if player_move == computer_move:
        winner = "It's a tie!"
    elif (player_move == 'rock' and computer_move == 'scissors') or (player_move == 'paper' and computer_move == 'rock') or (player_move == 'scissors' and computer_move == 'paper'):
        winner = "You win!"
    else:
        winner = "You lose."
    return {"computer": computer_move, "winner": winner}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)


if __name__ == '__main__':
    play_game()
