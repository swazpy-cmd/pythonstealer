import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time
import random

def generate_fake_chrome():
    return f"Found {random.randint(8,27)} passwords, {random.randint(45,120)} cookies"

def generate_fake_discord():
    token = f"mfa.{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=68))}"
    return f"Token: {token[:30]}... | Servers: {random.randint(3,52)}"

def generate_fake_roblox():
    user = f"RobloxUser{random.randint(10000,99999)}"
    return f"Username: {user} | Robux: {random.randint(800,45000)} | Cookie grabbed"

def generate_fake_wallets():
    w = ["MetaMask", "TrustWallet", "Exodus", "Phantom", "Ledger", "Ronin"]
    return "\n".join([f"{wallet}: ${random.randint(200,32000)}" for wallet in w])

class FakeRATBuilder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RAT Builder v2.3 - DataRoaming Edition")
        self.root.geometry("850x650")
        self.root.configure(bg="#0a0a0a")
        
        # Auto open guns.lol
        threading.Thread(target=self.open_site, daemon=True).start()
        
        self.webhook_var = tk.StringVar()
        
        tk.Label(self.root, text="RAT BUILDER - STEALTH STEALER", font=("Courier", 20, "bold"), fg="#00ff41", bg="#0a0a0a").pack(pady=15)
        
        # Webhook
        tk.Label(self.root, text="Discord Webhook:", fg="white", bg="#0a0a0a", font=("Arial", 11)).pack(anchor="w", padx=30)
        tk.Entry(self.root, textvariable=self.webhook_var, width=80, bg="#1f1f1f", fg="#00ff41", font=("Courier", 10)).pack(pady=8, padx=30)
        
        # Modules
        mod_frame = tk.LabelFrame(self.root, text="Active Stealers", fg="#00ff41", bg="#0a0a0a")
        mod_frame.pack(pady=15, padx=30, fill="x")
        
        self.mods = {
            "Chrome Passwords + Cookies": tk.BooleanVar(value=True),
            "Discord Token & Info": tk.BooleanVar(value=True),
            "Roblox Cookies": tk.BooleanVar(value=True),
            "Crypto Wallets (MetaMask etc)": tk.BooleanVar(value=True),
            "Steam Sessions": tk.BooleanVar(value=True),
            "Browser History & Autofill": tk.BooleanVar(value=True),
            "WiFi Saved Passwords": tk.BooleanVar(value=True),
            "Minecraft + Telegram": tk.BooleanVar(value=True)
        }
        
        for i, (name, var) in enumerate(self.mods.items()):
            tk.Checkbutton(mod_frame, text=name, variable=var, fg="#00ff41", bg="#0a0a0a", selectcolor="#222").grid(row=i//2, column=i%2, sticky="w", padx=40, pady=4)
        
        # Build button
        build_btn = tk.Button(self.root, text="BUILD RAT & STEAL DATA", font=("Arial", 16, "bold"), 
                            bg="#ff0000", fg="white", height=2, command=self.start_stealing)
        build_btn.pack(pady=25)
        
        # Log
        self.log_area = scrolledtext.ScrolledText(self.root, height=18, bg="black", fg="#00ff41", font=("Courier", 10))
        self.log_area.pack(pady=10, padx=30, fill="both", expand=True)
        
        self.log("RAT Builder loaded successfully.\nConnected to dataroaming source.\n")
        self.root.mainloop()
    
    def open_site(self):
        time.sleep(0.8)
        webbrowser.open("https://guns.lol/dataroaming", new=2)
        self.log("Opened https://guns.lol/dataroaming\n")
    
    def log(self, text):
        self.log_area.insert(tk.END, text)
        self.log_area.see(tk.END)
    
    def start_stealing(self):
        webhook = self.webhook_var.get().strip()
        if not webhook or "discord.com/api/webhooks" not in webhook:
            messagebox.showerror("Error", "Please enter a valid Discord webhook.")
            return
        
        threading.Thread(target=self.fake_steal_process, daemon=True).start()
    
    def fake_steal_process(self):
        self.log("\n[+] Starting steal sequence...\n")
        time.sleep(1)
        self.log("[CMD] rat_stealer.exe --webhook " + self.webhook_var.get()[:40] + "...\n")
        time.sleep(1.2)
        
        if self.mods["Chrome Passwords + Cookies"].get():
            self.log(f"[+] Chrome Stealer: {generate_fake_chrome()}\n")
            time.sleep(0.9)
        
        if self.mods["Discord Token & Info"].get():
            self.log(f"[+] Discord Grabber: {generate_fake_discord()}\n")
            time.sleep(0.8)
        
        if self.mods["Roblox Cookies"].get():
            self.log(f"[+] Roblox: {generate_fake_roblox()}\n")
            time.sleep(0.9)
        
        if self.mods["Crypto Wallets (MetaMask etc)"].get():
            self.log("[+] Wallets extracted:\n" + generate_fake_wallets() + "\n")
            time.sleep(1.3)
        
        for mod in ["Steam Sessions", "Browser History & Autofill", "WiFi Saved Passwords", "Minecraft + Telegram"]:
            if self.mods.get(mod, tk.BooleanVar(value=True)).get():
                self.log(f"[+] {mod}: Data harvested successfully\n")
                time.sleep(0.7)
        
        self.log("\n[!] All data packaged. Uploading to webhook...\n")
        time.sleep(1.8)
        self.log("[+] SUCCESS: 18.7 MB of victim data sent!\n")
        self.log("[+] RAT deployed. Victim is now monitored.\n")
        messagebox.showinfo("Success", "RAT Built & Data Sent!")

if __name__ == "__main__":
    FakeRATBuilder()
