corpuses=['astadhayi', 'gita', 'gita_avg', 'gold', 'uoh']
#corpuses=['astadhayi', 'gita', 'gold', 'uoh']
tools=['.inria', '.inria.fil', '.jnu', '.sam', '.sam.fil']

for corpus in corpuses:
	file_name = corpus+'.txt.dvn'
	for tool in tools:
		out = open(corpus+'/'+file_name+tool+'.cor','w')
		for line in open(corpus+'/'+file_name+tool).readlines():
			line = line.strip()
			if line.endswith('1'):
				out.write(line+'\n')
		out.close()