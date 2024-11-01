# -*- coding: utf-8 -*-
"""Marketing_Analyst_e_commerce.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11FOhFr5G3cte3kN36pl4GoKWA0QuUfBV

# Análise de Dados de Vendas e Clientes

Sejam bem-vindos a minha pipeline de algumas analises exploratorias.
Para me acompanhar em outras redes ou saber mais sobre o meu trabalho, você pode me encontrar em:
- GitHub: [Poterdev](https://github.com/Poterdev)
- LinkedIn: [Erickson Santos](https://www.linkedin.com/in/erickson-santos-36a607318)
- Medium: [Erickson Santos](https://medium.com/@erickson1.dev)

Vamos explorar juntos e descobrir insights valiosos nos dados!

# Analise exploratória de arquivos de um e-commerce de produtos em geral

Neste notebook estarei organizando meus estudos e criando um roteiro para a analise de um conjunto de dados do kanggle.
Este é o link dos dados: https://www.kaggle.com/datasets/quangvinhhuynh/marketing-and-retail-analyst-e-comerce?select=products.csv

"Analista de Marketing e Varejo E-commerce"

Esta analise será um pouco mais longa, onde criaremos dashboard profissionais para analise da saúde e métricas de ações para extratégia de vendas.

# Entendimento das Variáveis do Conjunto de Dados

Este conjunto de dados contém informações cruciais para o monitoramento de um e-commerce.Abaixo estão descritas as variáveis incluídas no DataFrame e o que cada uma representa:


## Identificadores

- `order_id`: Identificador único do pedido;
- `customer_id`: Identificador único do cliente;
- `seller_id`: Identificador único do vendedor;
- `product_id`: Identificador único do produto;
- `order_purchase_timestamp`: Data e hora da compra;
- `order_approved_at`: Data e hora da aprovação do pedido;
- `order_delivered_timestamp`: Data e hora real da entrega;
- `order_estimated_delivery_date`: Data estimada para entrega;
- `order_item_id`: Número do item no pedido;
- `price`: Preço unitário do produto;
- `shipping_charges`: Valor do frete;
- `payment_type`: Método de pagamento utilizado;
- `payment_installments`: Número de parcelas;
- `payment_value`: Valor total do pagamento;
- `product_category_name`: Nome da categoria do produto;
- `product_weight_g`: Peso do produto;
- `product_length_cm`: Comprimento do produto;
- `product_height_cm`: Altura do produto;
- `product_width_cm`: Largura do produto;
- `customer_zip_code_prefix`: Prefixo do CEP do cliente;
- `customer_city`: Cidade do cliente;
- `customer_state`: Estado do cliente;

# Objetivos

 O foco desta análise está nas premissas básicas de nosso dataframe, para entender melhor os dados e conseguir extrair nossas métricas para a criação de nosso dashboard.


## Vendas
- Total de Vendas:
- Valor Total:
- Ticket Médio:
- Métodos de Pagamento:
- Média de Parcelas:


---
## Entrega
- Tempo Médio de Entrega:
- Tempo Máximo de Entrega:
- Tempo Mínimo de Entrega:

---
## Geografia
- Vendas por Estado:
- Top 10 Cidades:

---
## Produtos
- Categorias Populares:
- Preço Médio por Categoria:
- Produtos Mais Vendidos:


---
## Clientes
- Total de Clientes:
- Clientes por Estado:
- Valor Médio por Cliente:

## Passos para o processamento de dados
- **Etapa:1** - Importar as bibiotecas nescessárias
- **Etapa:2** - Leitura do Dataset Dataset
- **Etapa:3** - 'Check Sanity' dos dados
- **Etapa:4** - Limpeza dos dados
- **Etapa:5** - Exploratory Data Analysis (EDA)
- **Etapa:6** - Concluções e métricas

<h1 style="font-size: 48px;">Etapa:1 - Importar as bibliotecas nescessárias </h1>
"""

import pandas as pd

"""
<h1 style="font-size: 48px;">Etapa:2 - Leitura do Dataset </h1>"""

#Carregar o dataframe
dados = "capstone_data_cleaned.csv"

df = pd.read_csv(dados)

#df.head()
df.head()

