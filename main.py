""" Test Script to create policy through Biberk.com in a Happy Path manner
    Author: Joshua Martinez
    Updated: 6/15/2023
"""
import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Different Variables for policy creation
Industry = "Flowers Shop"
businessName = "Automated Selenium Flower Shop"
yearBusinessStarted = "2015"
streetAddress = "155 Avenida Cabrillo"
city = "San Clemente"
firtsName = "Driver"
lastName = "LastName"
zipcode = "92672"
dateOfBirth = "03/04/1987"
vinNumber = "5YJSA1S20FF096314"
driverLicense = "V7298587"


"""""
    Here we call the the specific webdriver this case is for Chrome, also ChromeDriverManager makes it easy for us
"""""

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www-qa-portalspa.biberk.com/")

# Clicks on "Get a Quote" btn to begin quote flow
time.sleep(1)
getQuotebtn = driver.find_element(By.XPATH, "//button[@class='btn secondary width-med waves-effect with-icon-right']")
getQuotebtn.click()
assert getQuotebtn == "Get a Quote"

# Here we select the & click the industry we will test
industryClick = driver.find_element(By.XPATH, "//input[@name='autocompleteIndustryControl']")
industryClick.click()
industryClick.send_keys(Industry)
time.sleep(1)
letsGo = driver.find_element(By.XPATH, "//button[@data-qa='next-button']")
letsGo.click()

# Here we select if we have employess. We chose to say No employess
wait = WebDriverWait(driver, 30)
wEmployees = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='no-employees-button']"))).click()
time.sleep(1)
employeNextbtn = driver.find_element(By.XPATH, "//button[@data-qa='bbnav-navNext-tablet']")
employeNextbtn.click()

# Here is the business operation page
time.sleep(1)
businessOperation = driver.find_element(By.XPATH, "//button[@data-qa='TEBUILDING-button']")
businessOperation.click()
time.sleep(1)
bussinOpeBtn = driver.find_element(By.XPATH, "//button[@data-qa='bbnav-navNext-tablet']")
bussinOpeBtn.click()

# Here is the Business Owners Insurance, and we are choosing only Vehicles
time.sleep(1)
clickVehicles  = driver.find_element(By.XPATH, "//mat-checkbox[@data-qa='leaseItemTypes-0-checkbox']")
clickVehicles.click()
time.sleep(1)
vehiclesNextbtn = driver.find_element(By.XPATH, "//button[@data-qa='bbnav-navNext-tablet']")
vehiclesNextbtn.click()


# This is the zipcode page, and we just enter a zipcode
time.sleep(1)
zipcodeInput = driver.find_element(By.XPATH, "//input[@data-qa='zipCode-zipCodeControl-zipcode']")
zipcodeInput.click()
time.sleep(1)
zipcodeInput.send_keys(zipcode)
zipcodeNextBtn = driver.find_element(By.XPATH, "//button[@data-qa='bbnav-navNext-tablet']")
zipcodeNextBtn.click()

# Here we choose the Coverage Option we want to test. We selected Commercial Auto
wait = WebDriverWait(driver, 30)
CABtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='btn-lob-CA']"))).click()
CAbtn = driver.find_element(By.XPATH, "//button[@data-qa='btn-lob-CA']")


wait = WebDriverWait(driver, 30)
wbusinessName = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-qa='businessName']"))).click()
businessNameInput = driver.find_element(By.XPATH, "//input[@data-qa='businessName']")
businessNameInput.send_keys(businessName)

# Does your business go by another name?
time.sleep(1)
# Here we are clicking No
anotherNamebtn = driver.find_element(By.XPATH, "//button[@data-qa='hasDBA-no-button']")
anotherNamebtn.click()

time.sleep(1)
letsGobtn = driver.find_element(By.XPATH, "//button[@data-qa='bbnav-navNext-tablet']")
letsGobtn.click()

# what did the business start?
wait = WebDriverWait(driver, 30)
wyearBusiness = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-qa='_apollo_YearBusinessStarted']"))).click()
yearBusinessStartedClick = driver.find_element(By.XPATH, "//input[@data-qa='_apollo_YearBusinessStarted']")
yearBusinessStartedClick.send_keys(yearBusinessStarted)

