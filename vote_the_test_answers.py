"""
use as follows:

`python vote_the_test_answers.py model_predictions.txt`

returns the percentage of suitable answers
"""


import sys
import re

def vote(filename):
	answer = [0., 0.]

	with open(filename, 'r') as predictions:
		for line in predictions.readlines():
			if re.match('^Q: .*', line):
				answer[0] += 1
				print(line)

			elif re.match('^A: .*', line):
				print(line)
				try:
					mark = input("Please enter 1 (bad answer) or 2 (good answer): ")
					answer[1] += float(mark) - 1
				except ValueError:
					mark = input("Please enter 1 (bad answer) or 2 (good answer): ")
					answer[1] += float(mark) - 1

			else:
				print()

		return answer[1] / answer[0]

if __name__ == '__main__':
	#print(sys.argv)
	try:
		print(vote(sys.argv[1]))
	except KeyboardInterrupt:
		sys.exit(0)
