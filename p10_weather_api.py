import csv
import requests
from io import StringIO
from collections import defaultdict

class IndianWeatherAPIMapReduce:
    def __init__(self):
        # API credentials for data.gov.in
        self.api_key = "579b464db66ec23bdd0000016c4e9eb7c0244bcd783540de7a754501"
        self.resource_id = "45787c4b-3210-4fd0-b120-63336e042370"
        self.api_url = f"https://api.data.gov.in/resource/{self.resource_id}"
        self.raw_data = None

    def fetch_data(self):
        """Fetches weather CSV data from the internet."""
        params = {
            "api-key": self.api_key,
            "format": "csv",
            "limit": 5000
        }
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            self.raw_data = response.text
            print("Weather data fetched successfully from data.gov.in API")
            return True
        except Exception as e:
            print("API Error:", e)
            return False

    def mapper(self, row):
        """Extracts Year and Annual temperature from a CSV row."""
        try:
            year = row["YEAR"]
            temp = float(row["ANNUAL"])
            return (year, temp)
        except:
            # Handle empty or malformed data rows
            return None

    def reducer(self, grouped_data):
        """Calculates the average temperature for each year."""
        results = []
        for year, temps in grouped_data.items():
            avg_temp = sum(temps) / len(temps)
            results.append((year, avg_temp))
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
        grouped_data = defaultdict(list)
        for year, temp in mapped_data:
            grouped_data[year].append(temp)

        # 3. REDUCE PHASE
        yearly_avg = self.reducer(grouped_data)

        # 4. AGGREGATE RESULTS
        hottest = max(yearly_avg, key=lambda x: x[1])
        coolest = min(yearly_avg, key=lambda x: x[1])

        print("\n" + "="*50)
        print("MAPREDUCE ANALYSIS RESULT (INDIA)")
        print("="*50)
        print(f"Hottest Year : {hottest[0]} | Avg Temp : {hottest[1]:.2f} °C")
        print(f"Coolest Year : {coolest[0]} | Avg Temp : {coolest[1]:.2f} °C")
        print("="*50)

if __name__ == "__main__":
    app = IndianWeatherAPIMapReduce()
    app.run()
