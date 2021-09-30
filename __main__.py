from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback

#load chrom
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('log-level=3')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

#load page
driver.get('https://10fastfingers.com/advanced-typing-test/english')
timeout = 10
element_present = EC.presence_of_element_located((By.ID, 'main'))
WebDriverWait(driver, timeout).until(element_present)

#mainloop
try:
    while True:
        #get word
        letter = driver.find_element_by_class_name("highlight").text

        #execute autotype
        inputElement = driver.find_element_by_id("inputfield")
        inputElement.send_keys(letter)
        inputElement.send_keys(" ")
except Exception:
    traceback.print_exc()