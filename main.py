import cv2

# Path for Harcascade Model
harcascade = "model/haarcascade_russian_plate_number.xml"

# Initiate OpenCV Window

# Read Primary Camara
capture = cv2.VideoCapture(0)

# Seting window hight and width
capture.set(3, 640)  # (3)width
capture.set(4, 480)  # (4)height

while True:
    sucess, image = capture.read()

    # Check if the frame was read successfully
    if not sucess:
        print("Error: Could not read frame.")
        break

    # Convert Image to Grey
    greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
