# Aircraft Gliding Performance Simulation

## Overview
This repository contains Python scripts for simulating the gliding performance of an aircraft. The simulation models the aircraft's flight dynamics, aerodynamics, and environmental conditions.

## Features
* **Aerodynamic modeling:** Calculates lift, drag, and other aerodynamic forces.
* **Flight dynamics:** Simulates the aircraft's motion using a system of differential equations.
* **Atmospheric modeling:** Implements the International Standard Atmosphere (ISA) model.
* **Control system:** Includes basic flight control logic for gliding.
* **Simulation:** Numerically integrates the equations of motion to simulate the flight.

## Getting Started
### Prerequisites
* Python (version 3.x)
* NumPy
* SciPy
* Matplotlib

### Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/davilmds15/aircraft_performance_gliding]

2. Create a virtual environment (recommended):
Virtual environments help isolate project dependencies and avoid conflicts with other Python packages on your system. Here's how to create one:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate  # For Windows

3. Install dependencies:
Activate your virtual environment (if you created one) and install the required packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
If you don't have a `requirements.txt` file, create one and list all necessary Python packages for this project.

### Running the Simulation

1. Modify parameters: Edit the `parametros.py` file to set aircraft and simulation parameters according to your needs.
2. Run the simulation: Execute the `exemplos_planeio.py` script. Follow the prompts displayed on the screen to input desired values.

### Usage

* `exemplos_planeio.py`: The main script to run the simulation.
* `aerodinamica.py`: Contains aerodynamic models.
* `dinamica_translacao.py`: Defines the equations of motion.
* `controles.py`: Implements flight control logic.
* `modelo_ambiental.py`: Provides atmospheric data.
* `equilibrio.py`: Calculates equilibrium flight conditions.

### Contributing

Feel free to contribute to this project by:
* Reporting issues: Open an issue on GitHub to report bugs or suggest improvements.
* Submitting pull requests: Fork the repository, make your changes, and submit a pull request.






