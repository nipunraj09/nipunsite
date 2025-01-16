import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def load_image():
    """Function to load an image file and resize it if necessary."""
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_path:
        global img, img_tk, original_img
        original_img = Image.open(file_path)
        max_width, max_height = 800, 600  # Maximum canvas size
        
