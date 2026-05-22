import os

# قاعدة بيانات المزودين
PROVIDERS = {
    "1": {"name": "Sabafon", "mcc": "421", "mnc": "01"},
    "2": {"name": "Yemen-Mobile", "mcc": "421", "mnc": "04"},
    "3": {"name": "YOU", "mcc": "421", "mnc": "02"},
    "4": {"name": "Y", "mcc": "421", "mnc": "03"}
}

def update_config(provider_key):
    prov = PROVIDERS.get(provider_key)
    if not prov:
        print("خطأ: اختيار غير صحيح!")
        return
    
    print(f"تم اختيار: {prov['name']} | MCC: {prov['mcc']} | MNC: {prov['mnc']}")
    # هنا تضع كود تعديل ملفات الإعداد الخاصة بـ srsRAN

if __name__ == "__main__":
    print("--- اختيار مزود الخدمة ---")
    print("1: Sabafon | 2: Yemen-Mobile | 3: YOU | 4: Y")
    choice = input("ادخل رقم المزود: ")
    update_config(choice)
