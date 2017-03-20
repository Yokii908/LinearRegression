import matplotlib.pyplot as plt
import numpy as np

def total_sum_of_squares(values, average):
	total_sum = 0
	for y_i in values:
		total_sum += pow(y_i - average, 2)
	return total_sum

def get_basic_leading_coefficient(values, average):
	delta_y = values[len(values) - 1] - values[0]
	delta_x = len(values) - 1
	return delta_y / delta_x

def regression_sum_of_squares(a, b, average, size_set):
	total_sum = 0
	for x in range(size_set):
		total_sum += pow((a * x + b) - average, 2)
	return total_sum

def residual_sum_of_squares(a, b, values):
	total_sum = 0
	for x, y_i in zip(range(len(values)), values):
		total_sum += pow(y_i - (a * x + b), 2)
	return total_sum

def display_values_on_graph(fig, average, tot, reg, res, r_squared):
	ax = fig.add_subplot(111)
	ax.text(0, 19, r'average = %f' % average)
	ax.text(0, 18, r'total sum of squares = %f' % tot)
	ax.text(0, 17, r'regression sum of squares = %f' % reg)
	ax.text(0, 16, r'residual sum of squares = %f' % res)
	ax.text(0, 15, r'current r_squared = %f' % r_squared)

def main():
	fig = plt.figure()
	fig.suptitle('Linear Regression', fontsize=14, fontweight='bold')
	values = np.array([1,2,4,4,5,7,8,8,9,11])
	average = sum(values) / len(values)
	basic_a = get_basic_leading_coefficient(values, average)
	basic_b = values[0]
	x = np.arange(len(values))

	plt.axis([0, 10, 0, 20])
	plt.plot(x, values, 'ro')
	plt.plot(x, x * 0 + average)
	plt.plot(x, x * basic_a + basic_b)

	tot = total_sum_of_squares(values, average)
	reg = regression_sum_of_squares(basic_a, basic_b, average, len(values))
	res = residual_sum_of_squares(basic_a, basic_b, values)
	r_squared = 1 - (res / tot)
	display_values_on_graph(fig, average, tot, reg, res, r_squared)
	print(plt.get_backend())
	plt.show()

if __name__ == '__main__':
	main()