import sys
sys.path.append('../')
from utils import *
import re


input_val = read_textfile('input.txt')
test_val = read_textfile('test.txt')

def part1(input1):
	total = 0

	for line in input1:
		line = ''.join(c for c in line if c.isdigit())
		total += int(line[0]+line[-1])

	return total



def part2(input1, replace_dict):
	total = 0

	for line in input1:
		for old, new in replace_dict.items():
			line = line.replace(old, new)
		line = ''.join(c for c in line if c.isdigit())
		total += int(line[0]+line[-1])

	return total
		

replace_dict = {
	'one': 'o1e',
	'two': 't2o',
	'three': 't3e',
	'four': 'f4r',
	'five': 'f5e',
	'six': 's6x',
	'seven': 's7n',
	'eight': 'e8t',
	'nine': 'n9e',
}
print(f'Part One: {part1(input_val)}')
print(f'Part Two: {part2(input_val, replace_dict)}')