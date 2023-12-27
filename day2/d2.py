import sys
sys.path.append('../')
from utils import *
import re


input_val = read_textfile('input.txt')
test_val = read_textfile('test.txt')


def part1(lines):
	total = 0
	for line in lines:
		idx, game = line.split(':')
		possible = True
		
		for grab in re.split('; |,', game):
			num, color = grab.split()
			if color == 'red' and int(num) > 12:
				possible = False
				break
			elif color == 'green' and int(num) > 13:
				possible = False
				break
			elif color == 'blue' and int(num) > 14:
				possible = False
				break

		if possible:
			name, val = idx.split()
			total += int(val)

	return total


def part2(lines):
	total = 0
	for line in lines:
		idx, game = line.split(':')
		line_dict = {
			'red': 0,
			'green': 0,
			'blue': 0
		}
		for grab in re.split('; |,', game):
			num, color = grab.split()
			if int(num) > line_dict[color]:
				line_dict[color] = int(num)

		total += line_dict['red'] * line_dict['green'] * line_dict['blue']

	return total





print(f'Part One: {part1(input_val)}')
print(f'Part Two: {part2(input_val)}')