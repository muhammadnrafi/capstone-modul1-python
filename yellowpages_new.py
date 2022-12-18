directory = {
    '0800000000' : {'Nama':'Y-Education' , 'Kategori':'Pendidikan' , 'Kota':'Jakarta' , 'Alamat': 'Jln. Merdeka No 45' , 'Telepon':'0800000000' , 'Email':'Y-EDU.com' },
    '0811111111' : {'Nama':'PT YP-Abadi' , 'Kategori':'Kontruksi' , 'Kota':'Bandung' , 'Alamat': 'Jln. Rajawali No 10' , 'Telepon':'0811111111' , 'Email':'YP@abadi.id' },
    '0822222222' : {'Nama':'Steak House' , 'Kategori':'Restoran' , 'Kota':'Jakarta' , 'Alamat': 'Jln. Orchard Road' , 'Telepon':'0822222222' , 'Email':'S@house.id' },
    '0833333333' : {'Nama':'Delli Belli' , 'Kategori':'Restoran' , 'Kota':'Denpasar' , 'Alamat': 'Jln. Yoga Jaya No 9' , 'Telepon':'0833333333' , 'Email':'D-Bell.com' },
    '0844444444' : {'Nama':'Sumber ABC' , 'Kategori':'Keuangan' , 'Kota':'Jakarta' , 'Alamat': 'Jln. Maharaja Blok A' , 'Telepon':'0844444444' , 'Email':'sjaya@mail.com' },
    '0855555555' : {'Nama':'Bangun Jaya' , 'Kategori':'Kontruksi' , 'Kota':'Medan' , 'Alamat': 'Jln. Iskandar Muda 2' , 'Telepon':'0855555555' , 'Email':'Bangun-J.co' },
    '0866666666' : {'Nama':'PT PWK-BD' , 'Kategori':'Keuangan' , 'Kota':'Surabaya' , 'Alamat': 'Jln. Mampang Indah' , 'Telepon':'0866666666' , 'Email':'PWK-BD.co.id' },
    '0877777777' : {'Nama':'EduPages' , 'Kategori':'Pendidikan' , 'Kota':'Pontianak' , 'Alamat': 'Jln. Keadilan Nusa' , 'Telepon':'0877777777' , 'Email':'EduPages.ed' },
    '0888888888' : {'Nama':'BWM Motorad' , 'Kategori':'Otomotif' , 'Kota':'Surabaya' , 'Alamat': 'Jln. Johor Barat' , 'Telepon':'0888888888' , 'Email':'BWM.us' },
    '0899999999' : {'Nama':'Asto Oto' , 'Kategori':'Otomotif' , 'Kota':'Bandung' , 'Alamat': 'Jln. Siliwangi No 15' , 'Telepon':'0899999999' , 'Email':'Asto@Oto.com' }
}
admin = '12345'

def read_directory():
    if len(directory)==0:
        print("==============================\nTidak ada data yang tersimpan\n==============================")
    else:
        print("| NAMA  \t| KATEGORI \t| KOTA  \t| ALAMAT \t\t| TELEPON\t| EMAIL/WEB")
        for key in directory.keys():
            print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[key]["Nama"],directory[key]["Kategori"],directory[key]["Kota"],directory[key]["Alamat"],directory[key]["Telepon"],directory[key]["Email"]))

