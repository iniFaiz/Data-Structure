import random
import string

    # Define colors
RED = True
BLACK = False

class RedBlackNode():
        def __init__(self, key):
            self.key = key
            self.color = RED  # New nodes are red by default
            self.left = None
            self.right = None
            self.parent = None

        def setLeft(self, left):
            self.left = left
            if left:
                left.parent = self

        def setRight(self, right):
            self.right = right
            if right:
                right.parent = self

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def getValue(self):
            return self.key

class RedBlackTree():
        def __init__(self):
            self.NIL = RedBlackNode(None)
            self.NIL.color = BLACK
            self.NIL.left = self.NIL.right = self.NIL
            self.root = self.NIL

        def add(self, key):
            new_node = RedBlackNode(key)
            new_node.left = new_node.right = self.NIL
            parent = None
            current = self.root

            while current != self.NIL:
                parent = current
                if new_node.key < current.key:
                    current = current.left
                elif new_node.key > current.key:
                    current = current.right
                else:
                    print(f'Key {key} already exists in the tree, duplicates not allowed.\n')
                    return

            new_node.parent = parent
            if parent is None:
                self.root = new_node
            elif new_node.key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node

            new_node.color = RED
            self.fix_insert(new_node)
            print(f'Successfully inserted key {key} into the Red-Black Tree!\n')

        def left_rotate(self, x):
            y = x.right
            x.right = y.left
            if y.left != self.NIL:
                y.left.parent = x

            y.parent = x.parent
            if x.parent is None:
                self.root = y
            elif x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y

            y.left = x
            x.parent = y

        def right_rotate(self, y):
            x = y.left
            y.left = x.right
            if x.right != self.NIL:
                x.right.parent = y

            x.parent = y.parent
            if y.parent is None:
                self.root = x
            elif y == y.parent.right:
                y.parent.right = x
            else:
                y.parent.left = x

            x.right = y
            y.parent = x

        def fix_insert(self, k):
            while k.parent and k.parent.color == RED:
                if k.parent == k.parent.parent.left:
                    u = k.parent.parent.right
                    if u and u.color == RED:
                        k.parent.color = BLACK
                        u.color = BLACK
                        k.parent.parent.color = RED
                        k = k.parent.parent
                    else:
                        if k == k.parent.right:
                            k = k.parent
                            self.left_rotate(k)
                        k.parent.color = BLACK
                        k.parent.parent.color = RED
                        self.right_rotate(k.parent.parent)
                else:
                    u = k.parent.parent.left
                    if u and u.color == RED:
                        k.parent.color = BLACK
                        u.color = BLACK
                        k.parent.parent.color = RED
                        k = k.parent.parent
                    else:
                        if k == k.parent.left:
                            k = k.parent
                            self.right_rotate(k)
                        k.parent.color = BLACK
                        k.parent.parent.color = RED
                        self.left_rotate(k.parent.parent)
                if k == self.root:
                    break
            self.root.color = BLACK

        def contains(self, key):
            node = self.root
            while node != self.NIL:
                if key == node.key:
                    return True
                elif key < node.key:
                    node = node.left
                else:
                    node = node.right
            return False

        def remove(self, key):
            node = self.root
            z = self.NIL
            while node != self.NIL:
                if node.key == key:
                    z = node
                    break
                elif key < node.key:
                    node = node.left
                else:
                    node = node.right

            if z == self.NIL:
                print(f'Key {key} not found in the tree!')
                return

            y = z
            y_original_color = y.color
            if z.left == self.NIL:
                x = z.right
                self.rb_transplant(z, z.right)
            elif z.right == self.NIL:
                x = z.left
                self.rb_transplant(z, z.left)
            else:
                y = self.minimum(z.right)
                y_original_color = y.color
                x = y.right
                if y.parent == z:
                    x.parent = y
                else:
                    self.rb_transplant(y, y.right)
                    y.right = z.right
                    y.right.parent = y
                self.rb_transplant(z, y)
                y.left = z.left
                y.left.parent = y
                y.color = z.color

            if y_original_color == BLACK:
                self.fix_delete(x)
            print(f'Key {key} has been removed from the tree!')

        def rb_transplant(self, u, v):
            if u.parent == None:
                self.root = v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            v.parent = u.parent

        def fix_delete(self, x):
            while x != self.root and x.color == BLACK:
                if x == x.parent.left:
                    s = x.parent.right
                    if s.color == RED:
                        s.color = BLACK
                        x.parent.color = RED
                        self.left_rotate(x.parent)
                        s = x.parent.right

                    if s.left.color == BLACK and s.right.color == BLACK:
                        s.color = RED
                        x = x.parent
                    else:
                        if s.right.color == BLACK:
                            s.left.color = BLACK
                            s.color = RED
                            self.right_rotate(s)
                            s = x.parent.right

                        s.color = x.parent.color
                        x.parent.color = BLACK
                        s.right.color = BLACK
                        self.left_rotate(x.parent)
                        x = self.root
                else:
                    s = x.parent.left
                    if s.color == RED:
                        s.color = BLACK
                        x.parent.color = RED
                        self.right_rotate(x.parent)
                        s = x.parent.left

                    if s.left.color == BLACK and s.right.color == BLACK:
                        s.color = RED
                        x = x.parent
                    else:
                        if s.left.color == BLACK:
                            s.right.color = BLACK
                            s.color = RED
                            self.left_rotate(s)
                            s = x.parent.left

                        s.color = x.parent.color
                        x.parent.color = BLACK
                        s.left.color = BLACK
                        self.right_rotate(x.parent)
                        x = self.root
            x.color = BLACK

        def minimum(self, node):
            while node.left != self.NIL:
                node = node.left
            return node

        def in_order(self):
            def traverse(node):
                if node != self.NIL:
                    traverse(node.left)
                    print(f'{node.key}{"(R)" if node.color == RED else "(B)"}', end=' ')
                    traverse(node.right)
            traverse(self.root)
            print()

        def pre_order(self):
            def traverse(node):
                if node != self.NIL:
                    print(f'{node.key}{"(R)" if node.color == RED else "(B)"}', end=' ')
                    traverse(node.left)
                    traverse(node.right)
            traverse(self.root)
            print()

        def post_order(self):
            def traverse(node):
                if node != self.NIL:
                    traverse(node.left)
                    traverse(node.right)
                    print(f'{node.key}{"(R)" if node.color == RED else "(B)"}', end=' ')
            traverse(self.root)
            print()

        def height(self):
            def node_height(node):
                if node == self.NIL:
                    return 0
                left_height = node_height(node.left)
                right_height = node_height(node.right)
                return 1 + max(left_height, right_height)
            return node_height(self.root)

        def depth(self, key):
            def get_depth(node, key, current_depth):
                if node == self.NIL:
                    return -1
                if node.key == key:
                    return current_depth
                elif key < node.key:
                    return get_depth(node.left, key, current_depth + 1)
                else:
                    return get_depth(node.right, key, current_depth + 1)
            return get_depth(self.root, key, 1)

        def add_random_nodes(self, count=10):
            for _ in range(count):
                key = random.choice(string.ascii_uppercase)
                self.add(key)
            print(f"{count} random keys added to the tree.\n")

def menu():
        tree = RedBlackTree()
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
                        print(f"Key {key} tidak ditemukan di Tree.")
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
