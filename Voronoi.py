import numpy as np
import math
from PIL import Image, ImageDraw
colors = np.array([[180, 0, 0], [0, 25, 200], [10, 150, 45], [100,100,100], [24,24,24]])
dim = 512
num_colors = 3
points = np.array([[50, 50], [150, 350], [400, 150],[256, 256],[300,200]])
metric = 'euclidean'

def closest_point_euclidean(point):
	minimum = float('inf')
	closest_point = None
	i = None
	
	for index, p in enumerate(points):
		distance = round(((point[0] - p[0])**2 + (point[1] - p[1])**2)**(1/2))
		if distance < minimum:
			minimum = distance
			closest_point = p
			i = index

	return i

def closest_point_manhattan(point):
	minimum = float('inf')
	closest_point = None
	i = None

	for index, p in enumerate(points):
		distance = abs(point[0] - p[0]) + abs(point[1] - p[1])
		if distance < minimum:
			minimum = distance
			closest_point = p
			i = index

	return i

def main():
	plot = np.zeros((dim, dim, 3), 'uint8')

	for i in range(plot.shape[0]):
		for j in range(plot.shape[1]):
			if metric == 'manhattan':
				closest_point_index = closest_point_manhattan([i,j])
			elif metric == 'euclidean':
				closest_point_index = closest_point_euclidean([i,j])
			plot[i][j] = colors[closest_point_index]

	r = 2
	img = Image.fromarray(plot)
	draw = ImageDraw.Draw(img)
	for p in points:
		draw.ellipse([p[1] - r, p[0] - r, p[1] + r, p[0] + r], fill=(255,255,255))
	img.show()
	img.save('myEuclideanPlot.jpeg')

if __name__ == "__main__":
	main()