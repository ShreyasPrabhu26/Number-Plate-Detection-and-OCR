import cv2

# Path for Harcascade Model
harcascade = "model/haarcascade_russian_plate_number.xml"

# Initiate OpenCV Window

# Read Primary Camara
capture = cv2.VideoCapture(0)

# Seting window hight and width
capture.set(3, 640)  # (3)width
capture.set(4, 480)  # (4)height

# Initialize the minimum area
minArea = 500

while True:
    sucess, frame = capture.read()

    # Check if the frame was read successfully
    if not sucess:
        print("Error: Could not read frame.")
        break

    # Load Cascade File
    plateCascade = cv2.CascadeClassifier(harcascade)

    # Convert Image to Grey
    greyImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get Plate Coordinates
    plateCoordinates = plateCascade.detectMultiScale(greyImage, 1.1, 4)

    # print(plateCoordinates)

    for (x, y, w, h) in plateCoordinates:
        # Calculate the plate Area
        detectedArea = w*h

        if detectedArea > minArea:
            # Plate-Color -->{RGB}= 0,255,0
            # Thickness -> 2
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Show Number Plate Text on top of Plate
            cv2.putText(frame, "Number Plate", (x, y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

    cv2.imshow("Result", frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close the OpenCV window
capture.release()
cv2.destroyAllWindows()
