import csv
import matplotlib.pyplot as plt
import sys

""" example.csv contains the values for the system.

    Example call
    ===========
    
    max_value, rolling_times, rolling_avgs = calculate_rolling_average(time_array, input_array, averaging_period=600)

"""


def load_csv():
    """load the CSV containing the values.

    Returns:
        tuple: first element sampling points, second element values

    """
    time_array = []
    input_array = []
    with open("example.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for index, row in enumerate(reader):
            if index > 0:
                time_array.append(int(float(row[1])))
                input_array.append(int(float(row[2])))

    return time_array, input_array


def calculate_rolling_average(time_array, input_array, averaging_period=600):
    """Summary
    Calculate a rolling average. The output of this function could be second by second,
    or just the same sampled time points as the input,
    depending on how you want to implement your algorithm.

    Args:
        time_array (list): sampling points
        input_array (list): values
        averaging_period (int): (optional) default 10 minutes (600s)

    Returns:
        tuple: Max value of avgs, times, values


    """

    # edge cases
    if averaging_period < 1:
        print("Invalid Averaging Period. Must be 1 or Greater!")
        sys.exit()
    if averaging_period > len(input_array):
        print("Averaging Period Bigger Than Array Size!")
        sys.exit()

    averages = []
    sum = 0

    # Add the first averaging period and divide the sum by the length of the averaging period
    for i in range(averaging_period):
        sum += input_array[i]
    averages.append(sum / averaging_period)

    """
    The following method prevents us from reiterating through the array and recomputing the sum
    It allows us to compute the rolling average in one pass O(n) as opposed to O(n^2) if we were to recompute
    the sum each time.
    """
    # for the remainder of values in the input:
    for i in range(len(input_array) - averaging_period):
        sum -= input_array[i]  # drop the last value
        sum += input_array[i + averaging_period]  # add the next value
        averages.append(sum / averaging_period)

    plt.plot(time_array, input_array)
    plt.plot(time_array[averaging_period - 1 :], averages)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Input")
    plt.title("Graph of Input with Rolling Averages")
    plt.savefig("result")

    # This loop finds the max value in the array
    mymax = averages[0]
    for i in range(len(averages)):
        if averages[i] > mymax:  # if we find a greater value
            mymax = averages[i]  # replace the current max with the greater value

    return mymax, time_array[averaging_period - 1 :], averages


time_array, input_array = load_csv()
max_value, rolling_times, rolling_avgs = calculate_rolling_average(
    time_array, input_array, averaging_period=300
)
