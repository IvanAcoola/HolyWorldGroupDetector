from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def get_session_data():
    session = ''
    csrf = ''
    xsrf = ''
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get('https://holyworld.ru/payment/anarchy/custom')
    driver.find_element('xpath', "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[4]/div[2]/div[1]/div[1]/input").send_keys("I")
    sleep(1)
    for request in driver.requests:
        if 'https://holyworld.ru/api/pay/check-surcharge' in request.url:
            xsrf = request.headers['x-xsrf-token']
            csrf = request.headers['x-csrf-token']
            session = driver.get_cookies()[0]['value']
            break
    driver.close()
    return csrf, xsrf, session
