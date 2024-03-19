import matplotlib.pyplot as plt
import numpy as np

species = ("Test1", "Test2", "Test3", "Test4", "Test5")
penguin_means = {
    'With Normalizing': (0, 0, 0, 0, 0),
    'Without Normalizing': (164, 62, 245, 158, 92)
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Distance score')
ax.set_title('Comparison between with and without normalizing')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 300)

plt.show()