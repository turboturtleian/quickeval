import tkinter as tk
import keyboard
import time
import pyperclip
import threading

class CopyPasteApp:
    def __init__(self):
        # Initialize the GUI
        self.root = tk.Tk()
        self.root.title("QuickEval")
        self.root.geometry("300x150")
        self.root.configure(bg="#F5F5F5")

        # Add a label to display instructions
        self.instructions_label = tk.Label(self.root, text="Select text then press Alt+P to evaluate", font=("Arial", 10), bg="#F5F5F5")
        self.instructions_label.pack(side="top", pady=5)
        
        # Add a button to start and stop the program
        self.button = tk.Button(self.root, text="Start", font=("Arial", 14), bg="#4CAF50", fg="white", bd=0, activebackground="#4CAF50", activeforeground="white", command=self.toggle_program)
        self.button.pack(side="top", pady=20)
        
        # Add a label to display the program state
        self.status_label = tk.Label(self.root, text="Program stopped", font=("Arial", 12), bg="#F5F5F5")
        self.status_label.pack(side="top", pady=10)
        
        
        
        # Set the initial program state to "stopped"
        self.program_running = False
        
    def toggle_program(self):
        # Start or stop the program depending on its current state
        if self.program_running:
            self.stop_program()
        else:
            self.start_program()
            
    def start_program(self):
        # Start the program and update the button and label text
        self.program_running = True
        self.button.configure(text="Stop", bg="#E53935", activebackground="#E53935")
        self.status_label.configure(text="Program running", fg="#4CAF50")
        
        # Start a listener thread to handle key presses
        self.listener_thread = threading.Thread(target=self.listen_for_hotkey)
        self.listener_thread.start()
        
    def stop_program(self):
        # Stop the program and update the button and label text
        self.program_running = False
        self.button.configure(text="Start", bg="#4CAF50", activebackground="#4CAF50")
        self.status_label.configure(text="Program stopped", fg="#E53935")
        
        # Stop the listener thread
        self.listener_thread.stop()
        
    def listen_for_hotkey(self):
        # Listen for the "Alt + p" key combination and evaluate the selected text
        while self.program_running:
            try:
                if keyboard.is_pressed('alt+p'):
                    time.sleep(01.1)
                    keyboard.release('alt+p')
                    time.sleep(01.1)
                    keyboard.press_and_release('ctrl+c')
                    time.sleep(01.1)
                    copied_text = pyperclip.paste()
                    result = eval(copied_text)
                    pyperclip.copy(result)
                    keyboard.press_and_release('ctrl+v')
            except Exception as e:
                print("An error occurred:", e)
                self.restart_program()
                
    def restart_program(self):
        # Restart the program after a delay
        self.stop_program()
        time.sleep(1)
        self.start_program()

if __name__ == '__main__':
    app = CopyPasteApp()
    app.root.mainloop()
