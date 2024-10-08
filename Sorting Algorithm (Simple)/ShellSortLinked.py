import random
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def swap(self, index1, index2):
        if index1 == index2:
            return

        prev1 = None
        curr1 = self.head
        for _ in range(index1):
            if not curr1:
                return
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        for _ in range(index2):
            if not curr2:
                return
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    def remove_at_index(self, index):
        if not self.head:
            return None

        current = self.head

        if index == 0:
            self.head = current.next
            return current.data

        for i in range(index - 1):
            current = current.next
            if current is None:
                return None

        if current.next is None:
            return None

        removed_node = current.next
        current.next = current.next.next

        return removed_node.data

    def to_list(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr

    def from_list(self, arr):
        self.head = None
        for item in arr:
            self.append(item)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def shell_sort_linked_list(linked_list):
    arr = linked_list.to_list()
    swap_count = 0
    comparison_count = 0
    loop_count = 0
    waktu_awal = time.time()
    
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                loop_count += 1
                swap_count += 1
                # print(f"Swap: {arr[j]} <-> {arr[j + gap]}, index: {arr}")
            arr[j] = temp
            loop_count += 1
            if j >= gap:
                comparison_count += 1
                # print(f"Comparison: {temp} <-> {arr[j - gap]}, index: {arr}")
        gap //= 2
    
    waktu_akhir = time.time()
    waktu = waktu_akhir - waktu_awal
    linked_list.from_list(arr)
    return swap_count, comparison_count, loop_count, waktu

def input_reversed_data():
    n = int(input("Masukkan jumlah elemen: "))
    linked_list = LinkedList()
    for i in range(n, 0, -1):
        linked_list.append(i)
    return linked_list

def input_almost_sorted_data():
    n = int(input("Masukkan jumlah elemen: "))
    linked_list = LinkedList()
    arr = list(range(1, n + 1))
    if n > 2:
        for i in range(1, min(5, n)):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    linked_list.from_list(arr)
    return linked_list

def input_random_data():
    n = int(input("Masukkan jumlah elemen: "))
    linked_list = LinkedList()
    for _ in range(n):
        linked_list.append(random.randint(1, 10000))
    return linked_list

def main():
    linked_list = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Input data yang terbalik ke linked list")
        print("2. Input data yang hampir ter-sort ke linked list")
        print("3. Input data random ke linked list")
        print("4. Sort data dalam linked list")
        print("5. Exit")
        print("6. Lihat linked list")
        print("7. Push data ke linked list")
        print("8. Pop data dari linked list")
        print("9. Swap dua elemen dalam linked list")
        print("10. Remove data dari linked list berdasarkan index")
        choice = int(input("Pilih opsi: "))

        if choice == 1:
            linked_list = input_reversed_data()
            print("Linked list saat ini:")
            linked_list.print_list()
        elif choice == 2:
            linked_list = input_almost_sorted_data()
            print("Linked list saat ini:")
            linked_list.print_list()
        elif choice == 3:
            linked_list = input_random_data()
            print("Linked list saat ini:")
            linked_list.print_list()
        elif choice == 4:
            if linked_list.head:
                swap_count, comparison_count, loop_count, waktu = shell_sort_linked_list(linked_list)
                print("Linked list setelah diurutkan:")
                linked_list.print_list()
                # print(f"Total loop: {loop_count}")
                print(f"Jumlah swap: {swap_count}")
                # print(f"Jumlah perbandingan: {comparison_count}")
                # print(f"Waktu yang dibutuhkan untuk mengurutkan: {waktu:.6f} detik")
            else:
                print("Linked list kosong, silakan input data terlebih dahulu.")
        elif choice == 5:
            break
        elif choice == 6:
            if linked_list.head:
                print("Linked list saat ini:")
                linked_list.print_list()
            else:
                print("Linked list kosong, silakan input data terlebih dahulu.")
        elif choice == 7:
            data = int(input("Masukkan data yang ingin di-push: "))
            linked_list.push(data)
            print("Linked list saat ini:")
            linked_list.print_list()
        elif choice == 8:
            popped_data = linked_list.pop()
            if popped_data is not None:
                print(f"Data yang di-pop: {popped_data}")
            else:
                print("Linked list kosong, tidak ada data untuk di-pop.")
            print("Linked list saat ini:")
            linked_list.print_list()
        elif choice == 9:
            index1 = int(input("Masukkan index pertama: "))
            index2 = int(input("Masukkan index kedua: "))
            linked_list.swap(index1, index2)
            print("Linked list setelah swap:")
            linked_list.print_list()
        elif choice == 10:
            index = int(input("Masukkan index yang ingin dihapus: "))
            removed_data = linked_list.remove_at_index(index)
            if removed_data is not None:
                print(f"Data yang dihapus: {removed_data}")
            else:
                print("Index tidak valid.")
            print("Linked list saat ini:")
            linked_list.print_list()
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
      
if __name__ == "__main__":
    main()
