date_format = '%d-%m-%Y'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
PARAMS = {'includeAdjustedClose': True,
          'interval': '1d',
          'period1': 0,
          'period2': 99999999999}
URL_TEMPLATE = 'https://query1.finance.yahoo.com/v8/finance/chart/{}'