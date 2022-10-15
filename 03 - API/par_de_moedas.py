#%% Imports
import requests #api
import json #arquivo json

#%% Get from API
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

if data:
    print(data.text)
else:
    print('Falha')

# %% Definir funcao de error
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f'{func.__name__} falhou')
    return inner_func
# %% Definir funcao 

@error_check
def multi_pairs(qt, pair):
    url = f'https://economia.awesomeapi.com.br/json/last/{pair}'
    data_json = requests.get(url)
    price = json.loads(data_json.text)[pair.replace('-', '')]
    print(f"{qt} {pair[:3]} hoje custam {qt * int((float(price['bid']))*1000)/1000} {pair[-3:]}")

# %%
multi_pairs(30, "BTC-BRL")

# %%
