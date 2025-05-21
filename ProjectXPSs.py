import os
import platform
import webbrowser
import time

# Clear screen (Remains at the top for initial clear)
os.system('cls' if os.name == 'nt' else 'clear')

# Colors
RESET = '\033[0m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
PINK = '\033[95m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
GREEN = '\033[92m'

# --- Banners ---
# Sub-Menu Banner for Doxxing (existing)
DOXXING_SUB_MENU_BANNER = f"""{YELLOW}
██████╗  ██████╗ ██╗  ██╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗██╔╝██║████╗  ██║██╔════╝ 
██║  ██║██║   ██║ ╚███╔╝  ╚███╔╝ ██║██╔██╗ ██║██║  ███╗
██║  ██║██║   ██║ ██╔██╗  ██╔██╗ ██║██║╚██╗██║██║   ██║
██████╔╝╚██████╔╝██╔╝ ██╗██╔╝ ██╗██║██║ ╚████║╚██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
{RESET}"""

# Sub-Menu Banner for Phishing (existing)
PHISHING_SUB_MENU_BANNER = f"""{CYAN}
______ _     _     _     _             
| ___ \ |   (_)   | |   (_)            
| |_/ / |__  _ ___| |__  _ _ __   __ _ 
|  __/| '_ \| / __| '_ \| | '_ \ / _` |
| |   | | | | \__ \ | | | | | | | (_| |
\_|   |_| |_|_|___/_| |_|_|_| |_|\__, |
                                  __/ |
                                 |___/
{RESET}"""

# Sub-Menu Banner for RATs (existing)
RATS_SUB_MENU_BANNER = f"""{PINK}
██████╗ ███████╗███╗   ███╗ ██████╗ ████████╗███████╗     █████╗  ██████╗ ██████╗███████╗███████╗    ████████╗██████╗  ██████╗      ██╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝████╗ ████║██╔═══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██╔══██╗██╔═══██╗     ██║██╔══██╗████╗  ██║
██████╔╝█████╗  ██╔████╔██║██║   ██║   ██║   █████╗      ███████║██║     ██║     █████╗  ███████╗       ██║   ██████╔╝██║   ██║     ██║███████║██╔██╗ ██║
██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║   ██║   ██╔══╝      ██╔══██║██║     ██║     ██╔══╝  ╚════██║       ██║   ██╔══██╗██║   ██║██   ██║██╔══██║██║╚██╗██║
██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝   ██║   ███████╗    ██║  ██║╚██████╗╚██████╗███████╗███████║       ██║   ██║  ██║╚██████╔╝╚█████╔╝██║  ██║██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
{RESET}"""

# Sub-Menu Banner for Hidden Services (existing)
HIDDEN_SERVICES_SUB_MENU_BANNER = f"""{GREEN}
   ▄█    █▄     ▄█  ████████▄  ████████▄     ▄████████ ███▄▄▄▄           ▄████████    ▄████████    ▄████████  ▄█    █▄   ▄█   ▄████████    ▄████████ 
  ███    ███   ███  ███   ▀███ ███   ▀███   ███    ███ ███▀▀▀██▄        ███    ███   ███    ███   ███    ███ ███    ███ ███  ███    ███   ███    ███ 
  ███    ███   ███▌ ███    ███ ███    ███   ███    █▀  ███   ███        ███    █▀    ███    █▀    ███    ███ ███    ███ ███▌ ███    █▀    ███    █▀  
 ▄███▄▄▄▄███▄▄ ███▌ ███    ███ ███    ███  ▄███▄▄▄     ███   ███        ███         ▄███▄▄▄      ▄███▄▄▄▄██▀ ███    ███ ███▌ ███         ▄███▄▄▄     
▀▀███▀▀▀▀███▀  ███▌ ███    ███ ███    ███ ▀▀███▀▀▀     ███   ███      ▀███████████ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███    ███ ███▌ ███        ▀▀███▀▀▀     
  ███    ███   ███  ███    ███ ███    ███   ███    █▄  ███   ███               ███   ███    █▄  ▀███████████ ███    ███ ███  ███    █▄    ███    █▄  
  ███    ███   ███  ███   ▄███ ███   ▄███   ███    ███ ███   ███         ▄█    ███   ███    ███   ███    ███ ███    ███ ███  ███    ███   ███    ███ 
  ███    █▀    █▀   ████████▀  ████████▀    ██████████  ▀█   █▀        ▄████████▀    ██████████   ███    ███  ▀██████▀  █▀   ████████▀    ██████████ 
                                                                                                  ███    ███                                        
{RESET}"""

