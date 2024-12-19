# 🌍 Python CLI Project: Distance Calculator

## **Description**
This Python CLI application calculates the distance between two points on a plane or sphere. It supports both **2D Cartesian coordinates** and **geographical coordinates** (latitude and longitude). The project demonstrates practical Python programming concepts such as argument parsing, mathematical computations, and modular design for reusability.

For geographical calculations, the tool implements the **Haversine formula**, which computes the great-circle distance between two points on the Earth. This is particularly useful for applications involving geospatial data, such as navigation systems and geographic analysis.

Additionally, the project introduces users to basic Python CLI development, making it a valuable learning resource for beginners.

### **About `geopy` and Geographical Calculations**
The project optionally uses `geopy`, a Python library for geocoding and calculating distances between geographic points. While not required for this tool, `geopy` is widely used in geospatial applications for its simplicity and powerful features:
- Distance calculations (e.g., great-circle distance, Vincenty distance).
- Geocoding (converting addresses into geographic coordinates).
- Reverse geocoding (finding addresses based on coordinates).

You can enhance this CLI tool by integrating `geopy` for more advanced distance computations or address lookups.

## **✨ Features**
* 🟩 Calculate distance in 2D Cartesian coordinates
* 🌐 Calculate distance using the Haversine formula for geographical coordinates
* ✅ User-friendly command-line interface
* 🪶 Lightweight and portable script

## **Requirements**
* Python 3.7 or later
* Libraries:
  * `math`
  * `argparse`

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/distance-cli.git

2. Navigate to the project directory:
   ```bash 
   cd distance-cli

3. Ensure Python is installed:
   ```bash
   python --version

4. Install any dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

Run the script with the following syntax:
    ```bash
    python distance_calculator.py --type --point1 <x1,y1> --point2 <x2,y2>

### Example

- For Cartesian coordinates:
    ```bash
    python distance_calculator.py --type cartesian --point1 3,4 --point2 7,1

- For geographical coordinates:
    ```bash
    python distance_calculator.py --type geo --point1 36.8219,-1.2921 --point2 40.7128,-74.0060

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.

2. Create a new branch:
    ```bash 
    git checkout -b feature-branch-name

3. Commit your changes:
    ```bash
    git commit -m "Describe your feature"

4. Push to branch:
    ```bash
    git push origin feature-branch-name

5. Open a pull request.

## Acknowledgements

* Developed by **Keith Githinji**