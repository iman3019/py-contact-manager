# Contact Manager

Ustanova: Algebra
Grupa: OL-OPYT_DEV_H-04-25

**Contact Manager** - simple Python console app for managing contacts

## Opis aplikacije/projekta

Aplikacija koja čuva podatke o kontaktima koji rade za kupca (firma).

### Modeli

Svaki kontakt ima slijedeća svojstva:

- id
- ime
- prezime
- broj telefona
- email

Također treba čuvati podatke i o kupcu (firma) za kojeg je navedeni kontakt primarna kontakt osoba. To znači da firma može imati više kontakta.

Svaka firma ima slijedeća svojstva:

- id
- name
- vat_id
- contacts - VAŽNO: contacts kolekcija ima samo podatke o id-u kontakt ne cijeli kontakt

### Funkcionalnosti

Aplikacija korisniku omogućava:

- prikaz svih kontakata
- prikaz svih kontakata jedne firme
- dodavanje i ažuriranje firme
- dodavanje i ažuriranje kontakta