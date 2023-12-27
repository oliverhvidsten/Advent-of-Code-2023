import sys
sys.path.append('../')
from utils import *
import numpy as np
import re

input_val = read_textfile('input.txt')
test_val = read_textfile('test.txt')

def part1(lines):
	total = 0
	for line in lines:
		card, winnings, numbers = re.split('[|:]', line)
		matches = len(set(winnings.split()).intersection(set(numbers.split())))
		if matches:
			total += 2**(matches-1)
	return total

def part2(lines):
	total = len(lines)
	card_dict = {}
	for i in range(len(lines)):
		card_dict[i+1] = 1
	for i in range(len(lines)):
		card, winnings, numbers = re.split('[|:]', lines[i])
		matches = len(set(winnings.split()).intersection(set(numbers.split())))
		if matches:
			for new_card in range(matches):
				card_dict[new_card+1+i+1] += card_dict[i+1]
			total += matches * card_dict[i+1]
	return total


print(f'Part One: {part1(input_val)}')
print(f'Part Two: {part2(input_val)}')