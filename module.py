import csv
import pandas as pd

# KUMPULAN MODULE PROGRAM MANAJEMEN BARANG

def viewData(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        df = pd.DataFrame(csv_reader)

        print(df)

def addData(filename):
    IN_KODE_BARANG   = str(input('KODE BARANG   : '))
    IN_NAMA_BARANG   = str(input('NAMA BARANG   : '))
    IN_JENIS_BARANG  = str(input('JENIS BARANG  : '))
    IN_JUMLAH_BARANG = int(input('JUMLAH BARANG : '))
    IN_HARGA_BARANG  = int(input('HARGA BARANG  : '))

    with open(filename, mode='a',newline='') as csv_file:
        fieldnames = ['kode_barang', 'nama_barang', 'jenis_barang', 'jumlah', 'harga']

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')

        csv_writer.writerow({'kode_barang':IN_KODE_BARANG, 'nama_barang':IN_NAMA_BARANG, 'jenis_barang':IN_JENIS_BARANG, 'jumlah':IN_JUMLAH_BARANG, 'harga':IN_HARGA_BARANG})

def deleteData(filename):
    print('MASUKKAN KODE BARANG YANG AKAN DIHAPUS')

    input_kb = input('KODE BARANG : ')

    file_data = []

    with open(file=filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            file_data.append(line)

        # LINEAR SEARCH
        find = False
        indeks = 0
        for rows in file_data:
            if rows['kode_barang'] == input_kb:
                find = True
                break
            indeks += 1
        
        if find:
            del file_data[indeks]
            
            with open(file='barang.csv', mode='w', newline='') as csv_file:
                fieldnames = ['kode_barang', 'nama_barang', 'jenis_barang', 'jumlah', 'harga']

                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')

                csv_writer.writeheader()

                for rows in file_data:
                    csv_writer.writerow(rows)
            
            print('DATA TELAH DIHAPUS!')
        else:
            print('DATA TIDAK DITEMUKAN!')

def searchData(filename):
    print('MASUKKAN NAMA BARANG YANG AKAN DICARI')

    input_nb = input('NAMA BARANG : ').lower()

    with open(file=filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # LINEAR SEARCH
        file_data = []
        for row in csv_reader:
            if row['nama_barang'].lower().find(input_nb) != -1:
                file_data.append(row)
        
        if file_data != []:
            df = pd.DataFrame(file_data)
            print(df)
        else:
            print('DATA TIDAK DITEMUKAN!')



