## Note that there will be two seperate programs!!!!

**Progarm 1 => Number Plate Detection and OCR (Optical Character Recognition)**

**Program 2 => Parking-Space-Counter**

======================================================================================

## Installtion of Program-1
#Progarm 1 => Number Plate Detection and OCR (Optical Character Recognition)
🚗 This Python script detects number plates in a video stream, highlights them, and performs OCR to extract text from the detected number plates. 🚗

## Table of Contents

- [Installation](#installation)
- [Implementation](#implementation)

## Installation

1. **Clone the Repository**:

       git clone https://github.com/ShreyasPrabhu26/Number-Plate-Detection-and-OCR

2. **Install Dependencies**:

  - [OpenCV](https://pypi.org/project/opencv-python/): For capturing video frames and image processing.
  - [PyTesseract](https://pypi.org/project/pytesseract/): For OCR (Optical Character Recognition).
  - [Pillow (PIL)](https://pypi.org/project/Pillow/): For opening and processing images.

You can install these dependencies using `pip`:

       pip install -r requirements.txt

3. **Tesseract OCR Engine**:

  Download and install the Tesseract OCR engine from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki). Ensure that you set the correct path to the Tesseract executable (`pytesseract.pytesseract.tesseract_cmd`) in the script.

## Implementation

  1. **Run the Script**:

    python main.py

2. **Usage**:

  - The script captures video from the primary camera (you can adjust the camera source in the script).
  - Detected number plates are highlighted in green rectangles, and "Number Plate" text is displayed above them.
  - To save a detected number plate for OCR, press 's'.
  - OCR is performed on the saved number plate image, and the extracted text is saved to the `extracted_text.txt` file.
  - Press 'q' to exit the script.

3. **Output**:

  - The extracted text from the number plates is saved in `extracted_text.txt`.

4. **Enjoy!** 🚗

  Feel free to customize and extend this script to suit your specific needs. Happy coding! 😊👍

  =========================================================================================

## Program 2 => Parking Space Counter

First open the folder (Parking Space Counter) and install all the dependencies required to run these programs
2. **Install Dependencies**:

  - [OpenCV](https://pypi.org/project/opencv-python/): For capturing video frames and image processing.
  - [PyTesseract](https://pypi.org/project/pytesseract/): For OCR (Optical Character Recognition).
  - [Pillow (PIL)](https://pypi.org/project/Pillow/): For opening and processing images.
  - [cvzone](https://pypi.org/project/cvzone/): A computer vision library used for various computer vision tasks and utilities.

You can install these dependencies using `pip`:

       pip install -r requirements.txt

# Parking Space Picker

This Python script allows you to define and manage parking spaces in an image interactively.

## Usage

1. **[IMP]Run the script and allocate the Parking Space!**:

          python parkingSpacePicker.py
   
2 **Terminate the Program after defining Parking Space**

3.  **Run the Main Script**

          python main.py

4. **[OPTIOANL]Adjust the Parameter in the dialog Box**


   



  
