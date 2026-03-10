from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import os

ACCOUNT_EMAIL = "odysseas_98@icloud.com"
ACCOUNT_PASSWORD = "papagos000"
URL = "https://appbrewery.github.io/gym/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, 2)

login_button = driver.find_element(By.XPATH,"//*[@id='login-button']")
login_button.click()
email_input = driver.find_element(By.XPATH,"//*[@id='email-input']")
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)
password_input = driver.find_element(By.XPATH,"//*[@id='password-input']")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)
submit_button = driver.find_element(By.XPATH,"/html/body/div/main/div/form/button")
submit_button.click()

wait.until(ec.pressence_of_element_located(By.ID, "schedule-page"))

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")


booked_count = 0
waitlist_count = 0
already_booked_count = 0

processed_classes = []

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday OR Thursday
    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            # Track the class details
            class_info = f"{class_name} on {day_title}"

            if button.text == "Booked":
                print(f"✓ Already booked: {class_info}")
                already_booked_count += 1
                # Add detailed class info
                processed_classes.append(f"[Booked] {class_info}")
            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_booked_count += 1
                # Add detailed class info
                processed_classes.append(f"[Waitlisted] {class_info}")
            elif button.text == "Book Class":
                button.click()
                print(f"✓ Successfully booked: {class_info}")
                booked_count += 1
                # Add detailed class info
                processed_classes.append(f"[New Booking] {class_info}")
                time.sleep(0.5)
            elif button.text == "Join Waitlist":
                button.click()
                print(f"✓ Joined waitlist for: {class_info}")
                waitlist_count += 1
                # Add detailed class info
                processed_classes.append(f"[New Waitlist] {class_info}")
                time.sleep(0.5)

total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
my_bookings_link.click()

wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

verified_count = 0

all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")
