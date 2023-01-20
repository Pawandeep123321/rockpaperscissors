import streamlit as st
import cv2

st.set_page_config(page_title="Rock-Paper-Scissors Game", page_icon=":guardsman:", layout="wide")

def rock_paper_scissors():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Create a dictionary of possible hand gestures
    choices = { 0: "Rock", 1: "Paper", 2: "Scissors" }

    # Create a dictionary of the winning hand gestures
    rules = { "Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper" }

    while True:
        _, frame = cap.read()

        # Show the webcam feed on the Streamlit app
        st.image(frame, caption="Webcam Feed", use_column_width=True)

        # Get the user's choice
        choice = st.selectbox("Make your choice:", list(choices.values()))

        # Get the computer's choice
        computer_choice = choices[cv2.getNumberOfCPUs() % 3]

        # Display the results
        if choice == computer_choice:
            st.write("It's a tie!")
        elif rules[choice] == computer_choice:
            st.write("You win!")
        else:
            st.write("You lose!")

        # Add a button to start the game again
        if st.button("Play Again?"):
            pass

rock_paper_scissors()
