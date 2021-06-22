import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("StudentsPerformance.csv")
listMath = df["math score"].tolist()
listRead = df["reading score"].tolist()

mean_math = statistics.mean(listMath)
mean_reading = statistics.mean(listRead)

median_math = statistics.median(listMath)
median_reading = statistics.median(listRead)

mode_math = statistics.mode(listMath)
mode_reading = statistics.mode(listRead)

stdev_math = statistics.stdev(listMath)
stdev_reading = statistics.stdev(listRead)

print("Mean, median, mode of math scores are {},{}, and {}".format(mean_math, median_math, mode_math))
print("Mean, median, mode of reading scores are {},{}, and {}".format(mean_reading, median_reading, mode_reading))
print("Standard deviation of math scores are ", stdev_math)
print("Standard deviation of reading scores are ", stdev_reading)

first_stdev_start, first_stdev_end = mean_math - stdev_math, mean_math + stdev_math
second_stdev_start, second_stdev_end = mean_math - (2*stdev_math), mean_math + (2*stdev_math)
third_stdev_start, third_stdev_end = mean_math - (3*stdev_math), mean_math + (3*stdev_math)

firstStDevMathList = [result for result in listMath if first_stdev_start < result < first_stdev_end]
first_percentage = len(firstStDevMathList) * 100 / len(listMath)
print("Percentage between the first standard deviations in math is ", first_percentage)

secondStDevMathList = [result for result in listMath if second_stdev_start < result < second_stdev_end]
second_percentage = len(secondStDevMathList) * 100 / len(listMath)
print("Percentage between the second standard deviations in math is ", second_percentage)

thirdStDevMathList = [result for result in listMath if third_stdev_start < result < third_stdev_end]
third_percentage = len(thirdStDevMathList) * 100 / len(listMath)
print("Percentage between the third standard deviations in math is ", third_percentage)

fourth_stdev_start, fourth_stdev_end = mean_reading - stdev_reading, mean_reading + stdev_reading
fifth_stdev_start, fifth_stdev_end = mean_reading - (2*stdev_reading), mean_reading + (2*stdev_reading)
sixth_stdev_start, sixth_stdev_end = mean_reading - (3*stdev_reading), mean_reading + (3*stdev_reading)

firstStDevReadingList = [result for result in listRead if fourth_stdev_start < result < fourth_stdev_end]
fourth_percentage = len(firstStDevReadingList) * 100 / len(listRead)
print("Percentage between the first standard deviations in reading is ", fourth_percentage)

secondStDevReadingList = [result for result in listRead if fifth_stdev_start < result < fifth_stdev_end]
fifth_percentage = len(secondStDevReadingList) * 100 / len(listRead)
print("Percentage between the second standard deviations in reading is ", fifth_percentage)

thirdStDevReadingList = [result for result in listRead if sixth_stdev_start < result < sixth_stdev_end]
sixth_percentage = len(thirdStDevReadingList) * 100 / len(listRead)
print("Percentage between the third standard deviations in reading is ", sixth_percentage)