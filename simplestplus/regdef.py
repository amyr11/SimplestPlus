definitions = {}

definitions['all_alpha'] = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
definitions['digits'] = list('123456789')
definitions['all_digits'] = definitions['digits'] + ['0']
definitions['delim_1'] = [' ', '\n']
definitions['delim_2'] = definitions['all_digits'] + definitions['delim_1'] + definitions['all_alpha'] + ['"']
definitions['special_chars'] = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')