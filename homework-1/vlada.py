class Osoba:

    def __init__(self, ime, prezime, zanimanje, jmbg):
        self.ime = ime
        self.prezime = prezime
        self.zanimanje = zanimanje
        self.jmbg = jmbg

    def get_puno_ime(self):
        return self.ime + " " + self.prezime

    def __repr__(self):
        return self.ime


class Poslanik(Osoba):

    def __init__(self, ime, prezime, zanimanje, jmbg, partija):
        super().__init__(ime, prezime, zanimanje, jmbg)
        self.partija = partija

    def get_partija(self):
        return self.partija


class Ministar(Poslanik):

    def __init__(self,  ime, prezime, zanimanje, jmbg, partija, pozicija):
        super().__init__(ime, prezime, zanimanje, jmbg, partija)
        self.pozicija = pozicija

    def get_pozicija(self):
        return self.pozicija

    def set_pozicija(self, pozicija):
        self.pozicija = pozicija


ministar1 = Ministar("Zdravko", "Krivokapic",
                     "Profesor", 3107, "DF", "Premijer")
poslanik1 = Poslanik("Nebojsa", "Medojevic", "Politicar", 2209, "PZP")

print(f'{ministar1.get_puno_ime()} je u partiji {ministar1.get_partija()} i obavlja funkciju {ministar1.get_pozicija()}')
print(f'{poslanik1.get_puno_ime()} je u partiji {poslanik1.get_partija()}')

ministar1.set_pozicija("Ministar prosvjete")
print(f'{ministar1.get_puno_ime()} je sada na poziciji {ministar1.get_pozicija()}')

file_obj = open('./vlada.txt', 'w')
file_obj.write(
    f'{ministar1.get_puno_ime()} je u partiji {ministar1.get_partija()} i obavlja funkciju {ministar1.get_pozicija()} \n')
file_obj.close()
