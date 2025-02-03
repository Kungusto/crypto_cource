class CryptoService :
    @staticmethod
    async def get_current_data() :
        from bs4 import BeautifulSoup as bs
        import requests

        response = requests.get('https://ru.investing.com/')
        response.encoding = 'utf-8'

        html_text = response.text

        parser = bs(html_text, 'html.parser')

        all_courses = parser.find_all('div', 'relative dynamic-table-v2_dynamic-table-wrapper__fBEvo')

        crypto = all_courses[-1].text
            
        crypto = crypto[25:]

        list_of_currencyes = crypto.split('%')

        crypto_data = {}

        for index, crypto_currency_data in enumerate(list_of_currencyes[:-1], start=1) : 
            sub_data = {}
            
            index_of_first_number = 0

            # ищем индекс первого числа
            for ind, letter in enumerate(crypto_currency_data) : 
                if letter.isdigit() : 
                    index_of_first_number = ind
                    break
                                        
            sub_data['name_crypto'] = crypto_currency_data[:index_of_first_number].strip()
            price_data = crypto_currency_data[index_of_first_number:]
            int_pt = price_data.split(',')[0]
            float_pt = price_data.split(',')[1]
            result_float_pt = '.'
            
            for i in float_pt : 
                if i != '-' and i != '+' :
                    result_float_pt += i 
                else : 
                    break

            price = float(''.join([i for i in int_pt if i.isdigit()]).strip()+result_float_pt)
            sub_data['price_crypto'] = price
                        
            crypto_data[index] = sub_data
            
        # for data in crypto_data.values() :
        #     print(f"Название монеты: {data['name_crypto']}\nЦена: {data['price_crypto']:^10.2f}$")
        #     print()
        
        result = '📊 Текущие курсы криптовалют:\n\n'
        for i in range(1, 7) : 
            result += f"✨ {crypto_data[i]['name_crypto']} = {crypto_data[i]['price_crypto']}$\n"
    
        return result