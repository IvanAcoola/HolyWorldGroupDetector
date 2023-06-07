import requests
import json

from prices import temp_prices, lt_prices, donates


class HolyworldRequester:
    def __init__(self, csrf, xsrf, session):
        self.csrf = csrf
        self.xstf = xsrf
        self.session = session

    def request(self, nickname, donate, time_stage=None):
        cookies = {'holyworld_session': self.session}
        headers = {'x-csrf-token': self.csrf, 'x-xsrf-token': self.xstf}
        json_data = {'player': nickname, 'section': 1, 'currency': 'RUB', 'goodid': donate, 'server': 'anarchy'}
        if time_stage:
            json_data.update({'position': time_stage})  # 1 - 1 month, 2 - 3 month, 3 - lt
        response = requests.post('https://holyworld.ru/api/pay/check-surcharge', cookies=cookies, headers=headers,
                                 json=json_data)
        if response.status_code != 200:
            print('Session, csrf, xsrf error!')
            exit(-1)
        return json.loads(response.text)['response']

    def calculate_temp_days(self, donate, price_to_full):
        price_for_day = {}
        less30_day, more30_day = temp_prices[donate][0] / 30, temp_prices[donate][1] / 90
        for d in range(1, 90):
            if d <= 30:
                price_for_day.update({int(lt_prices[donate] - d * less30_day): d})
            else:
                price_for_day.update({int(lt_prices[donate] - d * more30_day): d})
        return price_for_day[price_to_full]

    def get_user_info(self, username):
        price_to_king = self.request(username, 'king', 3)['price']  # getting full price for group 'king'
        if self.request(username, 'king', 3)['label'] == 'Игрок не найден!':
            return 'Игрок не найден!'
        for price in list(lt_prices.items()):
            if price_to_king == lt_prices['king'] - price[1]:
                return f'{price[0]}'
        else:
            for don in donates:
                ans = self.request(username, don[0], don[1])
                if ans['price'] != 0:
                    price_to_full = self.request(username, don[0], 3)['price']
                    return f'{don[0]}-{self.calculate_temp_days(don[0], int(price_to_full))}'
