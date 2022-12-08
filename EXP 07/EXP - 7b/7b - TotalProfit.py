import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
mL = df['month_number'].tolist()

labels=['facecream','facewash','toothpaste','bathingsoap','moisturizer']
for na in labels :
    plt.plot(mL, df[na].tolist(), label=(na.capitalize()+" Sales Data"),marker='o', mfc='black', linewidth=3, linestyle='dashed',color='red')
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='lower right')
    plt.xticks(mL)
    plt.yticks([10000, 20000, 30000, 40000, 50000])
    plt.title('Sales Data')
    plt.show()
