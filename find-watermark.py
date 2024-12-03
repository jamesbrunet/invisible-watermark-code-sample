import cv2
from imwatermark import WatermarkDecoder

watermarked_image = cv2.imread('task-image.png')

decoder = WatermarkDecoder('bytes', 64)
watermark = decoder.decode(watermarked_image, 'dwtDctSvd')
print(watermark.decode('utf-8'))