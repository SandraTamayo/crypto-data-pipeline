# Crypto Data Pipeline

Pipeline de datos que extrae información de criptomonedas desde una API,
guarda histórico y permite análisis de evolución.

## Tecnologías
- Python
- DuckDB
- SQL

## Flujo
API → CSV → DuckDB → SQL

## Cómo correr
pip install -r requirements.txt
python scripts/extract.py
python scripts/transform.py