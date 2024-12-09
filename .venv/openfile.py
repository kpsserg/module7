from pprint import pprint

name = 'sample.txt'
file = open(name, 'a')


file.write('\nHello world')
file.close()


print('hi')
