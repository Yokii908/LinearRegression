import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


def setup_window(t1, t2):
    fig = plt.figure()
    fig.suptitle('Linear Regression', fontsize=14, fontweight='bold')
    plt.axis([min(t1), max(t1), min(t2) - 1, max(t2) + 1])
    return fig


def draw_set_and_average(x, values, average_y, basic_a, basic_b):
    plt.plot(x, values, 'ro')
    plt.plot(x, x * 0 + average_y)

def draw_fitting_line(x, slop, y_intercept):
    plt.plot(x, x * slop + y_intercept)

def get_average(values):
    return sum(values) / len(values)

def get_best_line_slop(x, values, average_x, average_y):
    num = 0
    den = 0
    for x_i, y_i in zip(x, values):
        num += (x_i - average_x) * (y_i - average_y)
        den += pow((x_i - average_x), 2)
    return num / den

def get_best_line_y_intercept(average_x, average_y, slop):
    return average_y - slop * average_x


def get_basic_leading_coefficient(values, average):
    delta_y = values[len(values) - 1] - values[0]
    print(values[0])
    print(values[len(values) - 1])
    delta_x = len(values)
    print(delta_y/delta_x)
    return delta_y / delta_x


def total_sum_of_squares(values, average):
    total_sum = 0
    for y_i in values:
        total_sum += pow(y_i - average, 2)
    return total_sum


def regression_sum_of_squares(x, a, b, average):
    total_sum = 0
    for x_i in x:
        total_sum += pow((a * x_i + b) - average, 2)
    return total_sum


def residual_sum_of_squares(a, b, x, values):
    total_sum = 0
    for x_i, y_i in zip(x, values):
        total_sum += pow(y_i - (a * x_i + b), 2)
    return total_sum


def display_basic_values_on_graph(fig, average, tot, reg, res, r_squared):
    ax = fig.add_subplot(111)
    ax.text(0.2, 19, r'average = %f' % average)
    ax.text(0.2, 18, r'total sum of squares = %f' % tot)
    ax.text(0.2, 17, r'regression sum of squares = %f' % reg)
    ax.text(0.2, 16, r'residual sum of squares = %f' % res)
    ax.text(0.2, 15, r'current r_squared = %f' % r_squared)

def display_best_values_on_graph(fig, reg, res, r_squared):
    ax = fig.add_subplot(111)
    ax.text(3.5, 17, r'| best regression sum of squares = %f' % reg)
    ax.text(3.5, 16, r'| best residual sum of squares = %f' % res)
    ax.text(3.5, 15, r'| best current r_squared = %f' % r_squared)

def main():
    data_set = [[8, 3], [2, 10], [11, 3], [6, 6], [5, 8], [4, 12], [12, 1], [9, 4], [6, 9], [1, 14]]
    sorted_data_set = sorted(data_set, key = lambda x: (x[0]))
    print(sorted_data_set)

    t1 = [ele[0] for ele in sorted_data_set]
    t2 = [ele[1] for ele in sorted_data_set]

    x = np.array(t1)
    values = np.array(t2)
    fig = setup_window(t1, t2)
    average_y = get_average(values)
    average_x = get_average(x)

    basic_a = get_basic_leading_coefficient(values, average_y)
    basic_b = t2[0]

    print(basic_a)
    print(basic_b)

    best_a = get_best_line_slop(x, values, average_x, average_y)
    best_b = get_best_line_y_intercept(average_x, average_y, best_a)

    draw_set_and_average(x, values, average_y, basic_a, basic_b)

    draw_fitting_line(x, basic_a, basic_b)
    draw_fitting_line(x, best_a, best_b)

    tot = total_sum_of_squares(values, average_y)
    reg = regression_sum_of_squares(x, basic_a, basic_b, average_y)
    res = residual_sum_of_squares(basic_a, basic_b, x, values)
    r_squared = 1 - (res / tot)

    best_reg = regression_sum_of_squares(x, best_a, best_b, average_y)
    best_res = residual_sum_of_squares(best_a, best_b, x, values)
    best_r_squared = 1 - (best_res / best_reg)

    display_basic_values_on_graph(fig, average_y, tot, reg, res, r_squared)
    display_best_values_on_graph(fig, best_reg, best_res, best_r_squared)

    axes = plt.axis()
    plt.xlim( [axes[0], axes[1]])
    plt.ylim( [axes[2], axes[3]])

    plt.show()

if __name__ == '__main__':
    main()
