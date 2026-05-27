import cv2
import numpy as np

def load_image(impath):
    # A load image function to fix the OpenCV BGR channel order
    # Loads the image specified in the string impath
    img = cv2.cvtColor(cv2.imread(impath), cv2.COLOR_BGR2RGB)
    return img

def channel_diff(img, channel_1, channel_2):
    # Find the channel-wise difference in img between channel_1 and channel_2
    # img should be a three channel image, channel_1 and channel_2 should not be equal
    # and channel_1 and channel_2 need to be in the range [0,2]
    assert len(img.shape) == 3, "The image needs to have three colour channels."
    assert channel_1 != channel_2, "Chanel 1 and Channel 2 cannot be the same channel!"
    
    return img[:,:,channel_1] - img[:,:,channel_2]

def integral_img(img):
    # Compute the integral image of an input image.
    # The input image needs to be a single channel image.
    assert len(img.shape) == 2, "Integral image is only defined for a 2D array."

    intimg = np.cumsum(img, axis=0)
    intimg = np.cumsum(intimg, axis=1)

    return intimg