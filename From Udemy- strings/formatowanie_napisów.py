message1 = "Processing file %s"
print(message1 % ('file_1.txt'))   #będzie podmieniać string (s) za wszystko to co podasz po %

message2 = 'File %s has size %d KB'
print(message2 % ('file1_txt', 100))

#print(message2 % (100, "file_txt")) #to nie zadziała, ponieważ tam gdzie %d musi być liczba

message3 = "file %20s has size %10d KB" # po s musi być 20 znakow a po d 10 znaków
print(message3 % ("file.txt", 100))

message4 = 'file {0:s} has size {1:d}' #wstawia coś w miejsce tego 0 a po : czy napis(s) czy liczba (d)
print(message4.format("file.txt", 100))

# można zrobić na odwrót:
message5 = 'file {1:s} has size {0:d}'
print(message5.format(100, 'plikchu'))


message6 = ("file size {0:5d}, name {1:5s}") # określa do ilu liter/liczb zarezerwowac dla jednej wartości
# jak jest więcej to spoko jak mniej to puste pole

print(message6.format(10, "njf"))


#SKONCZYŁEM NA 46 LEKCJI