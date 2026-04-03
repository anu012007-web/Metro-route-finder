"""ru
DELHI METRO ROUTE FINDER
Design and Analysis of Algorithms (DAA) Mini Project
SRM University Chennai

Implementation of Dijkstra's Algorithm to find shortest path
between metro stations using travel time as edge weights.
"""

import sys

class DelhiMetroRouteFinder:
    def __init__(self):
        """Initialize the metro network with stations and connections"""
        
        # Station names with line information
        self.stations = {
            0: {"name": "Rajiv Chowk", "line": "Blue Line & Yellow Line"},
            1: {"name": "New Delhi", "line": "Yellow Line & Airport Line"},
            2: {"name": "Central Secretariat", "line": "Violet Line"},
            3: {"name": "Patel Chowk", "line": "Yellow Line"},
            4: {"name": "Kashmere Gate", "line": "Red Line & Yellow Line"},
            5: {"name": "Chandni Chowk", "line": "Yellow Line"},
            6: {"name": "Lajpat Nagar", "line": "Violet Line & Pink Line"},
            7: {"name": "Hauz Khas", "line": "Yellow Line & Magenta Line"},
            8: {"name": "Noida City Centre", "line": "Blue Line"},
            9: {"name": "Dwarka Sector 21", "line": "Blue Line"}
        }
        
        # Graph representation: Adjacency list with travel times (minutes)
        self.graph = {
            0: {1: 2, 3: 1, 4: 5},      # Rajiv Chowk connections
            1: {0: 2, 2: 3, 4: 3},      # New Delhi connections
            2: {1: 3, 3: 2, 6: 4},      # Central Secretariat connections
            3: {0: 1, 2: 2, 5: 3},      # Patel Chowk connections
            4: {0: 5, 1: 3, 5: 2, 7: 6}, # Kashmere Gate connections
            5: {3: 3, 4: 2, 7: 4},      # Chandni Chowk connections
            6: {2: 4, 7: 3, 8: 7},      # Lajpat Nagar connections
            7: {4: 6, 5: 4, 6: 3, 9: 8}, # Hauz Khas connections
            8: {6: 7, 9: 5},            # Noida City Centre connections
            9: {7: 8, 8: 5}             # Dwarka Sector 21 connections
        }
    
    def display_all_stations(self):
        """Display all available stations with their line information"""
        print("\n" + "="*60)
        print("AVAILABLE METRO STATIONS")
        print("="*60)
        print(f"{'ID':<5} {'Station Name':<25} {'Metro Line':<30}")
        print("-"*60)
        for station_id, info in self.stations.items():
            print(f"{station_id:<5} {info['name']:<25} {info['line']:<30}")
        print("="*60)
    
    def dijkstra_algorithm(self, source, destination):
        """
        Implementation of Dijkstra's Algorithm
        Returns: (path list, total time, number of stations)
        """
        
        # Initialize distances (infinity for all except source)
        distances = {node: float('inf') for node in self.graph}
        distances[source] = 0
        
        # Store previous node for path reconstruction
        previous = {node: None for node in self.graph}
        
        # Set of unvisited nodes
        unvisited = set(self.graph.keys())
        
        # Main algorithm loop
        while unvisited:
            # Find node with minimum distance
            current = min(unvisited, key=lambda node: distances[node])
            
            # Stop if we reached destination
            if current == destination:
                break
            
            # Remove current from unvisited
            unvisited.remove(current)
            
            # Check all neighbors of current node
            for neighbor, travel_time in self.graph[current].items():
                if neighbor in unvisited:
                    new_distance = distances[current] + travel_time
                    
                    # Update if we found a shorter path
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current
        
        # Reconstruct the path from source to destination
        path = []
        current = destination
        
        # Handle case where no path exists
        if previous[destination] is None and source != destination:
            return None, float('inf'), 0
        
        while current is not None:
            path.insert(0, current)
            current = previous[current]
        
        total_time = distances[destination]
        num_stations = len(path)
        
        return path, total_time, num_stations
    
    def display_route(self, path, total_time, num_stations):
        """Display the route in a user-friendly format"""
        if path is None:
            print("\n❌ No route found between these stations!")
            return
        
        print("\n" + "="*60)
        print("SHORTEST ROUTE FOUND")
        print("="*60)
        
        # Display each station in the path
        for i, station_id in enumerate(path):
            station_info = self.stations[station_id]
            print(f"📍 {station_info['name']} ({station_info['line']})")
            
            # Show arrow except for last station
            if i < len(path) - 1:
                # Find travel time to next station
                next_station = path[i + 1]
                travel_time = self.graph[station_id].get(next_station, "?")
                print(f"   ↓ {travel_time} min")
        
        print("-"*60)
        print(f"📊 Total Travel Time: {total_time} minutes")
        print(f"🚉 Number of Stations: {num_stations}")
        print(f"🔄 Interchanges: {num_stations - 1 if num_stations > 0 else 0}")
        print("="*60)
    
    def get_user_input(self):
        """Get source and destination from user with validation"""
        while True:
            try:
                self.display_all_stations()
                
                source = int(input("\nEnter source station ID: "))
                destination = int(input("Enter destination station ID: "))
                
                # Validate input
                if source not in self.stations:
                    print(f"❌ Invalid source ID! Please enter number between 0 and {len(self.stations)-1}")
                    continue
                
                if destination not in self.stations:
                    print(f"❌ Invalid destination ID! Please enter number between 0 and {len(self.stations)-1}")
                    continue
                
                if source == destination:
                    print("❌ Source and destination cannot be the same!")
                    continue
                
                return source, destination
                
            except ValueError:
                print("❌ Please enter valid numbers only!")
    
    def run(self):
        """Main method to run the metro route finder"""
        print("\n" + "="*60)
        print("     DELHI METRO ROUTE FINDER")
        print("     Shortest Path using Dijkstra's Algorithm")
        print("="*60)
        print("\nWelcome! This system finds the shortest route")
        print("between any two Delhi Metro stations.\n")
        
        while True:
            # Get source and destination from user
            source, destination = self.get_user_input()
            
            # Find shortest path using Dijkstra's Algorithm
            path, total_time, num_stations = self.dijkstra_algorithm(source, destination)
            
            # Display the result
            source_name = self.stations[source]["name"]
            dest_name = self.stations[destination]["name"]
            print(f"\n📍 Finding route from {source_name} to {dest_name}...")
            
            self.display_route(path, total_time, num_stations)
            
            # Ask if user wants to continue
            again = input("\nDo you want to find another route? (yes/no): ").lower()
            if again not in ['yes', 'y']:
                print("\n" + "="*60)
                print("Thank you for using Delhi Metro Route Finder!")
                print("="*60)
                break

# Main execution
if __name__ == "__main__":
    metro = DelhiMetroRouteFinder()
    metro.run()
