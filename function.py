def getTypeData(data): #function cek tipe data
    return type(data)

def listInput(): # function list input / menu
    print('=' * 25)
    print('Operasi Matematika')
    print('  1. Jumlah \t [+]')
    print('  2. Kurang \t [-]')
    print('  3. Kali \t [*]')
    print('  4. Bagi \t [/]')
    print('=' * 25)

def getOperators(operator):
    print('=' * 25)
    if operator == '1':
        print('User memilih penjumlahan')
    elif operator == '2':
        print('User memilih pengurangan')
    elif operator == '3':
        print('User memilih perkalian')
    elif operator == '4':
        print('User memilih pembagian')
    else:
        print('Tidak valid')

def getCountResult(menu, bilangan_1, bilangan_2):
    if menu == '1':
        hasil = bilangan_1 + bilangan_2
        print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
    elif menu == '2':
        hasil = bilangan_1 - bilangan_2
        print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
    elif menu == '3':
        hasil = bilangan_1 * bilangan_2
        print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
    elif menu == '4':
        hasil = bilangan_1 / bilangan_2
        print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')
    else:
        print('Tidak valid')