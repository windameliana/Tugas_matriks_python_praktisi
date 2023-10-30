# 1. pengurangan dan penjumlahan matriks
# dua macam matriks 3x3
matriks1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
matriks2 = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
]

# perhitungan penjumlaan dan pengurangan
for x in range(0, len(matriks1)):
    for y in range(0, len(matriks1[0])):
        print(matriks1[x][y] + matriks2[x][y], end=''),
print()

# 2. perkalian matriks
import numpy as np

# matriks 2x2
matriks1 = np.array([[1, 2], [3, 4]])
matriks2 = np.array([[5, 6], [7, 8]])

print(np.dot(matriks1, matriks2))

# 3. transporse matriks
import numpy as np

# membuat transpose 3x2
matriks = np.array([[1, 2, 3], [4, 5, 6]])


print(np.transpose(matriks, ))

# 4. invers matriks
import numpy as np

matriks = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# transpose matriks
print(np.transpose(matriks))

# 5. matriks identitas
import numpy as np

# matriks 4x4
matriks_identitas = np.eye(4)

print(matriks_identitas)

# 6. reshape matriks
import numpy as np

matriks1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
matriks_reshape = np.reshape(matriks1, (2, 8))
print(matriks_reshape)