#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import sys

# %%
cidade = sys.argv[1]
i = 0
url = f'https://www.vivareal.com.br/venda/sp/{cidade}/apartamento_residencial/?pagina={i}'
ret = requests.get(url.format(cidade, i))
print(ret)
soup = bs(ret.text)
qtd_imoveis = int(soup.find('strong', {'class': 'results-summary__count js-total-records'}).text.replace('.', ''))
df = pd.DataFrame(columns=[
    'descricao', 
    'wlink', 
    'endereco', 
    'preco', 
    'preco_condominio', 
    'quartos',
    'area',
    'banheiros',
    'vagas',
    'piscina',
    'churrasqueira'
    ]
)
#%%
while qtd_imoveis > df.shape[0]:  
    i += 1  
    print(f"Carregando página {i}. \t\t Qtd imoveis: {df.shape[0]}")
    houses = soup.find_all('a', {'class': 'property-card__content-link js-card-title'})

    for house in houses:
        try: 
            descricao = house.find('span', {'class': 'property-card__title'}).text.strip()
        except:
            descricao = None
        try: 
            wlink = 'https://www.vivareal.com.br' + house['href']
        except:
            wlink = None
        try: 
            endereco = house.find('span', {'class': 'property-card__address'}).text
        except:
            endereco = None
        try: 
            preco = house.find('p').text.strip()
        except:
            preco = None
        try: 
            preco_condominio = house.find('strong', {'class': 'js-condo-price'}).text.strip()
        except:
            preco_condominio = None
        try: 
            quartos = house.find('li', {'class': 'property-card__detail-room'}).span.text.strip()
        except:
            quartos = None
        try: 
            area = house.find('span', {'class': 'property-card__detail-area'}).text
        except:
            area = None
        try: 
            banheiros = house.find('li', {'class': 'property-card__detail-bathroom'}).span.text.strip()
        except:
            banheiros = None
        try: 
            vagas = house.find('li', {'class': 'property-card__detail-garage'}).span.text.strip()
        except:
            vagas = None
        try: 
            piscina = house.find('li', {'class': 'amenities__item', 'title': 'Piscina'}).text
        except:
            piscina = None
        try: 
            churrasqueira = house.find('li', {'class': 'amenities__item', 'title': 'Churrasqueira'}).text
        except:
            churrasqueira = None

        df.loc[df.shape[0]] = [
            descricao, 
            wlink, 
            endereco, 
            preco, 
            preco_condominio, 
            quartos,
            area,
            banheiros,
            vagas,
            piscina,
            churrasqueira
        ]
    
#%%
df.to_csv(f"banco_de_imoveis_{cidade}.csv", sep=';', index=False)
