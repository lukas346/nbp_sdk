BASE_URL = "http://api.nbp.pl/api" 

LATEST_CURRENCY_RATE_URL = lambda table, currency: f"{BASE_URL}/exchangerates/rates/{table}/{currency}/"
CURRENCY_RATE_BATCH_URL = lambda table, currency, last: f"{BASE_URL}/exchangerates/rates/{table}/{currency}/{last}"
TODAY_CURRENCY_RATE_URL = lambda table, currency: f"{BASE_URL}/exchangerates/rates/{table}/{currency}/today"
CURRENCY_RATE_FROM_DATE_URL = lambda table, currency, date: f"{BASE_URL}/exchangerates/rates/{table}/{currency}/{date}/"
CURRENCY_RATE_FROM_START_DATE_TO_END_DATE_URL = lambda table, currency, start_date, end_date: f"{BASE_URL}/exchangerates/rates/{table}/{currency}/{start_date}/{end_date}/"

# gold
LATEST_GOLD_RATE_URL = f"{BASE_URL}/cenyzlota"
GOLD_RATE_BATCH_URL = lambda last: f"{BASE_URL}/cenyzlota/last/{last}"
TODAY_GOLD_RATE_URL = f"{BASE_URL}/cenyzlota/today"
GOLD_RATE_FROM_DATE_URL = lambda date: f"{BASE_URL}/cenyzlota/{date}"
GOLD_RATE_FROM_START_DATE_TO_END_DATE_URL = lambda start_date, end_date: f"{BASE_URL}/cenyzlota/{start_date}/{end_date}"
