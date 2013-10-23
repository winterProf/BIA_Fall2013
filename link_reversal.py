# input:
# quartermass_ii,bbc_television
# quartermass_ii,wuthering_heights
# lucky_jim,bbc_television


def mapper(input):
    return ','.join(input.split(',').reverse())



def reducer(key, values):
    return key + '\t' + ','.join(values)




fh= open('sample.txt', 'r')
key_values = {}
output = ''
for line in fh:
    key, value = mapper(line)
    if key in key_values:
        key_values[key].append(value)
    else:
        key_values[key] = [value]

for key, values in key_values.iteritems():
    output += reducer(key, values) + '\n'

print output
