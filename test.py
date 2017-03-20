import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


def setup_window(t1, t2):
    fig = plt.figure()
    fig.suptitle('Linear Regression', fontsize=14, fontweight='bold')
    plt.axis([min(t1), max(t1), min(t2) - 1, max(t2) + 1])
    axes = plt.axis()
    plt.xlim( [axes[0], axes[1]])
    plt.ylim( [axes[2], axes[3]])
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


def get_basic_leading_coefficient(data_set):
    delta_y = data_set[len(data_set) - 1][1] - data_set[0][1]
    delta_x = data_set[len(data_set) - 1][0] - data_set[0][0]
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
    ax.text(1, 4, r'average = %f' % average, fontsize=5)
    ax.text(1, 3, r'total sum of squares = %f' % tot, fontsize=5)
    ax.text(1, 2, r'regression sum of squares = %f' % reg, fontsize=5)
    ax.text(1, 1, r'residual sum of squares = %f' % res, fontsize=5)
    ax.text(1, 0, r'current r_squared = %f' % r_squared, fontsize=5)


def display_best_values_on_graph(fig, reg, res, r_squared):
    ax = fig.add_subplot(111)
    ax.text(4.5, 2, r'| best regression sum of squares = %f' % reg, fontsize=5)
    ax.text(4.5, 1, r'| best residual sum of squares = %f' % res, fontsize=5)
    ax.text(4.5, 0, r'| best current r_squared = %f' % r_squared, fontsize=5)


def get_basic_y_intercept(data_set, basic_leading_coeff):
    return data_set[0][1] - data_set[0][0] * basic_leading_coeff


def main():
    #send nudes
    #  hardcoded dataset values
    data_set = [[8, 3], [2, 10], [11, 3], [6, 6], [5, 8], [4, 12], [12, 1], [9, 4], [6, 9], [1, 14]]

    #  sorting data based on X values
    sorted_data_set = sorted(data_set, key = lambda x: (x[0]))
    print(sorted_data_set)

    #  getting X values and Y values in two differents arrays
    t1 = [ele[0] for ele in sorted_data_set]
    t2 = [ele[1] for ele in sorted_data_set]

    x = np.array(t1)
    values = np.array(t2)

    #  setting title and axis based on data max / min values
    fig = setup_window(t1, t2)

    average_y = get_average(values)
    average_x = get_average(x)

    #  we're creating a first prediction line based on the first and last value of our dataset
    basic_leading_coeff = get_basic_leading_coefficient(sorted_data_set)
    basic_y_intercept = get_basic_y_intercept(sorted_data_set, basic_leading_coeff)
    #basic_y_intercept = t2[0]

    #  drawing dots for each values and y-average line
    draw_set_and_average(x, values, average_y, basic_leading_coeff, basic_y_intercept)

    print(basic_leading_coeff)
    print(basic_y_intercept)

    #  now we're creating a prediction line based on linear regression model using least squares method
    best_leading_coeff = get_best_line_slop(x, values, average_x, average_y)
    best_y_intercept = get_best_line_y_intercept(average_x, average_y, best_leading_coeff)

    #  drawing our two previous prediction lines
    draw_fitting_line(x, basic_leading_coeff, basic_y_intercept)
    draw_fitting_line(x, best_leading_coeff, best_y_intercept)

    #  calculating sum of squares formulas we need to find r_squared aka "coefficient of determination"
    #  first for our first prediction line
    basic_tot = total_sum_of_squares(values, average_y)
    basic_reg = regression_sum_of_squares(x, basic_leading_coeff, basic_y_intercept, average_y)
    basic_res = residual_sum_of_squares(basic_leading_coeff, basic_y_intercept, x, values)
    basic_r_squared = 1 - (basic_res / basic_tot)

    #  then for our best prediction we got from real maths
    best_reg = regression_sum_of_squares(x, best_leading_coeff, best_y_intercept, average_y)
    best_res = residual_sum_of_squares(best_leading_coeff, best_y_intercept, x, values)
    best_r_squared = 1 - (best_res / best_reg)

    #  writing values somewhere on our graph so we can see the difference between our two lines
    display_basic_values_on_graph(fig, average_y, basic_tot, basic_reg, basic_res, basic_r_squared)
    display_best_values_on_graph(fig, best_reg, best_res, best_r_squared)

    plt.show()

if __name__ == '__main__':
    main()
