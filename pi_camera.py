import cv2

camera_no = 0 #Camera No.
window_title = "Window" #Window name

camera = cv2.VideoCapture(camera_no)


while True:
    ret, frame = camera.read()
    if not ret:
        break
    
    cv2.imshow(window_title, frame)
    key = cv2.waitKey(1)
    
    if key == 27: #Push Esc kye if you want to close the window.
        break
    
camera.release()
cv2.destroyAllWindows()