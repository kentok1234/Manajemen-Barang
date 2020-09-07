from module import *

# Variable

dataBarang = []
dataBarang.append({
    'KODE_BARANG'   : '8999909028234',
    'NAMA_BARANG'   : 'DJI SAM SOE KRETEK 12',
    'JENIS_BARANG'  : 'ROKOK',
    'JUMLAH_BARANG' : 36,
    'HARGA_SATUAN'  : 17000 # Rupiah
})
dataBarang.append({
    'KODE_BARANG'   : '8999909096004',
    'NAMA_BARANG'   : 'SAMPOERNA MILD FILTER 16',
    'JENIS_BARANG'  : 'ROKOK',
    'JUMLAH_BARANG' : 24,
    'HARGA_SATUAN'  : 1500 # Rupiah
})

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
        viewData(dataBarang)
    elif menu == '2':
        dataBarang.append(addData())
    elif menu == '3':
        del dataBarang[deleteData(dataBarang)]
    elif menu == '4':
        searchData(dataBarang)
    elif menu == 'x' or menu == 'X':
        break
    else:
        print('MENU TIDAK TERSEDIA!')
    
    # End Of Menu