import random
import time

def insertion_sort(arr):
  # waktu_awal = time.time()
  # swap_count = 0
  # comparison_count = 0
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      # comparison_count += 1
      arr[j + 1] = arr[j]
      j -= 1
      # swap_count += 1
    #   print(f"Swap: {arr[j+1]} <-> {arr[j+2]}, Array: {arr}")
    arr[j + 1] = key
    # if j >= 0:
    #   comparison_count += 1
      # print(f"Comparison: {key} <-> {arr[j]}, Array: {arr}")
  # return swap_count, comparison_count
    # print(arr)
  # global waktu
  # waktu_akhir = time.time()
  # waktu = waktu_akhir - waktu_awal



# def insertion_sort_reverse(arr):
#   for i in range(1, len(arr)):
#     key = arr[i]
#     j = i - 1
#     while j >= 0 and key > arr[j]:
#       arr[j + 1] = arr[j]
#       j -= 1
#     arr[j + 1] = key

def print_array(arr):
  for i in range(len(arr)):
    print(arr[i], end=" ")
  print()

def input_reversed_data():
  n = int(input("Masukkan jumlah elemen: "))
  arr = list(range(n, 0, -1))
  return arr

def input_almost_sorted_data():
  n = int(input("Masukkan jumlah elemen: "))
  arr = list(range(1, n + 1))
  if n > 2:
    # Introduce more swaps to make the array "almost sorted"
    for i in range(1, min(5, n)):
      arr[i], arr[i - 1] = arr[i - 1], arr[i]
  return arr

def input_random_data():
  n = int(input("Masukkan jumlah elemen: "))
  arr = [random.randint(1, 1000) for _ in range(n)]
  return arr

def main():
  arr = []
  while True:
    print("\nMenu:")
    print("1. Input data yang terbalik ke array")
    print("2. Input data yang hampir ter-sort ke array")
    print("3. Input data random ke array")
    print("4. Sort data dalam array")
    print("5. Exit")
    choice = int(input("Pilih opsi: "))

    if choice == 1:
      arr = input_reversed_data()
      print("Array saat ini:")
      print_array(arr)
    elif choice == 2:
      arr = input_almost_sorted_data()
      print("Array saat ini:")
      print_array(arr)
    elif choice == 3:
      arr = input_random_data()
      print("Array saat ini:")
      print_array(arr)
    elif choice == 4:
      if arr:
        # swap_count, comparison_count = insertion_sort(arr)
        insertion_sort(arr)
        print("Array setelah diurutkan:")
        print_array(arr)
        # print(f"Jumlah swap: {swap_count}")
        # print(f"Jumlah perbandingan: {comparison_count}")
        # print(f"Waktu yang dibutuhkan untuk mengurutkan: {waktu:.6f} detik")
      else:
        print("Array kosong, silakan input data terlebih dahulu.")
    elif choice == 5:
      break
    else:
      print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
  main()