def main_menu_1():
    if len(directory)==0:
        print("==============================\nTidak ada data yang tersimpan\n==============================")
    else:
        while True:
            menu_tampilan = input('''
======================================
        Menu Menampilkan Data
======================================
1. Tampilkan semua isi
2. Tampilkan perkategori
3. Tampilkan dengan kata kunci
4. kembali ke halaman sebelumnya
======================================
Masukkan Input (1-4): ''')
            if menu_tampilan=='1':
                read_directory()
            
            elif menu_tampilan=='2':
                menu_kategori = input('''
======================================
            Menu Kategori
======================================
1. Keuangan
2. Kontruksi
3. Pendidikan
4. Restoran
5. Otomotif
6. Kembali ke halaman sebelumnya
======================================
Masukkan Input (1-6): ''')
            
                if menu_kategori == '1':
                    print("| NAMA  \t| KATEGORI \t| KOTA  \t| ALAMAT \t\t| TELEPON\t| EMAIL/WEB")
                    for key in directory.keys():
                        if directory[key]['Kategori'] == 'Keuangan':
                            print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[key]["Nama"],directory[key]["Kategori"],directory[key]["Kota"],directory[key]["Alamat"],directory[key]["Telepon"],directory[key]["Email"]))
                        else:
                            continue
                elif menu_kategori == '2':
                    print("| NAMA  \t| KATEGORI \t| KOTA  \t| ALAMAT \t\t| TELEPON\t| EMAIL/WEB")
                    for key in directory.keys():
                        if directory[key]['Kategori'] == 'Kontruksi':
                            print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[key]["Nama"],directory[key]["Kategori"],directory[key]["Kota"],directory[key]["Alamat"],directory[key]["Telepon"],directory[key]["Email"]))
                        else:
                            continue
                elif menu_kategori == '3':
                    print("| NAMA  \t| KATEGORI \t| KOTA  \t| ALAMAT \t\t| TELEPON\t| EMAIL/WEB")
                    for key in directory.keys():
                        if directory[key]['Kategori'] == 'Pendidikan':
                            print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[key]["Nama"],directory[key]["Kategori"],directory[key]["Kota"],directory[key]["Alamat"],directory[key]["Telepon"],directory[key]["Email"]))
                        else:
                            continue
                elif menu_kategori == '4':
                    print("| NAMA  \t| KATEGORI \t| KOTA  \t| ALAMAT \t\t| TELEPON\t| EMAIL/WEB")
                    for key in directory.keys():
                        if directory[key]['Kategori'] == 'Restoran':
                            print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[key]["Nama"],directory[key]["Kategori"],directory[key]["Kota"],directory[key]["Alamat"],directory[key]["Telepon"],directory[key]["Email"]))
                        else:
                            continue
                elif menu_kategori == '5':
                    print("| NAMA  \t| KATEGORI \t| KOTA  \t| ALAMAT \t\t| TELEPON\t| EMAIL/WEB")
                    for key in directory.keys():
                        if directory[key]['Kategori'] == 'Otomotif':
                            print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[key]["Nama"],directory[key]["Kategori"],directory[key]["Kota"],directory[key]["Alamat"],directory[key]["Telepon"],directory[key]["Email"]))
                        else:
                            continue
            
            elif menu_tampilan == '3':
                kata_kunci = input('Masukkan kata kunci: ')
                print("| NAMA  \t| KATEGORI \t| KOTA  \t| ALAMAT \t\t| TELEPON\t| EMAIL/WEB")
                for key in directory.keys():
                    if kata_kunci.lower() in directory[key]["Nama"].lower():
                        print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[key]["Nama"],directory[key]["Kategori"],directory[key]["Kota"],directory[key]["Alamat"],directory[key]["Telepon"],directory[key]["Email"]))
                    elif kata_kunci.lower() in directory[key]["Kategori"].lower():
                        print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[key]["Nama"],directory[key]["Kategori"],directory[key]["Kota"],directory[key]["Alamat"],directory[key]["Telepon"],directory[key]["Email"]))
                    elif kata_kunci.lower() in directory[key]["Kota"].lower():
                        print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[key]["Nama"],directory[key]["Kategori"],directory[key]["Kota"],directory[key]["Alamat"],directory[key]["Telepon"],directory[key]["Email"]))
                    elif kata_kunci.lower() in directory[key]["Telepon"].lower():
                        print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[key]["Nama"],directory[key]["Kategori"],directory[key]["Kota"],directory[key]["Alamat"],directory[key]["Telepon"],directory[key]["Email"]))
                    elif kata_kunci.lower() in directory[key]["Email"].lower():
                        print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[key]["Nama"],directory[key]["Kategori"],directory[key]["Kota"],directory[key]["Alamat"],directory[key]["Telepon"],directory[key]["Email"]))
                    else:
                        continue
            
            elif menu_tampilan == '4':
                break

            else:
                print("Menu yang anda pilih tidak tersedia. Silahkan dicoba lagi.")

