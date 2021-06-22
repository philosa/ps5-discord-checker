from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0')

browser = webdriver.Chrome(options = options)
browser.set_page_load_timeout(60)

browser.get('https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller-white/6430163.p?skuId=6430163')

all_button = browser.find_elements_by_tag_name("button")
all_button = [i.text for i in all_button]

if "Sold Out" in all_button:
  print ("Item not in Stock") 
else:
  print("Item is in Stock") 
    from DiscordWebhook
    webhook = DiscordWebhook(url='', content='Webhook Message')
    response = webhook.execute()