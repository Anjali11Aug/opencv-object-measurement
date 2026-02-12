import cv2
import numpy as np

img = cv2.imread('images\sample2.jpg')

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

contours, _ = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

for cnt in contours:
    area = cv2.contourArea(cnt)

    if area < 500:  # ignore noise
        continue

    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(
        img, f"{int(area)}",
        (x, y - 5),
        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
        (0, 0, 255), 2
    )


def resize_with_aspect_ratio(image, width=None, height=None):
    h, w = image.shape[:2]

    if width is None and height is None:
        return image

    if width is not None:
        ratio = width / w
        dim = (width, int(h * ratio))
    else:
        ratio = height / h
        dim = (int(w * ratio), height)

    return cv2.resize(image, dim)


# Resize for display
output = resize_with_aspect_ratio(img, width=900)

cv2.imshow("Object Areas", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
