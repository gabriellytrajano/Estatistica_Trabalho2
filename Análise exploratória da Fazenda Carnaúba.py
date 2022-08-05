#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np 


# ### Importando a base de dados 

# In[2]:


fazenda_carnauba = pd.read_csv("dataset_carnauba2.csv")


# ### Listagem de colunas do dataset

# In[3]:


list(fazenda_carnauba.columns)


# ### Listando os dados da coluna de anos

# In[18]:


fazenda_carnauba['ano']


# ### Listando os dados da coluna de total de chuva

# In[6]:


fazenda_carnauba['total_chuva_mm']


# ### Contando o total de chuvas entre os anos (2013 a 2022)

# In[12]:


lista_fazenda = fazenda_carnauba['total_chuva_mm'].tolist()


# In[13]:


lista_fazenda


# In[17]:


contagem_total = 0

for i in range(len(lista_fazenda)):
   contagem_total+= lista_fazenda[i]

print(contagem_total)


# ### Temos a contagem total das chuvas, agora queremos a média

# In[21]:


total_de_anos = fazenda_carnauba['ano'].count()


# In[22]:


total_de_anos


# In[23]:


media_de_chuva = contagem_total/total_de_anos


# In[24]:


media_de_chuva


# ### A média de chuva entre os anos de 2013 à 2022 é de 453.5

# ### Listando a coluna de dias com mais de 5mm de chuva

# In[27]:


fazenda_carnauba['dias_chuva_mais_5mm']


# In[28]:


dias_com_mais_5mm = fazenda_carnauba['dias_chuva_mais_5mm'].tolist()


# In[29]:


dias_com_mais_5mm


# In[30]:


contagem_total_dias = 0

for i in range(len(dias_com_mais_5mm)):
   contagem_total_dias+= dias_com_mais_5mm[i]

print(contagem_total_dias)


# ### A contagem de dias com mais de 5mm é de 196.

# In[31]:


media_de_dias_5mm = contagem_total_dias/total_de_anos


# In[32]:


media_de_dias_5mm


# ### A média de dias de chuva com mais de 5mm entre os anos de 2013 e 2022 é de 19.6.

# ### Listando a coluna de dias com mais de 10mm de chuva

# In[34]:


fazenda_carnauba['dias_chuva_mais_10mm']


# In[36]:


dias_com_mais_10mm = fazenda_carnauba['dias_chuva_mais_10mm'].tolist()


# In[37]:


dias_com_mais_10mm


# In[38]:


contagem_total_dias_10mm = 0

for i in range(len(dias_com_mais_10mm)):
   contagem_total_dias_10mm+= dias_com_mais_10mm[i]

print(contagem_total_dias_10mm)


# ### A contagem de dias com mais de 10mm é de 124.
# 

# In[40]:


media_de_dias_10mm = contagem_total_dias_10mm/total_de_anos


# In[41]:


media_de_dias_10mm


# ### A média de dias de chuva com mais de 10mm entre os anos de 2013 e 2022 é de 19.6.

# ### Nesse ponto, podemos dizer que a média de dias de chuva com mais de 5mm é maior que a média de dias de chuva com mais de 10mm. 

# ### Agora queremos calcular a Variancia entre os dias de chuva com mais de 5mm

# In[47]:


print(np.var(dias_com_mais_5mm))


# ### Calculando a Variancia entre os dias de chuva com mais de 10mm

# In[46]:


print(np.var(dias_com_mais_10mm))


# ### Calculando o Desvio Padrão entre os dias de chuva com mais de 5mm

# In[49]:


print(np.std(dias_com_mais_5mm))


# ### Calculando o Desvio Padrão entre os dias de chuva com mais de 10mm

# In[51]:


print(np.std(dias_com_mais_10mm))

