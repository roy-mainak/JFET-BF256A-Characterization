import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel data
file_path = "./data/JFET_output_table.xlsx"
df = pd.read_excel(file_path)

# Set VDS column as X-axis
vds = df.iloc[:, 0]

# Plot IDS curves
plt.figure(figsize=(10, 6))
for col in df.columns[1:]:
    plt.plot(vds, df[col], marker='o', label=col)

# Labels and formatting
plt.title("JFET Output Characteristics")
plt.xlabel("VDS (Volts)")
plt.ylabel("IDS (mA)")
plt.grid(True)
plt.legend(title="Gate Voltage")
plt.tight_layout()

# Show

plt.show()
