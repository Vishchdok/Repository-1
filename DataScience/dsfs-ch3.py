""" Data Science from Scratch Chapter 3: Visualizing Data """

from matplotlib import pyplot as plt

""" matplotlib """

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='g', marker='o', linestyle='solid')

# add a title
plt.title("Nominal GDP")

# add a label to y-axis
plt.ylabel("Billions of $")
plt.show()

""" Bar Charts """

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Ghandi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]

# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.xlabel("My Favorite Movies")

# label x-axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()

