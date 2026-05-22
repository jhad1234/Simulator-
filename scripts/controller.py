import os
import sys

PROVIDERS = {
    "1": {"name": "Sabafon", "mcc": "421", "mnc": "01"},
    "2": {"name": "Yemen-Mobile", "mcc": "421", "mnc": "04"},
    "3": {"name": "YOU", "mcc": "421", "mnc": "02"}
}

def update_config(choice):
    if choice not in PROVIDERS:
        print("اختيار خاطئ!")
        return
    
    prov = PROVIDERS[choice]
    conf_path = "config/enb.conf"
    
    with open(conf_path, 'r') as f:
        lines = f.readlines()
    
    with open(conf_path, 'w') as f:
        for line in lines:
            if line.startswith("mcc ="): f.write(f"mcc = {prov['mcc']}\n")
            elif line.startswith("mnc ="): f.write(f"mnc = {prov['mnc']}\n")
            else: f.write(line)
            
    print(f"تم تحديث {prov['name']} (MCC:{prov['mcc']}, MNC:{prov['mnc']})")
    print("يرجى إعادة تشغيل خدمة srsenb لتطبيق التغييرات.")

if __name__ == "__main__":
    print("اختر المزود: 1:Sabafon, 2:Yemen-Mobile, 3:YOU")
    choice = input("الخيار: ")
    update_config(choice)
