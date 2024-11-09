import csv
import pandas
import psycopg
from pathlib import Path
# データベース接続情報
DB_NAME = "db_part1"
DB_USER = "dsuser"
DB_PASSWORD = "password"
DB_HOST = "db"
DB_PORT = "5432"

# インポートするCSVファイルのパスとターゲットテーブル
CSV_FILE_PATH = "transaction_detail_2.csv"
TABLE_NAME = "transaction_detail"
COLUMN_MAPPING = {
    "detail_id":"id",
    "quantity":"quantity",
    "transaction_id":"transaction_history_id",
    "item_id":"item_id",
}

# CSVデータのインポート関数
def import_csv_to_postgresql(cur, column_mapping):
    csv_file = open(csv_file_path(CSV_FILE_PATH), mode="r", encoding="utf-8")
    reader = csv.DictReader(csv_file)

    postgres_columns = [column_mapping[csv_col] for csv_col in reader.fieldnames if csv_col in column_mapping] # if csv_col in column_mappingはなくてもいい
    placeholders = ["%s"] * len(postgres_columns)  # プレースホルダーを生成

    # INSERTクエリを構築
    insert_query = f"INSERT INTO {TABLE_NAME} ({', '.join(postgres_columns)}) VALUES ({', '.join(placeholders)})"

    # データのインサート
    for row in reader:
        # CSV列名に基づき対応するPostgreSQL列の値リストを作成
        values = [row[csv_col] for csv_col in reader.fieldnames if csv_col in column_mapping]
        cur.execute(insert_query, values)

    # コミットして変更を保存
    conn.commit()
    print(f"Data from {CSV_FILE_PATH} successfully imported into {TABLE_NAME}.")
    if csv_file:
        csv_file.close()

def csv_file_path(file_name)->str:
    return Path(__file__).resolve().parent.parent / 'data' / file_name
    
if __name__ == '__main__':
    conn = None
    cur = None
    try:
        conn = psycopg.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        import_csv_to_postgresql(cur, COLUMN_MAPPING)
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        print("An error occurred:", e)
    finally:
        # カーソルと接続を閉じる
        
        if cur:
            cur.close()
        if conn:
            conn.close()
        