def main_menu_2():
    while True:
        input_telepon = input('Masukkan Nomor Telepon (5-12 Karakter): ')
        if input_telepon.isnumeric():
            index = input_telepon
            while len(input_telepon)>12 or len(input_telepon)<5:
                print("Mohon input ulang (5-12 Karakter)")
                input_telepon=input('Masukkan Nomor Telepon (5-12 Karakter): ')
            if input_telepon not in directory.keys():
                input_nama = input('Masukkan Nama kontak yang ingin disimpan (5-12 Karakter): ')
                while len(input_nama)>12 or len(input_nama)<5:
                    print('Mohon input ulang(5-12 Karakter)')
                    input_nama=input('Masukkan Nama kontak yang ingin disimpan (5-12 Karakter): ') 
                input_kategori=input('Masukkan Kategori (5-12 Karakter): ')
                while len(input_kategori)>12 or len(input_kategori)<5 :
                    print('Mohon input ulang (5-12 Karakter)')
                    input_kategori=input("Masukkan Kategori dari Produk Baru (5-12 Karakter): ")
                input_kota = input('Masukkan Kota (5-12 Karakter): ')
                while len(input_kota)>12 or len(input_kota)<5:
                    print("Mohon input ulang (5-12 Karakter)")
                    input_kota=input("Masukkan Kota (5-12 Karakter): ")
                input_alamat = input('Masukkan Alamat (5-12 Karakter): ')
                while len(input_alamat)>20 or len(input_alamat)<15:
                    print("Mohon input ulang (15-20 Karakter)")
                    input_alamat=input("Masukkan alamat (15-20 Karakter): ")
                input_email = input('Masukkan alamat Email (15-20 Karakter): ')
                while len(input_email)>20 or len(input_email)<15:
                    print("Mohon input ulang ")
                    input_email=input('Masukkan alamat Email (15-20 Karakter): ')
                check=input(f"Nama: {input_nama}, Kategori: {input_kategori}, Kota: {input_kota}, Alamat: {input_alamat}, Telepon: {input_telepon}, Email: {input_email} \n Apakah data tersebut ingin ditambahkan (Y/N): ")
                if check!="Y" and check!="Y".lower():
                    break
                else:
                    directory[index]={"Nama":input_nama.capitalize(),"Kategori":input_kategori.capitalize(),"Kota":input_kota.capitalize(), "Alamat": input_alamat.capitalize(),"Telepon":input_telepon,"Email":input_email}
                    read_directory()
                    break
            else:
                print("Mohon Maaf Nomor Tersebut Telah Terdaftar")
                break
        else:
            print('Input Telepon Salah, Tolong Masukkan Angka')

def main_menu_3():
    update_dir = input('Masukkan nomor Telepon: ')
    if update_dir not in directory.keys():
        print('Nomor yang anda masukkan tidak ditemukan')
    while update_dir in directory.keys():
        print("\nBerikut adalah detail data dengan nomor telepon tersebut:\n| NAMA  \t| KATEGORI \t| KOTA  \t| ALAMAT  \t\t| TELEPON\t| EMAIL/WEB")
        print("| {} \t| {} \t| {} \t| {} \t| {} \t| {}".format(directory[update_dir]["Nama"],directory[update_dir]["Kategori"],directory[update_dir]["Kota"],directory[update_dir]["Alamat"],directory[update_dir]["Telepon"],directory[update_dir]["Email"]))
        update_menu = input('''
======================================
            Menu Update
======================================
1. Update Nama
2. Update Kategori
3. Update Kota
4. Update Alamat
5. Update Telepon
6. Update Email
7. Kembali ke halaman sebelumnya
======================================
Pilih menu untuk melakukan tindakan terhadap data diatas.
Masukkan input (1-6): ''')
        if update_menu == '1':
            nama_update = input('Masukkan Nama baru: ')
            while len(nama_update)>12 or len(nama_update)<5:
                print('Mohon input ulang (5-12 Karakter)')
                nama_update = input('Masukkan Nama baru (5-12 Karakter): ')
            check2=input(f"Apakah anda yakin ingin menambahkan update Nama? (Y/N): ")
            if check2!="Y" and check2!="Y".lower():
                break
            else:
                directory[update_dir]["Nama"]=nama_update.capitalize()
                read_directory()
                print('\nData berhasil di Update\n')
                break
        elif update_menu == '2':
            kategori_update = input('Masukkan Kategori baru: ')
            while len(kategori_update)>12 or len(kategori_update)<5:
                print('Mohon input ulang (5-12 Karakter)')
                kategori_update = input('Masukkan Nama baru (5-12 Karakter): ')
            check2=input(f"Apakah anda yakin ingin menambahkan update Kategori? (Y/N): ")
            if check2!="Y" and check2!="Y".lower():
                break
            else:
                directory[update_dir]["Kategori"]=kategori_update.capitalize()
                read_directory()
                print('\nData berhasil di Update\n')
                break
        elif update_menu == '3':
            kota_update = input('Masukkan Kota baru (5-12 Karakter): ')
            while len(kota_update)>12 or len(kota_update)<5:
                print('Mohon input ulang(5-12 Karakter)')
                kota_update = input('Masukkan Nama baru (5-12 Karakter): ')
            check2=input(f"Apakah anda yakin ingin menambahkan update Kota? (Y/N): ")
            if check2!="Y" and check2!="Y".lower():
                break
            else:
                directory[update_dir]["Kota"]=kota_update.capitalize()
                read_directory()
                print('\nData berhasil di Update\n')
                break
        elif update_menu == '4':
            alamat_update = input('Masukkan Alamat baru (15-20 Karakter): ')
            while len(alamat_update)>12 or len(alamat_update)<5:
                print('Mohon input ulang(15-20 Karakter)')
                alamat_update = input('Masukkan Nama baru (15-20 Karakter): ')
            check2=input(f"Apakah anda yakin ingin menambahkan update Kota? (Y/N): ")
            if check2!="Y" and check2!="Y".lower():
                break
            else:
                directory[update_dir]["Alamat"]=alamat_update.capitalize()
                read_directory()
                print('\nData berhasil di Update\n')
                break
        elif update_menu == '5':
            while True:
                telepon_update = input('Masukkan Telepon baru (5-12 Karakter): ')
                if telepon_update.isnumeric():
                    while len(telepon_update)>12 or len(telepon_update)<5:
                        print('Mohon input ulang (5-12 Karakter)')
                        telepon_update = input('Masukkan Telepon baru (5-12 Karakter): ')
                    while telepon_update in directory.keys():
                        print('Nomor Telepon sudah ada, silahkan masukkan nomor Telepon baru')
                        telepon_update = input('Masukkan Telepon baru (5-12 Karakter): ')
                    check2=input(f"Apakah anda yakin ingin menambahkan update Telepon? (Y/N): ")
                    if check2!="Y" and check2!="Y".lower():
                        break
                    else:
                        directory[telepon_update] = directory[update_dir]
                        del directory[update_dir]
                        directory[telepon_update]["Telepon"]=telepon_update
                        read_directory()
                        print('\nData berhasil di Update\n')
                        break
                else:
                    print('Input anda salah, Tolong Masukkan Angka')
        elif update_menu == '6':
            email_update = input('Masukkan Email baru (5-12 Karakter): ')
            while len(email_update)>12 or len(email_update)<5:
                print('Mohon input ulang (5-12 Karakter)')
                email_update = input('Masukkan Nama baru (5-12 Karakter): ')
            check2=input(f"Apakah anda yakin ingin menambahkan update Email? (Y/N): ")
            if check2!="Y" and check2!="Y".lower():
                break
            else:
                directory[update_dir]["Email"]=email_update.capitalize()
                read_directory()
                print('\nData berhasil di Update\n')
                break
        elif update_menu == '7':
            break
        else:
            print('Menu yang anda pilih tidak tersedia. Silahkan dicoba lagi')


