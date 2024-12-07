import cv2
import numpy as np

# Global variables to track mouse drag position and ROI selection
dragging = False
selecting_roi = False
start_x, start_y = -1, -1
roi = None

# Image and the ROI list
image = cv2.imread("./frame_564.jpg")  # Replace with the correct image path
height, width, _ = image.shape
window_name = "Image Viewer"

# Create a window to show the image
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)


# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global dragging, selecting_roi, start_x, start_y, image, temp_image, roi

    # Right mouse button: Start dragging to scroll the image
    if event == cv2.EVENT_RBUTTONDOWN:
        dragging = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if dragging:
            dx = x - start_x
            dy = y - start_y
            # Translate the image to simulate scrolling
            M = np.float32([[1, 0, dx], [0, 1, dy]])
            temp_image = cv2.warpAffine(image, M, (width, height))
            start_x, start_y = x, y
            # Display the modified image (scrolling effect)
            cv2.imshow(window_name, temp_image)

        elif selecting_roi:
            # Draw the ROI while moving the mouse with the left button pressed
            temp_image = image.copy()
            cv2.rectangle(temp_image, (start_x, start_y), (x, y), (0, 255, 0), 2)
            cv2.imshow(window_name, temp_image)

    elif event == cv2.EVENT_LBUTTONDOWN:
        # Left mouse button: Start selecting ROI
        selecting_roi = True
        start_x, start_y = x, y
        # Print pixel position when clicked
        print(f"Left Button Clicked at ({x}, {y})")

    elif event == cv2.EVENT_LBUTTONUP:
        # Left mouse button: End selecting ROI
        selecting_roi = False
        roi = (start_x, start_y, x, y)  # Store the coordinates of the selected ROI
        print(f"Selected ROI: {roi}")
        cv2.rectangle(temp_image, (start_x, start_y), (x, y), (0, 255, 0), 2)
        cv2.imshow(window_name, temp_image)

    elif event == cv2.EVENT_RBUTTONUP:
        # Right mouse button: End dragging
        dragging = False
        start_x, start_y = -1, -1
        # Print pixel position when right-click is released
        print(f"Right Button Released at ({x}, {y})")


# Set mouse callback function
cv2.setMouseCallback(window_name, mouse_callback)

# Display the original image
temp_image = image.copy()
cv2.imshow(window_name, temp_image)

# Wait for key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
