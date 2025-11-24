# G2P-DLP (grapheme-to-phoneme converter)
The present repository presents the automatic conversion system designed for the syllabification, stress marking, and phonetic transcription of the [Vocabulário Fundamental](https://doi.org/10.5281/zenodo.10889986) do [_Dicionário da Língua Portuguesa_ (DLP)](https://dicionario.acad-ciencias.pt/).

This system is composed of three main modules, implemented through Python scripts and demonstrated in Jupyter notebooks. Each module performs a specific task within the conversion process:
## Modules

### Syllabic Division
Marks the stressed syllable of the lemmas, following the general stress paradigm of non-verbal Portuguese words.

### Stress Marking
Marks the stressed syllable of the accented lemmas, following the general stress paradigm of non-verbal Portuguese words.

### Phonetic Transcription
Produces the phonetic transcription of the 730 lemmas, converting graphemes into characters from the International Phonetic Alphabet [(IPA)](https://www.internationalphoneticassociation.org/).

Each module operates on a corpus structured in ODS tables, using rules based on regular expressions.

---

## Repository Structure

```
├── Debug/
│   └── Log and debug files generated during the execution of the scripts and notebooks.
│
├── Notebooks/
│   └── Jupyter notebooks corresponding to the three modules (syllable, stress, phonetics).
│       They present the process of developing the Python files and the results obtained.
│
├── Python/
│   └── Standalone Python scripts for the three main modules.
│       - silaba.py
│       - acento.py
│       - fonetica.py
│
├── ODS/
│   └── ODS-format data files containing the corpora used in the modules.
│       These files specify the contexts, patterns, and substitutions applied.
│
├── Regex/
│   └── CSV tables with the regular expressions used in each module.
│       Each line includes:
│       - Regex ID
│       - Context Pattern
│       - Regex expression (Find)
│       - Applied substitution (Replace)
│       - Example of application
```

### Related publications
Martins, L. (2025). [Desenvolvimento de um sistema de conversão grafema-fone[ma] para o Vocabulário Fundamental da Academia das Ciências de Lisboa](https://repositorio-aberto.up.pt/handle/10216/168957). Dissertação de Mestrado. Faculdade de Letras da Universidade do Porto.

Reis, L. (2025). [Vocabulário Fundamental da Academia das Ciências de Lisboa: seleção lexical, alinhamento dos sentidos e codificação](https://run.unl.pt/handle/10362/186964). Dissertação de Mestrado, Universidade NOVA de Lisboa. 

Simões, A., Almeida, J. J. & Salgado, A. (2016). Building a Dictionary Using XML Technology. In *5th Symposium on Languages, Applications and Technologies* (SLATE'16). *Open Access Series in Informatics* (OASIcs), Vol. 51, pp. 14:1-14:8, Schloss Dagstuhl – Leibniz-Zentrum für Informatik. <https://doi.org/10.4230/OASIcs.SLATE.2016.14>

Wilkens, R., Pintard, A., François, T., Barbosa, S., Reis, M. L., Amaro, R., Ribeiro, E., Mamede, N., Baptista, J., Blanco, X., Catena, A., Gauchola, R., & MU, K. (2024). *iRead4Skills – Basic Lexicons per Complexity Level (v1.0)* [Data set]. Zenodo. <https://doi.org/10.5281/zenodo.10889986>
