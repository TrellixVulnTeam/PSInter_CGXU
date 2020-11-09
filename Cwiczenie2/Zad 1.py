import Cwiczenie2.file_manager
def funkcja(lista,lista2):
    wynik = []
    i=0
    for j in lista:
        if i % 2 == 0:
            wynik.append(lista[i])
        else:
            wynik.append(lista2[i])
        i = i+1
    return wynik

lista = [0, 2, 4, 6, 8, 10]
lista2 = [1, "x", 5, 'd', 9, 'e']
print(funkcja(lista,lista2))

def funkcja2(data_text):
    tab=[]
    for i in data_text:
        tab.append(i)
    dict = {
        'length':len(data_text),
        'letters':tab,
        'big_letters':data_text.upper(),
        'small_letters':data_text.lower()}
    return dict
print(funkcja2("Kanalia"))

def funkcja3 (text, letter):
    for i in letter:
        text=text.replace(i,"")
    return text
print(funkcja3("Kanalia",'an'))
def funkcja4(wartość,typ):
    if typ == 'R':
        wartość=int((wartość+273.15)*1.8)
        return print(str(wartość) + " Rankineów")
    elif typ =='K':
        wartość=wartość+273.15
        return print(str(wartość) + " Kelwinów")
    elif typ == 'F':
        wartość = int((wartość * 1.8) + 32)
        return print(str(wartość) + " Fahrenheitów")
    else:
        return print("Podano zły typ: R,K,F")
funkcja4(13,'R')

def funkcja5(text):
    j=-1
    for i in text:
        print(text[j],end="")
        j=j-1
funkcja5("Ala ma kota")
print("\n")
class Calculator:

    def add(a,b):
        return a+b
    def diff(a,b):
        return a-b
    def multi(a,b):
        return a*b
    def devi(a,b):
        return a/b

print(Calculator.add(6,3))
print(Calculator.diff(6,3))
print(Calculator.multi(6,3))
print(Calculator.devi(6,3))
class ScienceCalculator (Calculator):
    def expo(a,b):
        return a**b
print(ScienceCalculator.expo(2,4))

plik=Cwiczenie2.file_manager.FileManager('nazwa.txt')
plik.update_file(" Jabko")
plik.read_file()