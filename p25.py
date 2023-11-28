import re

def calculate_average_temperature(temperature_message):
    temperature_values = re.findall(r'\b\d+\b', temperature_message)
    if temperature_values:
        temperatures = [int(value) for value in temperature_values]
        average_temperature = sum(temperatures) / len(temperatures)
        return average_temperature
    else:
        return None
if __name__ == "__main__":
    temperature_message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
    average_temperature = calculate_average_temperature(temperature_message)
    if average_temperature is not None:
        print(f"The average temperature for the next three days is: {average_temperature}C")
    else:
        print("No temperature values found in the message.")