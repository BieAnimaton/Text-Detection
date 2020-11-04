import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\User\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('images\\book2.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(pytesseract.image_to_string(img))

### Detecting Characters
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    # print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 1)
    cv2.putText(img, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

resize = ResizeWithAspectRatio(img, width=640)

cv2.imshow('Result', resize)
cv2.waitKey(0)