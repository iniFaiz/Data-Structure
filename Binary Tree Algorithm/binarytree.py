import random
import string

class Node():
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def setRight(self, ri):
        self.right = ri

    def setLeft(self, le):
        self.left = le

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getValue(self):
        return self.key


class Tree():
    def __init__(self):
        self.root = None

    def add(self, key):
        newNode = Node(key)
        if self.root is None:
            self.root = newNode
            print(f'Berhasil insert key bernilai {key} ke Tree!\n')
            return

        sem = self.root
        if self.contains(key):
            print(f'key dengan nilai {key} sudah ada di Tree, tidak boleh ada duplikat\n')
            return
        else:
            while True:
                if key < sem.getValue():
                    if sem.getLeft() is None:
                        sem.setLeft(newNode)
                        print(f'Berhasil insert key bernilai {key} ke Tree!\n')
                        return
                    sem = sem.getLeft()
                else:
                    if sem.getRight() is None:
                        sem.setRight(newNode)
                        print(f'Berhasil insert key bernilai {key} ke Tree!\n')
                        return
                    sem = sem.getRight()

    def contains(self, key):
        sem = self.root
        while sem:
            if key == sem.getValue():
                return True
            sem = sem.getLeft() if key < sem.getValue() else sem.getRight()
        return False

    def remove(self, key):
        def remove_node(node, key):
            if node is None:
                return node

            if key < node.getValue():
                node.setLeft(remove_node(node.getLeft(), key))
            elif key > node.getValue():
                node.setRight(remove_node(node.getRight(), key))
            else:
                if node.getLeft() is None:
                    return node.getRight()
                elif node.getRight() is None:
                    return node.getLeft()
                sem = self.find_min(node.getRight())
                node.key = sem.key
                node.setRight(remove_node(node.getRight(), sem.key))
            return node

        if self.contains(key):
            self.root = remove_node(self.root, key)
            print(f'key dengan nilai {key} berhasil dihapus dari Tree!')
        else:
            print(f'key dengan nilai {key} tidak ditemukan di Tree!')

    def find_min(self, node):
        sem = node
        while sem.getLeft():
            sem = sem.getLeft()
        return sem

    def in_order(self):
        def display_in_order(node):
            if node:
                display_in_order(node.getLeft())
                print(node.getValue(), end=' ')
                display_in_order(node.getRight())
        display_in_order(self.root)
        print()

    def post_order(self):
        def post_order_traversal(node):
            if node:
                post_order_traversal(node.getLeft())
                post_order_traversal(node.getRight())
                print(node.getValue(), end=' ')

        post_order_traversal(self.root)
        print()

    def pre_order(self):
        def pre_order_traversal(node):
            if node:
                print(node.getValue(), end=' ')
                pre_order_traversal(node.getLeft())
                pre_order_traversal(node.getRight())

        pre_order_traversal(self.root)
        print()


    def height(self):
        def node_height(node):
            if node is None:
                return 0
            left_height = node_height(node.getLeft())
            right_height = node_height(node.getRight())
            return 1 + max(left_height, right_height)

        return node_height(self.root)
    
    def add_random_nodes(self, count=10):
        for _ in range(count):
            key = random.choice(string.ascii_uppercase)
            self.add(key)
        print(f"{count} random key added to the tree.\n")
        
    def depth(self, key):
        def get_depth(node, key, current_depth):
            if node is None:
                return -1
            if node.getValue() == key:
                return current_depth
            elif key < node.getValue():
                return get_depth(node.getLeft(), key, current_depth + 1)
            else:
                return get_depth(node.getRight(), key, current_depth + 1)
        
        return get_depth(self.root, key, 1)

def menu():
    tree = Tree()
    while True:
        print("\nMenu:")
        print("1. Tambah key")
        print("2. Hapus key")
        print("3. Tampilkan Tinggi Tree")
        print("4. Tambah 10 key Random")
        print("5. Cari Depth key")
        print("6. Tampilkan Tree (In-order)")
        print("7. Tampilkan Tree (Pre-order)")
        print("8. Tampilkan Tree (Post-order)")
        print("9. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            key = input("Masukkan nilai key yang akan ditambahkan: ")
            if len(key) != 1:
                print("Harap masukkan satu karakter.")
            else:
                tree.add(key)
        elif choice == '2':
            key = input("Masukkan nilai key yang akan dihapus: ")
            if len(key) != 1:
                print("Harap masukkan satu karakter.")
            else:
                tree.remove(key)
        elif choice == '3':
            print(f"Tinggi Tree: {tree.height()}")
        elif choice == '4':
            tree.add_random_nodes()
        elif choice == '5':
            key = input("Masukkan nilai key yang ingin dicari depth-nya: ")
            if len(key) != 1:
                print("Harap masukkan satu karakter.")
            else:
                depth = tree.depth(key)
                if depth != -1:
                    print(f"Depth key {key} adalah {depth}")
                else:
                    print(f"key {key} tidak ditemukan di Tree.")
        elif choice == '6':
            print("In-order traversal:")
            tree.in_order()
        elif choice == '7':
            print("Pre-order traversal:")
            tree.pre_order()
        elif choice == '8':
            print("Post-order traversal:")
            tree.post_order()
        elif choice == '9':
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()
