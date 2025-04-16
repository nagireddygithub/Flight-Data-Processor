import unittest
from flight_data_processor import FlightDataProcessor

class TestFlightDataProcessor(unittest.TestCase):
    def setUp(self):
        self.sample_flights = [
            {
                "flight_number": "AZ001",
                "departure_time": "2025-02-19 15:30",
                "arrival_time": "2025-02-20 03:45",
                "duration_minutes": 735,
                "status": "ON_TIME"
            },
            {
                "flight_number": "AZ002",
                "departure_time": "2025-02-21 11:00",
                "arrival_time": "2025-02-21 16:00",
                "duration_minutes": 300,
                "status": "DELAYED"
            }
        ]
        self.processor = FlightDataProcessor(self.sample_flights.copy())

    def test_add_flight_new(self):
        new_flight = {
            "flight_number": "AZ003",
            "departure_time": "2025-03-01 10:00",
            "arrival_time": "2025-03-01 12:30",
            "duration_minutes": 150,
            "status": "ON_TIME"
        }
        self.processor.add_flight(new_flight)
        self.assertEqual(len(self.processor.flights), 3)
        self.assertIn(new_flight, self.processor.flights)

    def test_add_flight_duplicate(self):
        duplicate_flight = self.sample_flights[0].copy()
        self.processor.add_flight(duplicate_flight)
        self.assertEqual(len(self.processor.flights), 2)

    def test_remove_flight_existing(self):
        self.processor.remove_flight("AZ001")
        self.assertEqual(len(self.processor.flights), 1)
        remaining_numbers = [f['flight_number'] for f in self.processor.flights]
        self.assertNotIn("AZ001", remaining_numbers)

    def test_remove_flight_non_existent(self):
        self.processor.remove_flight("AZ999")
        self.assertEqual(len(self.processor.flights), 2)

    def test_flights_by_status_existing(self):
        on_time_flights = self.processor.flights_by_status("ON_TIME")
        self.assertEqual(len(on_time_flights), 1)
        self.assertEqual(on_time_flights[0]['flight_number'], "AZ001")

    def test_flights_by_status_non_existent(self):
        cancelled_flights = self.processor.flights_by_status("CANCELLED")
        self.assertEqual(len(cancelled_flights), 0)

    def test_get_longest_flight(self):
        longest = self.processor.get_longest_flight()
        self.assertEqual(longest['flight_number'], "AZ001")

    def test_get_longest_flight_empty(self):
        empty_processor = FlightDataProcessor()
        with self.assertRaises(ValueError):
            empty_processor.get_longest_flight()

    def test_update_flight_status_existing(self):
        self.processor.update_flight_status("AZ001", "DELAYED")
        updated_flight = next(f for f in self.processor.flights if f['flight_number'] == "AZ001")
        self.assertEqual(updated_flight['status'], "DELAYED")

    def test_update_flight_status_non_existent(self):
        self.processor.update_flight_status("AZ999", "CANCELLED")
        self.assertEqual(len(self.processor.flights), 2)

if __name__ == '__main__':
    unittest.main()