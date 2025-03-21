import os
import sys
import django
import yfinance as yf
from pyspark.sql import SparkSession

# Define the correct project root (one level up from 'stock_monitor')
project_root = os.path.dirname(os.path.abspath(__file__))  # spark_pipeline
project_root = os.path.dirname(project_root)  # stock_monitor

sys.path.append(project_root)  # Add project root to sys.path

# Debugging: Print sys.path
print("System Path:", sys.path)

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stock_monitor.settings")

# Initialize Django
django.setup()

# Now, import the Django model
from django_app.models import StockData  # Ensure django_app exists

# Create Spark Session
spark = SparkSession.builder \
    .appName("StockDataPipeline") \
    .getOrCreate()

def fetch_and_process_stock_data():
    # Fetch data using yfinance
    data = yf.download('AAPL', period='1d', interval='1m')
    if data.empty:
        print("No data fetched.")
        return

    # Convert to Spark DataFrame
    df = spark.createDataFrame(data.reset_index())
    
    # Process data (filtering, handling nulls, etc.)
    df = df.fillna(0)

    # Save to Django Model
    for row in df.collect():
        StockData.objects.create(
            timestamp=row['Datetime'],
            open_price=row['Open'],
            close_price=row['Close'],
            high=row['High'],
            low=row['Low']
        )
    print("Data successfully ingested!")

if __name__ == "__main__":
    fetch_and_process_stock_data()
