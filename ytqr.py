import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Function to generate QR code
def generate_qr():
    website_link = entry.get()
    if not website_link:
        messagebox.showerror("Error", "Please enter a website link.")
        return

    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(website_link)
    qr.make()

    img = qr.make_image(fill_color='black', back_color='white')

    # Save the QR code to a file
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        display_qr(save_path)

# Function to display QR code

def display_qr(image_path):
    img = Image.open(image_path)
    img = img.resize((200, 200))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)

    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# Create the GUI window
root = tk.Tk()
root.title("QR Code Generator")

# Input field
entry_label = tk.Label(root, text="Enter website link:")
entry_label.pack(pady=10, padx=125)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=15)

# Label to display QR code
qr_label = tk.Label(root)
qr_label.pack(pady=20)

# Run the GUI
root.mainloop()