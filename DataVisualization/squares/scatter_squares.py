import matplotlib.pyplot as plt

input_values = list(range(1,1001))
output_values = [x**2  for x in input_values]
#plt.scatter(input_values,output_values,c=output_values,cmap= plt.cm.Blues,edgecolor='none',s=40)
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')
