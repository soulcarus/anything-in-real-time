from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import time

def capture_screenshot(driver, url, file_name):
    try:
        driver.get(url)
        wait_for_page_load(driver)

        try:
            WebDriverWait(driver, 3).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".sr-only.ng-binding"))
            )
        except:
            pass

        try:
            button = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-button.primary"))
            )
            button.click()
            WebDriverWait(driver, 1).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "ui-loader"))
            )
            driver.execute_script("document.querySelector('.report__section').remove();")
            
        except:
            pass
  
        driver.save_screenshot(file_name)
    
    except Exception as e:
        print(f"Error on trying to capture the URL {url}: {e}")


def capture_screenshots_from_urls(driver, urls_and_files):
    for url, file_name in urls_and_files:
        capture_screenshot(driver, url, file_name)

def wait_for_page_load(driver):
    while driver.execute_script("return document.readyState") != "complete":
        time.sleep(0.1) 

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu") 
chrome_options.add_argument("--window-size=1920,1920")
driver = webdriver.Chrome(options=chrome_options)

urls_and_files = [
    ("https://budget.digital.mass.gov/summary/fy20/enacted/public-safety/?tab=budget-summary", "././screenshots_massachussets/budget_massachussets_2020.png"),
    ("https://budget.digital.mass.gov/summary/fy21/enacted/public-safety/?tab=budget-summary", "././screenshots_massachussets/budget_massachussets_2021.png"),
    ("https://budget.digital.mass.gov/summary/fy22/enacted/public-safety/?tab=budget-summary", "././screenshots_massachussets/budget_massachussets_2022.png"),
    ("https://budget.digital.mass.gov/summary/fy23/enacted/public-safety/?tab=budget-summary", "././screenshots_massachussets/budget_massachussets_2023.png"),
    ("https://budget.digital.mass.gov/summary/fy24/enacted/public-safety/?tab=budget-summary", "././screenshots_massachussets/budget_massachussets_2024.png"),
    ("https://operatingbudget.maryland.gov/#!/year/2020/operating/0/category_title/Public+Safety/0/agency_name/Department+of+State+Police/0/unit_name/Maryland+State+Police/0/organization_code/W00_A01_03/0/subprogram_name","././screenshots_maryland/budget_maryland_2020.png"),
    ("https://operatingbudget.maryland.gov/#!/year/2021/operating/0/category_title/Public+Safety/0/agency_name/Department+of+State+Police/0/unit_name/Maryland+State+Police/0/organization_code/W00_A01_03/0/subprogram_name","././screenshots_maryland/budget_maryland_2021.png"),
    ("https://operatingbudget.maryland.gov/#!/year/2022/operating/0/category_title/Public+Safety/0/agency_name/Department+of+State+Police/0/unit_name/Maryland+State+Police/0/organization_code/W00_A01_03/0/subprogram_name","././screenshots_maryland/budget_maryland_2022.png"),
    ("https://operatingbudget.maryland.gov/#!/year/2023/operating/0/category_title/Public+Safety/0/agency_name/Department+of+State+Police/0/unit_name/Maryland+State+Police/0/organization_code/W00_A01_03/0/subprogram_name","././screenshots_maryland/budget_maryland_2023.png"),
    ("https://operatingbudget.maryland.gov/#!/year/2024/operating/0/category_title/Public+Safety/0/agency_name/Department+of+State+Police/0/unit_name/Maryland+State+Police/0/organization_code/W00_A01_03/0/subprogram_name","././screenshots_maryland/budget_maryland_2024.png"),
    ("https://idaho.opengov.com/transparency/#/89045/accountType=expenses&embed=n&breakdown=types&currentYearAmount=cumulative&currentYearPeriod=years&graph=bar&legendSort=desc&proration=true&saved_view=581585&selection=FF514DE1EF23970778EF87EB25938406&projections=null&projectionType=null&highlighting=null&highlightingVariance=null&year=2024&selectedDataSetIndex=null&fiscal_start=earliest&fiscal_end=latest","././screenshots_idaho/budgets_idaho.png"),
]

try:
    capture_screenshots_from_urls(driver, urls_and_files) 
finally:
    driver.quit()