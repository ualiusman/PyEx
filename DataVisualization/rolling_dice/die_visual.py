from die import Dice
import pygal

d = Dice()

results = []
for n in range(1000):
    result = d.roll()
    results.append(result)
    
frequencies = []

for value in range(1, d.num_sides+1):
    f = results.count(value)
    frequencies.append(f)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')