# 📡 Yemen Network & ISP Emulator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Pylint](https://github.com/jhad1234/Simulator-/actions/workflows/pylint.yml/badge.svg)](https://github.com/jhad1234/Simulator-/actions/workflows/pylint.yml)

مشروع مفتوح المصدر لمحاكاة شبكات الاتصالات (LTE) اليمنية وتغيير هوية مزود الإنترنت.

## 🚀 نظرة عامة (Overview)
هذا المحاكي متخصص في إدارة وتغيير إعدادات الشبكة لمزودي الاتصالات المختلفين في اليمن (Sabafon, Yemen-Mobile, YOU) عن طريق تحديث ملفات الإعداد (\`enb.conf\`) تلقائياً. مصمم للأغراض التعليمية والبحثية في بيئة مغلقة.

## 🛠️ المزودون المدعومون (Supported Providers)
| المزود (Provider) | MCC | MNC |
| :--- | :--- | :--- |
| **Sabafon** | 421 | 01 |
| **Yemen-Mobile** | 421 | 04 |
| **YOU** | 421 | 02 |

## 📁 هيكلية المشروع (Project Structure)
- \`scripts/controller.py\`: الواجهة الأساسية للتحكم في MCC/MNC.
- **srsRAN**: المحرك الأساسي للشبكة (يتطلب تثبيت خارجي).
- \`config/\`: المجلد الذي يحتوي على ملفات إعداد الشبكة.

## 💻 طريقة الاستخدام (Usage)
1. قم بتثبيت srsRAN:
   \\\`bash
   sudo apt install srsran
   \\\`
2. تشغيل واجهة التحكم:
   \\\`bash
   python3 scripts/controller.py
   \\\`
3. اختر المزود من القائمة ثم أعد تشغيل خدمة \`srsenb\` لتطبيق التغييرات.

## ⚠️ تنبيه هام (Disclaimer)
هذا المشروع مخصص للأغراض التعليمية في بيئة مغلقة فقط. لا يتحمل المطور أي مسؤولية عن سوء الاستخدام خارج النطاق التجريبي.

## 🛡️ ضمان الجودة (Quality Assurance)
يتم فحص الكود بدقة باستخدام **Pylint** لضمان أعلى مستويات الجودة والالتزام بأفضل ممارسات البرمجة.

---
*تم التطوير بواسطة [jhad1234](https://github.com/jhad1234)*
