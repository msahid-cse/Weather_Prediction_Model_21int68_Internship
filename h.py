import pandas as pd

def add_season_column(input_file, output_file):
    # Read dataset (space-separated)
    df = pd.read_csv('D:\Project\Weather_Prediction_Model_21int68_Internship\Weather_Data.csv')

    # Ensure 'Date' column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Function to determine season(s) based on month
    def get_season(month):
        seasons = []
        if month in [4, 5]:  # April, May
            seasons.extend(["Boro", "Aus"])
        elif month in [6]:  # June
            seasons.append("Aus")
        elif month in [7]:  # July
            seasons.extend(["Aus", "Aman"])
        elif month in [8, 9, 10]:  # Aug, Sep, Oct
            seasons.append("Aman")
        elif month == 11:  # November
            seasons.append("Aman")
        elif month == 12:  # December
            seasons.extend(["Boro", "Aman"])
        elif month == 1 or month == 2 or month == 3:  # Jan, Feb, Mar
            seasons.append("Boro")
        return ", ".join(seasons)

    # Apply function to get season
    df['Season'] = df['Date'].dt.month.apply(get_season)

    # Save final dataset
    df.to_csv(output_file, index=False)
    print(f"Dataset with season saved to {output_file}")

# Example usage:
# add_season_column("weather_data.txt", "weather_with_season.csv")
