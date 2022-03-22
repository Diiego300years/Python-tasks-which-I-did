atext='This is a text.'

print(atext.endswith('ext.'))  #czy kończy się na txt.    true

print(atext.islower()) #czy jest tylko z małych znaków  false

print(atext.upper())   #zmienia na duze litery

print(atext.upper().isupper()) #sprawdza czy sa tylko duże litery  true bo upper przekształcił

print(atext.find('is')) #nr znaku na którym się znajduje "is" na 2 pozycji bo liczy od 0

print(atext.find('is', 3))  #poszukuje od 3 znaku cyzli tutaj będzie na 5

print(atext.replace('a', '4')) #wymienia a na 4

print(atext.replace('a', '4').replace('i', '1').replace('e', '3'))

print(atext.split(" ")) #podziela na spacjach i robi tablicę

somethingLikeNumber = "1000"

print(somethingLikeNumber.isdigit())   #sprawdza czy to jest liczbą

#można zrobić np.:
if somethingLikeNumber.isdigit() == True:
    print(int(somethingLikeNumber) + 2)
else:
    print("nie")

print(somethingLikeNumber.isdecimal()) #sprawdza czy jest liczba która może miec coś po przecinku #True

print(somethingLikeNumber.isalpha())  #sprawdza czy są same literki # false

print(somethingLikeNumber.isalnum())  #sprwdz czy są same liczby i literki  #True