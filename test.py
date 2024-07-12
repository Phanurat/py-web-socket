from selenium import webdriver

# สร้าง WebDriver object สำหรับ Chrome
driver = webdriver.Chrome()

# ใช้ Session ในการเปิด URL
driver.get("https://facebook.com")

# สร้าง session ID ที่เป็นตัวระบุเพื่อเก็บข้อมูลเช่น
session_id = driver.session_id

# เพื่อใช้งานของ cookie ตัวอย่าง บันทึกจำ cookies
