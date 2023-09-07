import cv2
#Función asociada a la barra deslizante
def nada(x):
    pass

#Cargarlas imágenes
img1 = cv2.imread("Galapagos.jpg")
img2 = cv2.imread("Cotopaxi.jpg")

#Crear una ventana y la barra deslizante
cv2.namedWindow("BarraDeslizante")
cv2.createTrackbar("Porcentaje", "BarraDeslizante", 20, 100, nada)
cv2.createTrackbar("Gamma", "BarraDeslizante", 0, 100, nada)

while True:
    alpha = cv2.getTrackbarPos('Porcentaje', 'BarraDeslizante') / 100
    betha = 1 - alpha
    gamma = cv2.getTrackbarPos('Gamma', 'BarraDeslizante')
    res = cv2.addWeighted(img1, alpha, img2, betha, gamma)
    cv2.imshow("BarraDeslizante", res)
    if (cv2.waitKey(1) == ord('s')):
        break

cv2.destroyAllWindows()
