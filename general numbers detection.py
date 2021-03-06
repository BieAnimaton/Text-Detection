import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\User\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('images\\book2.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(pytesseract.image_to_string(img))

### Detecting Words
hImg, wImg, _ = img.shape
conf = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(imgGray, config=conf)
print('-' * 80)
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()


        try:
           print(b[11], end=" ")
        except IndexError:
            continue

        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
            cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

print('\n')
print('-' * 80)

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