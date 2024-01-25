from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


def browserCreator():
    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    return browser


def itemFinder():
    item_urls = []
    
    items = browser.find_elements(By.CLASS_NAME, 'product-image')
    for item in items:
        item_url = item.get_attribute('href')
        item_urls.append(item_url)
    
    return item_urls


def propertyCollector():
    title = browser.find_element(By.TAG_NAME, 'h1').text
    price = browser.find_element(By.CSS_SELECTOR, 'p.price').text
    sku = browser.find_element(By.CSS_SELECTOR, 'span.sku').text
    
    cat_loc = browser.find_elements(By.CSS_SELECTOR, 'span.posted_in a')
    categories = []
    for category in cat_loc:
        categories.append(category.text)

    tag_loc = browser.find_elements(By.CSS_SELECTOR, 'span.tagged_as a')
    tags = []
    for tag in tag_loc:
        tags.append(tag.text)

    description = browser.find_element(By.CSS_SELECTOR, 'div#tabs-list-description p').text
    
    return [browser.current_url, title, price, sku, categories, tags, description]


browser = browserCreator()
browser.get('https://yorukana.com/urunlerimiz/')
export_items = []
item_urls = itemFinder()

for item_url in item_urls:
    print(f'System will work on {item_url}')
    try:
        browser.get(item_url)
        print(f'{item_url} is working...')
        item_data = propertyCollector()
        export_items.append(item_data)
    except:
        print(f'ERROR: {browser.current_url}')

df = pd.DataFrame(export_items)
df.to_excel('yoruk_ana.xlsx')