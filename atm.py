
balance = 10000
pin = "1234"

languages = {
    "1": {
        "name": "English",
        "welcome": "WELCOME TO ATM",
        "enter_pin": "Enter your PIN: ",
        "wrong_pin": "Incorrect PIN.",
        "success": "Login successful!",
        "blocked": "Too many incorrect attempts. Your card has been blocked.",
        "menu": "ATM MENU",
        "balance": "Check Balance",
        "withdraw": "Withdraw Money",
        "deposit": "Deposit Money",
        "change_pin": "Change PIN",
        "exit": "Exit",
        "choice": "Enter your choice: ",
        "current_balance": "Your current balance is",
        "withdraw_amount": "Enter withdrawal amount: ₹",
        "invalid_amount": "Please enter a valid amount.",
        "insufficient": "Insufficient balance.",
        "multiple": "Please enter an amount in multiples of ₹100.",
        "collect": "Please collect your cash",
        "remaining": "Remaining balance",
        "deposit_amount": "Enter deposit amount: ₹",
        "deposited": "deposited successfully.",
        "new_balance": "New balance",
        "current_pin": "Enter your current PIN: ",
        "new_pin": "Enter your new 4-digit PIN: ",
        "pin_changed": "PIN changed successfully.",
        "pin_error": "PIN must contain exactly 4 digits.",
        "invalid_choice": "Invalid choice. Please select 1-5.",
        "invalid_number": "Invalid input. Please enter a number.",
        "thank": "Thank you for using our ATM.",
        "card": "Please take your card."
    },

    "2": {
        "name": "বাংলা",
        "welcome": "ATM-এ স্বাগতম",
        "enter_pin": "আপনার PIN দিন: ",
        "wrong_pin": "ভুল PIN।",
        "success": "লগইন সফল হয়েছে!",
        "blocked": "তিনবার ভুল PIN দেওয়া হয়েছে। আপনার কার্ড ব্লক করা হয়েছে।",
        "menu": "ATM মেনু",
        "balance": "ব্যালেন্স দেখুন",
        "withdraw": "টাকা তুলুন",
        "deposit": "টাকা জমা দিন",
        "change_pin": "PIN পরিবর্তন করুন",
        "exit": "বেরিয়ে যান",
        "choice": "আপনার পছন্দ দিন: ",
        "current_balance": "আপনার বর্তমান ব্যালেন্স",
        "withdraw_amount": "কত টাকা তুলবেন: ₹",
        "invalid_amount": "সঠিক পরিমাণ লিখুন।",
        "insufficient": "পর্যাপ্ত ব্যালেন্স নেই।",
        "multiple": "অনুগ্রহ করে ₹100-এর গুণিতকে টাকা তুলুন।",
        "collect": "আপনার টাকা সংগ্রহ করুন",
        "remaining": "অবশিষ্ট ব্যালেন্স",
        "deposit_amount": "কত টাকা জমা দেবেন: ₹",
        "deposited": "সফলভাবে জমা হয়েছে।",
        "new_balance": "নতুন ব্যালেন্স",
        "current_pin": "বর্তমান PIN দিন: ",
        "new_pin": "নতুন 4 সংখ্যার PIN দিন: ",
        "pin_changed": "PIN সফলভাবে পরিবর্তন হয়েছে।",
        "pin_error": "PIN অবশ্যই 4 সংখ্যার হতে হবে।",
        "invalid_choice": "ভুল পছন্দ। 1-5 এর মধ্যে নির্বাচন করুন।",
        "invalid_number": "ভুল ইনপুট। একটি সংখ্যা দিন।",
        "thank": "আমাদের ATM ব্যবহার করার জন্য ধন্যবাদ।",
        "card": "আপনার কার্ডটি নিয়ে নিন।"
    },

    "3": {
        "name": "हिन्दी",
        "welcome": "ATM में आपका स्वागत है",
        "enter_pin": "अपना PIN दर्ज करें: ",
        "wrong_pin": "गलत PIN।",
        "success": "लॉगिन सफल हुआ!",
        "blocked": "तीन बार गलत PIN दर्ज किया गया। आपका कार्ड ब्लॉक कर दिया गया है।",
        "menu": "ATM मेनू",
        "balance": "बैलेंस देखें",
        "withdraw": "पैसे निकालें",
        "deposit": "पैसे जमा करें",
        "change_pin": "PIN बदलें",
        "exit": "बाहर निकलें",
        "choice": "अपना विकल्प चुनें: ",
        "current_balance": "आपका वर्तमान बैलेंस",
        "withdraw_amount": "कितने पैसे निकालने हैं: ₹",
        "invalid_amount": "कृपया सही राशि दर्ज करें।",
        "insufficient": "पर्याप्त बैलेंस नहीं है।",
        "multiple": "कृपया ₹100 के गुणक में राशि दर्ज करें।",
        "collect": "कृपया अपने पैसे ले लें",
        "remaining": "बाकी बैलेंस",
        "deposit_amount": "कितने पैसे जमा करने हैं: ₹",
        "deposited": "सफलतापूर्वक जमा किए गए।",
        "new_balance": "नया बैलेंस",
        "current_pin": "अपना वर्तमान PIN दर्ज करें: ",
        "new_pin": "नया 4 अंकों का PIN दर्ज करें: ",
        "pin_changed": "PIN सफलतापूर्वक बदल दिया गया।",
        "pin_error": "PIN में ठीक 4 अंक होने चाहिए।",
        "invalid_choice": "गलत विकल्प। 1-5 में से चुनें।",
        "invalid_number": "गलत इनपुट। कृपया संख्या दर्ज करें।",
        "thank": "हमारा ATM इस्तेमाल करने के लिए धन्यवाद।",
        "card": "कृपया अपना कार्ड ले लें।"
    }
}

