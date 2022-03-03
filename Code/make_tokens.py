
from pprint import pprint

def get_tokens(file, debug=False):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    
    dumb_lines = []
    on_line = False
    for line in lines:
        if on_line:
            dumb_lines.append(line)
            on_line = False
        if line == 'DUMBLEDORE':
            on_line = True
    
    ret_tokens = []
    for line in dumb_lines:
        words = line.split()
        for i in range(len(words)):
            if i == len(words)-1:
                ret_tokens.append(words[i] + '.')
            else:
                ret_tokens.append(words[i])
    
    if debug is True:
        pprint(dumb_lines)
        
    return ret_tokens

if __name__ == '__main__':
    print('Start')
    tokens = get_tokens('data/script.txt')
    # pprint(tokens)s