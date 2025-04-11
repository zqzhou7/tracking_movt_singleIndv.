# SLEAP Movement Analysis - Single Individual

This repository contains a Python script that processes SLEAP output data to:
- Plot the movement track of a tracked subject using keypoint coordinates.
- Compute instantaneous speed (velocity) and acceleration from the movement track.
- Generate a time-series plot with speed and acceleration shown in two vertically stacked subplots.
- Export an extended CSV with the computed metrics (speed, acceleration, and time).

## Features

- **Movement Track Plot:**  
  Visualizes the tracked subject’s movement based on the `cntrl1_1.x` and `cntrl1_1.y` columns with start and end markers.

- **Speed & Acceleration Calculation:**  
  Computes speed as the Euclidean distance between consecutive frames and derives acceleration as the derivative of speed (with smoothing applied).

- **Time-Series Visualization:**  
  Combines speed and acceleration into one figure with two stacked subplots for easy time-series analysis.

- **CSV Output:**  
  Saves an extended CSV file including the computed speed, acceleration, and time columns.

## Prerequisites

- **Python 3.x**

Required Python packages:
- `numpy`
- `pandas`
- `matplotlib`

You can install these dependencies with:

```bash
pip install numpy pandas matplotlib
```

## Usage

### Prepare Your Data:
Ensure that your SLEAP output CSV file (named `sleap_output.csv`) is located in the root of the repository. This file should include at least these columns:

- **track** (with values like `track_0`)
- **cntrl1_1.x** and **cntrl1_1.y** (to represent X and Y coordinates)
- **frame_idx** (optional; used for generating the time column)

### Run the Script:
Execute the script by running:

```bash
python your_script_name.py
```

## Contributing

Contributions are welcome! To contribute:

- **Fork the repository:**  
  Create a copy of the project on your GitHub account.
- **Create a branch:**  
  Use a descriptive branch name for your new feature or bug fix.
- **Make your changes:**  
  Ensure your code is well-documented and passes any existing tests.
- **Submit a pull request:**  
  Provide a clear description of your changes and reference any relevant issues.
  
Feel free to open an issue if you have any questions or need help with improvements.

## Acknowledgements

- **SLEAP:** [sleap.ai](https://sleap.ai) for their innovative multi-animal pose tracking solution.
- **NumPy:** [numpy.org](https://numpy.org) for numerical computation support.
- **Pandas:** [pandas.pydata.org](https://pandas.pydata.org) for data manipulation and analysis.
- **Matplotlib:** [matplotlib.org](https://matplotlib.org) for plotting capabilities.
- Thanks to the open-source community for continuous support and contributions.