# Sub-Menu Banner for Other Tools (existing)
OTHER_TOOLS_SUB_MENU_BANNER = f"""{YELLOW}
████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
   ██║   ██║   ██║██║   ██║██║     ███████╗
   ██║   ██║   ██║██║   ██║██║     ╚════██║
   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
{RESET}"""

# Sub-Menu Banner for Extreme Tools (existing)
EXTREME_TOOLS_SUB_MENU_BANNER = f"""{PINK}
▓█████ ▒██   ██▒▄▄▄█████▓ ██▀███  ▓█████  ███▄ ▄███▓▓█████ 
▓█   ▀ ▒▒ █ █ ▒░▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▓█   ▀ 
▒███   ░░  █   ░▒ ▓██░ ▒░▓██ ░▄█ ▒▒███   ▓██    ▓██░▒███   
▒▓█  ▄  ░ █ █ ▒ ░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ ▒▓█  ▄ 
░▒████▒▒██▒ ▒██▒  ▒██▒ ░ ░██▓ ▒██▒░▒████▒▒██▒   ░██▒░▒████▒
░░ ▒░ ░▒▒ ░ ░▓ ░  ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░░░ ▒░ ░
 ░ ░  ░░░   ░▒ ░    ░      ░▒ ░ ▒░ ░ ░  ░░  ░      ░ ░ ░  ░
   ░    ░    ░    ░        ░░   ░    ░   ░      ░      ░   
   ░  ░ ░    ░              ░        ░  ░       ░      ░  ░
{RESET}"""

# NEW: Sub-Menu Banner for SQL Injection Tools
SQL_INJECTION_TOOLS_SUB_MENU_BANNER = f"""{BLUE}
███████╗ ██████╗ ██╗         ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔═══██╗██║         ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
███████╗██║   ██║██║         ██║██╔██╗ ██║     ██║█████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║
╚════██║██║▄▄ ██║██║         ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║
███████║╚██████╔╝███████╗    ██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
{RESET}"""

# Main Banner (Your original banner)
MAIN_BANNER = f"""{MAGENTA}
██████╗░██╗░░░░░░█████╗░██████╗░██╗████████╗██╗░░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║╚══██╔══╝╚██╗░██╔╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝██║░░░░░███████║██████╔╝██║░░░██║░░░░╚████╔╝░  ░░░██║░░░███████║██║░░██║██║░░░░░
██╔═══╝░██║░░░░░██╔══██║██╔═══╝░██║░░░██║░░░░░╚██╔╝░░  ░░░██║░░░██╔══██║██║░░██║██║░░░░░
██║░░░░░███████╗██║░░██║██║░░░░░██║░░░██║░░░░░░██║░░░  ░░░██║░░░██║░░██║╚█████╔╝███████╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░░░░╚═╝░░░  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝
{RESET}"""

# Function to clear screen and display a specific banner
def refresh_and_banner(banner_to_display=MAIN_BANNER):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner_to_display)

# Initial display of the main banner
refresh_and_banner(MAIN_BANNER)

# Info box
print(f"{CYAN}Made with <3 by ANS! - version 1 {RESET}")
print(f"{PINK}╔══════════════════════════════════════════════════════╗")
print(f"║{RESET} {CYAN}[!] welcome to the door to hacking.{PINK} ║")
print(f"╚══════════════════════════════════════════════════════╝{RESET}")

# Menu boxes - Your original options
left_menu = [
    "[1] > Doxxing tools",
    "[2] > Phishing",
    "[3] > RATs",
    "[4] > Hidden services",
    "[5] > Dark web links",
    "[6] > Other tools",
    "[7] > Extreme tools"
]

right_menu = [
    "[10] > Advanced Exploitation", # Renamed
    "[11] > ClarityAI (beta)",
    "[12] > Self Security",
    "[13] > SQL Injection Tools",
    "[14] > Network Penetration", # New
    "[15] > Reverse Engineering", # New
    "[16] > Social Engineering", # New
    "[17] > Cloud Security Assessment", # New
    "[18] > Bug Bounty Resources" # New
]

# Draw boxes
def draw_box(left, right):
    print(f"{PINK}╔{'═'*35}╗    ╔{'═'*35}╗")
    for l, r in zip(left, right):
        print(f"║ {CYAN}{l:<33}{PINK}║    ║ {CYAN}{r:<33}{PINK}║")
    print(f"╚{'═'*35}╝    ╚{'═'*35}╝{RESET}")

