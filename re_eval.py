# -*- coding: utf-8 -*-

import sys
import codecs

infile = codecs.open(sys.argv[1], encoding='utf-8')
outfile = codecs.open('new_results/' + sys.argv[1] + '.new', encoding='utf-8', mode='w')

total = 0
correct = 0

for line in infile:
	spl = line.split(':')

	word1 = spl[1].strip()
	word2 = spl[3].strip()[:-1]

	word1 = word1.replace(' ', '').replace(u'ऽ', '')
	word2 = word2.replace(' ', '').replace(u'ऽ', '')

	res = int(word1 == word2)

	outfile.write(line.strip() + ',' + str(res) + '\n')

	total += 1
	correct += res

print '%.2f' % (((correct*1.0)/total)*100.0)
print correct
print total