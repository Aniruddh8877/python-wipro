import statistics

dates = [1, 2, 2, 3, 4, 5, 5, 5, 6]

print("Dates:", dates)

mean_date = statistics.mean(dates)
median_date = statistics.median(dates)
mode_date = statistics.mode(dates)
variance_date = statistics.variance(dates)
stdev_date = statistics.stdev(dates)

print("Mean:", mean_date)
print("Median:", median_date)
print("Mode:", mode_date)
print("Variance:", variance_date)
print("Standard Deviation:", stdev_date)
