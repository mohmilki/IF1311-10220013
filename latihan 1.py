#tipe data integer
data_integer = 10

print ("===================================")
print ("data        :", data_integer)
print ("bertipe     :", type(data_integer))

#tipe data float
data_float = 10.5
print ("===================================")
print ("data        :", data_float)
print ("bertype     :", type(data_float))

#tipe data string
data_string = "Moh. Milki I. M"
print ("===================================")
print ("data        :", data_string)
print ("bertype     :", type (data_string))


#tipe data complex
data_complex = complex(5,6)
print ("===================================")
print ("data        :", data_complex)
print ("bertype     :", type(data_complex))

#tipe data: biner true/flase (boolean)
data_bool = False

print ("===================================")
print ("data        :", data_bool)
print ("bertype     :", type(data_bool))

#tipe data double dan chart (import dari bahasa C)
from ctypes import c_double, c_char
data_c_double = c_double(10,5)
print ("===================================")
print ("data        :", data_c_double)
print ("bertype     :", type(data_c_double))
print ("===================================")