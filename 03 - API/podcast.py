#%%
import requests
import logging
import pandas as pd
from bs4 import BeautifulSoup as bs

# %%
url = 'https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true'
ret = requests.get(url.format(1))

# %%
soup = bs(ret.text)

#%%
soup.find('h5').text

#%%
soup.find('h5').a['href']

# %%
list_ep = soup.find_all('h5')

#%%
for item in list_ep:
    print(f"EP: {soup.find('h5').text} - Link: {soup.find('h5').a['href']}")

# %%
def get_podcast(url):
    ret = requests.get(url)
    soup = bs(ret.text)
    return soup.find_all('h5')

#%%
get_podcast(url.format(3))

#%%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

#%%
i = 1
list_podcast = []
list_get = get_podcast(url.format(i))
log.debug(f"{len(list_get)} links coletados da pagina {i}")

while len(list_get) > 0:
    list_podcast = list_podcast + list_get
    i += 1
    list_get = get_podcast(url.format(i))
    log.debug(f"{len(list_get)} links coletados da pagina {i}")
    
#%%
df = pd.DataFrame(columns=['nome', 'link'])

# %%
for item in list_podcast:
    df.loc[df.shape[0]] = [item.text, item.a['href']]
    
#%%
df.to_csv('lista_de_podcast.csv', sep=';', index=False)