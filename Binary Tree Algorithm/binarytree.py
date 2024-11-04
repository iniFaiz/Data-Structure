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
            print(f'Berhasil insert Node bernilai {key} ke Tree!\n')
            return

        sem = self.root
        if self.contains(key):
            print(f'Node dengan nilai {key} sudah ada di Tree, tidak boleh ada duplikat\n')
            return
        else:
            while True:
                if key < sem.getValue():
                    if sem.getLeft() is None:
                        sem.setLeft(newNode)
                        print(f'Berhasil insert Node bernilai {key} ke Tree!\n')
                        return
                    sem = sem.getLeft()
                else:
                    if sem.getRight() is None:
                        sem.setRight(newNode)
                        print(f'Berhasil insert Node bernilai {key} ke Tree!\n')
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
                node.setRight(remove_node(node.getRight(), sem))
            return node

        if self.contains(key):
            self.root = remove_node(self.root, key)
            print(f'Node dengan nilai {key} berhasil dihapus dari Tree!')
        else:
            print(f'Node dengan nilai {key} tidak ditemukan di Tree!')

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


def menu():
    tree = Tree()
    while True:
        print("\nMenu:")
        print("1. Tambah Node")
        print("2. Hapus Node")
        print("3. Tampilkan Tree (In-order)")
        print("4. Tampilkan Tree (Pre-order)")
        print("5. Tampilkan Tree (Post-order)")
        print("6. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            key = int(input("Masukkan nilai Node yang akan ditambahkan: "))
            tree.add(key)
        elif choice == '2':
            key = int(input("Masukkan nilai Node yang akan dihapus: "))
            tree.remove(key)
        elif choice == '3':
            print("In-order traversal:")
            tree.in_order()
        elif choice == '4':
            print("Pre-order traversal:")
            tree.pre_order()
        elif choice == '5':
            print("Post-order traversal:")
            tree.post_order()
        elif choice == '6':
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()
