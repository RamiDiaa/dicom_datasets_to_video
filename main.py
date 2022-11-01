import numpy as np
import matplotlib.pyplot as plt
import pydicom
import os

seriesPath = 'head'#input('enter the path to dataset folder : ')
browsed_files = []
for path in os.listdir(seriesPath):
    full_path = os.path.join(seriesPath, path)
    if os.path.isfile(full_path):
        browsed_files.append(full_path)

ct_images = browsed_files
slices = [pydicom.read_file(image_file, force=True) for image_file in ct_images]
slices = sorted(slices,key=lambda x:x.ImagePositionPatient[2])
img_shape = list(slices[0].pixel_array.shape)
img_shape.append(len(slices))
volume3d=np.zeros(img_shape)
print(slices[0])

for i,s in enumerate(slices):
    array2D = s.pixel_array
    volume3d[:,:,i] = array2D

k = 100
plt.ion()
array = np.zeros((k, k))

#axial
for i in range(img_shape[2]):
        plt.imshow(volume3d[:,:,i],cmap='gray')
        plt.title('Axial')
        plt.show()
        plt.pause(0.001)
        plt.clf()
#coronal
for i in range(img_shape[2]):
        plt.imshow(volume3d[i,:,:],cmap='gray')
        plt.title('Coronal')
        plt.show()
        plt.pause(0.001)
        plt.clf()

# sagittal
for i in range(img_shape[2]):
        plt.imshow(volume3d[:,i,:],cmap='gray')
        plt.title('Sagittal')
        plt.show()
        plt.pause(0.001)
        plt.clf()
