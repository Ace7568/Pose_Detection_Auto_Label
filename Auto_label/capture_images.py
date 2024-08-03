import cv2
import os
import time

def capture_images(output_dir, num_images, folder):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize video capture
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Loop to show camera feed until user input
    show_text = True
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the camera feed
        if show_text:
            cv2.putText(frame, "Press Q and esc to Capture", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Camera Feed", frame)

        # Check for user input
        key = cv2.waitKey(1) 
        
        if key == ord('q'):
            show_text = False  # Remove text when 'q' is pressed

        elif key == 27:  # 27 is the ASCII code for the Esc key
            break  # If Esc is pressed, exit the loop

    # Destroy the OpenCV window
    cv2.destroyWindow("Camera Feed")

    # Create a window for capturing feedback
    cv2.namedWindow("Capturing")

    # Loop to capture images
    for i in range(num_images):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if frame is captured successfully
        if not ret:
            print("Error: Could not capture frame.")
            break

        # Display feedback in the "Capturing" window
        feedback = f"Image {i+1}/{num_images} captured"
        cv2.putText(frame, feedback, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Capturing", frame)

        # Save the captured image
        folder_name = str(folder)
        image_dir = os.path.join(output_dir, folder_name)
        os.makedirs(image_dir, exist_ok=True)
        img_name = str(folder)+ "_" + str(i) + ".jpg"
        cv2.imwrite(os.path.join(image_dir, img_name), frame)

        print(f"Image {i+1}/{num_images} captured and saved as {img_name}")

        
        cv2.waitKey(50)  # Display the feedback for 500 milliseconds

    # Release the capturing window
    cv2.destroyWindow("Capturing")

    # Release the camera
    cap.release()
    print("Image capturing completed.")

if __name__ == "__main__":
    output_directory = "./captured_images"
    num_images = 500  # Number of images to capture

    # Start capturing images
    num_session = 3
    for session in range(num_session):
        capture_images(output_directory, num_images, 2)
