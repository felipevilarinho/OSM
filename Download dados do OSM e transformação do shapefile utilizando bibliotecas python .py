#!/usr/bin/env python
# coding: utf-8

# ### Bibliotecas utilizadas

# In[ ]:


import osmnx as ox
import geoplot as gplt
import geopandas as gpd
import pandas as pd
from shapely import wkt
import os


# ### Criar variável da localidade onde se pretende realizar a consulta

# In[ ]:


localidade_nome = 'São Paulo, BR'


# ### Criar variável com o tipo de estabelecimento que se pretende realizar a consulta

# In[ ]:


tags = {'building': 'supermarket'} 


# ### Realizar consulta

# In[ ]:


varejo_alimentar = ox.geometries_from_place(localidade_nome, tags)
varejo_alimentar.head()


# ### Resultado da consulta no limite do município de São Paulo

# In[ ]:


limite_municipio = ox.geocoder.geocode_to_gdf(localidade_nome, which_result=2)
ax = limite_municipio.plot(facecolor = '#494D4D', figsize=(85,85))
ax.set_facecolor('#2C2E2E')
varejo_alimentar['geometry'].plot(facecolor = '#C61313',
                             edgecolor = '#C61313',
                             linewidth = 10,
                             markersize = 1,
                             ax = ax)


# ### Criar pasta Resultado no C:
# 

# In[ ]:


os.mkdir('C:/Resultado')
pasta_dados = 'C:/Resultado'


# ### Exportação de planilha a partir do Pandas

# In[ ]:


planilha = "C:/Resultado/Planilha.csv"
df = pd.DataFrame(varejo_alimentar, copy = True)
df.to_csv(planilha, index = True)


# ### Identificação da coluna de geometria na planilha

# In[ ]:


leitura_arquivo = pd.read_csv(planilha)
leitura_arquivo['geometry'] = gpd.GeoSeries.from_wkt(leitura_arquivo['geometry'])


# ### Identificação do sistema de referência

# In[ ]:


gdf = gpd.GeoDataFrame(leitura_arquivo,geometry='geometry')
gdf.crs


# ### Inserção do sistema de referência no geodataframe

# In[ ]:


insercao_referencia_espacial = gdf.set_crs(epsg=4674)
insercao_referencia_espacial.crs


# ### Exportação do dado para shapefile

# In[ ]:


insercao_referencia_espacial.to_file('C:/Resultado/dado_geoespacial.shp')

