# Steganografija - Maturski rad iz predmeta Programiranje i programski jezici

## Instalacija

Prvo je potrebno klonirati repozitorijum sledećom komandom:

```
git clone https://github.com/dolijan/steganografija.git
```

Zatim se prebaciti u odgovarajuci folder(steganografija) i instalirati odgovarajuce python module:

```
pip install -r requirements.txt
```

## Ugradjivanje fajlova u sliku

Prvo je potrebno sacuvati sliku u koju se ugradjuje fajl i fajl koji ugradjujemo (moguce je ugraditi skoro svaki format fajla).

Zatim treba pokrenuti komandu

```
python3 steganografija.py -e ime_slike.png -m ime_fajla.txt
```

Iz postojece slike moze se izvuci fajl komandom

```
python3 steganografija.py -d ime_slike.png
```

Ukoliko fajl koji je ekstraktovan nece da se otvori, onda ga treba preimenovati i dodati mu odgovarajuci sufiks (.txt, .png , .exe) . Ovo ocekujem da moze da se desi na windowsu.

## Ugradjivanje nevidljive poruke u tekst

Treba napraviti 2 text fajla: jedan u koji se ugradjuje poruka i jedan koji sadrzi samu poruku.

```
python3 steganografija.py -e fajl.txt -m ime_fajla_sa_porukom.txt
```

Dekodiranje se vrsi sledecom komandom:

```
python3 steganogradija.py -d fajl.txt
```

