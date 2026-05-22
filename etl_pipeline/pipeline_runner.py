from extract import extract_news_data
from transform import transform_news_data
from load import load_processed_data

# STEP 1 - Extract
raw_data = extract_news_data()

# STEP 2 - Transform
transformed_data = transform_news_data(raw_data)

# STEP 3 - Load
load_processed_data(transformed_data)

print("Complete ETL Pipeline Executed Successfully!")