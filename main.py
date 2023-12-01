'''Vocês precisam instalar o opencv e o matplotlib na maquina de vocês '''
import cv2 
import matplotlib.pyplot as plt
from funcoes import *


def main():
	image = cv2.imread("lulu.jpg")
	img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	img = img.tolist()

	m = menu()
	while(m != 0):
		if m == 1:
			plt.imshow(cinza(img), cmap="gray")
			plt.show()
		elif m == 2:
			compare(img, negative(img))
		m = menu()

	return

if __name__ == "__main__":
	main()