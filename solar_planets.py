import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255))
cv2.putText(img,
            "Mercury",
            (100,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Venus",
            (180,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Earth",
            (280,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Mars",
            (380,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Jupiter",
            (520,70),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255))
cv2.putText(img,
            "Saturn",
            (760,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.75,
            (255,255,255))
cv2.putText(img,
            "Uranus",
            (960,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.75,
            (255,255,255))
cv2.putText(img,
            "Neptune",
            (1080,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.75,
            (255,255,255))










cv2.imshow("output",img)
cv2.waitKey(0)