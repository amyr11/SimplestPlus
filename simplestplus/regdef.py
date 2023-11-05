definitions = {}

definitions['all_alpha'] = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
definitions['digits'] = list('123456789')
definitions['all_digits'] = definitions['digits'] + ['0']

definitions['delim_space'] = definitions['all_alpha'] + ['"']
definitions['delim_indent'] = definitions['all_alpha'] + ['\n']
definitions['delim_newline'] = definitions['all_alpha'] + ['\n', ' ']
definitions['delim_res_words'] = [' ', '\n']
definitions['delim_word'] = definitions['delim_res_words']