#Primul Laborator la POO#

Ca limbaj de programare am folosit python.

Sarcina lucrării:
Am implementat doua clase ( Class si Biblioteca)

In clasa Carte am implementat atributele precum (autor, numar de pagini, titlu, codul ISBN)
```python
class Carte:
    def __init__(self, titlu, autor, isbn, pagini):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn
        self.pagini = pagini
```
Clasa Bibliotecă trebuie să dețină o listă de cărți si și metode pentru a adăuga o carte, a elimina o carte și a afișa toate cărțile din bibliotecă

Metoda de adaugare a unei carti:
```python
def adauga_carte(self):
        titlu = input("Introdu titlul cărții: ")
        autor = input("Introdu autorul cărții: ")
        isbn = input("Introdu ISBN-ul cărții: ")
        pagini = input("Introdu numărul de pagini: ")

        carte = Carte(titlu, autor, isbn, pagini)
        self.carti.append(carte)
        print(f"Cartea '{carte.titlu}' a fost adăugată în bibliotecă.")
```

Metoda de eliminare a unei carti:
```python
def elimina_carte(self, isbn):
        for carte in self.carti:
            if carte.isbn == isbn:
                self.carti.remove(carte)
                print(f"Cartea '{carte.titlu}' a fost eliminată din bibliotecă.")
                return
        print(f"Cartea cu ISBN {isbn} nu a fost găsită în bibliotecă.")
```

Metoda de afisare a unei carti:
```python
 def afiseaza_carti(self):
        if not self.carti:
            print("Biblioteca este goală.")
        else:
            print("Cărțile din bibliotecă:")
            for carte in self.carti:
                print(carte)
```

