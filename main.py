import os
import pyautogui
import sqlite3
from time import sleep

def clear_screen():
    os.system("cls")

def menu_header(text):
    print("\n>  " + text + "  <\n")

def listFormat():
    print("Liste Formatı: İsim, Soyisim, Doğum Tarihi, Telefon Numarası, Okuduğu Kitap\n")

def menu():
    menu_header("Ana Menü")
    print("[1] Üye Kayıt Et")
    print("[2] Üye Kayıt Sil")
    print("[3] Üye Bilgi Güncelle")
    print("[4] Üye Sorgula")
    print("[5] Bütün Üyeleri Listele")
    print("[6] Üyeye Kitap Ver\n")

def add_user():
    menu_header("Üye Kayıt Et")

    register_user_first_name = input("İsim: ")
    register_user_second_name = input("Soyisim: ")
    register_user_birth_date = input("Doğum Tarihi(Gün/Ay/Yıl): ")
    register_user_phone_number = input("Telefon Numarası: 0")
    register_user_book_name = ""

    if len(register_user_phone_number) == 10 and len(register_user_birth_date) == 10:
        with sqlite3.connect("Üyeler.db") as connect:
            cursor = connect.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS Üyeler(İsim TEXT, Soyisim TEXT, Doğum_Tarihi TEXT, Telefon_Numarası TEXT, Okuduğu_Kitap TEXT)")
            cursor.execute("INSERT INTO Üyeler VALUES('{}', '{}', '{}', '0{}', '{}')".format(register_user_first_name, register_user_second_name, register_user_birth_date, register_user_phone_number, register_user_book_name))
            connect.commit()
            clear_screen()
            print("(!) Üye kayıt edildi.")
            sleep(3)
            clear_screen()
            
    else:
        pyautogui.alert("1 - Telefon numarasında boşluk kullanmayınız.\n2 - Doğum tarihi örnek format: 01/01/2000", title="Hata")
        clear_screen()

def delete_user():
    menu_header("Üye Kayıt Sil")

    delete_user_phone_number = input("Silinecek üyenin telefon numarasını girin: ")

    with sqlite3.connect("Üyeler.db") as connect:
        cursor = connect.cursor()
        cursor.execute("DELETE FROM Üyeler WHERE Telefon_Numarası = '{}'".format(delete_user_phone_number))
        connect.commit()
        clear_screen()
        print("(!) Üyenin kaydı silindi.")
        sleep(3)
        clear_screen()

def update_user():
    menu_header("Üye Bilgi Güncelle")

    print("[1 - İsim]  [2 - Soyisim]  [3 - Doğum Tarihi]  [4 - Telefon Numarası]  [5 - Okuduğu Kitap ]\n")
    update_user_change_type = input("Üyenin hangi bilgisini güncellemek istersiniz: ")
    update_user_change_varieble = input("Üyenin yeni bilgisi ne olucak: ")
    update_user_phone_number = input("Bilgisi güncellenicek üyenin telefon numarasını girin: ")

    with sqlite3.connect("Üyeler.db") as connect:
        cursor = connect.cursor()
        
        match update_user_change_type:
            case "1":
                cursor.execute("UPDATE Üyeler SET İsim = '{}' WHERE Telefon_Numarası = '{}'".format(update_user_change_varieble, update_user_phone_number))
            case "2":
                cursor.execute("UPDATE Üyeler SET Soyisim = '{}' WHERE Telefon_Numarası = '{}'".format(update_user_change_varieble, update_user_phone_number))
            case "3":
                cursor.execute("UPDATE Üyeler SET Doğum_Tarihi = '{}' WHERE Telefon_Numarası = '{}'".format(update_user_change_varieble, update_user_phone_number))
            case "4":
                cursor.execute("UPDATE Üyeler SET Telefon_Numarası = '{}' WHERE Telefon_Numarası = '{}'".format(update_user_change_varieble, update_user_phone_number))
            case "5":
                cursor.execute("UPDATE Üyeler SET Okuduğu_Kitap = '{}' WHERE Telefon_Numarası = '{}'".format(update_user_change_varieble, update_user_phone_number))
            case _:
                pyautogui.alert("Geçersiz karakter.", title="Hata")

        connect.commit()
        clear_screen()
        print("(!) Üyenin bilgileri güncellendi.")
        sleep(3)
        clear_screen()

def search_user():
    menu_header("Üye Sorgula")

    print("[1 - İsim]  [2 - Soyisim]  [3 - Doğum Tarihi]  [4 - Telefon Numarası]  [5 - Okuduğu Kitap ]\n")
    search_type = input("Arama tipini girin: ")
    search_varieble = input("Bilgiyi girin: ")

    with sqlite3.connect("Üyeler.db") as connect:
        cursor = connect.cursor()

        match search_type:
            case "1":
                cursor.execute("SELECT * from Üyeler WHERE İsim == '{}'".format(search_varieble))
            case "2":
                cursor.execute("SELECT * from Üyeler WHERE Soyisim == '{}'".format(search_varieble))
            case "3":
                cursor.execute("SELECT * from Üyeler WHERE Doğum_Tarihi == '{}'".format(search_varieble))
            case "4":
                cursor.execute("SELECT * from Üyeler WHERE Telefon_Numarası == '{}'".format(search_varieble))
            case "5":
                cursor.execute("SELECT * from Üyeler WHERE Okuduğu_Kitap == '{}'".format(search_varieble))
            case _:
                pyautogui.alert("Geçersiz karakter.", title="Hata")
        
        clear_screen()
        listFormat()
        
        for data in cursor.fetchall():
            print(data)

        connect.commit()
        want_exit = input("\nÇıkmak için herhangi bir rakam veya harf girin: ")

        if want_exit == 1:
            main()
        else:
            main()

def list_all_users():
    menu_header("Bütün Üyeleri Listele")
    listFormat()

    with sqlite3.connect("Üyeler.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * from Üyeler")

        for data in cursor.fetchall():
            print(data)

        connect.commit()
        want_exit = input("\nÇıkmak için herhangi bir rakam veya harf girin: ")

        if want_exit == 1:
            main()
        else:
            main() 

def give_book_user():
    menu_header("Üyeye Kitap Ver")

    give_book_user_phone_number = input("Kitap verilecek üyenin telefon numarasını girin: ")
    give_book_user_book_name = input("Üyeye verilecek kitap ismini girin: ")

    with sqlite3.connect("Üyeler.db") as connect:
        cursor = connect.cursor()
        cursor.execute("UPDATE Üyeler SET Okuduğu_Kitap = '{}' WHERE Telefon_Numarası = '{}'".format(give_book_user_book_name, give_book_user_phone_number))
        connect.commit()
        clear_screen()
        print("(!) Üyeye kitap verildi.")
        sleep(3)
        clear_screen()

def main():
    while True:
        clear_screen()
        menu()

        process_choice = input("> ")
        match process_choice:
            case "1":
                clear_screen()
                add_user()
            case "2":
                clear_screen()
                delete_user()
            case "3":
                clear_screen()
                update_user()
            case "4":
                clear_screen()
                search_user()
            case "5":
                clear_screen()
                list_all_users()
            case "6":
                clear_screen()
                give_book_user()
            case _:
                pyautogui.alert("Geçersiz karakter.", title="Hata")

main()