#df.tail()
df.tail()

"""
<h1 style="font-size: 48px;">Etapa:3 - 'Check Sanity' dos dados </h1>"""

#shape()
df.shape

#info()
df.info()

#dados nulos
df.isnull().sum()

#Dados duplicados
df[df.duplicated()].head(50)

df.nunique()

df.describe().T

#verificação dos dados "garbage" de nosso dataFrame
for i in df.select_dtypes(include="object").columns:
    print(df[i].value_counts())
    print("***"*10)

"""<h1 style="font-size: 48px;">Etapa:4 - Limpeza dos dados </h1>

Como vimos acima a valores duplicados, optei por mostrar mais linhas para analisar com detalhes a insidência.
Vou isolar ela uma variavel para analisar depois, com mais detalhes, mas aprincipio a linha toda consiste dos mesmo dados.
"""

#isolando duplicadas
duplicated_df = df[df.duplicated()]

# Remover duplicatas do DataFrame original, mantendo apenas a primeira ocorrência
df = df.drop_duplicates()

df.duplicated().sum()

"""Depois de limpos de nosso data frame vamos analisar novamente;"""

df.info()

df.shape

df.describe().T

"""<h1 style="font-size: 48px;">Etapa:5 - Exploratory Data Analysis (EDA) </h1>

Para exemplificar um método de diferente para analise exploratória dos dados vou usar o SQL para fazer as consultas dos principais KPI's dos desempenho do e-commerce;
"""

df.columns

#Uma base apenas da variaveis para analisarmos
df.select_dtypes(include='number').head(2)

