import tkinter as tk
import json

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("NOVA")
        self.window.geometry('384x640')

        self.floor = 0
        self.pos = 'Java Coffee House'
        self.data = [[['void' for k in range(3)] for j in range(3)] for i in range(2)]
        path = 'data/'
        for floor in json.load(open(path + 'properties.json')):
            data = json.load(open(path + floor + '.json'))
            for shop in data:
                x, y, z = data[shop]['coords']
                self.data[z][x][y] = shop

        self.introScreen()

    def introScreen(self):
        intro_frame = tk.Frame(self.window)
        intro_frame.pack(expand=True, fill='both')
        
        intro_label = tk.Label(intro_frame, text="Welcome to NOVA", font=("Helvetica", 24))
        intro_label.pack(pady=20)

        continue_button = tk.Button(intro_frame, text="Continue", command=self.homeScreen)
        continue_button.pack(pady=10)

    def homeScreen(self):
        home_frame = tk.Frame(self.window)
        home_frame.pack(expand=True, fill='both')
        
        home_label = tk.Label(home_frame, text="Home Screen", font=("Helvetica", 24))
        home_label.pack(pady=20)

        login_button = tk.Button(home_frame, text="Login", command=self.login)
        login_button.pack(pady=10)

        signup_button = tk.Button(home_frame, text="Sign Up", command=self.signUp)
        signup_button.pack(pady=10)

    def login(self):
        login_frame = tk.Frame(self.window)
        login_frame.pack(expand=True, fill='both')

        login_label = tk.Label(login_frame, text="Login Page", font=("Helvetica", 24))
        login_label.pack(pady=20)

        # Add login form fields and submit button here

    def signUp(self):
        signup_frame = tk.Frame(self.window)
        signup_frame.pack(expand=True, fill='both')

        signup_label = tk.Label(signup_frame, text="Sign Up Page", font=("Helvetica", 24))
        signup_label.pack(pady=20)

        # Add sign-up form fields and submit button here

    def homePage(self):
        homepage_frame = tk.Frame(self.window)
        homepage_frame.pack(expand=True, fill='both')

        homepage_label = tk.Label(homepage_frame, text="Home Page", font=("Helvetica", 24))
        homepage_label.pack(pady=20)

        # Add content for the home page here, e.g., user profile, notifications, etc.

    def scanQR(self):
        qr_frame = tk.Frame(self.window)
        qr_frame.pack(expand=True, fill='both')

        qr_label = tk.Label(qr_frame, text="Scan QR Code", font=("Helvetica", 24))
        qr_label.pack(pady=20)

        # Add QR scanning functionality here

    def profile(self):
        profile_frame = tk.Frame(self.window)
        profile_frame.pack(expand=True, fill='both')

        profile_label = tk.Label(profile_frame, text="User Profile", font=("Helvetica", 24))
        profile_label.pack(pady=20)

        # Add user profile information and settings here

    def wishList(self):
        wishlist_frame = tk.Frame(self.window)
        wishlist_frame.pack(expand=True, fill='both')

        wishlist_label = tk.Label(wishlist_frame, text="Wishlist", font=("Helvetica", 24))
        wishlist_label.pack(pady=20)

        # Add wishlist items and management here

    def wallet(self):
        wallet_frame = tk.Frame(self.window)
        wallet_frame.pack(expand=True, fill='both')

        wallet_label = tk.Label(wallet_frame, text="Wallet", font=("Helvetica", 24))
        wallet_label.pack(pady=20)

        # Add wallet balance and transactions here

    def displayMap(self):
        map_frame = tk.Frame(self.window)
        map_frame.pack(expand=True, fill='both')

        map_label = tk.Label(map_frame, text="Map Display", font=("Helvetica", 24))
        map_label.pack(pady=20)

        # Add map display and navigation functionality here

    def viewShop(self, shop):
        shop_frame = tk.Frame(self.window)
        shop_frame.pack(expand=True, fill='both')

        shop_label = tk.Label(shop_frame, text=f"Shop: {shop}", font=("Helvetica", 24))
        shop_label.pack(pady=20)

        # Add shop information, products, and interaction options here

app = App()
app.window.mainloop()