draw_box(left_menu, right_menu)

# Function to open links (adjusted for sub-menu context)
# This function is primarily for lists of external links, not for handling sub-menu navigation logic itself.
# Sub-menu navigation (like "coming soon" or going back) is handled within the specific choice blocks.
def open_links(title, options, banner_to_use=MAIN_BANNER):
    refresh_and_banner(banner_to_use) # Refresh with the appropriate banner

    print(f"\n{GREEN}-- {title} --{RESET}")
    for i, (name, url) in enumerate(options, 1):
        print(f"{i}. {name}")
    print(f"0. Back to previous menu")

    while True:
        selected = input(f"\n{YELLOW}Choose an option (0-{len(options)}): {RESET}")
        if selected.isdigit():
            selected_int = int(selected)
            if selected_int == 0:
                break # Exit the loop, function will return
            elif 1 <= selected_int <= len(options):
                print(f"{BLUE}Opening {options[selected_int-1][0]}...{RESET}")
                webbrowser.open_new_tab(options[selected_int-1][1])
                input(f"{CYAN}Press Enter to continue...{RESET}")

                # After returning from browser, re-display the current link list menu
                refresh_and_banner(banner_to_use)

                print(f"\n{GREEN}-- {title} --{RESET}")
                for i, (name, url) in enumerate(options, 1):
                    print(f"{i}. {name}")
                print(f"0. Back to previous menu")
            else:
                print(f"{PINK}Invalid selection. Please try again.{RESET}")
        else:
            print(f"{PINK}Invalid input. Please enter a number.{RESET}")


