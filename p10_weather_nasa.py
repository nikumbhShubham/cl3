import csv
import requests
from io import StringIO
from collections import defaultdict

class NASAWeatherMapReduce:
    def __init__(self):
        # NASA GISS Global Land-Ocean Temperature Index (Public Data)
        # No API key required.
        self.url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
        self.raw_data = None

    def fetch_data(self):
        """Downloads the global temperature dataset directly from NASA servers."""
        print(f"Connecting to NASA GISS (Goddard Institute for Space Studies)...")
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            
            # NASA CSVs contain a few lines of metadata at the top.
            # We must find the actual CSV header to start parsing correctly.
            content = response.text
            header_start = content.find("Year,Jan,Feb")
            if header_start == -1:
                print("Error: Could not find data header in NASA file.")
                return False
                
            self.raw_data = content[header_start:]
            print("NASA Global Climate Data downloaded successfully.")
            return True
        except Exception as e:
            print("Connection Error: ", e)
            return False

    def mapper(self, row):
        """
        Extracts Year and the Annual Mean from NASA's CSV format.
        'J-D' stands for January-December average anomaly.
        """
        try:
            year = row["Year"]
            # We use the J-D column which is the pre-calculated annual mean anomaly
            temp_anomaly = float(row["J-D"]) 
            return (year, temp_anomaly)
        except:
            # Skip rows with missing data (often marked as '***' in NASA files)
            return None

    def reducer(self, grouped_data):
        """
        In this implementation, the reducer identifies the 
        final yearly value from the mapped pairs.
        """
        results = []
        for year, values in grouped_data.items():
            # Since NASA already provides one average per year, 
            # we just take that value.
            results.append((year, values[0]))
        return results

    def run(self):
        if not self.fetch_data():
            return

        # 1. MAP PHASE
        mapped_data = []
        reader = csv.DictReader(StringIO(self.raw_data))
        for row in reader:
            pair = self.mapper(row)
            if pair:
                mapped_data.append(pair)

        # 2. SHUFFLE/GROUP PHASE
        # Groups all temperature anomalies by their respective years
        grouped_data = defaultdict(list)
        for year, anomaly in mapped_data:
            grouped_data[year].append(anomaly)

        # 3. REDUCE PHASE
        yearly_results = self.reducer(grouped_data)

        # 4. FINAL AGGREGATION
        # Find the year with the maximum and minimum anomalies
        hottest = max(yearly_results, key=lambda x: x[1])
        coolest = min(yearly_results, key=lambda x: x[1])

        print("\n" + "="*60)
        print("NASA GLOBAL TEMPERATURE ANALYSIS (1880 - PRESENT)")
        print("="*60)
        print(f"Hottest Year Globally : {hottest[0]} | Anomaly: +{hottest[1]}°C")
        print(f"Coolest Year Globally : {coolest[0]} | Anomaly: {coolest[1]}°C")
        print("="*60)
        print("Interpretation: Anomaly values are relative to the 1951-1980 mean.")

if __name__ == "__main__":
    app = NASAWeatherMapReduce()
    app.run()
