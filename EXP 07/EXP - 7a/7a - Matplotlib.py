import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sale_data.csv")
pL = df['total_profit'].tolist()
mL = df['month_number'].tolist()
plt.plot(mL, pL, label="Month-wise profit data of last year")
plt.xlabel('Month Number')
plt.ylabel('Profit in Dollar')
plt.xticks(mL)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
