import cv2

def resize(image, width=None, height=None):
    h, w = image.shape[:2]

    if width is None and height is None:
        return image

    if width is not None:
        ratio = width / float(w)
        dim = (width, int(h * ratio))
    else:
        ratio = height / float(h)
        dim = (int(w * ratio), height)

    return cv2.resize(image, dim)

def rotate(image, angle):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, matrix, (w, h))

def flip(image, direction):
    if direction == "horizontal":
        return cv2.flip(image, 1)
    elif direction == "vertical":
        return cv2.flip(image, 0)
    elif direction == "both":
        return cv2.flip(image, -1)
    else:
        return image

def crop(image, y1, y2, x1, x2):
    return image[y1:y2, x1:x2]