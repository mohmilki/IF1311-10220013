#latihan soal boolean dan komparaasi

# --------0++++++++5---------8+++++++++11-----------
print ("====================Kasus irisan==================")
print ("--------0++++++++5---------8+++++++++11-----------")
inputUser = float(input("Masukkan nilai lebih dari 0 dan kurang dari 5 \n lebih dari 8 dan kurang dari 11 :"))

# definisi variabel

# memeriksa nilai lebih dari 0
isLebihDari = (inputUser > 0)

print ("Nilai lebih dari 0 tersebut",isLebihDari)
# memeriksa nilai kurang dari 5

isKurangDari = (inputUser < 5)

print ("Nilai Kurang dari 5 tersebut",isKurangDari)

# memeriksa nilai lebih dari 8

isLebihDari1 = (inputUser > 8)

print ("Nilai lebih dari 8 tersebut",isLebihDari1)
# memeriksa nilai kurang dari 5

isKurangDari1 = (inputUser < 11)

print ("Nilai Kurang dari 11 tersebut",isKurangDari1)

# hasil per irisan

isCorrect = isLebihDari and isKurangDari
isCorrect1 = isLebihDari1 and isKurangDari1

isCorrect2 = isCorrect or isCorrect1
print ("====================Hasil irisan==================")
print ("--------0++++++++5---------8+++++++++11-----------")
print ("Nilai yang Anda masukkan", isCorrect2)

print ("==================Kasus Gabungan==================")
print ("++++++++0--------5+++++++++8---------11+++++++++++")
inputUser = float(input("Masukkan nilai kurang dari 0 atau lebih dari 5 \n kurang dari 8 atau lebih dari 11 :"))

# memeriksa nilai kurang dari 0

isKurangDari = (inputUser < 0)
print ("Nilai kurang dari 0", isKurangDari)

# memeriksa nilai lebih dari 5

isLebihDari = (inputUser > 5)
print ("Nilai lebih dari 5",isLebihDari)

# memeriksa nilai kurang dari 8
isKurangDari1 = (inputUser < 8)
print ("Nilai kurang dari 8", isKurangDari1)

# memeriksa lebih dari 11
isLebihDari1 = (inputUser > 11)
print ("Nilai lebih dari 11",isLebihDari1)


# hasil per gabungan
print ("==================Hasil Gabungan==================")
print ("++++++++0--------5+++++++++8---------11+++++++++++")
isCorrect = isLebihDari or isKurangDari
isCorrect1 = isLebihDari1 or isKurangDari1

isCorrect2 = isCorrect and isCorrect1

print ("Nilai yang anda masukkan",isCorrect2)