import customtkinter as ctk
import tkinter as tk
import subprocess
import os
import random
from PIL import Image, ImageTk
from tkinter import Toplevel
from tkinter import messagebox

class Node:
    def __init__(self, key, value, color='red', left=None, right=None, parent=None):
        self.key = key            # Indonesia
        self.value = value        # English
        self.color = color
        self.left = left          
        self.right = right       
        self.parent = parent      

# Red-Black Tree
class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, None, color='black') 
        self.root = self.NIL

    def insert(self, key, value):
        node = Node(key, value, left=self.NIL, right=self.NIL)
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent == None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = 'red'
        self.fix_insert(node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
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
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def search(self, key):
        current = self.root
        while current != self.NIL and key != current.key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current

    def inorder(self, node, result):
        if node != self.NIL:
            self.inorder(node.left, result)
            result.append((node.key, node.value))
            self.inorder(node.right, result)

    def search_prefix(self, prefix):
        result = []
        self._search_prefix_helper(self.root, prefix, result)
        return result

    def _search_prefix_helper(self, node, prefix, result):
        if node != self.NIL:
            self._search_prefix_helper(node.left, prefix, result)
            if node.key.startswith(prefix):
                result.append(node.key)
            self._search_prefix_helper(node.right, prefix, result)

    def get(self, key):
        node = self._search(self.root, key)
        if node != self.NIL:
            return node.value
        return None

    def _search(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

dictionary_data = [
    # A
    ('anak', 'child'),
    ('api', 'fire'),
    ('air', 'water'),
    ('ayam', 'chicken'),
    ('alamat', 'address'),
    ('antara', 'between'),
    ('asing', 'foreign'),
    ('almari', 'cupboard'),
    ('alat', 'tool'),
    ('anjing', 'dog'),

    # B
    ('buku', 'book'),
    ('bunga', 'flower'),
    ('besar', 'big'),
    ('bola', 'ball'),
    ('burung', 'bird'),
    ('baju', 'shirt'),
    ('bulan', 'moon'),
    ('buah', 'fruit'),
    ('beras', 'rice'),
    ('bensin', 'gasoline'),

    # C
    ('cinta', 'love'),
    ('cahaya', 'light'),
    ('cermin', 'mirror'),
    ('cokelat', 'chocolate'),
    ('cap', 'cap'),
    ('cerita', 'story'),
    ('coretan', 'scribble'),
    ('cuaca', 'weather'),
    ('cabang', 'branch'),
    ('cacing', 'worm'),

    # D
    ('dalam', 'in'),
    ('dapur', 'kitchen'),
    ('daun', 'leaf'),
    ('daging', 'meat'),
    ('domba', 'sheep'),
    ('dokter', 'doctor'),
    ('dalami', 'deeply'),
    ('danau', 'lake'),
    ('daftar', 'list'),
    ('daya', 'power'),

    # E
    ('empat', 'four'),
    ('ekor', 'tail'),
    ('emas', 'gold'),
    ('ekonomi', 'economy'),
    ('elastis', 'elastic'),
    ('emosi', 'emotion'),
    ('energi', 'energy'),
    ('endal', 'slander'),
    ('enteng', 'lightweight'),
    ('eritrea', 'Eritrea'),

    # F
    ('fajar', 'dawn'),
    ('foto', 'photo'),
    ('film', 'movie'),
    ('fasilitas', 'facility'),
    ('faktor', 'factor'),
    ('festival', 'festival'),
    ('fibra', 'fiber'),
    ('finite', 'finite'),
    ('fitness', 'fitness'),
    ('flat', 'flat'),

    # G
    ('gunung', 'mountain'),
    ('gula', 'sugar'),
    ('gedung', 'building'),
    ('gitar', 'guitar'),
    ('gelas', 'glass'),
    ('gerakan', 'movement'),
    ('gerai', 'stall'),
    ('gambar', 'picture'),
    ('gembira', 'happy'),
    ('gigi', 'tooth'),

    # H
    ('hutan', 'forest'),
    ('hari', 'day'),
    ('haus', 'thirsty'),
    ('hewan', 'animal'),
    ('hidup', 'life'),
    ('hujan', 'rain'),
    ('hiasan', 'decoration'),
    ('hati', 'heart'),
    ('hidangan', 'dish'),
    ('helikopter', 'helicopter'),

    # I
    ('ibu', 'mother'),
    ('ikan', 'fish'),
    ('indah', 'beautiful'),
    ('isi', 'content'),
    ('internet', 'internet'),
    ('inggris', 'English'),
    ('idaman', 'ideal'),
    ('ikat', 'tie'),
    ('ilmu', 'science'),
    ('ikon', 'icon'),

    # J
    ('jalan', 'road'),
    ('jari', 'finger'),
    ('jam', 'clock'),
    ('jarum', 'needle'),
    ('jembatan', 'bridge'),
    ('jahitan', 'sewing'),
    ('jendela', 'window'),
    ('jarang', 'rare'),
    ('jaringan', 'network'),
    ('jatuh', 'fall'),

    # K
    ('kota', 'city'),
    ('kucing', 'cat'),
    ('kertas', 'paper'),
    ('kursi', 'chair'),
    ('kunci', 'key'),
    ('kelapa', 'coconut'),
    ('kaki', 'foot'),
    ('kantor', 'office'),
    ('kamera', 'camera'),
    ('kapal', 'ship'),
    ('kalkulator', 'calculator'),
    ('keluar', 'exit'),

    # L
    ('laut', 'sea'),
    ('lembah', 'valley'),
    ('lingkungan', 'environment'),
    ('lima', 'five'),
    ('lampu', 'lamp'),
    ('lama', 'old'),
    ('limbah', 'waste'),
    ('lari', 'run'),
    ('ladang', 'field'),
    ('leher', 'neck'),

    # M
    ('matahari', 'sun'),
    ('mobil', 'car'),
    ('masakan', 'cuisine'),
    ('meja', 'table'),
    ('minuman', 'drink'),
    ('makanan', 'food'),
    ('medan', 'field'),
    ('menara', 'tower'),
    ('morfin', 'morphine'),
    ('musik', 'music'),

    # N
    ('nasi', 'rice'),
    ('nenek', 'grandmother'),
    ('nomor', 'number'),
    ('nasi goreng', 'fried rice'),
    ('negara', 'country'),
    ('nelayan', 'fisherman'),
    ('nikah', 'marriage'),
    ('noda', 'stain'),
    ('nama', 'name'),
    ('nilai', 'value'),

    # O
    ('orang', 'person'),
    ('ongkir', 'shipping cost'),
    ('obat', 'medicine'),
    ('opel', 'Opel'),
    ('organisasi', 'organization'),
    ('olahraga', 'sport'),
    ('optimis', 'optimistic'),
    ('opera', 'opera'),
    ('obrolan', 'conversation'),
    ('oksigen', 'oxygen'),

    # P
    ('pohon', 'tree'),
    ('pintu', 'door'),
    ('paket', 'package'),
    ('pesawat', 'airplane'),
    ('pelajar', 'student'),
    ('perahu', 'boat'),
    ('pakaian', 'clothes'),
    ('pulau', 'island'),
    ('pizza', 'pizza'),
    ('penyanyi', 'singer'),

    # Q
    ('quran', 'Quran'),
    ('qualitas', 'quality'),
    ('quad', 'quad'),
    ('quantum', 'quantum'),
    ('quasar', 'quasar'),
    ('quota', 'quota'),
    ('quartz', 'quartz'),
    ('quiche', 'quiche'),
    ('quiet', 'quiet'),
    ('quiz', 'quiz'),

    # R
    ('rumah', 'house'),
    ('roda', 'wheel'),
    ('radio', 'radio'),
    ('raja', 'king'),
    ('rantai', 'chain'),
    ('rasa', 'taste'),
    ('roti', 'bread'),
    ('rezeki', 'livelihood'),
    ('restoran', 'restaurant'),
    ('rawan', 'vulnerable'),
    ('acak', 'random'),

    # S
    ('satu', 'one'),
    ('sapi', 'cow'),
    ('sepeda', 'bicycle'),
    ('senja', 'dusk'),
    ('sawah', 'rice field'),
    ('sungai', 'river'),
    ('sapu', 'broom'),
    ('santai', 'relax'),
    ('sirkus', 'circus'),
    ('surat', 'letter'),

    # T
    ('tangga', 'stairs'),
    ('tikus', 'mouse'),
    ('televisi', 'television'),
    ('teh', 'tea'),
    ('teman', 'friend'),
    ('tangan', 'hand'),
    ('tanah', 'soil'),
    ('topi', 'hat'),
    ('talang', 'gutter'),
    ('tikus', 'rat'),
    ('teka teki', 'puzzle'),

    # U
    ('ular', 'snake'),
    ('udara', 'air'),
    ('uang', 'money'),
    ('uji', 'test'),
    ('universitas', 'university'),
    ('ubah', 'change'),
    ('ulah', 'resist'),
    ('umpan', 'bait'),
    ('upacara', 'ceremony'),
    ('unggulan', 'excellent'),

    # V
    ('virus', 'virus'),
    ('vaksin', 'vaccine'),
    ('velg', 'rim'),
    ('voltage', 'voltage'),
    ('vase', 'vase'),
    ('vegetarian', 'vegetarian'),
    ('video', 'video'),
    ('vintage', 'vintage'),
    ('volt', 'volt'),
    ('variasi', 'variation'),

    # W
    ('warna', 'color'),
    ('warna-warni', 'colorful'),
    ('wifi', 'wifi'),
    ('waktu', 'time'),
    ('wirausaha', 'entrepreneurship'),
    ('wilayah', 'region'),
    ('warnet', 'internet cafe'),
    ('warung', 'small shop'),
    ('wajib', 'mandatory'),
    ('wisata', 'tourism'),

    # X
    ('xenon', 'xenon'),
    ('xilofon', 'xylophone'),
    ('xenophobia', 'xenophobia'),
    ('xeroksis', 'xerox'),
    ('xenial', 'friendly'),
    ('xanthic', 'yellowish'),
    ('xenolith', 'xenolith'),
    ('xylem', 'xylem'),
    ('xenogamy', 'xenogamy'),
    ('xenogenesis', 'xenogenesis'),

    # Y
    ('yoga', 'yoga'),
    ('yakin', 'sure'),
    ('yatim', 'orphan'),
    ('yoghurt', 'yogurt'),
    ('yusuf', 'Joseph'),
    ('yoyo', 'yo-yo'),
    ('yakin', 'confidence'),
    ('yel', 'yell'),
    ('yankees', 'Yankees'),
    ('yupa', 'sailboat'),

    # Z
    ('zebra', 'zebra'),
    ('zaman', 'time/era'),
    ('zon', 'zone'),
    ('zikir', 'remembrance'),
    ('zoologi', 'zoology'),
    ('zakat', 'almsgiving'),
    ('zenit', 'zenith'),
    ('zona', 'zone'),
    ('zarah', 'particle'),
    ('zirkon', 'zircon'),
]

tree = RedBlackTree()
for ind_word, eng_word in dictionary_data:
    tree.insert(ind_word, eng_word)

# GUI
class DictionaryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Kamus Indonesia - Inggris")
        self.geometry("600x400")

        # Search bar 
        self.search_entry = ctk.CTkEntry(self, placeholder_text="Cari kata...")
        self.search_entry.pack(fill='x', padx=10, pady=10)
        self.search_entry.bind("<KeyRelease>", self.update_list)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.indonesian_list = tk.Listbox(self.frame)
        self.indonesian_list.pack(side='left', fill='both', expand=True)
        self.indonesian_list.bind('<<ListboxSelect>>', self.on_select)

        self.english_list = tk.Listbox(self.frame)
        self.english_list.pack(side='left', fill='both', expand=True)
        
        self.tree = RedBlackTree()
        for ind_word, eng_word in dictionary_data:
            self.tree.insert(ind_word, eng_word)

        self.populate_listviews()

    def populate_listviews(self, words=None):
        if words is None:
            words = []
            self.tree.inorder(self.tree.root, words)

        self.indonesian_list.delete(0, 'end')
        self.english_list.delete(0, 'end')
        for ind_word, eng_word in words:
            self.indonesian_list.insert('end', ind_word)
            self.english_list.insert('end', eng_word)

    def update_list(self, event=None):
        query = self.search_entry.get().lower()
        if query == '':
            self.populate_listviews()
        else:
            results = self.tree.search_prefix(query)
            words = [(word, self.tree.get(word)) for word in results]
            self.populate_listviews(words)
    
    def on_select(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            selected_word = event.widget.get(index).lower()
            corresponding_translation = self.english_list.get(index)

            # Gimmick 'besar'
            if selected_word == 'besar':
                self.indonesian_list.config(font=("Arial", 16, "bold"))
                self.english_list.config(font=("Arial", 16, "bold"))
            
            # Gimmick 'kucing'
            if selected_word == 'kucing':
                self.show_cat_gif()
                
            # Gimmick 'paksa keluar'
            if selected_word == 'keluar':
                self.destroy()
            
            if selected_word == 'acak':
                random_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
                self.english_list.delete(index)
                self.english_list.insert(index, random_number)
            else:
                if selected_word == 'kalkulator':
                    try:
                        os.startfile('calc.exe')
                    except Exception as e:
                        messagebox.showerror("Error", f"Error opening calculator: {e}")
                        
    def show_cat_gif(self):
        popup = Toplevel(self)
        popup.title("meow")
        popup.geometry("300x300")
        popup.resizable(False, False)

        try:
            cat_image = Image.open(r"G:\py\Tugas Struktur Data\Tubes Strukdat\kucing.gif")

            self.cat_frames = []
            try:
                while True:
                    frame = ImageTk.PhotoImage(cat_image.copy().convert('RGBA'))
                    self.cat_frames.append(frame)
                    cat_image.seek(len(self.cat_frames))
            except EOFError:
                pass

            if not self.cat_frames:
                raise ValueError("No frames found in GIF.")

            self.cat_label = tk.Label(popup)
            self.cat_label.pack()

            self.current_cat_frame = 0
            self.animate_cat_gif()

        except Exception as e:
            messagebox.showerror("Error", f"Error loading GIF: {e}")

    def animate_cat_gif(self):
        if hasattr(self, 'cat_frames') and self.cat_frames:
            frame = self.cat_frames[self.current_cat_frame]
            self.cat_label.config(image=frame)
            self.current_cat_frame = (self.current_cat_frame + 1) % len(self.cat_frames)
            self.cat_label.after(30, self.animate_cat_gif)

if __name__ == "__main__":
    app = DictionaryApp()
    app.mainloop()