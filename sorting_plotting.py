import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# -------------------------------
# Parameters & File Names
# -------------------------------
input_csv = "sleap_output.csv"  # SLEAP output file with track_0 data
output_csv = "sleap_output_speed_acceleration.csv"  # Extended CSV output with computed metrics
rolling_window = 3500           # Rolling window size for smoothing (adjust if needed)
fps = 30                        # Frames per second (as per your video)
frames_per_minute = fps * 60    # Number of frames per minute

# -------------------------------
# Read the CSV File
# -------------------------------
try:
    df = pd.read_csv(input_csv)
except Exception as e:
    sys.exit(f"Error reading {input_csv}: {e}")

# -------------------------------
# (Optional) Filter for track_0 rows
# -------------------------------
if "track" in df.columns:
    df = df[df["track"] == "track_0"].copy()

# -------------------------------
# Check for required coordinate columns
# -------------------------------
required_columns = ["cntrl1_1.x", "cntrl1_1.y"]
missing = [col for col in required_columns if col not in df.columns]
if missing:
    sys.exit(f"Missing required columns: {missing}")

# -------------------------------
# Section 1: Plot the Movement Track of Track 0
# -------------------------------
x = df["cntrl1_1.x"]
y = df["cntrl1_1.y"]

fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.plot(x, y, color="blue", label="Movement Track")
# Mark the starting point with a circle and the ending point with a square
ax1.plot(x.iloc[0], y.iloc[0], marker="o", color="blue", markersize=8, label="Start")
ax1.plot(x.iloc[-1], y.iloc[-1], marker="s", color="blue", markersize=8, label="End")
ax1.set_title("Movement Track of Track 0")
ax1.set_xlabel("X Position (pixels)")
ax1.set_ylabel("Y Position (pixels)")
ax1.legend()
ax1.invert_yaxis()  # Invert y-axis if necessary
movement_plot_file = "movement_track_track0.png"
plt.savefig(movement_plot_file, dpi=300, bbox_inches="tight")
plt.show()
print(f"Movement track plot saved to: {os.path.abspath(movement_plot_file)}")

# -------------------------------
# Section 2: Compute Speed and Acceleration
# -------------------------------
# Compute the differences between consecutive frames
dx = x.diff()
dy = y.diff()

# Calculate instantaneous speed (Euclidean distance between frames)
speed = np.sqrt(dx**2 + dy**2)
# Smooth the speed using a rolling window
speed_smooth = speed.rolling(window=rolling_window, center=True).mean()

# Compute acceleration as the difference in the smoothed speed and then smooth it
acceleration = speed_smooth.diff()
acceleration_smooth = acceleration.rolling(window=rolling_window, center=True).mean()

# Append computed speed and acceleration to the DataFrame
df["speed"] = speed_smooth
df["acceleration"] = acceleration_smooth

# -------------------------------
# Section 3: Add a Time Column (in minutes)
# -------------------------------
if "frame_idx" in df.columns:
    df["time_min"] = df["frame_idx"] / frames_per_minute
else:
    # If frame_idx is not available, use the DataFrame index as a proxy for frame order
    df["time_min"] = df.index / frames_per_minute

# Save the extended DataFrame to a new CSV file
df.to_csv(output_csv, index=False)
print(f"Extended CSV saved to: {os.path.abspath(output_csv)}")

# -------------------------------
# Section 4: Plot Time-Series of Speed and Acceleration
# -------------------------------
fig2, (ax_top, ax_bottom) = plt.subplots(2, 1, sharex=True, figsize=(12, 8))
time = df["time_min"]

# Upper subplot: Speed vs. Time
ax_top.plot(time, df["speed"], color="blue")
ax_top.set_title("Track 0: Speed vs. Time")
ax_top.set_ylabel("Speed (pixel/frame)")
ax_top.grid(True)

# Lower subplot: Acceleration vs. Time
ax_bottom.plot(time, df["acceleration"], color="red")
ax_bottom.set_title("Track 0: Acceleration vs. Time")
ax_bottom.set_xlabel("Time (minutes)")
ax_bottom.set_ylabel("Acceleration (pixel/frame²)")
ax_bottom.grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.95])
time_series_file = "track0_speed_acceleration_timeseries.png"
plt.savefig(time_series_file, dpi=300, bbox_inches="tight")
plt.show()
print(f"Time-series plot saved to: {os.path.abspath(time_series_file)}")
