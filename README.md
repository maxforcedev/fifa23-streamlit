
# ⚽ FIFA 23 – Dashboard Interativo com Python + Streamlit

Este é um projeto de análise interativa utilizando **Python**, **Streamlit** e **pandas**, com um conjunto de dados oficial e limpo do FIFA 23. O objetivo é permitir a visualização intuitiva de estatísticas de jogadores e clubes, com interface moderna e dinâmica.

---

## 📊 Demonstração das Páginas

| Página | Visão |
|--------|-------|
| 🏠 Início | Descrição do projeto e botão para navegação externa |
| 👦 Jogadores | Estatísticas individuais, fotos, clubes, posições, valores |
| ⚽ Clube | Visualização completa dos jogadores de cada clube com métricas e imagens |

---

## 🧠 Funcionalidades

- 🗂️ Navegação multipágina com Streamlit
- 📊 Filtros por clube e jogador
- 📈 Métricas de valor, salário, cláusula
- 🖼️ Exibição de fotos e bandeiras
- 🔢 Progress bars para overall e salários
- 📄 Leitura eficiente de CSV com pandas
- 📦 Armazenamento em `st.session_state` para performance

---

## 🗃️ Dataset

> 📥 `datasets/CLEAN_FIFA23_official_data.csv`

O conjunto de dados possui mais de **17 mil jogadores**, com atributos como:
- Nome, Idade, Nacionalidade, Clube, Posição
- Foto e Bandeira
- Overall
- Altura, Peso
- Valor de mercado, Salário, Cláusula
- Data de ingresso e validade do contrato

---

## 🛠️ Tecnologias Usadas

- Python 3
- Streamlit
- Pandas
- Webbrowser (para botão externo)
- Dataset CSV limpo e estruturado

---



