import sys
sys.path.append('../')
from utils import *
import numpy as np
import re

input_val = read_textfile('input.txt')
test_val = read_textfile('test.txt')


def part1(lines):
	width = len(lines[0])
	total = 0
	number_dict = {}
	sym_idx = set()
	num_idx = 0

	for i in range(len(lines)):
		numbers = re.finditer(r'\d+', lines[i])

		for x in numbers:
			left = x.span()[0] + (i*width)
			right = (x.span()[1]-1) + (i*width)
			all_idx = np.arange(left, right+1)

			around = []
			for idx in all_idx:
				around.append(idx+width)
				around.append(idx-width)

			around.extend(
				[left-1, 
				right+1, 
				left-1+width, 
				left-1-width, 
				right+1+width, 
				right+1-width]
				)
			number_dict[f"{x.group()}_{num_idx}"] = set(around)
			num_idx+=1


		possible_symbols = re.findall(r'[^0-9.]', lines[i])
		possible_symbols = list(set(possible_symbols))
		if '-' in possible_symbols:
			possible_symbols.remove('-')
			possible_symbols.insert(0,'-')
		symbs = f"[{''.join(possible_symbols)}]"

		if len(possible_symbols) > 0:
			symbols = re.finditer(symbs, lines[i])
			sym_idx.update([x.span()[0]+(i*width) for x in symbols])

	
	for key, value in number_dict.items():
		key = key.split('_')[0]
		if len(sym_idx.intersection(value)) > 0:
			total += int(key)

	return total




def part2(lines):
	width = len(lines[0])
	total = 0
	number_dict = {}
	sym_idx = set()
	num_idx = 0

	for i in range(len(lines)):
		numbers = re.finditer(r'\d+', lines[i])

		for x in numbers:
			left = x.span()[0] + (i*width)
			right = (x.span()[1]-1) + (i*width)
			all_idx = np.arange(left, right+1)

			around = []
			for idx in all_idx:
				around.append(idx+width)
				around.append(idx-width)

			around.extend(
				[left-1, 
				right+1, 
				left-1+width, 
				left-1-width, 
				right+1+width, 
				right+1-width]
				)
			number_dict[f"{x.group()}_{num_idx}"] = set(around)
			num_idx+=1


		symbols = re.finditer('[*]', lines[i])
		sym_idx.update([x.span()[0]+(i*width) for x in symbols])

	idx_dict = {}
	for key, value in number_dict.items():
		if len(sym_idx.intersection(value)):
			idx_dict[key] = sym_idx.intersection(value)

	for key1, value1 in idx_dict.items():
		for key2, value2 in idx_dict.items():
			if key1 != key2:
				if len(value1.intersection(value2)) > 0:
					total += (int(key1.split('_')[0]) * int(key2.split('_')[0]))


	return total//2




print(f'Part One: {part1(input_val)}')
print(f'Part Two: {part2(input_val)}')