import matplotlib.pyplot as plt

input_values = range(1,7)
squares = [1,4,9,16,25,36]
plt.plot(input_values,squares,linewidth=4)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()