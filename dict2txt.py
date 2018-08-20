def dict2txt(data, filename, delimiter = '\t'):
    '''
        Takes a dictionary of dictionaries and prints it as a txt file.

        data: dictionary
            The dictionary to be used. Should be a dictionary of dictionaries.

        filename: string
            The name of the file to be created. Include '.txt'.

        delimiter: string
            Optional. The delimiter to use. Defaults to tab.
    '''
    with open(filename, 'w') as f:
        f.write(delimiter.join(['col'] + data[data.keys()[0]].keys()) + '\n')
        for row in data.keys():
            r = [row]
            for col in data[row].keys():
                r.append(data[row][col])
            f.write(delimiter.join(r).encode('utf-8') + '\n')
    f.close()
