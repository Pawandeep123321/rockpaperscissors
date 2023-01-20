import streamlit as st
import cv2

# Function to capture webcam image
def capture_webcam():
    # Open webcam
    webcam = cv2.VideoCapture(0)

    # Get webcam image
    _, frame = webcam.read()

    # Close webcam
    webcam.release()

    # Return image
    return frame

# Main function
def main():
    st.title("Rock Paper Scissors Game")

    # Capture webcam image
    frame = capture_webcam()

    # Show webcam image
    st.image(frame)

    # Get user input for move
    move = st.selectbox("Select your move:", ["Rock", "Paper", "Scissors"])

    # Play game
    if move == "Rock":
        st.write("You selected Rock.")
    elif move == "Paper":
        st.write("You selected Paper.")
    else:
        st.write("You selected Scissors.")

if _name_ == "_main_":
    main()