def main_menu_4():
    delete_menu = input('''
======================================
            Menu Hapus
======================================
1. Hapus Data Tertentu
2. Hapus Semua Data
3. Kembali ke halaman sebelumnya
======================================
Masukkan input (1-3): ''')

    if delete_menu == '1':
        delete_input = input('Masukkan Data yang ingin di Hapus berdasarkan Telepon: ')
        while delete_input in directory.keys():
            check3=input(f"Apakah anda yakin Data akan dihapus {delete_input}? (Y/N): ")
            while check3=="Y" and check3=="Y".lower():
                break
            else:
                del directory[delete_input]
            read_directory()
            print('Data berhasil dihapus')
            break
        else:
            print('Nomor yang anda masukkan tidak ditemukan')
    elif delete_menu == '2':
        check4=input(f"Apakah anda yakin Data akan dihapus? (Y/N): ")
        while check4!="Y" and check4!="Y".lower():
            break
        else:
            directory.clear()
            print('Seluruh Data Berhasil Dihapus')
    elif delete_menu != '1' and delete_menu != '2' and delete_menu != '3':
        print('Menu yang anda pilih tidak tersedia. Silahkan dicoba lagi')
    while delete_menu == '3':
        break
    

while True:
    menu_awal = input('''
======================================
            YP-Directory
======================================
1. Menu Admin
2. Menu Pembaca
3. Keluar Program
======================================
Masukkan Input (1-3) : ''')

    while menu_awal == '1':
        pass_admin = input('Masukkan Password Admin: ')
        if pass_admin == admin:
            main_menu = input('''
======================================
           Main Menu Admin
======================================
1. Tampilkan isi Yellow Pages
2. Tambah isi Yellow Pages 
3. Mengubah isi Yellow Pages
4. Menghapus isi Yellow Pages
5. Kembali ke halaman sebelumnya
======================================
Masukkan Input (1-5): ''')

            if main_menu == '1':
                main_menu_1()

            elif main_menu == '2':
                main_menu_2()

            elif main_menu == '3':
                read_directory()
                main_menu_3()
                
            elif main_menu == '4':
                read_directory()
                main_menu_4()
            
            elif main_menu == '5': 
                break
            else:
                print('Menu yang anda pilih tidak tersedia. Silahkan dicoba lagi')
        else:
            print('Password salah, anda tidak dapat mengakses Menu Admin')
            break

    if menu_awal == '2':
        main_menu_1()
    
    elif menu_awal == '3':
        print('=====================================================\nTerima Kasih Telah Menggunakan Layanan Yellow Pages!\n=====================================================')
        break

    elif menu_awal != 1 and menu_awal != 2 and menu_awal != 3:
        print('Input Salah, Anda akan kembali ke Menu Sebelumnya')