#latihan logika dan komparasi

#membuat gabungan area rentang dari angka

# +++++++++3-------------10++++++++++++

inputUser = float(input("masukkan angka yang bernilai\nkurang dari 3\n atau\n lebih besar dari 10\n:"))

# +++++++++3-----------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)

print ("Kurang dari 3=",isKurangDari)

# ----------10++++++++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)

print ("Lebih dari 10=",isLebihDari)

# ++++++++3------------10++++++++++

isCorrect = isKurangDari or isLebihDari

print ("angka yang dimasukkan :",isCorrect)

print ("\n",10*"=","\n")
# kasus irisan
# ----------3+++++++++++++++10-------------

inputUser = float(input("masukkan angka yang bernilai\nlebih dari 3\n dan\n kurang dari 10\n:"))

# memeriksa angka lebih dari 3

isLebihDari = (inputUser > 3)

print ("Lebih dari 3=",isLebihDari)

# memeriksa kurang dari 10

isKurangDari = (inputUser < 10)

print ("Kurang dari 10=",isKurangDari)

# hasil irisan
# ----------3+++++++++++++++10-------------

isCorrect = isLebihDari and isKurangDari

print ("angka yang dimasukkan :",isCorrect)
