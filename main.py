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
        print('3. Display Contacts of One Customer')
        print('4. Add Customer')
        print('5. Add Contacts')
        print('6. Update Customer')
        print('7. Update Contacts')
        print('0. Exit')

        meni_item = input('Upisite broj ispred funkcionalnosti koju zelite napraviti: ')

        if meni_item.isdigit() and int(meni_item) < 8: # isdigit = True i za broj 123456 koejg nema u izborniku!!!
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

def display_contacts_one_customer():
    for customer in customers:
        print()
        print(f'Kontakti {customer['name']} su sljedeći: ', end='')
        for contact in contacts:
            if contact['id'] in customer['contacts']:
                print(f'{contact_full_name(contact)} ', end='')
        print()

def add_contacts():
    
    while True:
        contact = {}
        contact['id'] = contacts[-1]['id']+1
        contact['first_name'] = input('Upisite ime kontakta: ')
        contact['last_name'] = input('Upisite prezime kontakata: ')
        contact['phone'] = input('Upisite telefon novog kontakta: ')
        contact['email'] = input('Upisite email novog kontakta: ')

        new_contact = input('Zelite li dodati novi kontakt (Da/Ne): ')
        if new_contact.lower() != 'da':
            break
        else:
            ('Za nastavak upisite ENTER.')
        
    contacts.append(contact)

def update_contacts():
    while True:
        contact = {}
        display_contacts()
        
        contact_to_update = input('Upisite broj ispred kontakta kojeg zelite azurirati: ')
        
        if contact_to_update.isdigit() and int(contact_to_update) > 1 and int(contact_to_update) < len(contacts):
            contact['id'] = contact_to_update
            contact['first_name'] = input('Azurirajte ime kontakta: ')
            contact['last_name'] = input('Azurirajte prezime kontakta: ')
            contact['phone'] = input('Azurirajte telefon kontakta: ')
            contact['email'] = input('Azurirajte e-mail kontakta: ')
        else:
            print('Neispravan unos. Pokusajte ponovno.')
            input('Za nastavak pritisnite tipku ENTER.')
        new_update = input('Zelite li azurirati i neki drugi kontakt (Da/Ne): ')
        if new_update != 'da':
            break
        else:
            input('Za nastavak pritisnite tipku ENTER.')
    contacts[int(contact_to_update)-1] = contact




#endregion

#region CUSTOMERS MODUL

def display_customers():
    print('display_customers() iz working!')
    for customer in customers:
        print(f'{customer['id']}, {customer['name']}, {customer['vat_id']}, {customer['contacts'][0]},')
        
def add_customers():
    while True:
        customer = {
            'contacts':[]
        }
        
        customer['id'] = customers[-1]['id']+1
        customer['name'] = input('Upisite ime novog kupca: ')
        customer['vat_id'] = input('Upisite vat_id novog kupca: ')
        while True:
            contact_id = input('Upisite id kontakta kupca: ')
            customer['contacts'].append(int(contact_id))
            new_contact_id = input('Zelite li dodati id novog kontakta kupca (Da/Ne): ')
            if new_contact_id.lower() != 'da':
                break
            else:
                input('Za nastavak pritisnite tipku ENTER.')
        new_customer = input('Zelite li dodati novog kupca (Da/Ne): ')
        if new_customer != 'da':
            break
        else:
            input('Za nastavak pritisnite tipku ENTER.')
    customers.append(customer)
    
    
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
        elif menu_item == 3:
            display_contacts_one_customer()
            print()
            input('Za nastavak pritisnite tipku ENTER! ')
        elif menu_item == 4:
            add_customers()
            print()
            input('Za nastavak pritisnite tipku ENTER! ')
        elif menu_item == 5:
            add_contacts()
            print()
            input('Za nastavak pritisnite tipku ENTER! ')
        elif menu_item == 6:
            update_customers()
            print()
            input('Za nastavak pritisnite tipku ENTER! ')
        elif menu_item == 7:
            update_contacts()
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