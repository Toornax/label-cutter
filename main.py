import cv2

# Charger l'image
image = cv2.imread("Scan test/image2.jpg")

# Afficher l'image
cv2.imshow("Image", image)

# Dessiner la bounding box (ici, vous pouvez dessiner manuellement la bounding box)

# Attendre la sélection de la bounding box par l'utilisateur
rect = cv2.selectROI("Image", image, fromCenter=False, showCrosshair=True)

# Récupérer les coordonnées de la bounding box
x, y, w, h = rect

# Définir les limites des régions d'intérêt
roi_x1 = x
roi_y1 = y
roi_x2 = x + w
roi_y2 = y + h

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer un filtre de Canny uniquement sur la région d'intérêt
edges = cv2.Canny(gray[roi_y1:roi_y2, roi_x1:roi_x2], 50, 150)

# Trouver les contours dans l'image
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Définir les seuils pour la taille des contours
aire_minimale = 1000  # Ajustez ce seuil selon vos besoins
aspect_ratio_min = 0.5  # Ajustez ces seuils selon vos besoins
aspect_ratio_max = 2.0



# Dessiner les contours sur l'image originale
contour_img = image.copy()

# Dessiner les rectangles englobants autour des éléments détectés
for contour in contours:
	x_contour, y_contour, w_contour, h_contour = cv2.boundingRect(contour)
	# Dessiner le rectangle englobant sur l'image originale
	cv2.rectangle(image, (roi_x1 + x_contour, roi_y1 + y_contour), (roi_x1 + x_contour + w_contour, roi_y1 + y_contour + h_contour), (0, 255, 0), 2)


# Afficher les contours détectés dans la région d'intérêt
cv2.imshow("Contours", contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
