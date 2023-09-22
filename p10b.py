import json

# Function to fetch current weather data from a JSON file
def fetch_weather_data(json_file):
    try:
        with open(json_file, "r") as file:
            weather_data = json.load(file)
        return weather_data
    except FileNotFoundError:
        print(f"Error: The file {json_file} was not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON in {json_file}. {e}")
        return None

# Main program
if __name__ == "__main__":
    json_file = "weather_data.json"  # Replace with the actual path to your JSON file

    weather_data = fetch_weather_data(json_file)

    if weather_data:
        print("Current Weather Data:")
        print(f"City: {weather_data['city']}")
        print(f"Temperature: {weather_data['temperature']}°F")
        print(f"Weather Conditions: {weather_data['weather_conditions']}")
        print(f"Humidity: {weather_data['humidity']}%")
