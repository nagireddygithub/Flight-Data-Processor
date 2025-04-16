# Flight Data Processor

A Python class to process flight data with robust methods for data manipulation and insights. Includes comprehensive unit tests.

## Features

- **Add/Remove Flights**: Manage flight entries with duplicate prevention.
- **Filter by Status**: Retrieve flights based on their status (e.g., `ON_TIME`, `DELAYED`).
- **Longest Flight**: Identify the flight with the maximum duration.
- **Update Flight Status** (Bonus): Modify the status of an existing flight.
- **Unit Tests**: Validate correctness with `unittest`.

## Prerequisites

- Python 3.6+ (for type hints)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flight-data-processor.git
   cd flight-data-processor

## Usage
#Import the Class
from flight_data_processor import FlightDataProcessor

# Initialize with Sample Data
flight_data = [
    {
        "flight_number": "AZ001",
        "departure_time": "2025-02-19 15:30",
        "arrival_time": "2025-02-20 03:45",
        "duration_minutes": 735,
        "status": "ON_TIME"
    },
    # Add more flights as needed
]

processor = FlightDataProcessor(flight_data)

# Add a Flight

new_flight = {
    "flight_number": "AZ003",
    "departure_time": "2025-03-01 10:00",
    "arrival_time": "2025-03-01 12:30",
    "duration_minutes": 150,
    "status": "ON_TIME"
}
processor.add_flight(new_flight)

# Remove a Flight

processor.remove_flight("AZ001")

# Filter Flights by Status

delayed_flights = processor.flights_by_status("DELAYED")

# Get Longest Flight

longest_flight = processor.get_longest_flight()

# Update Flight Status 

processor.update_flight_status("AZ002", "CANCELLED")


## TESTING

Run all tests: python -m unittest test_flight_data_processor.py -v

#Test Cases Covered
Adding new flights and handling duplicates.

Removing existing/non-existent flights.

Filtering by valid/invalid statuses.

updating flight status.
