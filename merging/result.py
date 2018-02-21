import sys

def ast_process(file):	
	jnuMap = {}
	inriaMap = {}
	inriaFilMap = {}
	samMap = {}
	samFilMap = {}
	out = open(file+'.fin','w')
	for line in open(file+'.jnu').readlines():
		line = line.strip().split(':')
		print line[0], line[7]
		jnuMap[line[0]] = line[7]
	for line in open(file+'.ext.inria').readlines():
		line = line.strip().split(':')
		inriaMap[line[0]] = line[7]
	for line in open(file+'.int.inria').readlines():
		line = line.strip().split(':')
		inriaFilMap[line[0]] = line[7]
	for line in open(file+'.uoh').readlines():
		line = line.strip().split(':')
		samMap[line[0]] = line[7]
		
	for line in open(file).readlines():
		lineArr = line.strip().split(',')[0].split(':')
		out.write(line.strip())
		print lineArr[0]
		if jnuMap.has_key(lineArr[0]):
			out.write(','+jnuMap[lineArr[0]])
		else:
			out.write(',');
		if inriaMap.has_key(lineArr[0]):
			out.write(','+inriaMap[lineArr[0]])
		else:
			out.write(',');
		if inriaFilMap.has_key(lineArr[0]):
			out.write(','+inriaFilMap[lineArr[0]])
		else:
			out.write(',');
		if samMap.has_key(lineArr[0]):
			out.write(','+samMap[lineArr[0]])
		else:
			out.write(',');
		out.write('\n')
	out.close()

def process(file):	
	jnuMap = {}
	inriaMap = {}
	inriaFilMap = {}
	samMap = {}
	samFilMap = {}
	out = open(file+'.fin','w')
	for line in open(file+'.jnu').readlines():
		line = line.strip().split(':')
		print line[0], line[5]
		jnuMap[line[0]] = line[5]
	for line in open(file+'.ext.inria').readlines():
		line = line.strip().split(':')
		inriaMap[line[0]] = line[5]
	for line in open(file+'.int.inria').readlines():
		line = line.strip().split(':')
		inriaFilMap[line[0]] = line[5]
	for line in open(file+'.uoh').readlines():
		line = line.strip().split(':')
		samMap[line[0]] = line[5]
		
	for line in open(file).readlines():
		lineArr = line.strip().split(',')
		out.write(line.strip())
		if jnuMap.has_key(lineArr[0]):
			out.write(','+jnuMap[lineArr[0]])
		else:
			out.write(',');
		if inriaMap.has_key(lineArr[0]):
			out.write(','+inriaMap[lineArr[0]])
		else:
			out.write(',');
		if inriaFilMap.has_key(lineArr[0]):
			out.write(','+inriaFilMap[lineArr[0]])
		else:
			out.write(',');
		if samMap.has_key(lineArr[0]):
			out.write(','+samMap[lineArr[0]])
		else:
			out.write(',');
		out.write('\n')
	out.close()
def main():
	files=['gita.txt.dvn', 'gita_avg.txt.dvn', 'gold.txt.dvn', 'uoh.txt.dvn']
	#path = sys.argv[1]
	for path in files:
		process(path)
	ast_process('astadhayi.txt.dvn')

if __name__ =="__main__":
    main()
