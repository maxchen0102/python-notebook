import SimpleITK  as sitk  
from PIL import Image 
from matplotlib import pyplot as plt
import os 
import numpy as np 
def showNii(img): #把此file所有圖片印出來看 
    for i in range(img.shape[0]):
        plt.imshow(img[i,:,:],cmap='gray')
        plt.show()
        
        
 
itk_img = sitk.ReadImage("C:/Users/acer_PC/Desktop/2045_dream/brain/image/2ABGOEM3.nii.gz")
img = sitk.GetArrayFromImage(itk_img)
print(img.shape)    # (155, 240, 240) 表示各個維度的切片數量
#showNii(img)

#plt.imshow(img[1,:,:],cmap="gray") #印單張圖片 
