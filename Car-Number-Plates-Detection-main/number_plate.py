# import cv2

# harcascade = "model/haarcascade_russian_plate_number.xml"

# cap = cv2.VideoCapture(0)

# cap.set(3, 640) # width
# cap.set(4, 480) #height

# min_area = 500
# count = 0

# while True:
#     success, img = cap.read()

#     plate_cascade = cv2.CascadeClassifier(harcascade)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

#     for (x,y,w,h) in plates:
#         area = w * h

#         if area > min_area:
#             cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
#             cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

#             img_roi = img[y: y+h, x:x+w]
#             cv2.imshow("ROI", img_roi)


    
#     cv2.imshow("Result", img)

#     if cv2.waitKey(1) & 0xFF == ord('s'):
#         cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
#         cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
#         cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
#         cv2.imshow("Results",img)
#         cv2.waitKey(500)
#         count += 1





import cv2

# Path to the Haar Cascade file
harcascade = "model/haarcascade_russian_plate_number.xml"

# Ask the user for the image path
image_path = input("Enter the path to the image: ")

# Load the image
img = cv2.imread(image_path)

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not read the image. Please check the path and try again.")
    exit()

# Minimum area of the detected plate
min_area = 500
count = 0

# Load the Haar Cascade for license plate detection
plate_cascade = cv2.CascadeClassifier(harcascade)

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect plates in the image
plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

# Loop through detected plates
for (x, y, w, h) in plates:
    area = w * h

    if area > min_area:
        # Draw a rectangle around the detected plate
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

        # Extract the region of interest (ROI)
        img_roi = img[y: y + h, x: x + w]
        cv2.imshow("ROI", img_roi)

# Display the result
cv2.imshow("Result", img)

# Wait for the user to save the plate
if cv2.waitKey(0) & 0xFF == ord('s'):
    # Save the ROI
    cv2.imwrite("plates/scanned_img_" + str(count) + ".jpg", img_roi)
    print(f"Plate saved as scanned_img_{count}.jpg in the 'plates' folder.")
    count += 1

# Close all OpenCV windows
cv2.destroyAllWindows()
