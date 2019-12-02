import pandas as pd
import matplotlib.pyplot as plt
import pygal

hist = pygal.Line()

data = pd.read_csv("company_sales_data.csv")
month_list = data["month_number"].tolist()
profit = data["total_profit"].tolist()
plt.plot(month_list,profit,label="Month wise profit of an year")
plt.xlabel("Months")
plt.ylabel("Profit")
plt.title("Company profit per month")
plt.xticks(month_list)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()