menu = {
    "Phone book": {
        "Search": None,
        "Service Nos": None,
        "Add name": None,
        "Erase": None,
        "Edit": None,
        "Assign tone": None,
        "Send b_card": None,
        "Option": {
            "Type of view": None,
            "Memory status": None
        },
        "Speed dials": None,
        "Voice tags": None
    },
    "Messages": {
        "Write Message": None,
        "Inbox": None,
        "Outbox": None,
        "Picture Messages": None,
        "Templates": None,
        "Smileys": None,
        "Message Settings": {
            "Set": {
                "Message center number": None,
                "Message sent as": None,
                "Message validity": None
            },
            "Common": {
                "Delivery reports": None,
                "Reply via same centre": None,
                "Character support": None
            }
        },
        "Info service": None,
        "Voice mailbox number": None,
        "Service command editor": None
    },
    "Chat": None,
    "Call Register": {
        "Missed Calls": None,
        "Received Calls": None,
        "Dialed Numbers": None,
        "Erase recent call list": None,
        "Show call Duration": {
            "Last call duration": None,
            "All calls duration": None,
            "Received calls duration": None,
            "Dialled calls duration": None,
            "Clear timers": None
        },
        "Show call Costs": {
            "Last call cost": None,
            "All call cost": None,
            "Clear counter": None
        },
        "Call cost settings": {
            "Call cost limit": None,
            "Show cost in": None
        },
        "Prepaid credit": None
    },
    "Tones": {
        "Ringing Tone": None,
        "Ringing Volume": None,
        "Incoming call alert": None,
        "Composer": None,
        "Message Alert Tone": None,
        "Keypad Tones": None,
        "Warning and game tones": None,
        "Vibrating alert": None,
        "Screen saver": None
    },
    "Settings": {
        "Call settings": {
            "Automatic redial": None,
            "Speed dialling": None,
            "Call waiting option": None,
            "Own number sending": None,
            "Phone line in use": None,
            "Automatic answer": None
        },
        "Phone Settings": {
            "Language": None,
            "Cell info display": None,
            "Welcome note": None,
            "Network selection": None,
            "Lights": None,
            "Confirm SIM actions": None
        },
        "Security Settings": {
            "PIN code request": None,
            "Call barring service": None,
            "Fixed dialling": None,
            "Closed user group": None,
            "Phone security": None,
            "Change access code": None
        },
        "Restore factory settings": None
    },
    "Call divert": None,
    "Games": None,
    "Calculator": None,
    "Reminder": None,
    "Clock": {
        "Alarm clock": None,
        "Clock settings": None,
        "Date settings": None,
        "Stopwatch": None,
        "Countdown timer": None,
        "Auto update of date and time": None
    },
    "Profiles": None,
    "SIM Services": None
}

def navigate_menu(menu_dict, path="Main Menu"):
    while True:
        print(f"\n--- {path} ---")
        options = list(menu_dict.keys())
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print("0. Back")

        user_input = input("Select an option (0 to go back): ").strip()
        if user_input.isdigit():
            choice = int(user_input)
            if choice == 0:
                break
            elif 1 <= choice <= len(options):
                selected_option = options[choice - 1]
                sub_menu = menu_dict[selected_option]
                if isinstance(sub_menu, dict):
                    navigate_menu(sub_menu, path=f"{path} > {selected_option}")
                else:
                    print(f"You selected: {selected_option}")
            else:
                print("Invalid selection.")
        else:
            print("Please enter a valid number.")

def main():
    print("=== Nokia 3310 Menu ===")
    navigate_menu(menu)

if __name__ == "__main__":
    main()