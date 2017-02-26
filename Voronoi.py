import numpy as np
import math
from PIL import Image
colors = np.array([[180, 0, 0], [0, 25, 200], [10, 150, 45], [100,100,100]])
dim = 512
num_colors = 3
points = np.array([[0, 0], [100, 350], [400, 150],[256, 256, 256]])
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

	img = Image.fromarray(plot)
	img.show()

	'''
	r = 0.5
	g = 0.1
	b = 0.7
	
	rgbArray = np.zeros((512,512,3), 'uint8')
	rgbArray[..., 0] = r*256
	rgbArray[..., 1] = g*256
	rgbArray[..., 2] = b*256
	img = Image.fromarray(rgbArray)
	img.save('myimg.jpeg')

	'''

if __name__ == "__main__":
	main()