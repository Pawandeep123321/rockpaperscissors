import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="Rock Paper Scissors", page_icon=":guardsman:", layout="wide")

# Create a function to process the webcam image
def process_image(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the hand using a Haar cascade classifier
    hand_cascade = cv2.CascadeClassifier("hand.xml")
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw a rectangle around the hand
    for (x, y, w, h) in hands:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    return img

# Create a function to determine the hand gesture
def get_hand_gesture(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use thresholding to segment the hand
    ret, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find the contours of the hand
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Determine the number of fingers based on the number of defects
    defects = cv2.convexityDefects(contours[0], hierarchy[0])
    if defects is not None:
        fingers = 0
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(contours[0][s][0])
            end = tuple(contours[0][e][0])
            far = tuple(contours[0][f][0])
            fingers += 1

    # Determine the hand gesture based on the number of fingers
    if fingers == 0:
        gesture = "rock"
    elif fingers == 1:
        gesture = "scissors"
    else:
        gesture = "paper"

    return gesture

# Create the main function
def main():
    st.title("Rock Paper Scissors")

    # Create a button to start the webcam
    if st.button("Start webcam"):
        # Open the webcam
        cap = cv2.VideoCapture(0)

        while True:
            # Get the webcam image
            ret, frame = cap.read()

            # Process the image
            processed_img = process_image(frame)

            # Display the processed image
# Release the webcam and close the window
cv2.release()
cv2.destroyAllWindows()
