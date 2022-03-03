import sys

BAD_CHARS = '''!()[]—-{};:'"\…,<>./?@#$%‼^&*_~”„“‥\n'''
def read_file(dir):
    file = open(dir, 'r', encoding="UTF-8")
    data_list = []
    for line in file:
        buffer = ''
        for char in line:
            if char not in BAD_CHARS:
                buffer += char
        data_list.extend(buffer.lower().split())
    file.close()
    return data_list

def handle_args():
    settings = {
        'source_text': '',
        'debug': False,
    }

    #inputs
    args = sys.argv[1:]
    if len(args) > 0:
        #debug mode
        settings['debug'] = '-d' in args

        if '-f' in args:
            #using a file 
            file = args[args.index('-f') + 1]
            settings['source_text'] = read_file(file)
            return settings

        if '-s' in args:
            args.remove('-s')
            arg_list = []
            for arg in args:
                arg_list.append(arg)
            final_list = []
            for word in arg_list:
                buffer = ''
                for char in word:
                    if char not in BAD_CHARS:
                        buffer += char
                final_list.append(buffer)
            
            settings['source_text'] = final_list
            return settings

    return settings
