# Different data loading methods

# Imports
import numpy
import csv
import matplotlib.pyplot as plt

# Load in data
with open('Stock Valuation 23_12_18.csv', newline='') as csvfile:
    data_in = list(csv.reader(csvfile))

# Stack data
ShoeData = numpy.column_stack(data_in)
ShoeName = ShoeData[0, 1:]
ShoeName = ShoeName.tolist()
Type = ShoeData[1, 1:]
price = list(map(float, ShoeData[2, 1:]))
MarkUp = list(map(float, ShoeData[3, 1:]))
Wholesale = list(map(float, ShoeData[4, 1:]))
Retail = list(map(float, ShoeData[5, 1:]))
sizefrom = list(map(float, ShoeData[6, 1:]))
ShoeData[7, 1] = 5
sizeto = list(map(float, ShoeData[7, 1:]))
pairs = list(map(float, ShoeData[8, 1:]))
allocation = list(map(float, ShoeData[9, 1:]))
GrandTotal = list(map(float, ShoeData[10, 1:]))
Value = list(map(float, ShoeData[11, 1:]))
TotalShoeValue = list(map(float, ShoeData[12, 1:]))
# Format Plots
plt.rcParams['lines.linewidth'] = 0.5
# Plot data 1
plt.subplot(221)
plt.plot(ShoeName, price, 'r-', label='Price')
plt.plot(ShoeName, Wholesale, 'b-', label='Wholesale')
plt.plot(ShoeName, Retail, 'g-', label='Retail')
plt.ylabel('Price (£)')
plt.xlabel('Shoe Name')
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)
plt.title('Stock Valuation')
plt.legend(loc='upper left')

# Plot data 2
plt.subplot(222)
plt.plot(ShoeName, sizefrom, 'r-', label='Size From')
plt.plot(ShoeName, sizeto, 'g-', label='Size to')
plt.ylabel('Shoe Size')
plt.xlabel('Shoe Name')
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)
plt.legend(loc='upper left')

# Plot data 3
plt.subplot(223)
plt.plot(ShoeName, pairs, 'r-', label='Pairs')
plt.plot(ShoeName, allocation, 'g-', label='Allocation')
plt.plot(ShoeName, GrandTotal, 'b-', label='Grand Total')
plt.plot([ShoeName[0], ShoeName[len(ShoeName)-1]], [1000, 1000], 'r--')
plt.ylabel('No. of Pairs')
plt.xlabel('Shoe Name')
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=90)
plt.legend(loc='upper left')
plt.show()


a, b = 0, 1
while True:
    a, b = a, a + b
    if b > 20:
        break
    print(a)