# settings.py

import pyfiglet 

# -------------------------
# Game Settings Dictionary
# -------------------------
game_settings = {
    "text_speed": "normal",        # Options: 'slow', 'normal', 'fast'
    "narration": True,             # Narrator on/off
    "text_color": 15,              # ANSI 256-color code (default: white)
    "background_color": 0,         # ANSI 256-color code (default: black)
    "border_color": 14,            # ANSI 256-color code (default: light gray)
    "font": "default"              # Placeholder for future font styles
}

# -------------------------
# Text Speed Options
# -------------------------
def change_text_speed():
    print("\nChoose text speed:")
    print("1. Slow")
    print("2. Normal")
    print("3. Fast")

    choice = input("Select an option: ").strip()
    if choice == "1":
        game_settings["text_speed"] = "slow"
    elif choice == "2":
        game_settings["text_speed"] = "normal"
    elif choice == "3":
        game_settings["text_speed"] = "fast"
    else:
        print("Invalid choice. Text speed not changed.")

# -------------------------
# Narration Toggle
# -------------------------
def toggle_narration():
    game_settings["narration"] = not game_settings["narration"]
    print(f"Narration {'enabled' if game_settings['narration'] else 'disabled'}.")

# -------------------------
# 256-Color Preview Grid
# -------------------------
def preview_256_colors():
    print("\nAvailable 256 ANSI Colors:")
    for i in range(0, 256):
        if i % 16 == 0:
            print()
        print(f"\033[48;5;{i}m {i:3} \033[0m", end=" ")
    print("\n")  # Final newline

# -------------------------
# 256-Color Selector
# -------------------------
def choose_256_color(setting_key):
    preview_256_colors()
    choice = input(f"Enter color code (0–255) for {setting_key.replace('_', ' ')}: ").strip()
    if choice.isdigit() and 0 <= int(choice) <= 255:
        game_settings[setting_key] = int(choice)
        print(f"{setting_key.replace('_', ' ').title()} set to color code {choice}.")
    else:
        print("Invalid choice. Color not changed.")

# -------------------------
# Font Selection Placeholder
# -------------------------
def change_font():
    print("\nAvailable fonts:")
    print("1. Default")
    print("2. Bold (simulated)")
    print("3. Italic (simulated)")

    choice = input("Select a font: ").strip()
    if choice == "1":
        game_settings["font"] = "default"
    elif choice == "2":
        game_settings["font"] = "bold"
    elif choice == "3":
        game_settings["font"] = "italic"
    else:
        print("Invalid choice. Font not changed.")
