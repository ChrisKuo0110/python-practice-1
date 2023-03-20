celcius = input('請輸入攝氏(°C)溫度:')
celcius = float(celcius)
fahrenheit = celcius * (9 / 5) + 32
fahrenheit = round(fahrenheit, 2)
print('攝氏',celcius, '度(°C)等於華氏', fahrenheit, '度(°F)')