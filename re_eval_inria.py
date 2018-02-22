# -*- coding: utf-8 -*-

import sys
import codecs

file1 = codecs.open('new_results/merging/' + sys.argv[1] + '.txt.dvn.ext.inria.new', encoding='utf-8')
file2 = codecs.open('new_results/merging/' + sys.argv[1] + '.txt.dvn.int.inria.new', encoding='utf-8')

res = []

for line in file1:
	res.append(int(line.split(',')[-1].strip()))

i = 0
for line in file2:
	r = int(line.split(',')[-1].strip())
	if res[i] == 0 and r == 1:
		res[i] == 1
	i += 1

print '%.2f' % (((sum(res)*1.0)/len(res))*100.0)
print sum(res)
print len(res)