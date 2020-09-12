from module import *

# Variable

filename = 'barang.csv'

# Main Program

while True:

    # Menu
    
    print('PROGRAM MANAJEMEN BARANG'.center(25))
    print('+', end='-'*23)
    print('+')
    print('MENU'.center(int(25)))
    print('+', end='-'*23)
    print('+')
    print('1. LIHAT DATA\n'
        '2. TAMBAH DATA\n'
        '3. HAPUS DATA\n'
        '4. CARI DATA\n'
        'x. KELUAR')

    menu = input('PILIH MENU : ')
    
    if menu == '1':
        viewData(filename)
    elif menu == '2':
        addData(filename)
    elif menu == '3':
        deleteData(filename)
    elif menu == '4':
        searchData(filename)
    elif menu == 'x' or menu == 'X':
        break
    else:
        print('MENU TIDAK TERSEDIA!')
    
    # End Of Menu