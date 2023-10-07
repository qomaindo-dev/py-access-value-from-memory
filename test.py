#Python Get ID data and revert Get Value by ID data in memory python
import ctypes 

buku = ""
print(buku)
print(id(buku))
print("=============")

buku = "Ini Buku Budi"
print(buku)
idBuku = id(buku)
print(idBuku)

print("*****Access Data from memory by ID****")
revertData = ctypes.cast(idBuku, ctypes.py_object).value
print(f'Hasil Revert Data: {revertData}')
