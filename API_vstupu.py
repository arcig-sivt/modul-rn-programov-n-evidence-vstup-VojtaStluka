from tělo import *

# Registrace osob a karet
registruj_osobu(1, "Jan Novák")
registruj_osobu(2, "Eva Svobodová")
prirad_kartu("A123", 1)
prirad_kartu("B456", 2)

# Zaznamenání vstupů a výstupů
zaznamenej_pohyb("A123")  # Jan Novák přichází
zaznamenej_pohyb("B456")  # Eva Svobodová přichází
zaznamenej_pohyb("A123")  # Jan Novák odchází

# Výpis historie pro konkrétní kartu
print("Historie karty A123:")
for zaznam in vrat_historii(id_karty="A123"):
    print(zaznam)

# Výpis historie pro konkrétní osobu
print("Historie osoby Jan Novák:")
for zaznam in vrat_historii(id_osoby=1):
    print(zaznam)

# Kdo je aktuálně uvnitř?
print("Kdo je aktuálně uvnitř:")
for id_karty in kdo_je_uvnitr():
    print(id_karty)
