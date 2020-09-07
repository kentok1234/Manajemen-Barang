# KUMPULAN MODULE PROGRAM MANAJEMEN BARANG

def viewData(dataBarang):
    no = 1
    
    for i in range(len(dataBarang)):
        print('+' + '-'*48 + '+')
        for key, value in dataBarang[i].items():
            if key == 'JENIS_BARANG':
                print(no, end='.')
                print('| ' + key + ' : ' + str(value))
                no += 1
            else:
                print(' '*(len(str(no)) + 1) + '| ' + key + ' : ' + str(value))
        print('+' + '-'*48 + '+')

def addData():
    IN_KODE_BARANG   = str(input('KODE BARANG   : '))
    IN_NAMA_BARANG   = str(input('NAMA BARANG   : '))
    IN_JENIS_BARANG  = str(input('JENIS BARANG  : '))
    IN_JUMLAH_BARANG = int(input('JUMLAH BARANG : '))
    IN_HARGA_BARANG  = int(input('HARGA BARANG  : '))

    return {
        'KODE_BARANG' : IN_KODE_BARANG.upper(),
        'NAMA_BARANG' : IN_NAMA_BARANG.upper(),
        'JENIS_BARANG' : IN_JENIS_BARANG.upper(),
        'JUMLAH_BARANG' : IN_JUMLAH_BARANG,
        'HARGA_BARANG' : IN_HARGA_BARANG
        }

def deleteData(dataBarang):
    print('MASUKKAN KODE BARANG YANG AKAN DIHAPUS')

    IN_KODE_BARANG = input('KODE BARANG : ')

    # LINEAR SEARCH
    find = -1
    indeks = 0
    for data in dataBarang:
        if data['KODE_BARANG'].find(IN_KODE_BARANG) != -1:
            find = data['KODE_BARANG'].find(IN_KODE_BARANG)
            break
        indeks += 1
    
    if find >= 0:
        print('DATA TELAH DIHAPUS!')
        return indeks
    else:
        print('DATA TIDAK DITEMUKAN!')

def searchData(dataBarang):
    print('MASUKKAN NAMA BARANG YANG AKAN DICARI')

    IN_NAMA_BARANG = input('NAMA BARANG : ').upper()

    # LINEAR SEARCH
    find = -1
    indeks = 0
    searchData = []
    for data in dataBarang:
        if data['NAMA_BARANG'].find(IN_NAMA_BARANG) != -1:
            find = data['NAMA_BARANG'].find(IN_NAMA_BARANG)
            searchData.append(dataBarang[indeks])
        indeks += 1
    
    if find >= 0:
        viewData(searchData)
    else:
        print('DATA TIDAK DITEMUKAN!')



