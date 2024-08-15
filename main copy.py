import cv2
import numpy as np

# Charger l'image en niveaux de gris
image = cv2.imread("Scan Test/image2.jpg", 0)

# # Convertir l'image en niveaux de gris
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Appliquer un filtre de renforcement des bords (optionnel)
# gray = cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize=5)

# Appliquer un flou gaussien pour réduire le bruit
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imwrite("result/image_blurred.jpg", blurred)

# Appliquer l'algorithme de Canny pour détecter les contours
edges = cv2.Canny(blurred, 1, 150)

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
	area = cv2.contourArea(contour)
	# Obtenir les coordonnées du rectangle englobant
	x, y, w, h = cv2.boundingRect(contour)
	aspect_ratio = float(w) / h
	# Filtrer les contours basés sur l'aire et le rapport largeur/hauteur
	if area > aire_minimale and aspect_ratio_min < aspect_ratio < aspect_ratio_max:
		# Dessiner le rectangle englobant sur l'image originale
		cv2.rectangle(contour_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
cv2.imwrite("result/image_contours.jpg", contour_img)


# # Détecter les objets entiers
# for i, contour in enumerate(contours):
#     # Calculer l'aire du contour
#     area = cv2.contourArea(contour)
#     # Calculer le rectangle englobant
#     x, y, w, h = cv2.boundingRect(contour)
#     # Calculer le rapport largeur/hauteur
#     aspect_ratio = float(w) / h
#     # Filtrer les contours basés sur l'aire et le rapport largeur/hauteur
#     if area > aire_minimale and aspect_ratio_min < aspect_ratio < aspect_ratio_max:
#         roi = image[y:y+h, x:x+w]
#         cv2.imwrite("result/zetiquette_{}.jpg".format(i), roi)