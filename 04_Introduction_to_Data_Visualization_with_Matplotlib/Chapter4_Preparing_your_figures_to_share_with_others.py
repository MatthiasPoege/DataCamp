### Part1 There are different pre-set style packages for matplotlib
# There is a website showing many of them:
# https://matplotlib.org/2.0.2/gallery.html

#plt.style.use('default')
#plt.style.use('seaborn-colorblind')
#plt.style.use('grayscale')
#plt.style.use('tableau-colorblind10')
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.bar(medals.index, medals["Gold"])
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"])
ax.bar(medals.index, medals["Bronze"], bottom=medals["Gold"]+medals["Silver"])
plt.show()

### Part2 Switching between styles
# Use the "ggplot" style and create new Figure/Axes
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()

# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

### Part3 Saving a file several times
# Save as a PNG file
fig.savefig('my_figure.png')
# Save as a PNG file with 300 dpi
fig.savefig('my_figure_300dpi.png', dpi=300)

### Part4 Save a figure with different sizes
# Set figure dimensions and save as a PNG
fig.set_size_inches([3,5])
fig.savefig('figure_3_5.png')
# Set figure dimensions and save as a PNG
fig.set_size_inches([5,3])
fig.savefig('figure_5_3.png')

### Part5 Unique values of a column
# Extract the "Sport" column
sports_column = summer_2016_medals["Sport"]

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)

# Automate your visualization
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
