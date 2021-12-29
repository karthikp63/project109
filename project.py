import plotly.figure_factory as ff
import pandas as pd
import csv
import pltly.graph_objects as go
import statistics as ss
import random

df =  pd.read_csv("data.csv")
data = df["reading score"].toList()

mean = sum(data) / len(data)
std_deviation = ss.median(data)
median = ss.median(data)
mode = ss.mode(data)

std_deviation_start, std_deviation_end  = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end  = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end  = mean-(3*std_deviation), mean+(3*std_deviation)

fig = ff.create_distplot([data], ['reading scores'], show_hist = false)
fig.add_trace(go.Scatter(x=[mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[std_deviation_start, std_deviation_start], y = [0, 0.17], mode = "lines", name = "FSDS"))
fig.add_trace(go.Scatter(x=[std_deviation_end, std_deviation_end], y = [0, 0.17], mode = "lines", name = "FSDE"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y = [0, 0.17], mode = "lines", name = "SSDS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y = [0, 0.17], mode = "lines", name = "SSDE"))
fig.show()

list1 = [result for result in data if result > std_deviation_start and result < std_deviation_end]
list2 = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list3 = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("the mean of this data is {}".format(mean))
print("the median of this data is {}".format(median))
print("the mdoe of this data is {}".format(mode))
print("the standard deviation of this data is {}".format(std_deviation))
print("{}% of data lies within 1 standard deviation".format(len(list1)*100/len(data)))
print("{}% of data lies within 2 standard deviation".format(len(list2)*100/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(list3)*100/len(data)))