# CCXT Exchange Balance Checker

Этот скрипт на Python позволяет проверять баланс аккаунта на криптовалютных биржах с использованием библиотеки **CCXT**.

## Установка

Для работы скрипта необходим Python 3 и библиотека **CCXT**. Установите её с помощью `pip`:

```bash
pip install ccxt
```

## Настройка

1. **Склонируйте репозиторий или скопируйте код скрипта.**
2. **Добавьте свои API ключи**:
   - Вставьте ваши API ключи (`apiKey` и `secret`) в соответствующие строки в коде:
   ```python
   api_key = 'ВАШ_API_KEY'
   api_secret = 'ВАШ_API_SECRET'
   ```

3. **Выберите биржу**:
   - В переменной `exchange_name` укажите биржу, с которой хотите работать (например, `'binance'`, `'kraken'`, `'bitfinex'` и т.д.):
   ```python
   exchange_name = 'binance'  # замените на нужную биржу
   ```

## Использование

1. Запустите скрипт в терминале или командной строке:

   ```bash
   python test_exchange_api.py
   ```

2. Если API ключи и соединение с биржей корректны, в терминале выведется баланс вашего аккаунта. Пример успешного вывода:

   ```json
   {
       'total': {
           'BTC': 0.05,
           'USDT': 1500,
           ...
       },
       'free': {
           'BTC': 0.03,
           'USDT': 1000,
           ...
       },
       'used': {
           'BTC': 0.02,
           'USDT': 500,
           ...
       }
   }
   ```

3. В случае ошибки будет выведено сообщение с деталями:

   ```bash
   Ошибка: <текст ошибки>
   ```
## Дополнительные параметры

1. Получение информации о вашем аккаунте: Можно запросить информацию о вашем аккаунте, что также подтверждает корректную работу API. Например, для Binance:
   
   ```bash
   account_info = exchange.fetch_account()
   print(account_info)
   ```

2. Получение текущих цен (тикеров): Чтобы проверить работу API, можно запросить текущие цены активов. Этот метод не требует наличия привилегий на аккаунт (например, не требует прав доступа к балансу):

   ```bash
   ticker = exchange.fetch_ticker('BTC/USDT')  # Замените на нужную торговую пару
   print(ticker)
   ```

3. Получение книги ордеров: Можно запросить книгу ордеров для любой торговой пары, чтобы убедиться, что API работает:

   ```bash
   order_book = exchange.fetch_order_book('BTC/USDT')
   print(order_book)
   ```


4. Создание тестового ордера: Если ваши API ключи поддерживают торговлю, можно попробовать создать тестовый ордер. Это полезно, чтобы проверить торговую функциональность.

Пример создания лимитного ордера:

    ```bash
    order = exchange.create_limit_buy_order('BTC/USDT', 0.001, 30000)  # Покупка 0.001 BTC по цене $30,000
    print(order)
    ```

 Пример создания маркет ордера:
 
   ```bash
   order = exchange.create_market_buy_order('BTC/USDT', 0.001)  # Покупка 0.001 BTC по рыночной цене
   print(order)
   ```

5. Получение истории сделок: Также можно запросить историю ваших сделок на бирже:

   ```bash
   trades = exchange.fetch_my_trades('BTC/USDT')
   print(trades)
   ```

## Поддерживаемые биржи

Скрипт работает с любыми биржами, поддерживаемыми **CCXT**, включая:

- Binance
- Kraken
- Bitfinex
- Huobi
- KuCoin
- И многие другие (полный список можно получить с помощью команды `print(ccxt.exchanges)`).

## Примечание

- Убедитесь, что ваши API ключи имеют права на выполнение необходимых операций (например, просмотр баланса).
- Если вы столкнулись с ошибкой, связанной с доступом из вашего региона, возможно, ваш доступ к бирже ограничен. Ознакомьтесь с условиями использования выбранной биржи.

## Требования

- Python 3.x
- CCXT библиотека

## Лицензия

Этот проект распространяется под лицензией MIT.

```
