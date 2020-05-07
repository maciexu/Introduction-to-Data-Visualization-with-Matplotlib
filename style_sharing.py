"""
https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html
"""

# Switching between styles
# Use the "Solarize_Light2" style and create new Figure/Axes. Other: ggplot

plt.style.use("Solarize_Light2")

fig, ax = plt.subplots()

ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()


""" Saving """

fig.savefig('my_figure.png', dpi=300)

fig.set_size_inches([5,3])


""" iterating the different categories """
# Extract the "Sport" column
sports_column = summer_2016_medals['Sport']

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)

fig, ax = plt.subplots()

# Loop over the different sports branches
for sport in sports:
  # Extract the rows only for this sport
  sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
  # Add a bar for the "Weight" mean with std y error bar
  ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)

# Save the figure to file
fig.savefig("sports_weights.png")



