import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_excel("D:/THESIS/OUTPUTS/master.xlsx", sheet_name="forstatistics") 

df_renamed = df.rename(columns={
    "HRC-MP1": "1",
    "HRC-MP2": "2",
    "HRC-MP3": "3",
    "HRC-MP4": "4",
    "HRC-MP5": "5",
    "HRC-MP6": "6",
    "HRC-MP7": "7",
    "HRC-MP8": "8",
    "HRC-MP9": "9"
})

#We create a list with every column name ['1', '2', ... ]:
distortion_cols = [f"{i}" for i in range(1, 10)]

#Since Seaborn require long format, we use .melt to transfrom the data frame:
df_melted = df_renamed.melt(value_vars=distortion_cols, var_name="Node", value_name="Hardness")

# Plot with seaborn
plt.figure(figsize=(12, 6))
sns.boxplot(x="Node", y="Hardness", data=df_melted, palette={'orange'})
plt.title("Boxplot of Hardness Values per Node")
plt.ylabel("Hardness [-]")
plt.savefig('Boxplot of Hardness Values per Node.jpg', dpi=300, bbox_inches='tight')
plt.show()