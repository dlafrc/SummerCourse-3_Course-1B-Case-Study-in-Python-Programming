import statistics

# COVID-19 infection data over 20 days
infection_numbers = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

# Calculate statistics
minimum = min(infection_numbers)
maximum = max(infection_numbers)
range_ = maximum - minimum
mean = statistics.mean(infection_numbers)
median = statistics.median(infection_numbers)
variance = statistics.variance(infection_numbers)
stdev = statistics.stdev(infection_numbers)

# Display statistics
print("COVID-19 Infection Statistics:")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range_}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {stdev}")
