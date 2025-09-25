import os
from typing import Dict


#region INITIAL DATA

contacts = [
    {
        'id': 1,
        'first_name': 'Pero',
        'last_name': 'Peric',
        'phone': '09x 1234 567',
        'email': 'pero.peric@email.hr'
    },
    {
        'id': 2,
        'first_name': 'Ana',
        'last_name': 'Anic',
        'phone': '09x 7654 321',
        'email': 'ana.anic@email.hr'
    },
    {
        'id': 3,
        'first_name': 'Mirko',
        'last_name': 'Mirkic',
        'phone': '09x 9513 579',
        'email': 'mirko.mirkic@email.hr'
    },
    {
        'id': 4,
        'first_name': 'Slavko',
        'last_name': 'Slavkic',
        'phone': '09x 3578 963',
        'email': 'slavko.slavkic@email.hr'
    },
]

customers = [
    {
        'id': 1,
        'name': 'Pajdo und Jaranen GmbH',
        'vat_id': '01234567890',
        'contacts': [1, 2]
    },
    {
        'id': 2,
        'name': 'The Best Software Ltd.',
        'vat_id': '98765432100',
        'contacts': [3, 4]
    }
]

#endregion


#region FUNCTIONS


#region GUI MODUL

def clear_display() -> None:
    os.system('cls') if os.name == 'nt' else os.system('clear')
    print('clear_display() is working')
    

def main_menu() -> int:
    while True:
        # Ocisti ekran -> funkcija clear_display()
        clear_display()

        print('main_menu() is working.')
        print('1. Display Customers')
        print('2. Display Contacts')
        print('0. Exit')

        meni_item = input('Upisite broj ispred funkcionalnosti koju zelite napraviti: ')

        if meni_item.isdigit(): # isdigit = True i za broj 123456 koejg nema u izborniku!!!
            return int(meni_item)
        else:
            print('Neispravan unos! Pokusajte ponovno.')
            input('Za novi izbor pritisnite tipku ENTER.')

#endregion

#region CONTACTS MODUL

def contact_full_name(contact: Dict) -> str:
    return f'{contact['first_name']} {contact['last_name']}'


def display_contacts():
    for contact in contacts:
        print(f'{contact['id']}, {contact_full_name(contact)}')

#endregion

#region CUSTOMERS MODUL

def display_customers():
    print('display_customers() iz working!')

#endregion


def main():
    while True:
        # Prikazati izbornik -> funkcija main_menu()
        menu_item = main_menu()

        # Ovisno o izboru meni_item pozvati odgovarajucu funkciju
        if menu_item == 0:
            return
        elif menu_item == 1:
            display_customers()
            print()
            input('Za nastavak pritisnite tipku ENTER! ')
        elif menu_item == 2:
            display_contacts()
            print()
            input('Za nastavak pritisnite tipku ENTER! ')
        else:
            print(menu_item)
            input()

#endregion


#region MAIN PROGRAM
if __name__ == '__main__':
    main()
#endregion