from prettytable import PrettyTable
import os

os.system('cls')

class MenuItem:
    def __init__(self, name, price, prev_item=None, next_item=None):
        self.name = name
        self.price = price
        self.prev_item = prev_item
        self.next_item = next_item

class Menu:
    def __init__(self):
        self.food_head = None
        self.food_tail = None
        self.drink_head = None
        self.drink_tail = None

    def insert_item(self, category, name, price):
        new_item = MenuItem(name, price)

        if category == "food":
            head = self.food_head
            tail = self.food_tail
        elif category == "drink":
            head = self.drink_head
            tail = self.drink_tail
        else:
            print("Kategori tidak valid. Silakan coba lagi.")
            return

        if head is None:
            head = new_item
            tail = new_item
        else:
            tail.next_item = new_item
            new_item.prev_item = tail
            tail = new_item

        if category == "food":
            self.food_head = head
            self.food_tail = tail
        elif category == "drink":
            self.drink_head = head
            self.drink_tail = tail

    def remove_item(self, category, name):
        if category == "food":
            current_item = self.food_head
            tail = self.food_tail
        elif category == "drink":
            current_item = self.drink_head
            tail = self.drink_tail
        else:
            print("Kategori tidak valid. Silakan coba lagi.")
            return

        while current_item:
            if current_item.name == name:
                if current_item.prev_item:
                    current_item.prev_item.next_item = current_item.next_item
                else:
                    if category == "food":
                        self.food_head = current_item.next_item
                    elif category == "drink":
                        self.drink_head = current_item.next_item
                if current_item.next_item:
                    current_item.next_item.prev_item = current_item.prev_item
                else:
                    if category == "food":
                        self.food_tail = current_item.prev_item
                    elif category == "drink":
                        self.drink_tail = current_item.prev_item
                print(f"{name} telah dihapus dari menu {category}.")
                return
            current_item = current_item.next_item
        print(f"{name} tidak ditemukan pada menu {category}.")

    def display_menu(self, category):
        if category == "food":
            head = self.food_head
        elif category == "drink":
            head = self.drink_head
        else:
            print("Kategori tidak valid. Silakan coba lagi.")
            return

        table = PrettyTable()
        table.field_names = ["Nama Item", "Harga"]
        current_item = head
        while current_item:
            table.add_row([current_item.name, f"Rp {current_item.price}"])
            current_item = current_item.next_item

        print(f"Menu {category.capitalize()}:")
        print(table)

food_menu = Menu()
food_menu.insert_item("food", "Nasi Goreng", 10000)
food_menu.insert_item("food", "Mie Goreng", 8000)
food_menu.insert_item("food", "Ayam Goreng", 12000)
food_menu.insert_item("food", "Sate", 15000)
food_menu.insert_item("food", "Tahu Goreng", 5000)

drink_menu = Menu()
drink_menu.insert_item("drink", "Es Teh", 3000)
drink_menu.insert_item("drink", "Es Jeruk", 5000)
drink_menu.insert_item("drink", "Kopi", 6000)
drink_menu.insert_item("drink", "Redvelvet", 10000)

a = "y"
while (a == "y"):
    print("===============================")
    print("|   Program Menu Restaurant   |")
    print("===============================")
    print("1. Tampilkan menu makanan")
    print("2. Tampilkan menu minuman")
    print("3. Tambah item pada menu")
    print("4. Hapus item dari menu")
    print("5. Cari item pada menu")
    print("6. Keluar dari program")
    print("===============================")
    
    pilih = input("\nMasukkan pilihan Anda (1/2/3/4/5/6): ")
    
    if pilih == "1":
        food_menu.display_menu("food")
        a = input("Kembali ke menu [y/t] : ")
        os.system('cls')
    elif pilih == "2":
        drink_menu.display_menu("drink")
        a = input("Kembali ke menu [y/t] : ")
        os.system('cls')
    elif pilih == "3":
        category = input("Masukkan kategori item baru (food/drink): ")
        name = input("Masukkan nama item baru: ")
        price = input("Masukkan harga item baru: ")
        if not price.isdigit():
            print("Harga harus berupa angka. Silakan coba lagi.")
            continue
        if category == "food":
            food_menu.insert_item("food", name, int(price))
        elif category == "drink":
            drink_menu.insert_item("drink", name, int(price))
        else:
            print("Kategori tidak valid. Silakan coba lagi.")
            continue
        print(f"{name} telah ditambahkan pada menu {category}.")
        a = input("Kembali ke menu [y/t] : ")
        os.system('cls')
    elif pilih == "4":
        category = input("Masukkan kategori item yang akan dihapus (food/drink): ")
        if category == "food":
            food_menu.display_menu("food")
            name = input("Masukkan nama item yang akan dihapus: ")
            food_menu.remove_item("food", name)
        elif category == "drink":
            drink_menu.display_menu("drink")
            name = input("Masukkan nama item yang akan dihapus: ")
            drink_menu.remove_item("drink", name)
        else:
            print("Kategori tidak valid. Silakan coba lagi.")
            continue
        a = input("Kembali ke menu [y/t] : ")
        os.system('cls')
    elif pilih == "5":
        query = input("Masukkan nama item yang ingin dicari: ")
        found = False
        for category in ["food", "drink"]:
            if category == "food":
                head = food_menu.food_head
            elif category == "drink":
                head = drink_menu.drink_head
            else:
                print("Kategori tidak valid. Silakan coba lagi.")
                continue
            current_item = head
            while current_item:
                if query.lower() in current_item.name.lower():
                    if not found:
                        table = PrettyTable()
                        table.field_names = ["Nama Item", "Harga"]
                    found = True
                    table.add_row([current_item.name, f"Rp {current_item.price}"])
                current_item = current_item.next_item
        if found:
            print(f"Hasil pencarian untuk '{query}':")
            print(table)
        else:
            print(f"'{query}' tidak ditemukan pada menu.")
        a = input("Kembali ke menu [y/t] : ")
        os.system('cls')
    elif pilih == "6":
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        break
    else:
        if a == "t":
            break
        else :
            print("Pilihan tidak valid. Silakan coba lagi.")