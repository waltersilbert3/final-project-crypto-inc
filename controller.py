class CryptoTrackerController:
    def __init__(self):
        self.root = tk.Tk()
        self.crypto_tracker = CryptoTracker(self.root)
        self.root.mainloop()


controller = CryptoTrackerController()

#CryptoTrackerController class acts as the sole controller. It manages the interactions between the CryptoTracker class, which handles cryptocurrency data and display updates, and the tkinter window for the graphical display. This CryptoTrackerController class oversees the initialization and continuous update process of the tracker and display.







