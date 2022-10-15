#!/usr/bin/env python
# coding: utf-8

# # *[Hora da prática: Loterias](https://how-bootcamps.memberkit.com.br/78660-engenharia-de-dados-modulos-episodios-outubro-2022/1861659-hora-da-pratica-loterias-parte-01)*
# 
# 
# 
# 
# 
# 
# 

# In[1]:


#pip install requests
#pip install pandas
#pip install lxml
#pip install iphython


# In[40]:


import requests
import pandas as pd
import collections
import sys


# In[3]:


#url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotof%C3%A1cil'
url = sys.argv[1]
r = requests.get(url, verify=False) 


# In[4]:


r_txt = r.text #Tranformando em text


# In[5]:


#Removendo os \\r\\n e \r\n
r_txt = r_txt.replace('\\r\\n', '') 
r_txt = r_txt.replace('\r\n', '') 

#Removendo o inicio e fim do json
r_txt = r_txt.replace('{  "html": "', '') 
r_txt = r_txt.replace('"}', '')


# In[6]:


#Transformar em um dataframe
df = pd.read_html(r_txt, encoding='utf-8')[0]


# In[7]:


type(df)


# In[8]:


#Backup. remove registros nulos e reseta index
df_bkup = df 
df = df[df['Bola1'] == df['Bola1']]
df = df.reset_index(drop=True)


# In[9]:


#Gerar listas de números possiveis da loteria
nr_pop = list(range(1, 26))
nr_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
nr_impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
nr_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]


# In[10]:


#Variaveis de suport
comb = []
v_01 = 0
v_02 = 0
v_03 = 0
v_04 = 0
v_05 = 0
v_06 = 0
v_07 = 0
v_08 = 0
v_09 = 0
v_10 = 0
v_11 = 0
v_12 = 0
v_13 = 0
v_14 = 0
v_15 = 0
v_16 = 0
v_17 = 0
v_18 = 0
v_19 = 0
v_20 = 0
v_21 = 0
v_22 = 0
v_23 = 0
v_24 = 0
v_25 = 0

lst_campos = ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5',
              'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12',
              'Bola13', 'Bola14', 'Bola15']


# In[11]:


#Loop rodando em cada linha do df vendo quais numeros ja sairam e incluindo nas variaveis e lista comb
for index, row in df.iterrows(): 
    v_pares = 0
    v_impares = 0
    v_primos = 0
    for campo in lst_campos:
        if row[campo] in nr_pares:
            v_pares += 1
        if row[campo] in nr_impares:
            v_impares += 1
        if row[campo] in nr_primos:
            v_primos += 1
        if row[campo] == 1:
            v_01 += 1
        if row[campo] == 2:
            v_02 += 1
        if row[campo] == 3:
            v_03 += 1
        if row[campo] == 4:
            v_04 += 1
        if row[campo] == 5:
            v_05 += 1
        if row[campo] == 6:
            v_06 += 1
        if row[campo] == 7:
            v_07 += 1
        if row[campo] == 8:
            v_08 += 1
        if row[campo] == 9:
            v_09 += 1
        if row[campo] == 10:
            v_10 += 1
        if row[campo] == 11:
            v_11 += 1
        if row[campo] == 12:
            v_12 += 1
        if row[campo] == 13:
            v_13 += 1
        if row[campo] == 14:
            v_14 += 1
        if row[campo] == 15:
            v_15 += 1
        if row[campo] == 16:
            v_16 += 1
        if row[campo] == 17:
            v_17 += 1
        if row[campo] == 18:
            v_18 += 1
        if row[campo] == 19:
            v_19 += 1
        if row[campo] == 20:
            v_20 += 1
        if row[campo] == 21:
            v_21 += 1
        if row[campo] == 22:
            v_22 += 1
        if row[campo] == 23:
            v_23 += 1
        if row[campo] == 24:
            v_24 += 1
        if row[campo] == 25:
            v_25 += 1
    comb.append(str(v_pares) + 'p-' + str(v_impares) + 'i-'+str(v_primos)+'np')


# In[12]:


comb


# In[13]:


#Cria uma lista com a frequencia de cada número
freq_nr = [
    [1, v_01],
    [2, v_02],
    [3, v_03],
    [4, v_04],
    [5, v_05],
    [6, v_06],
    [7, v_07],
    [8, v_08],
    [9, v_09],
    [10, v_10],
    [11, v_11],
    [12, v_12],
    [13, v_13],
    [14, v_14],
    [15, v_15],
    [16, v_16],
    [17, v_17],
    [18, v_18],
    [19, v_19],
    [20, v_20],
    [21, v_21],
    [22, v_22],
    [23, v_23],
    [24, v_24],
    [25, v_25]
]
freq_nr


# In[14]:


#Ordenar pela quantidade
freq_nr.sort(key=lambda tup: tup[1])
freq_nr


# In[15]:


freq_nr[-1]


# In[16]:


df.describe()


# In[18]:


counter = collections.Counter(comb)
counter


# In[19]:


df_result = pd.DataFrame(counter.items(), columns = ['Combinacao', 'Frequencia'])
df_result


# In[32]:


df_result['perc_todo'] = df_result['Frequencia']/df_result['Frequencia'].sum()
df_result = df_result.sort_values(by='perc_todo')


# In[39]:


print('''
Nr mais frequente = {}
Nr menos frequente = {}
Combinacao mais frequente = {} com frequencia de {}%
'''.format(freq_nr[-1][0], freq_nr[0][0], df_result['Combinacao'].values[-1], int(df_result['perc_todo'].values[-1]*10000)/100 )
)


# In[ ]:




