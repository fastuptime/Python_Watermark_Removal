import cv2
import numpy as np

img = cv2.imread("test.jpg")
new = 2.0 * img + -160
new = np.clip(new, 0, 255).astype(np.uint8)
cv2.imwrite("test_new.png", new)
