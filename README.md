# 🌡️ IoT Temperature Data Pipeline

## 📌 Descrição
Projeto de pipeline de dados utilizando sensores IoT para análise de temperatura.

O sistema realiza:
- ingestão de dados (CSV)
- processamento com Python
- armazenamento em PostgreSQL
- visualização com Streamlit

---

## 🚀 Tecnologias
- Python
- PostgreSQL
- Docker
- Streamlit
- Plotly

---

## ⚙️ Como executar

### 1. Subir banco com Docker
docker run --name postgres-iot -e POSTGRES_PASSWORD=1234 -e POSTGRES_USER=postgres -e POSTGRES_DB=iot -p 5432:5432 -d postgres

### 2. Rodar ETL
cd src
python etl.py

### 3. Criar views SQL
Executar o arquivo views.sql no PostgreSQL

### 4. Rodar dashboard
python -m streamlit run dashboard.py

---

## 📊 Funcionalidades
- análise de temperatura média
- distribuição de leituras por hora
- variação térmica por dia

---

## 📸 Dashboard
<img width="1920" height="1021" alt="{639509EF-9BFD-4F7E-B91F-9A76D8EABDC1}" src="https://github.com/user-attachments/assets/b0146e6f-e4b0-42fc-987a-83518c71c168" />

<img width="1920" height="1019" alt="{F4AD30BC-153D-4990-AFC4-7401D3AED690}" src="https://github.com/user-attachments/assets/4bda1e99-4c32-4f99-ab4d-0b7cca7209b9" />


---

## 💡 Insights
- variação significativa de temperatura
- padrões ao longo do tempo
- potencial para monitoramento ambiental
