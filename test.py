import random
import os
import signal

def generate_credit_card():
    prefix = "494577"
    random_digits = ''.join(random.choice('0123456789') for _ in range(10))
    expiration_date = f"{random.randint(1, 12):02d}|{random.randint(2022, 2030)}"
    security_code = random.randint(100, 999)
    credit_card_number = f"{prefix}{random_digits}|{expiration_date}|{security_code}"
    return credit_card_number

# Luhn algoritması kontrolü
def is_luhn_valid(card_number):
    digits = [int(digit) for digit in card_number if digit.isdigit()]
    checksum = digits.pop()
    digits.reverse()
    doubled_digits = [int(digit) * 2 if i % 2 == 0 else int(digit) for i, digit in enumerate(digits)]
    summed_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]
    total = sum(summed_digits) + checksum
    return total % 10 == 0

# Dosya adı
file_name = "cc.txt"

# Ctrl+C sinyali alındığında çağrılacak fonksiyon
def handle_exit(signal, frame):
    print("\nUygulama kapatılıyor. Son kredi kartı numaraları dosyaya kaydediliyor.")
    exit(0)

# Ctrl+C sinyali için işlemleri tanımla
signal.signal(signal.SIGINT, handle_exit)

# Renkli banner ve bilgilendirici mesajlar
print("""
\033[94m
    _                 _                      
   /_\  _ _ _  _ _ __(_)_ _  __ _            
  / _ \| '_| || | '_ \ | ' \/ _` |           
 /_/ \_\_| \_,_| .__/_|_||_\__, |           
   ___ ___    __|_|__ ___   |___/__ ___  ___ 
  / __/ __|  / __| _ \ __| /_\_   _/ _ \| _ \\
 | (_| (__  | (__|   / _| / _ \| || (_) |   /
  \___\___|  \___|_|_\___/_/ \_\_| \___/|_|_\\
  
  \033[0m
  		 CREATING CC...
\033[91m		CTRL + C SAVING \033[0m
""")

try:
    while True:
        generated_card = generate_credit_card()

        if is_luhn_valid(generated_card):
            with open(file_name, "a") as file:
                file.write(generated_card + "\n")
except KeyboardInterrupt:
    pass
finally:
    print("\nUygulama kapatıldı. Son kredi kartı numaraları dosyaya kaydedildi:", file_name)
