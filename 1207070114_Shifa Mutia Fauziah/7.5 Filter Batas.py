# Import Library
import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
import numpy as np

# Load & Plot Input Image

# membaca citra
citra1 = imread(fname="Image/mobil.tif")
citra2 = imread(fname="Image/boneka2.tif")

# menampilkan shape
print('Shape citra 1 : ', citra1.shape)
print('Shape citra 1 : ', citra2.shape)

# Membuat subplot dengan 1 baris dan 2 kolom.
fig, axes = plt.subplots(1, 2, figsize=(10, 10))
ax = axes.ravel()

# Menampilkan citra dan memberikan title
ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Citra 1")
ax[1].imshow(citra2, cmap = 'gray')
ax[1].set_title("Citra 2")

# Menyiapkan variable output

# membuat salinan citra
copyCitra1 = citra1.copy()
copyCitra2 = citra2.copy()

# Mendapatkan dimensi baris dan kolom citra.
m1,n1 = copyCitra1.shape
# Membuat matriks kosong dengan dimensi yang sama seperti citra sebelumnya  untuk menyimpan output.
output1 = np.empty([m1, n1])
m2,n2 = copyCitra2.shape
output2 = np.empty([m2, n2])

# menampilkan shape dari salinan citra
print('Shape copy citra 1 : ', copyCitra1.shape)
print('Shape output citra 1 : ', output1.shape)

print('m1 : ', m1)  # Menampilkan nilai m1 (jumlah baris) citra 1.
print('n1 : ', n1)  # Menampilkan nilai n1 (jumlah kolom) citra 1.
print()

# menampilkan shape dari salinan citra
print('Shape copy citra 2 : ', copyCitra2.shape)
print('Shape output citra 3 : ', output2.shape)
print('m2 : ',m2)
print('n2 : ',n2)
print()

# Proses Filter Batas Pada Citra Input 1

 # Looping untuk setiap baris dan kolom citra
for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        
         # Mengatur variabel menjadi indeks baris saat ini.
        a1 = baris
        b1 = kolom
        
        arr = np.array([copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1, b1+1], \
            copyCitra1[a1, b1-1], copyCitra1[a1, b1+1], copyCitra1[a1+1, b1-1],  \
            copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]])
        

        # Menentukan piksel dengan nilai minimum dan maksimum dari array 'arr'
        minPiksel = np.amin(arr);        
        maksPiksel = np.amax(arr);    
            
        # Jika piksel di citra 'copyCitra1' pada posisi (baris, kolom) kurang dari piksel dengan nilai minimum,
        if copyCitra1[baris, kolom] < minPiksel :
            output1[baris, kolom] = minPiksel
        else :
            # Jika piksel di citra 'copyCitra1' pada posisi (baris, kolom) lebih dari piksel dengan nilai maksimum,
            if copyCitra1[baris, kolom] > maksPiksel :
                output1[baris, kolom] = maksPiksel
            else :
                output1[baris, kolom] = copyCitra1[baris, kolom] # Jika tidak, setel piksel di citra hasil (output1) pada posisi (baris, kolom) menjadi piksel asli dari citra 'copyCitra1'.


# Proses Filter Batas Pada Citra Input 2

# komennya hampir sama kayak yang atas
for baris1 in range(0, m2-1):
    for kolom1 in range(0, n2-1):
        
        a1 = baris1
        b1 = kolom1
        
        arr = np.array([copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1, b1+1], \
            copyCitra2[a1, b1-1], copyCitra2[a1, b1+1], copyCitra2[a1+1, b1-1],  \
            copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]])
        
        minPiksel = np.amin(arr);        
        maksPiksel = np.amax(arr);    
            
        if copyCitra2[baris1, kolom1] < minPiksel :
            output2[baris1, kolom1] = minPiksel
        else :
            if copyCitra2[baris1, kolom1] > maksPiksel :
                output2[baris1, kolom1] = maksPiksel
            else :
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]

# Plot Citra Input dan Output Hasil dari Filter Batas¶

# membuat subplot
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()


# Menampilkan citra pada sumbu indeks 0 dan memberi title
ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap = 'gray')
ax[1].set_title("Input Citra 2")

# Menampilkan output citra  pada sumbu indeks dan memberikan title
ax[2].imshow(output1, cmap = 'gray')
ax[2].set_title("Output Citra 1")

ax[3].imshow(output2, cmap = 'gray')
ax[3].set_title("Output Citra 2")
plt.show()