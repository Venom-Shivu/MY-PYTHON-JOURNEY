import tkinter as tk
from tkinter import font as tkfont

class AnimatedButton(tk.Button):
    """A custom button class that handles hover and click animations."""
    def __init__(self, master, **kw):
        self.default_bg = kw.get('bg', '#333333')
        self.hover_bg = kw.get('activebackground', '#444444')
        self.click_bg = '#ffffff' # Flash white on click
        self.text_color = kw.get('fg', 'white')
        
        super().__init__(master, **kw)
        
        # Remove border to make it look flat and modern
        self.configure(relief=tk.FLAT, borderwidth=0)
        
        # Bind events for animation
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
        self.bind("<ButtonRelease-1>", self.on_release)

    def on_enter(self, e):
        self['bg'] = self.hover_bg

    def on_leave(self, e):
        self['bg'] = self.default_bg

    def on_click(self, e):
        self['bg'] = self.click_bg
        self['fg'] = 'black' # Invert text color on click for flash effect

    def on_release(self, e):
        self['bg'] = self.hover_bg
        self['fg'] = self.text_color

class DigitalCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("NEON CALC v1.0")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")

        # Define Fonts
        self.display_font = tkfont.Font(family="Consolas", size=30, weight="bold")
        self.btn_font = tkfont.Font(family="Verdana", size=14)

        # --- Display Screen ---
        # Using a Frame to create a 'border' effect
        display_frame = tk.Frame(root, bg="#00ffcc", padx=2, pady=2)
        display_frame.pack(pady=20, padx=20, fill="x")

        self.expression = ""
        self.input_text = tk.StringVar()
        
        self.display = tk.Entry(display_frame, 
                                textvariable=self.input_text, 
                                font=self.display_font, 
                                bg="#1e1e1e", 
                                fg="#00ffcc", # Neon Cyan text
                                justify="right",
                                bd=0,
                                insertbackground="#00ffcc") # Cursor color
        self.display.pack(fill="both", ipady=15)

        # --- Button Grid ---
        btns_frame = tk.Frame(root, bg="#121212")
        btns_frame.pack(padx=10, pady=10)

        # Button Layout Configuration
        # (Text, Row, Column, ColorType)
        buttons = [
            ('C', 0, 0, 'danger'), ('/', 0, 1, 'op'), ('*', 0, 2, 'op'), ('DEL', 0, 3, 'danger'),
            ('7', 1, 0, 'num'),    ('8', 1, 1, 'num'), ('9', 1, 2, 'num'), ('-', 1, 3, 'op'),
            ('4', 2, 0, 'num'),    ('5', 2, 1, 'num'), ('6', 2, 2, 'num'), ('+', 2, 3, 'op'),
            ('1', 3, 0, 'num'),    ('2', 3, 1, 'num'), ('3', 3, 2, 'num'), ('=', 3, 3, 'equal'),
            ('%', 4, 0, 'op'),     ('0', 4, 1, 'num'), ('.', 4, 2, 'num'), 
        ]

        # Define Colors
        colors = {
            'num': {'bg': '#2b2b2b', 'fg': '#ffffff', 'hover': '#3a3a3a'},
            'op':  {'bg': '#1f1f1f', 'fg': '#00ffcc', 'hover': '#2a2a2a'}, # Neon accents
            'danger': {'bg': '#3d1010', 'fg': '#ff4444', 'hover': '#521414'},
            'equal': {'bg': '#008066', 'fg': '#ffffff', 'hover': '#00b38f'}
        }

        for btn in buttons:
            text, row, col, type_key = btn
            
            # Handle the spanning of the "=" button
            rowspan = 2 if text == '=' else 1
            
            color_scheme = colors[type_key]
            
            button = AnimatedButton(btns_frame,
                                    text=text,
                                    font=self.btn_font,
                                    width=5,
                                    height=2 if text != '=' else 5, # Adjust height for equals
                                    bg=color_scheme['bg'],
                                    fg=color_scheme['fg'],
                                    activebackground=color_scheme['hover'],
                                    command=lambda t=text: self.on_button_click(t))
            
            button.grid(row=row, column=col, rowspan=rowspan, padx=5, pady=5, sticky="nsew")

        # Configure grid weights to make it responsive inside the frame
        for i in range(4):
            btns_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        
        elif char == 'DEL':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
            
        elif char == '=':
            try:
                # Evaluate the string math expression
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except ZeroDivisionError:
                self.input_text.set("Error")
                self.expression = ""
            except SyntaxError:
                self.input_text.set("Error")
                self.expression = ""
                
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalCalculator(root)
    root.mainloop()