#Transformando as colunas em datas
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_approved_at'] = pd.to_datetime(df['order_approved_at'])
df['order_delivered_timestamp'] = pd.to_datetime(df['order_delivered_timestamp'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

len(df['order_id'].unique())

#Análise de Vendas
insigth = {}

insigth ['vendas'] = {
    'total_vendas': len(df['order_id'].unique()),
    'valor_total': df['payment_value'].sum(),
    'ticket_medio': df['payment_value'].mean(),
    'metodos_pagamento': df['payment_type'].value_counts().to_dict(),
    'parcelas_media': df['payment_installments'].mean()
    }

print(insigth['vendas'])

#########  Engenharia de recurso ###################
#criando uma coluna de tempo de entrega
df['tempo_entrega'] = (df['order_delivered_timestamp'] - df['order_purchase_timestamp']).dt.total_seconds() / 86400

df['tempo_entrega'].describe()

df[df['tempo_entrega'] > 15.40].value_counts()

#Análise de Entrega
insigth['entrega'] = {
        'tempo_medio_entrega': df['tempo_entrega'].mean(),
        'tempo_maximo_entrega': df['tempo_entrega'].max(),
        'tempo_minimo_entrega': df['tempo_entrega'].min()
    }

print(insigth['entrega'])

#Análise Geográfica
insigth['geografia'] = {'vendas_por_estado': df['customer_state'].value_counts().to_dict(),
                        'top_10_cidades': df['customer_city'].value_counts().head(10).to_dict()
                        }

print(insigth['geografia'])

#Análise de Produtos
insigth['produtos'] = {'categorias_populares': df['product_category_name'].value_counts().head(10).to_dict(),
                       'preco_medio_por_categoria': df.groupby('product_category_name')['price'].mean().to_dict(),
                       'produtos_mais_vendidos': df['product_id'].value_counts().head(10).to_dict()
                       }

print(insigth['produtos'])

#Análise de Clientes
insigth['clientes'] = {
        'total_clientes': df['customer_id'].nunique(),
        'clientes_por_estado': df.groupby('customer_state')['customer_id'].nunique().to_dict(),
        'valor_medio_por_cliente': df.groupby('customer_id')['payment_value'].mean().mean()
    }

print(insigth['clientes'])

for i in insigth.keys():
    print('Setor')
    print("***"*10)
    print(i)
    for j in insigth[i].keys():
        print(j)
        print(insigth[i][j])
    print("***"*10)
    print()

"""<h1 style="font-size: 48px;"> Etapa:6 - Concluções e métricas </h1>

# Setor
## Vendas
- Total de Vendas: 92.928;
- Valor Total:  16.092.123,37;
- Ticket Médio:  145,84;
- Métodos de Pagamento:
  - Cartão de Crédito: 81.781;
  - Carteira Digital: 21.613;
  - Voucher: 5.333;
  - Cartão de Débito: 1.616;
- Média de Parcelas: 2,84;


---
## Entrega
- Tempo Médio de Entrega: 12,39 dias;
- Tempo Máximo de Entrega: 209,63 dias;
- Tempo Mínimo de Entrega: 0,53 dias;


---
## Geografia
- Vendas por Estado:
  - SP: 46.713;
  - RJ: 14.260;
  - MG: 12.966;
  - RS: 6.085;
  - PR: 5.607;
  - SC: 4.092;
  - BA: 3.702;
  - DF: 2.363;
  - ES: 2.255;
  - GO: 2.234;
  - PE: 1.743;
  - CE: 1.388;
  - MT: 1.030;
  - PA: 1.014;
  - MS: 798;
  - MA: 777;
  - PB: 566;
  - RN: 526;
  - PI: 505;
  - AL: 419;
  - SE: 366;
  - TO: 298;
  - RO: 257;
  - AM: 167;
  - AC: 91;
  - AP: 78;
  - RR: 43;

- Top 10 Cidades:
  - São Paulo: 17.522;
  - Rio de Janeiro: 7.615;
  - Belo Horizonte: 3.120;
  - Brasília: 2.346;
  - Curitiba: 1.723;
  - Campinas: 1.645;
  - Porto Alegre: 1.535;
  - Salvador: 1.372;
  - Guarulhos: 1.327;
  - São Bernardo do Campo: 1.062;


---
## Produtos
- Categorias Populares:
  - Brinquedos: 83.096;
  - Saúde & Beleza: 3.003;
  - Cama, Mesa e Banho: 2.669;
  - Esportes & Lazer: 2.296;
  - Móveis & Decoração: 2.161;
  - Computadores & Acessórios: 2.161;
  - Utensílios Domésticos: 1.649;
  - Relógios & Presentes: 1.514;
  - Telefonia: 1.210;
  - Jardim & Ferramentas: 1.040;

- Preço Médio por Categoria:
  - Agro, Indústria e Comércio: 220,10
  - Ar Condicionado: 153,73
  - Arte: 92,19
  - Artesanato: 75,96
  - Áudio: 35,71
  - Automotivo: 110,23
  - Bebês: 99,96
  - Cama, Mesa e Banho: 85,85
  - Livros - Interesse Geral: 103,32
  - Livros Importados: 123,56
  - Livros Técnicos: 63,17
  - Suprimentos de Natal: 80,64
  - Cine & Foto: 128,41
  - Computadores: 655,12
  - Computadores & Acessórios: 103,48
  - Consoles e Jogos: 130,92
  - Construção - Ferramentas e Equipamentos: 112,44
  - Construção - Iluminação: 70,88
  - Construção - Segurança: 155,61
  - Cool Stuff: 147,24
  - Ferramentas para Jardim: 101,62
  - Ferramentas Diversas: 89,32
  - Fraldas e Higiene: 134,90
  - Bebidas: 59,07
  - DVDs & Blu-Ray: 65,10
  - Eletrônicos: 47,56
  - Moda - Roupas Femininas: 54,24
  - Moda - Bolsas e Acessórios: 73,34
  - Moda - Roupas Infantis: 89,99
  - Moda - Roupas Masculinas: 102,89
  - Moda - Calçados: 74,31
  - Moda - Esportes: 106,92
  - Moda - Roupas Íntimas e Praia: 54,16
  - Telefonia Fixa: 155,65
  - Flores: 27,92
  - Alimentos: 85,25
  - Alimentos e Bebidas: 61,65
  - Móveis - Quarto: 220,32
  - Móveis e Decoração: 82,12
  - Móveis - Sala de Estar: 143,21
  - Móveis - Colchões e Estofados: 249,00
  - Jardim e Ferramentas: 86,07
  - Saúde e Beleza: 86,86
  - Eletrodomésticos: 88,63
  - Eletrodomésticos 2: 303,74
  - Conforto em Casa: 59,90
  - Casa e Conforto: 137,73
  - Construção - Material de Construção: 112,13
  - Utensílios Domésticos: 81,37
  - Indústria e Comércio: 102,42
  - Móveis para Cozinha, Lavanderia e Jardim: 94,26
  - La Cuisine: 137,60
  - Malas e Acessórios: 99,62
  - Marketplace: 73,28
  - Música: 205,66
  - Instrumentos Musicais: 153,84
  - Mobiliário de Escritório: 130,83
  - Artigos para Festa: 101,80
  - Perfumaria: 109,53
  - Pet Shop: 109,77
  - Segurança e Serviços: 100,00
  - Sinalização e Segurança: 69,96
  - Pequenos Eletrodomésticos: 205,84
  - Fornos e Cafeteiras de Pequeno Porte: 469,31
  - Esportes e Lazer: 97,82
  - Papelaria: 88,83
  - Tablets, Impressão e Imagem: 92,02
  - Telefonia: 56,33
  - Brinquedos: 104,56
  - Relógios e Presentes: 152,38

- Produtos Mais Vendidos:
  - ID: aca2eb7d00ea1a7b8ebd4e68314663af - 529 unidades
  - ID: 99a4788cb24856965c36a24e339b6058 - 510 unidades
  - ID: 422879e10f46682990de24d770e7f83d - 489 unidades
  - ID: 389d119b48cf3043d311335e499d9c6b - 402 unidades
  - ID: 368c6c730842d78016ad823897a372db - 397 unidades
  - ID: 53759a2ecddad2bb87a079a1f1519f73 - 383 unidades
  - ID: d1c427060a0f73f6b889a5c7c61f2ac4 - 341 unidades
  - ID: 53b36df67ebb7c41585e8d54d6772e08 - 338 unidades
  - ID: 154e7e31ebfa092203795c972e5804a6 - 278 unidades
  - ID: 3dd2a17168ec895c781a9191c1e95ad7 - 268 unidades

---
## Clientes
- Total de Clientes: 89.980
- Clientes por Estado:
  - AC: 73
  - AL: 364
  - AM: 136
  - AP: 62
  - BA: 3.030
  - CE: 1.181
  - DF: 1.961
  - ES: 1.870
  - GO: 1.825
  - MA: 667
  - MG: 10.622
  - MS: 647
  - MT: 821
  - PA: 860
  - PB: 466
  - PE: 1.490
  - PI: 431
  - PR: 4.611
  - RJ: 11.462
  - RN: 442
  - RO: 209
  - RR: 37
  - RS: 4.985
  - SC: 3.340
  - SE: 309
  - SP: 37.872
  - TO: 247
- Valor Médio por Cliente: 136,55

Com os dados acima podemos ter uma base sobre o nosso e-commerce em analise, com isso podemos estipular algumas métricas para anlise, mas para efetuar as seguintes analise criaremos uma dashboard para uma melhor visualização, de nossa pesquisa abaixo:

- **Tendências de Vendas**: Poderíamos analisar as tendências sazonais ou mensais nos dados de vendas para verificar se há picos em determinadas épocas do ano, especialmente na categoria de brinquedos, o que ajudaria no planejamento de estoque e em promoções.

- **Segmentação de Clientes**: Analisar o perfil ou padrões de compra dos clientes recorrentes versus os que compram apenas uma vez pode fornecer insights sobre lealdade, auxiliando no marketing direcionado.

- **Otimização de Entregas**: Com tempos médios de entrega já baixos, uma análise mais detalhada do desempenho logístico em diferentes regiões poderia revelar oportunidades de ajustes, especialmente em locais com tempos de entrega médios mais altos.

- **Desempenho de Produtos por Região**: Entender se determinadas categorias, como Saúde e Beleza ou Eletrodomésticos, apresentam melhor desempenho em certas regiões poderia permitir campanhas de marketing regionais mais direcionadas.

- **Correlação entre Método de Pagamento e Ticket Médio**: Explorar como a preferência de método de pagamento varia com o ticket médio ou com a categoria pode ajudar a criar estratégias para promover certas opções de pagamento, como carteiras digitais, para compras de valor menor.
"""