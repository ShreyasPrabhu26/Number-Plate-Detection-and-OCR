# For Number Plate detection
import cv2
# For OCR
from PIL import Image
import pytesseract

# Path for Harcascade Model
harcascade = "model/haarcascade_russian_plate_number.xml"

# Path for Pytesseract Engine
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Initiate OpenCV Window

# Read Primary Camara
capture = cv2.VideoCapture(0)

# Seting window hight and width
capture.set(3, 640)  # (3)width
capture.set(4, 480)  # (4)height

# Initialize the minimum area
minArea = 500

# Initialize the count for saving Croped Number Plate Portion
imageNumber = 1

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

            # Crop Coordinates of the Number Plate Portion
            NumberPlateFrameCoordinates = frame[y:y+h, x:x+w]
            cv2.imshow("NumberPlateFrame", NumberPlateFrameCoordinates)

    cv2.imshow("Number Plate Detecter", frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Saving Croped Number Plate Portion for OCR
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Save the croped image in the Local Folder
        cv2.imwrite("plateImages/scaned_img_" + str(imageNumber) +
                    ".jpg", NumberPlateFrameCoordinates)

        cv2.rectangle(frame, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)

        cv2.putText(frame, "Plate Saved", (150, 265),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)

        cv2.imshow("Results", frame)

        cv2.waitKey(500)

        # Open an image using Pillow (PIL)
        image_path = "plateImages/scaned_img_" + str(imageNumber)+".jpg"
        img = Image.open(image_path)

        # Perform OCR on the image
        text = pytesseract.image_to_string(img)
        output_file_path = 'extracted_text.txt'

        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(text)

        print(text)

        print(f'Text saved to {output_file_path}')

        imageNumber += 1


# Release the VideoCapture and close the OpenCV window
capture.release()
cv2.destroyAllWindows()
