import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Add text for each planet
cv2.putText(img, "Earth", (280, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img, "Venus", (210, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Sun", (125, 370), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "marcury", (120, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Mars", (380, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Jupiter", (630, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Saturn", (780, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Uranus", (950, 330), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Neptune", (1150, 290), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

# Display the image
cv2.imshow("output", img)

# Wait for user input
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_systemwithname.jpg", img)
