import streamlit as st
import cv2
import numpy as np
import streamlit as st
import setuptools

setuptools.setup(
    name="streamlit-webcam-example",
    version="0.1.0",
    author="Tim Conkling",
    author_email="tim@streamlit.io",
    description="",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 0.73",
    ],
)

# Load the cascade for hand gesture recognition
hand_cascade = cv2.CascadeClassifier('hand.xml')

# Define the choices for the game
choices = {0: 'rock', 1: 'paper', 2: 'scissors'}

# Start the webcam

cap = cv2.VideoCapture(0)



while True:
    # Read a frame from the webcam
    _, frame = cap.read()

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

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
