# Delhi Metro Route Finder

A Python-based CLI application that implements **Dijkstra's Algorithm** to find the shortest path between Delhi Metro stations using travel time as edge weights.

## Features
- Calculates the fastest route between any two given stations based on transit minutes.
- Displays full path tracking with specific metro line information (e.g., Blue Line, Yellow Line).
- Outputs total travel time, the number of stations in the route, and the total interchanges required.
- Robust exception handling for invalid inputs.

## Prerequisites
- Python 3.x (Built-in libraries only, no external dependencies required)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/anu012007-web/Metro-route-finder.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Metro-route-finder
   ```
3. Run the script:
   ```bash
   python metro_route_finder.py
   ```

## Example Usage

When prompted, ensure you input the **numeric ID** (e.g., `1`) corresponding to the station you want, instead of the station's full name.

```text
============================================================
AVAILABLE METRO STATIONS
============================================================
ID    Station Name              Metro Line                    
------------------------------------------------------------
...
0     Rajiv Chowk               Blue Line & Yellow Line       
1     New Delhi                 Yellow Line & Airport Line    
...
8     Noida City Centre         Blue Line                     
9     Dwarka Sector 21          Blue Line                     
============================================================

Enter source station ID: 1
Enter destination station ID: 8

============================================================
SHORTEST ROUTE FOUND
============================================================
📍 New Delhi (Yellow Line & Airport Line)
   ↓ 2 min
📍 Rajiv Chowk (Blue Line & Yellow Line)
   ↓ 1 min
...
------------------------------------------------------------
📊 Total Travel Time: 18 minutes
🚉 Number of Stations: 5
🔄 Interchanges: 4
============================================================
```

## Algorithm Highlights
- **Graph Representation**: The metro network is constructed as an Adjacency List using nested Python dictionaries. Nodes represent stations, and edges represent the travel time between them.
- **Shortest Path**: Uses Dijkstra's Algorithm to greedily find the minimum cumulative travel time from the source node to all other reachable nodes. 
