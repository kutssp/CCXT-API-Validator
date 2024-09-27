import ccxt

# Ваши API ключи
api_key = 'ВАШ_API_KEY'
api_secret = 'ВАШ_API_SECRET'

# Название биржи (например, 'binance', 'kraken', 'bitfinex', и т.д.)
exchange_name = 'binance'  # замените на нужную биржу

# Инициализация объекта биржи
exchange = getattr(ccxt, exchange_name)({
    'apiKey': api_key,
    'secret': api_secret,
})

# Проверка баланса
try:
    balance = exchange.fetch_balance()
    print(balance)
except ccxt.BaseError as error:
    print(f"Ошибка: {error}")
