from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Dict

# Modely jako datové struktury
class Osoba(BaseModel):
    id: int
    jmeno: str

class Karta(BaseModel):
    id_karty: str
    id_osoby: Optional[int] = None

class Zaznam(BaseModel):
    id_karty: str
    cas: datetime
    smer: str  # 'prichod' nebo 'odchod'

# Globální proměnné
osoby: Dict[int, Osoba] = {}
karty: Dict[str, Karta] = {}
historie: List[Zaznam] = []

def registruj_osobu(id_osoby: int, jmeno: str) -> None:
    osoby[id_osoby] = Osoba(id=id_osoby, jmeno=jmeno)

def prirad_kartu(id_karty: str, id_osoby: int) -> None:
    karty[id_karty] = Karta(id_karty=id_karty, id_osoby=id_osoby)

def zaznamenej_pohyb(id_karty: str) -> None:
    ted = datetime.now()
    smer = 'prichod'
    if historie and historie[-1].id_karty == id_karty and historie[-1].smer == 'prichod':
        smer = 'odchod'
    historie.append(Zaznam(id_karty=id_karty, cas=ted, smer=smer))

def vrat_historii(id_karty: Optional[str] = None, id_osoby: Optional[int] = None) -> List[Zaznam]:
    vysledek = historie
    if id_karty:
        vysledek = [z for z in vysledek if z.id_karty == id_karty]
    if id_osoby:
        karty_osoby = [k.id_karty for k in karty.values() if k.id_osoby == id_osoby]
        vysledek = [z for z in vysledek if z.id_karty in karty_osoby]
    return vysledek

def kdo_je_uvnitr() -> List[str]:
    stav: Dict[str, str] = {}
    for zaznam in historie:
        stav[zaznam.id_karty] = zaznam.smer
    uvnitr = [id_karty for id_karty, smer in stav.items() if smer == 'prichod']
    return uvnitr
