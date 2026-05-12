import duckdb

con = duckdb.connect()

result = con.execute("""
SELECT
    symbol,
    date,
    current_price,
    LAG(current_price) OVER (PARTITION BY symbol ORDER BY date) AS prev_price,
    current_price - LAG(current_price) OVER (PARTITION BY symbol ORDER BY date) AS price_change
FROM read_csv_auto('data/crypto_data.csv')
""").fetchdf()

print(result.head())