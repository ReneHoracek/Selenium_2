from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import csv
import time

# --- KONFIGURACE ---
CSV_FILE = ''
BASE_URL = ""

# 1. Inicializace prohlížeče
driver = webdriver.Chrome()
driver.get(BASE_URL)

print("PŘIHLAŠ SE RUČNĚ DO WORDPRESSU.")
print("Až budeš na stránce 'Nová transakce', stiskni v tomto terminálu ENTER...")
input()



# 2. Načtení a zpracování CSV
try:
    with open(CSV_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row: continue
            email = row[0].strip()
            
            driver.get(BASE_URL)
            wait = WebDriverWait(driver, 15)

            try:
                user_input = wait.until(EC.presence_of_element_located((By.ID, "user_login")))
                user_input.clear()
                user_input.send_keys(email)
                
                status_select = Select(driver.find_element(By.ID, "status"))
                status_select.select_by_visible_text("Dokončeno")
                
                create_button = driver.find_element(By.ID, "submit")
                create_button.click()

                print(f"✅ Úspěšně zpracováno: {email}")
                time.sleep(1)

            except Exception as e:
                print(f"❌ Chyba u e-mailu {email}: {e}")
                continue

except FileNotFoundError:
    print(f"Soubor {CSV_FILE} nebyl nalezen. Ujisti se, že je ve stejné složce jako skript.")

print("\n--- HOTOVO ---")
driver.quit()