# Main menu loop
while True:
    # Menu Input
    choice = input(f"\n{YELLOW}Select an option (1-7 or 10-18, or 'exit' to quit): {RESET}").lower()

    if choice == "exit":
        refresh_and_banner(MAIN_BANNER) # Clear screen before exiting
        print(f"{BLUE}Exiting Multi-Tool. Goodbye!{RESET}")
        break
    elif choice.isdigit():
        choice_int = int(choice)

        if choice_int == 1:
            # DOXXING TOOLS SUB-MENU LOGIC
            while True:
                refresh_and_banner(DOXXING_SUB_MENU_BANNER) # Clear and display Doxxing banner
                print(f"\n{GREEN}choose option{RESET}")
                print(f"1. Doxxing tools (Search on GitHub)")
                print(f"2. Doxxing websites (Comprehensive OSINT resources)")
                print(f"0. exit")

                doxxing_sub_choice = input(f"\n{YELLOW}Choose an option (0-2): {RESET}")

                if doxxing_sub_choice == "1":
                    print(f"{BLUE}Opening GitHub search for 'OSINT tools' and 'doxxing tools'...{RESET}")
                    webbrowser.open_new_tab("https://github.com/search?q=osint+tools&type=repositories")
                    webbrowser.open_new_tab("https://github.com/search?q=doxxing+tools&type=repositories")
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif doxxing_sub_choice == "2":
                    osint_websites = [
                        ("OSINT Framework", "https://osintframework.com/"),
                        ("Bellingcat's OSINT Guide", "https://www.bellingcat.com/resources/how-tos/"),
                        ("SANS OSINT Cheat Sheet", "https://www.sans.org/blog/osint-cheat-sheet/"),
                        ("Intelligence X (OSINT Search Engine)", "https://intelx.io/")
                    ]
                    open_links("Comprehensive OSINT Resource Websites", osint_websites, banner_to_use=DOXXING_SUB_MENU_BANNER)
                elif doxxing_sub_choice == "0":
                    refresh_and_banner(MAIN_BANNER)
                    draw_box(left_menu, right_menu)
                    break
                else:
                    print(f"{PINK}Invalid selection. Please try again.{RESET}")

                time.sleep(0.5)

        elif choice_int == 2:
            # PHISHING SUB-MENU LOGIC
            while True:
                refresh_and_banner(PHISHING_SUB_MENU_BANNER) # Clear and display Phishing banner
                print(f"\n{GREEN}choose an option{RESET}")
                print(f"1. Maxphisher (GitHub Repo)")
                print(f"2. Zphisher (GitHub Repo)")
                print(f"3. GoPhish (GitHub Repo)")
                print(f"4. HiddenEye (GitHub Repo)")
                print(f"5. Phishing tool search (GitHub)") 
                print(f"0. exit")

                phishing_sub_choice = input(f"\n{YELLOW}Choose an option (0-5): {RESET}")

                if phishing_sub_choice == "1":
                    print(f"{BLUE}Opening Maxphisher GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/KasRaudra/MaxPhisher") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif phishing_sub_choice == "2":
                    print(f"{BLUE}Opening Zphisher GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/htr-tech/zphisher") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif phishing_sub_choice == "3":
                    print(f"{BLUE}Opening GoPhish GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/gophish/gophish") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif phishing_sub_choice == "4":
                    print(f"{BLUE}Opening HiddenEye GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/Morsmalleo/HiddenEye_Legacy") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif phishing_sub_choice == "5":
                    print(f"{BLUE}Opening GitHub search for 'phishing tools'...{RESET}")
                    webbrowser.open_new_tab("https://github.com/search?q=phishing+tools&type=repositories") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif phishing_sub_choice == "0":
                    refresh_and_banner(MAIN_BANNER)
                    draw_box(left_menu, right_menu)
                    break
                else:
                    print(f"{PINK}Invalid selection. Please try again.{RESET}")

                time.sleep(0.5)

        elif choice_int == 3:
            # RATs SUB-MENU LOGIC
            while True:
                refresh_and_banner(RATS_SUB_MENU_BANNER) # Clear and display RATs banner
                print(f"\n{GREEN}choose option{RESET}")
                print(f"1. NjRAT")
                print(f"2. QuasarRAT")
                print(f"3. (coming soon)")
                print(f"4. (coming soon)")
                print(f"5. (coming soon)")
                print(f"6. Remote Access Tool Search (GitHub)")
                print(f"0. exit")

                rats_sub_choice = input(f"\n{YELLOW}Choose an option (0-6): {RESET}")

                if rats_sub_choice == "1":
                    print(f"{BLUE}Opening NjRAT...{RESET}")
                    # PUT YOUR NJRAT LINK HERE
                    webbrowser.open_new_tab("PUT_NJRAT_LINK_HERE") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif rats_sub_choice == "2":
                    print(f"{BLUE}Opening QuasarRAT GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/quasar/Quasar") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif rats_sub_choice in ["3", "4", "5"]:
                    print(f"\n{BLUE}More remote access Trojan tools coming soon!{RESET}")
                    input(f"{CYAN}Press Enter to return to RATs menu...{RESET}")
                elif rats_sub_choice == "6":
                    print(f"{BLUE}Opening GitHub search for 'remote access tools'...{RESET}")
                    webbrowser.open_new_tab("https://github.com/search?q=remote+access+tools&type=repositories")
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif rats_sub_choice == "0":
                    refresh_and_banner(MAIN_BANNER)
                    draw_box(left_menu, right_menu)
                    break
                else:
                    print(f"{PINK}Invalid selection. Please try again.{RESET}")

                time.sleep(0.5)

        elif choice_int == 4:
            # HIDDEN SERVICES LOGIC - Directly display list of links
            refresh_and_banner(HIDDEN_SERVICES_SUB_MENU_BANNER) # Clear screen and show banner
            print(f"\n{GREEN}--- Hidden Services Links ---{RESET}\n")

            hidden_service_links = [
                ("Doxbin", "doxbin.com"),
                ("hackforums", "hackforums.com"),
                ("Game Pirating", "https://itorrents-igruha.org/"),
            ]

            for name, url in hidden_service_links:
                print(f"{BLUE}{name}{RESET} = {CYAN}{url}{RESET}")

            print("\n" + f"{CYAN}Copy the links and paste them into your Tor browser.{RESET}")
            input(f"{CYAN}Press Enter to return to Main Menu...{RESET}")
            refresh_and_banner(MAIN_BANNER)
            draw_box(left_menu, right_menu)

        elif choice_int == 5:
            # Dark Web Links - This currently uses open_links which opens browsers.
            # As discussed, this will be a project for later.
            links = [
                ("coming soon", "coming soon"),
                ("coming soon", "coming soon")
            ]
            open_links("Dark Web Links", links)

        elif choice_int == 6:
            # OTHER TOOLS SUB-MENU LOGIC
            while True:
                refresh_and_banner(OTHER_TOOLS_SUB_MENU_BANNER) # Clear and display Other Tools banner
                print(f"\n{GREEN}choose an option{RESET}")
                print(f"1. Red-tiger")
                print(f"2. Titan-multitools")
                print(f"3. Thefatrat")
                print(f"4. hackingtool")
                print(f"5. hackingtoolkit")
                print(f"6. hacking tools (search github)") 
                print(f"0. exit") 

                other_tools_sub_choice = input(f"\n{YELLOW}Choose an option (0-6): {RESET}")

                if other_tools_sub_choice == "1":
                    print(f"{BLUE}Opening Red-tiger GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/loxy0dev/RedTiger-Tools") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif other_tools_sub_choice == "2":
                    print(f"{BLUE}Opening Titan-multitools GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/HeartWay-Project/Titan-Multitool") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif other_tools_sub_choice == "3":
                    print(f"{BLUE}Opening Thefatrat GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/screetsec/TheFatRat") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif other_tools_sub_choice == "4":
                    print(f"{BLUE}Opening hackingtool GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/Z4nzu/hackingtool") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif other_tools_sub_choice == "5":
                    print(f"{BLUE}Opening hackingtoolkit GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/CodingRanjith/hackingtoolkit") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif other_tools_sub_choice == "6":
                    print(f"{BLUE}Opening GitHub search for 'hacking tools'...{RESET}")
                    webbrowser.open_new_tab("https://github.com/search?q=hacking+tools&type=repositories") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif other_tools_sub_choice == "0":
                    refresh_and_banner(MAIN_BANNER)
                    draw_box(left_menu, right_menu)
                    break
                else:
                    print(f"{PINK}Invalid selection. Please try again.{RESET}")

                time.sleep(0.5)

        elif choice_int == 7:
            # EXTREME TOOLS SUB-MENU LOGIC
            while True:
                refresh_and_banner(EXTREME_TOOLS_SUB_MENU_BANNER) # Clear and display Extreme Tools banner
                print(f"\n{GREEN}Choose an Option{RESET}")
                print(f"1. Fsociety")
                print(f"2. XERXES")
                print(f"3. Kraken")
                print(f"4. HACKERPRO")
                print(f"5. DDOS (github search)") 
                print(f"0. exit") # Exit option for this sub-menu

                extreme_tools_sub_choice = input(f"\n{YELLOW}Choose an option (0-5): {RESET}")

                if extreme_tools_sub_choice == "1":
                    print(f"{BLUE}Opening Fsociety GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/Manisso/fsociety") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif extreme_tools_sub_choice == "2":
                    print(f"{BLUE}Opening XERXES GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/XCHADXFAQ77X/XERXES") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif extreme_tools_sub_choice == "3":
                    print(f"{BLUE}Opening Kraken GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/jasonxtn/Kraken") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif extreme_tools_sub_choice == "4":
                    print(f"{BLUE}Opening HACKERPRO GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/H4CK3RPR0/HACKERPRO") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif extreme_tools_sub_choice == "5":
                    # GitHub search for DDOS tools
                    print(f"{BLUE}Opening GitHub search for DDOS tools...{RESET}")
                    webbrowser.open_new_tab("https://github.com/search?q=ddos+tools&type=repositories") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif extreme_tools_sub_choice == "0": # Exit option for this sub-menu
                    refresh_and_banner(MAIN_BANNER)
                    draw_box(left_menu, right_menu)
                    break
                else:
                    print(f"{PINK}Invalid selection. Please try again.{RESET}")

                time.sleep(0.5) # Small delay before re-displaying menu

        elif choice_int == 13:
            # NEW: SQL INJECTION TOOLS SUB-MENU LOGIC
            while True:
                refresh_and_banner(SQL_INJECTION_TOOLS_SUB_MENU_BANNER) # Clear and display SQL Injection banner
                print(f"\n{GREEN}Choose an Option{RESET}")
                print(f"1. SQLmap")
                print(f"2. SQLninja")
                print(f"3. bbqSQL")
                print(f"4. pySQLi")
                print(f"5. SQL-Injection-Scanner")
                print(f"6. SQL injection (github search)") 
                print(f"0. exit") # Exit option for this sub-menu

                sql_injection_sub_choice = input(f"\n{YELLOW}Choose an option (0-6): {RESET}")

                if sql_injection_sub_choice == "1":
                    print(f"{BLUE}Opening SQLmap official website...{RESET}")
                    webbrowser.open_new_tab("https://sqlmap.org/") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif sql_injection_sub_choice == "2":
                    print(f"{BLUE}Opening SQLninja GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/xxgrunge/sqlninja") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif sql_injection_sub_choice == "3":
                    print(f"{BLUE}Opening bbqSQL GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/CiscoCXSecurity/bbqsql") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif sql_injection_sub_choice == "4":
                    print(f"{BLUE}Opening pySQLi GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/sysdream/pysqli") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif sql_injection_sub_choice == "5":
                    print(f"{BLUE}Opening SQL-Injection-Scanner GitHub repository...{RESET}")
                    webbrowser.open_new_tab("https://github.com/WooshanGamage/SQL-Injection-Scanner") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif sql_injection_sub_choice == "6":
                    # GitHub search for SQL injection tools
                    print(f"{BLUE}Opening GitHub search for SQL injection tools...{RESET}")
                    webbrowser.open_new_tab("https://github.com/search?q=sql+injection+tools&type=repositories") 
                    input(f"{CYAN}Press Enter to continue...{RESET}")
                elif sql_injection_sub_choice == "0": # Exit option for this sub-menu
                    refresh_and_banner(MAIN_BANNER)
                    draw_box(left_menu, right_menu)
                    break
                else:
                    print(f"{PINK}Invalid selection. Please try again.{RESET}")

                time.sleep(0.5) # Small delay before re-displaying menu

        # Updated handling for options 10, 14-18 with new names
        elif choice_int == 10:
            print(f"\n{GREEN}-- Advanced Exploitation (Coming Soon) --{RESET}")
            print(f"This section will feature advanced exploitation techniques and frameworks.")
            input(f"{CYAN}Press Enter to return to Main Menu...{RESET}")
            refresh_and_banner(MAIN_BANNER)
            draw_box(left_menu, right_menu)

        elif choice_int == 11:
            print(f"\n{GREEN}-- ClarityAI (beta) --{RESET}")
            print(f"ClarityAI is an AI assistant to help with security queries. (Feature coming soon!)")
            input(f"{CYAN}Press Enter to return to Main Menu...{RESET}")
            refresh_and_banner(MAIN_BANNER)
            draw_box(left_menu, right_menu)

        elif choice_int == 12:
            print(f"\n{GREEN}-- Self Security --{RESET}")
            print(f"Information on self-security best practices.")
            input(f"{CYAN}Press Enter to return to Main Menu...{RESET}")
            refresh_and_banner(MAIN_BANNER)
            draw_box(left_menu, right_menu)

        elif choice_int == 14:
            print(f"\n{GREEN}-- Network Penetration (Coming Soon) --{RESET}")
            print(f"This section will cover tools and resources for network security assessments.")
            input(f"{CYAN}Press Enter to return to Main Menu...{RESET}")
            refresh_and_banner(MAIN_BANNER)
            draw_box(left_menu, right_menu)

        elif choice_int == 15:
            print(f"\n{GREEN}-- Reverse Engineering (Coming Soon) --{RESET}")
            print(f"This section will provide resources for software reverse engineering and malware analysis.")
            input(f"{CYAN}Press Enter to return to Main Menu...{RESET}")
            refresh_and_banner(MAIN_BANNER)
            draw_box(left_menu, right_menu)

        elif choice_int == 16:
            print(f"\n{GREEN}-- Social Engineering (Coming Soon) --{RESET}")
            print(f"This section will offer insights and tools related to social engineering tactics and defense.")
            input(f"{CYAN}Press Enter to return to Main Menu...{RESET}")
            refresh_and_banner(MAIN_BANNER)
            draw_box(left_menu, right_menu)

        elif choice_int == 17:
            print(f"\n{GREEN}-- Cloud Security Assessment (Coming Soon) --{RESET}")
            print(f"This section will focus on tools and best practices for securing cloud environments.")
            input(f"{CYAN}Press Enter to return to Main Menu...{RESET}")
            refresh_and_banner(MAIN_BANNER)
            draw_box(left_menu, right_menu)

        elif choice_int == 18:
            print(f"\n{GREEN}-- Bug Bounty Resources (Coming Soon) --{RESET}")
            print(f"This section will provide resources for bug bounty hunting and vulnerability disclosure.")
            input(f"{CYAN}Press Enter to return to Main Menu...{RESET}")
            refresh_and_banner(MAIN_BANNER)
            draw_box(left_menu, right_menu)

        else:
            print(f"{PINK}Invalid selection.{RESET}")
    else:
        print(f"{PINK}Invalid input. Please enter a number or 'exit'.{RESET}")
