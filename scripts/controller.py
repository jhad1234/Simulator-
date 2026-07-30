"""
Module to update the eNB configuration for different providers in Yemen.
"""

PROVIDERS = {
    "1": {"name": "Sabafon", "mcc": "421", "mnc": "01"},
    "2": {"name": "Yemen-Mobile", "mcc": "421", "mnc": "04"},
    "3": {"name": "YOU", "mcc": "421", "mnc": "02"}
}

def update_config(provider_choice):
    """
    Updates the enb.conf file with the MCC and MNC of the selected provider.
    """
    if provider_choice not in PROVIDERS:
        print("اختيار خاطئ!")
        return

    prov = PROVIDERS[provider_choice]
    conf_path = "config/enb.conf"

    try:
        with open(conf_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open(conf_path, 'w', encoding='utf-8') as f:
            for line in lines:
                if line.startswith("mcc ="):
                    f.write(f"mcc = {prov['mcc']}\n")
                elif line.startswith("mnc ="):
                    f.write(f"mnc = {prov['mnc']}\n")
                else:
                    f.write(line)

        print(f"تم تحديث {prov['name']} (MCC:{prov['mcc']}, MNC:{prov['mnc']})")
        print("يرجى إعادة تشغيل خدمة srsenb لتطبيق التغييرات.")
    except FileNotFoundError:
        print(f"خطأ: لم يتم العثور على ملف الإعداد في {conf_path}")

if __name__ == "__main__":
    print("اختر المزود: 1:Sabafon, 2:Yemen-Mobile, 3:YOU")
    user_choice = input("الخيار: ")
    update_config(user_choice)
