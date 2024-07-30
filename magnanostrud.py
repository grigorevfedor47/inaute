import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ingest_data(url):
    try:
        # Simulate data ingestion here (this is just an example)
        raise ValueError("Simulated ingestion error")  # Simulating an error
    except Exception as err:
        logging.warning('Data ingestion failed: %s, URL: %s', err, url)

# Example URL
url = "http://example.com/data.csv"

# Call the ingest_data function
ingest_data(url)
