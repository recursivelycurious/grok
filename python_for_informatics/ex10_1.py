def check_for_exit(command):
	if command.lower() == 'quit()' or command.lower() == 'exit()':
		exit()

emails = dict()
error_check = 0
while True:
	filename = raw_input('Enter a filename: ')
	check_for_exit(filename)
	if filename == '':
		filename = 'mbox-short.txt'
		print 'Using default: ', filename
	try:
		fhand = open(filename)
		break
	except:
		print 'Please enter a valid filename: '

for line in fhand:
	words = line.split()
	if len(words) < 3 or line.find('From ', 0) != 0 or line.count('@') != 1 : continue
	error_check = error_check + 1
	emails[words[1]] = emails.get(words[1],0) +1 # same as 9.2, looks at email address rather than day of week
fhand.close()

lst = list()
for email, count in emails.items():
	lst.append((count, email))

lst.sort(reverse=True)

for count, email in lst[:1]:
	print 'Person sending most email:', email, count

error_check = error_check - sum(emails.values())
if error_check > 0: print 'Lines that passeed the guardian logic in excess of total count:', error_check
