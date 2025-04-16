from typing import List, Optional, Dict, Any

class FlightDataProcessor:
    def __init__(self, flights: Optional[List[Dict[str, Any]]] = None) -> None:
        self.flights: List[Dict[str, Any]] = flights.copy() if flights is not None else []

    def add_flight(self, data: Dict[str, Any]) -> None:
        existing_numbers = {flight['flight_number'] for flight in self.flights}
        if data['flight_number'] in existing_numbers:
            return
        self.flights.append(data)

    def remove_flight(self, flight_number: str) -> None:
        self.flights = [flight for flight in self.flights if flight['flight_number'] != flight_number]

    def flights_by_status(self, status: str) -> List[Dict[str, Any]]:
        return [flight for flight in self.flights if flight['status'] == status]

    def get_longest_flight(self) -> Dict[str, Any]:
        if not self.flights:
            raise ValueError("No flights available")
        return max(self.flights, key=lambda x: x['duration_minutes'])

    def update_flight_status(self, flight_number: str, new_status: str) -> None:
        for flight in self.flights:
            if flight['flight_number'] == flight_number:
                flight['status'] = new_status
                break

            