# Sistema de conversão grafema-fone(ma) e de translineação
O presente repositório apresenta o sistema de conversão automático utilizado na translineação, marcação da sílaba tónica e transcrição fonética de 730 lemas do Nível 1 do [Vocabulário Fundamental](https://doi.org/10.5281/zenodo.10889986) do [_Dicionário da Língua Portuguesa_ (DLP)](https://dicionario.acad-ciencias.pt/).

Este sistema é composto por três módulos principais, organizados em scripts Python e demonstrados em notebooks Jupyter. Cada módulo realiza uma tarefa específica no processo de conversão:
## Módulos

#### Sílaba
Efetua a translineação dos 730 lemas, com base em princípios fonológicos silábicos do português.

#### Acento 
Efetua a marcação da sílaba tónica dos 713 lemas acentuados, com base do paradigma acentual geral das palavras não-verbais do português.

#### Fonética
Efetua a transcrição fonética dos 730 lemas, convertendo os grafemas em caracteres fornecidos pelo [AFI](https://www.internationalphoneticassociation.org/).

Cada módulo opera sobre um *corpus* estruturado em tabelas ODS com regras baseadas em expressões regulares.

---

## Estrutura do Repositório

```
├── Debug/
│   └── Ficheiros de *logs* e *debug* gerados durante a execução dos scripts e notebooks.
│
├── Notebooks/
│   └── Notebooks Jupyter correspondentes aos três módulos (sílaba, acento, fonética).
│       Apresenta o processo de elaboração dos ficheiros Pyhton e os resultados obtidos.
│
├── Python/
│   └── Scripts Python autónomos para os três módulos principais.
│       - silaba.py
│       - acento.py
│       - fonetica.py
│
├── ODS/
│   └── Ficheiros de dados no formato ODS com os corpora utilizados nos módulos.
│       Estes ficheiros especificam os contextos, padrões e substituições aplicadas.
│
├── Regex/
│   └── Tabelas CSV com as expressões regulares utilizadas em cada módulo.
│       Cada linha inclui:
│       - ID da *regex*
│       - Padrão de contexto
│       - Expressão *regex* usada (Find)
│       - Substituição aplicada (Replace)
│       - Exemplo de aplicação
```

### Publicações relacionadas
Simões, A., Almeida, J. J. & Salgado, A. (2016). Building a Dictionary Using XML Technology. In *5th Symposium on Languages, Applications and Technologies* (SLATE'16). *Open Access Series in Informatics* (OASIcs), Vol. 51, pp. 14:1-14:8, Schloss Dagstuhl – Leibniz-Zentrum für Informatik. <https://doi.org/10.4230/OASIcs.SLATE.2016.14>
Wilkens, R., Pintard, A., François, T., Barbosa, S., Reis, M. L., Amaro, R., Ribeiro, E., Mamede, N., Baptista, J., Blanco, X., Catena, A., Gauchola, R., & MU, K. (2024). *iRead4Skills – Basic Lexicons per Complexity Level (v1.0)* [Data set]. Zenodo. <https://doi.org/10.5281/zenodo.10889986>
