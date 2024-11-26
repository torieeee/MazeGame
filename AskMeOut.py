import tkinter as tk
from PIL import Image, ImageTk
import random
import requests
from io import BytesIO


class ValentineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Will You Go Out With Me?")
        self.root.geometry("600x700")
        self.root.configure(bg='#F8C8DC')

        # Create main frame
        self.main_frame = tk.Frame(root, bg='#F8C8DC')
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Create initial screen
        self.create_initial_screen()

    def create_initial_screen(self):
        # Clear any existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Header text
        self.header = tk.Label(
            self.main_frame,
            text="Do you wanna go out with me?",
            font=('Nunito', 40, 'bold'),
            fg='white',
            bg='#F8C8DC'
        )
        self.header.pack(pady=(10, 20))

        # Load and display GIF
        self.load_gif()

        # Button frame for positioning
        self.button_frame = tk.Frame(self.main_frame, bg='#F8C8DC')
        self.button_frame.pack(pady=20)

        # Yes button
        self.yes_button = tk.Button(
            self.main_frame,
            text="Yes",
            command=self.on_yes_click,
            bg='#FFB6C1',
            fg='white',
            font=('Arial', 16),
            width=10,
            borderwidth=0,
            highlightthickness=0
        )
        self.yes_button.place(x=150, y=500)

        # No button
        self.no_button = tk.Button(
            self.main_frame,
            text="No",
            bg='#FFB6C1',
            fg='white',
            font=('Arial', 16),
            width=10,
            borderwidth=0,
            highlightthickness=0,
            command=self.move_no_button  # Add this line to move button on click
        )
        self.no_button.place(x=350, y=500)

        # Bind mouse hover and click events to move the No button
        self.no_button.bind('<Enter>', self.move_no_button)
        self.no_button.bind('<Button-1>', self.move_no_button)

        # Start moving stars
        self.create_stars()

    def move_no_button(self, event=None):
        # Get window dimensions
        window_width = self.main_frame.winfo_width()
        window_height = self.main_frame.winfo_height()

        # Get button dimensions
        button_width = self.no_button.winfo_reqwidth()
        button_height = self.no_button.winfo_reqheight()

        # Ensure window dimensions are not zero
        if window_width == 1 or window_height == 1:
            window_width = 600
            window_height = 700

        # Generate new random position
        new_x = random.randint(0, max(0, window_width - button_width))
        new_y = random.randint(350, max(350, window_height - button_height))

        # Move the button
        self.no_button.place(x=new_x, y=new_y)

    def load_gif(self):
        # Download and display GIF
        try:
            gif_url = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDdtZ2JiZDR0a3lvMWF4OG8yc3p6Ymdvd3g2d245amdveDhyYmx6eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/cLS1cfxvGOPVpf9g3y/giphy.gif"
            response = requests.get(gif_url)
            gif_data = Image.open(BytesIO(response.content))

            # Resize the image to fit the window
            gif_data = gif_data.resize((300, 300), Image.LANCZOS)

            # Convert gif to PhotoImage
            self.gif_photo = ImageTk.PhotoImage(gif_data)

            # Create label to display gif
            self.gif_label = tk.Label(
                self.main_frame,
                image=self.gif_photo,
                bg='#F8C8DC'
            )
            self.gif_label.pack(pady=20)
        except Exception as e:
            print(f"Error loading GIF: {e}")
            # Fallback text if GIF fails to load
            self.gif_label = tk.Label(
                self.main_frame,
                text="😍",
                font=('Arial', 100),
                bg='#F8C8DC'
            )
            self.gif_label.pack(pady=20)

    def create_stars(self):
        # Remove existing stars
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, tk.Canvas):
                widget.destroy()

        # Create twinkling star effect
        self.stars = []
        for _ in range(20):
            x = random.randint(0, 600)
            y = random.randint(0, 700)
            size = random.randint(2, 6)
            star = tk.Canvas(self.main_frame, width=size, height=size,
                             bg='#F8C8DC', highlightthickness=0)
            star.create_oval(0, 0, size, size, fill='white')
            star.place(x=x, y=y)
            self.stars.append(star)

        # Start twinkling animation
        self.twinkle_stars()

    def twinkle_stars(self):
        for star in self.stars:
            # Randomly change star opacity and position
            opacity = random.random()
            new_x = random.randint(0, 600)
            new_y = random.randint(0, 700)
            star.place(x=new_x, y=new_y)

        # Schedule next twinkle
        self.root.after(500, self.twinkle_stars)

    def on_yes_click(self):
        # Clear the existing content
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create the "Yes" screen
        self.create_yes_screen()

    def create_yes_screen(self):
        # Configure background
        self.main_frame.configure(bg='#F8C8DC')

        # Celebratory header
        yes_label = tk.Label(
            self.main_frame,
            text="Yeeeyyyy!!",
            font=('Nunito', 50, 'bold'),
            fg='white',
            bg='#F8C8DC'
        )
        yes_label.pack(pady=(20, 10))

        # Load and display the specific celebration GIF
        try:
            gif_url = "https://media0.giphy.com/media/T86i6yDyOYz7J6dPhf/giphy.gif"
            response = requests.get(gif_url)
            gif_data = Image.open(BytesIO(response.content))

            # Resize the image
            gif_data = gif_data.resize((400, 400), Image.LANCZOS)

            # Convert gif to PhotoImage
            self.yes_gif_photo = ImageTk.PhotoImage(gif_data)

            # Create label to display gif
            yes_gif_label = tk.Label(
                self.main_frame,
                image=self.yes_gif_photo,
                bg='#F8C8DC'
            )
            yes_gif_label.pack(expand=True)

        except Exception as e:
            print(f"Error loading GIF: {e}")
            # Fallback text if GIF fails to load
            yes_gif_label = tk.Label(
                self.main_frame,
                text="🎉",
                font=('Arial', 200),
                bg='#F8C8DC'
            )
            yes_gif_label.pack(pady=20)


def main():
    root = tk.Tk()
    app = ValentineApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()