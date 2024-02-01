import sys
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

website = 'https://cekdptonline.kpu.go.id/'
path = 'chromedriver.exe'

# NIK yang ingin dicari
nik_to_search = sys.argv[1]

driver = webdriver.Chrome()

try:
    driver.get(website)
    pencarian = driver.find_element("xpath", '//input[@class="form-control is-valid"]')
    pencarian.clear()
    pencarian.send_keys(nik_to_search)
    pencarian.send_keys(Keys.RETURN)

    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="row row-1"]')))
    element = driver.find_element("xpath", '//div[@class="row row-1"]')
    hasil = element.text
    lines = hasil.split('\n')
    nama_pemilih = lines[1] if len(lines) > 1 else ''
    tps = lines[3] if len(lines) > 3 else ''

    element_2 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="row row-1"]')))
    element_2 = driver.find_element("xpath", '//div[@class="row row-3"]')
    hasil_2 = element_2.text
    lines_2 = hasil_2.split('\n')
    kabupaten = lines_2[1] if len(lines_2) > 1 else ''
    kecamatan = lines_2[3] if len(lines_2) > 3 else ''
    kelurahan = lines_2[5] if len(lines_2) > 5 else ''

    element_3 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//p[@class="row--left"]')))
    element_3 = driver.find_elements("xpath", '//p[@class="row--left"]')
    if element_3 and len(element_3) >= 2:
        element_yang_kedua = element_3[1]
        hasil_3 = element_yang_kedua.text
        lines_3 = hasil_3.split('\n')
        alamat = lines_3[1] if len(lines_3) > 1 else ''

    individual_data = {
        'nama_pemilih': nama_pemilih,
        'tps': tps,
        'kabupaten': kabupaten,
        'kecamatan': kecamatan,
        'kelurahan': kelurahan,
        'alamat': alamat
    }
    print(json.dumps(individual_data))

except TimeoutException:
    print(json.dumps({'error':'error'}))

driver.quit()
