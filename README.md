# Sistema de Detecção de Rachaduras em Paredes

## Integrantes

- Gustavo Koerich Cardoso
- Iago Fermiano Orsi
- Igor Orsi Dalagnello

Curso: Ciência da Computação – UNIVALI

---

# Descrição do Projeto

Este projeto tem como objetivo desenvolver um sistema capaz de detectar automaticamente rachaduras em paredes utilizando técnicas de Processamento Digital de Imagens (PDI).

A proposta busca auxiliar processos de inspeção visual em construções, permitindo identificar regiões com possíveis fissuras ou rachaduras por meio da análise de fotografias digitais.

O projeto será desenvolvido ao longo das etapas M1, M2 e M3 da disciplina de Processamento de Imagens.

---

# Problema Investigado

A identificação de rachaduras em estruturas normalmente é realizada por inspeção visual humana, processo que pode ser demorado e sujeito a erros.

O projeto pretende investigar como técnicas de processamento digital de imagens podem ser utilizadas para localizar automaticamente rachaduras em imagens de paredes, destacando suas regiões e fornecendo informações úteis para análise.

---

# Contexto de Aplicação

A solução poderá ser aplicada em:

- Inspeção predial;
- Avaliação de imóveis;
- Manutenção preventiva;
- Monitoramento de estruturas;
- Apoio técnico para engenheiros e arquitetos.

---

# Objetivo Geral

Desenvolver um sistema capaz de detectar rachaduras em imagens de paredes utilizando técnicas de processamento digital de imagens.

## Objetivos Específicos

- Obter um conjunto de imagens contendo rachaduras;
- Estudar técnicas de pré-processamento;
- Aplicar métodos de detecção de bordas;
- Avaliar técnicas de segmentação;
- Destacar automaticamente regiões com rachaduras;
- Comparar os resultados obtidos por diferentes métodos.

---

# Visão Geral da Solução

O sistema receberá uma imagem de uma parede como entrada.

A imagem passará por etapas de pré-processamento, redução de ruído e detecção de bordas. Em seguida, serão aplicadas técnicas para destacar possíveis rachaduras.

Ao final do processamento, o sistema deverá produzir uma imagem contendo as regiões identificadas como rachaduras.

---

# Entrada e Saída Esperadas

## Entrada

- Fotografias digitais de paredes;
- Imagens contendo ou não rachaduras.

## Saída

- Imagem processada;
- Rachaduras destacadas visualmente;
- Informações sobre as regiões detectadas.

---

# Conjunto de Imagens

O projeto utilizará imagens de paredes contendo rachaduras obtidas por:

- Bases públicas de pesquisa;
- Repositórios acadêmicos;
- Bancos de imagens gratuitos;
- Fotografias produzidas pelos integrantes do grupo.

As imagens serão armazenadas na pasta `images/input`.

---

# Tecnologias Previstas

- Python 3
- OpenCV
- NumPy
- Matplotlib
- Git
- GitHub

---

# Estrutura do Repositório

```text
projeto-rachaduras/
│
├── README.md
├── docs/
│   └── proposta.md
│
├── images/
│   ├── input/
│   └── results/
│
├── src/
│
├── notebooks/
│
├── tests/
│
└── .gitignore
```

---

# Estágio Atual do Projeto

O projeto encontra-se na etapa de definição do problema, organização das imagens e validação inicial do pipeline de processamento.

Foi realizado um experimento preliminar utilizando OpenCV, aplicando conversão para escala de cinza, filtro Gaussiano e detecção de bordas com Canny.

O experimento foi executado sobre cinco imagens de entrada. Os arquivos originais estão em `images/input/` e os resultados processados estão em `images/results/`.

Os resultados demonstraram a capacidade da técnica de detecção de bordas em destacar características presentes nas imagens, incluindo possíveis rachaduras. Entretanto, também foram observadas outras bordas relacionadas à textura e iluminação, indicando a necessidade de refinamento do método nas próximas etapas.

---

# Reprodução dos Experimentos

Para instalar as dependências:

    pip install -r requirements.txt

Para executar o experimento:

    python src/main.py

As imagens de entrada estão armazenadas em:

    images/input/

Os resultados são armazenados em:

    images/results/

---

# Documentação Adicional

- `docs/proposta.md`

---

# Vídeo da M1

Link do vídeo (YouTube Não Listado):

```text
https://youtu.be/5gtmJQ07VWs
```
