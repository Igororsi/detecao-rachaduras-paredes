# Proposta do Projeto

## Título

Sistema de Detecção de Rachaduras em Paredes Utilizando Processamento Digital de Imagens

---

# 1. Problema

A identificação de rachaduras em paredes é uma atividade importante para a manutenção e avaliação de estruturas civis.

Normalmente essa tarefa é realizada por inspeção visual humana, exigindo tempo e atenção dos responsáveis pela análise.

Este projeto pretende investigar como técnicas de Processamento Digital de Imagens podem ser utilizadas para detectar automaticamente rachaduras em fotografias de paredes.

A informação que se deseja obter é a localização das regiões que apresentam possíveis rachaduras, permitindo destacar essas áreas para posterior análise.

---

# 2. Contexto de Aplicação

A solução poderá ser utilizada em atividades relacionadas à construção civil e manutenção predial.

Entre os possíveis cenários de aplicação estão:

- Inspeção de imóveis;
- Avaliação de edificações;
- Monitoramento de estruturas;
- Manutenção preventiva;
- Apoio à identificação de danos estruturais.

Embora o projeto possua caráter acadêmico, o problema tratado possui relevância prática e aplicação real.

---

# 3. Objetivo

## Objetivo Geral

Desenvolver um sistema capaz de detectar rachaduras em imagens de paredes utilizando técnicas de processamento digital de imagens.

## Objetivos Específicos

- Obter um conjunto representativo de imagens;
- Estudar métodos de pré-processamento;
- Aplicar filtros para redução de ruído;
- Implementar técnicas de detecção de bordas;
- Avaliar métodos de segmentação;
- Destacar automaticamente rachaduras;
- Comparar os resultados obtidos.

---

# 4. Entrada e Saída Esperadas

## Entrada

Imagens digitais contendo superfícies de paredes.

Exemplos:

- Paredes internas;
- Paredes externas;
- Superfícies com rachaduras;
- Superfícies sem rachaduras.

## Saída

Imagem processada contendo:

- Regiões destacadas;
- Indicação visual das rachaduras detectadas;
- Informações relacionadas às áreas identificadas.

---

# 5. Conjunto de Dados

O conjunto inicial de imagens será composto por fotografias contendo paredes com e sem rachaduras.

## Origem das imagens

- Bases públicas de pesquisa;
- Bancos de imagens gratuitos;
- Fotografias produzidas pelos integrantes.

## Quantidade inicial

Pretende-se iniciar o projeto com aproximadamente 30 a 50 imagens.

## Formatos

- JPG
- JPEG
- PNG

## Resolução

Variável, dependendo da origem das imagens.

---

# 6. Pipeline Preliminar

```text
Imagem Original
        ↓
Conversão para Escala de Cinza
        ↓
Redução de Ruído
        ↓
Detecção de Bordas
        ↓
Operações Morfológicas
        ↓
Identificação das Regiões
        ↓
Resultado Final
```

---

## Etapa 1 – Conversão para Escala de Cinza

Objetivo:

Reduzir a complexidade da imagem removendo informações de cor que não são essenciais para a detecção de rachaduras.

---

## Etapa 2 – Redução de Ruído

Objetivo:

Remover pequenas variações e imperfeições presentes na imagem.

Técnicas consideradas:

- Gaussian Blur;
- Median Blur.

---

## Etapa 3 – Detecção de Bordas

Objetivo:

Destacar regiões onde há mudanças bruscas de intensidade.

Técnicas consideradas:

- Canny Edge Detection;
- Sobel.

---

## Etapa 4 – Operações Morfológicas

Objetivo:

Conectar regiões relevantes e eliminar pequenos artefatos.

Técnicas consideradas:

- Dilatação;
- Erosão;
- Closing.

---

## Etapa 5 – Identificação das Rachaduras

Objetivo:

Selecionar estruturas que apresentem características compatíveis com rachaduras.

Critérios iniciais:

- Comprimento;
- Espessura;
- Continuidade;
- Formato irregular.

---

# 7. Arquitetura Preliminar

```text
Usuário
   ↓
Imagem de Entrada
   ↓
Módulo de Pré-Processamento
   ↓
Módulo de Detecção
   ↓
Módulo de Análise
   ↓
Resultado
```

---

# 8. Estudo Inicial de Viabilidade

A viabilidade do projeto é sustentada pelos seguintes fatores:

- Existência de bibliotecas consolidadas para PDI;
- Disponibilidade de imagens públicas;
- Grande quantidade de material acadêmico relacionado;
- Facilidade de implementação dos métodos iniciais;
- Possibilidade de evolução gradual durante as próximas etapas do projeto.

A biblioteca OpenCV fornece recursos suficientes para a implementação inicial do sistema.

---

# 9. Experimentos Preliminares

Como experimento inicial, pretende-se realizar:

1. Leitura das imagens;
2. Conversão para escala de cinza;
3. Aplicação de filtro Gaussiano;
4. Detecção de bordas utilizando Canny;
5. Comparação visual dos resultados.

Esses testes servirão para verificar a capacidade do sistema em destacar regiões compatíveis com rachaduras.

---

# 10. Próximos Passos (M2)

- Expandir o conjunto de imagens;
- Refinar o pipeline;
- Ajustar parâmetros dos filtros;
- Avaliar novas técnicas de segmentação;
- Desenvolver métricas de avaliação;
- Melhorar a precisão da detecção.

---

# 11. Referências

OpenCV Documentation. Disponível em: https://opencv.org/

OpenCV Python Tutorials. Disponível em: https://docs.opencv.org/

Bradski, G.; Kaehler, A. Learning OpenCV: Computer Vision with the OpenCV Library.

Gonzalez, R. C.; Woods, R. E. Processamento Digital de Imagens.

Documentação NumPy. Disponível em: https://numpy.org/

## Experimento preliminar

Foi realizado um experimento preliminar utilizando a biblioteca OpenCV com o objetivo de verificar a viabilidade da detecção de características semelhantes a rachaduras nas imagens.

O processamento utilizado consiste inicialmente na conversão das imagens para escala de cinza, seguida pela aplicação de um filtro Gaussiano para redução de ruídos e, posteriormente, pela detecção de bordas utilizando o algoritmo Canny.

Foram processadas cinco imagens de entrada, armazenadas em `images/input/`. Os resultados do processamento foram armazenados em `images/results/`.

O experimento permitiu observar as bordas presentes nas imagens, incluindo regiões correspondentes a possíveis rachaduras. Também foram identificadas outras bordas provenientes da textura da parede, iluminação e demais características presentes nas imagens.

Dessa forma, o experimento preliminar indica que a abordagem possui potencial para destacar características relacionadas às rachaduras. Entretanto, ainda são necessárias etapas adicionais de processamento e análise para reduzir falsos positivos e melhorar a identificação das regiões de interesse.