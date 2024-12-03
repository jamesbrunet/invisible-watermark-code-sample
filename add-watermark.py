import cv2
from imwatermark import WatermarkEncoder

original_image = cv2.imread('james.jpg')
watermark = 'test'

encoder = WatermarkEncoder()
encoder.set_watermark('bytes', watermark.encode('utf-8'))
watermarked_image = encoder.encode(original_image, 'dwtDctSvd')

cv2.imwrite('james-watermarked.jpg', watermarked_image)