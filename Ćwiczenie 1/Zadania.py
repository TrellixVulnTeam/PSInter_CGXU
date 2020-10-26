zmienna = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz" \
          " pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki." \
          " Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym." \
          " Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty" \
          " Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do" \
          " realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Przemysław"
nazwisko = "Krajewski"
litera_1 = imie[2]
litera_2 = nazwisko[3]
print("W tekście jest "+ str(zmienna.count(litera_1)) + " liter "+imie[2]+" oraz "+str(zmienna.count(litera_2)) +
      " liter " +litera_2)
print(imie[::-1] + " " + nazwisko[::-1])
L=[1,2,3,4,5,6,7,8,9,10]
W = L[5:]
L=L[:5]
L.extend(W)
L.insert(0,0)
L.sort()
L=L[::-1]
print(L)
krotka = (162427,"Jan Kowalski"),(555555,"Andrzej Dudeł"),(652231,"Majster Klask")
krotkaa = tuple([162427,"Jan Kowalski"])
slownik = {}
slownik = dict(krotka)
slownik[162427]=slownik[162427],21,"man@wp.pl","Starograd 22"
slownik[555555]=slownik[555555],19,"Dudek@wp.pl","Olsztyn/Iwaszkiewiczq 13/2"
slownik[652231]=slownik[652231],23,'Majsteroo@wp.pl',"Pruszcz Gdański 12"
print(slownik)
tel=[600500400,600500400,690500400,512555684,512555684,772350220,772350220]
tel=list(set(tel))
print(tel)
x = range(1,11)
for n in x:
  print(n,end=" ")
print()
y = range(100,19,-5)
for n in y:
    print(n, end=" ")
print()
slownik1={"Janusz":"Uno","Marcin":"Donna"}
slownik2={1:"Due",2:'Mamma'}
slownik3={222:"Rike",333:"Ess"}
lista=[slownik1,slownik2,slownik3]
for d in lista:
    for s in d:
        print("%s %s"%(s,d[s]),end=" ")