print("================================ - atm.py:109")
print("SELECT LANGUAGE - atm.py:110")
print("================================ - atm.py:111")
print("1. English - atm.py:112")
print("2. বাংলা - atm.py:113")
print("3. हिन्दी - atm.py:114")
print("================================ - atm.py:115")

language_choice = input("Select language / ভাষা নির্বাচন করুন / भाषा चुनें: ")

if language_choice not in languages:
    print("Invalid language selection. - atm.py:120")
    exit()

L = languages[language_choice]

print("\n================================ - atm.py:125")
print("       " + L["welcome"])
print("================================ - atm.py:127")

for attempt in range(3):

    entered_pin = input(L["enter_pin"])

    if entered_pin == pin:
        print(L["success - atm.py:134"])
        break
    else:
        print(L["wrong_pin - atm.py:137"])

else:
    print(L["blocked - atm.py:140"])
    exit()

while True:

    print("\n================================ - atm.py:145")
    print("          " + L["menu"])
    print("================================ - atm.py:147")

    print("1. - atm.py:149" + L["balance"])
    print("2. - atm.py:150" + L["withdraw"])
    print("3. - atm.py:151" + L["deposit"])
    print("4. - atm.py:152" + L["change_pin"])
    print("5. - atm.py:153" + L["exit"])

    print("================================ - atm.py:155")

    choice = input(L["choice"])

    if choice == "1":

        print("\n - atm.py:161" + L["current_balance"] + ": ₹" + format(balance, ".2f"))


    elif choice == "2":

        try:

            amount = float(input(L["withdraw_amount"]))

            if amount <= 0:
                print(L["invalid_amount - atm.py:171"])

            elif amount > balance:
                print(L["insufficient - atm.py:174"])

            elif amount % 100 != 0:
                print(L["multiple - atm.py:177"])

            else:
                balance -= amount

                print("\n - atm.py:182" + L["collect"] + ": ₹" + format(amount, ".2f"))
                print(L["remaining - atm.py:183"] + ": ₹" + format(balance, ".2f"))

        except ValueError:
            print(L["invalid_number - atm.py:186"])


    elif choice == "3":

        try:

            amount = float(input(L["deposit_amount"]))

            if amount <= 0:
                print(L["invalid_amount - atm.py:196"])

            else:
                balance += amount

                print("\n₹ - atm.py:201" + format(amount, ".2f") + " " + L["deposited"])
                print(L["new_balance - atm.py:202"] + ": ₹" + format(balance, ".2f"))

        except ValueError:
            print(L["invalid_number - atm.py:205"])


    elif choice == "4":

        old_pin = input(L["current_pin"])

        if old_pin == pin:

            new_pin = input(L["new_pin"])

            if len(new_pin) == 4 and new_pin.isdigit():

                pin = new_pin
                print(L["pin_changed - atm.py:219"])

            else:
                print(L["pin_error - atm.py:222"])

        else:
            print(L["wrong_pin - atm.py:225"])



    elif choice == "5":

        print("\n - atm.py:231" + L["thank"])
        print(L["card - atm.py:232"])
        break


    else:
        print(L["invalid_choice - atm.py:237"])
