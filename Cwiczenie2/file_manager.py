#Stwórz nowy moduł w projekcie o nazwie file_manager. Stwórz klasę FileManager z parametrem w konstruktorze file_name.
#Klasa będzie zawierać dwie metody: read_file oraz update_file. Funkcja update_file powinna zawierac parametr text_data,
#które w efekcie ma być dopisane na końcu pliku. Funkcja read_file powinna zwrócić zawartość pliku.

class FileManager:
    def __init__(self, file_name):
        """ konstruktor """
        self.file_name=file_name
    def update_file(self,text_data):
        text_file = open(self.file_name, "a+")
        text_file.write(text_data)
        text_file.close()
    def read_file(self):
        text_file = open(self.file_name, "r")
        print(text_file.readlines())
        text_file.close()
#plik=FileManager("nazwa.txt")
#plik.update_file("Witam")
#plik.read_file()