# How is your Business Structured?
wait = WebDriverWait(driver, 30)
wbusinnesStructure = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@data-qa='_apollo_BusinessStructure']"))).click()
businessStructure = driver.find_element(By.XPATH, "//mat-select[@data-qa='_apollo_BusinessStructure']")


# Clicks on Coporation option within Business Structure
corporationBtn = driver.find_element(By.XPATH, "//*[text()=' Corporation ']")
corporationBtn.click()


# Here we enter the Business Address
streetAddressClick = driver.find_element(By.XPATH, "//input[@data-qa='_apollo_PhysicalBusinessAddress-line1']")
streetAddressClick.click()
streetAddressClick.send_keys("155 Avenida Cabrillo")
cityClick = driver.find_element(By.XPATH, "//input[@data-qa='_apollo_PhysicalBusinessAddress-majorMunicipality-city']")
cityClick.click()
cityClick.send_keys(city)
time.sleep(2)
letsContinue1 = driver.find_element(By.XPATH, "//button[@data-qa='bbnav-navNext-tablet']")
letsContinue1.click()

# Here we enter the vin number for the vehicle
wait = WebDriverWait(driver, 30)
yvinBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='vin-0-yes']"))).click()
vinNumberClick = driver.find_element(By.XPATH, "//input[@data-qa='vin-0']")
vinNumberClick.send_keys(vinNumber)

# here we click on the errands only option
wait = WebDriverWait(driver, 30)
werrandsOnly = wait.until(EC.element_to_be_clickable((By.XPATH, ("//label[@for='_apollo_VehicleUseRetail_0-9010-Errands only - no Delivery/Catering']")))).click()
errandsOnly = driver.find_element(By.XPATH, "//label[@for='_apollo_VehicleUseRetail_0-9010-Errands only - no Delivery/Catering']")
errandsOnly.click()

# Here we click on the "Is this vehicle used to deliver goods or materials?" Question
deliverGoodsQ = driver.find_element(By.XPATH, "//button[@data-qa='_apollo_GoodsOrMaterialsRetail_0-9010-no-button']")
deliverGoodsQ.click()
letsContinue2 = driver.find_element(By.XPATH, "//button[@data-qa='bbnav-navNext-tablet']")
letsContinue2.click()

# Here we enter the first and last name for the driver
wait = WebDriverWait(driver, 30)
firtsNameClick = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Drivers-0-firstName']"))).click()
firstNameInput = driver.find_element(By.XPATH, "//input[@name='Drivers-0-firstName']")
firstNameInput.send_keys(firtsName)
lastNameClick = driver.find_element(By.XPATH, "//input[@name='Drivers-0-lastName']")
lastNameClick.send_keys(lastName)

# Here we select the state of the driver's license
wait = WebDriverWait(driver, 30)
driverLicenseState = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@data-qa='_apollo_DriverLicenseState_0']"))).click()
driverLicenseStateClick = driver.find_element(By.XPATH, "//mat-select[@data-qa='_apollo_DriverLicenseState_0']")
driverLicenseStateClick.click()
caLicense = driver.find_element(By.XPATH, "mat-option[@data-qa='_apollo_DriverLicenseState_0-CA']")
caLicense.click()
# date of birth
dobClick = driver.find_element(By.XPATH, "//input[@placeholder='MM/DD/YYYY']")
dobClick.send_keys(dateOfBirth)
# Question: Has this driver had an accident or violation...
dViolationQ = driver.find_element(By.XPATH, "//bb-buttonlist-item[@value='false']")
dViolationQ.click()
# Enter driver license
driverLicenseClick = driver.find_element(By.XPATH, "//input[@data-qa='_apollo_DriverLicenseNumber_CA_0']")
driverLicenseClick.send_keys(driverLicense)
letsContinue3 = driver.find_element(By.XPATH, "//button[@data-qa='bbnav-navNext-tablet']")
letsContinue3.click()






















