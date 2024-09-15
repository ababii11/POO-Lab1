class Carte:
    def __init__(self, titlu, autor, isbn, pagini):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn
        self.pagini = pagini

    def __str__(self):
        return f"Titlu: {self.titlu}, Autor: {self.autor}, ISBN: {self.isbn}, Pagini: {self.pagini}"

class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self):
        titlu = input("Introdu titlul cărții: ")
        autor = input("Introdu autorul cărții: ")
        isbn = input("Introdu ISBN-ul cărții: ")
        pagini = input("Introdu numărul de pagini: ")

        carte = Carte(titlu, autor, isbn, pagini)
        self.carti.append(carte)
        print(f"Cartea '{carte.titlu}' a fost adăugată în bibliotecă.")

    def elimina_carte(self, isbn):
        for carte in self.carti:
            if carte.isbn == isbn:
                self.carti.remove(carte)
                print(f"Cartea '{carte.titlu}' a fost eliminată din bibliotecă.")
                return
        print(f"Cartea cu ISBN {isbn} nu a fost găsită în bibliotecă.")

    def afiseaza_carti(self):
        if not self.carti:
            print("Biblioteca este goală.")
        else:
            print("Cărțile din bibliotecă:")
            for carte in self.carti:
                print(carte)

if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        optiune = input("Dorești să adaugi o carte? (da/nu): ").lower()
        if optiune == 'da':
            biblioteca.adauga_carte()
        else:
            break

    biblioteca.afiseaza_carti()

    isbn = input("Introdu ISBN-ul cărții de eliminat: ")
    biblioteca.elimina_carte(isbn)

    biblioteca.afiseaza_carti()

