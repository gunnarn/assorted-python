def txt2dict(filename, delimiter = '\t'):

    '''
        Takes a tab delimited txt file (or a csv file) and turns it into a 
        dictionary of dictionaries. The first column becomes the first key,
        and subsequent columns are added to the main key as a dictionary.

        filename: string
            The name of the file to open.

        delimiter: string
            The delimiter of the file, defaults to tab.
    '''

    with open(filename, 'r') as f:
        data = f.readlines()
        sub_keys = data.pop(0).split()[1:]
        main = {}
        for row in data:
            r = row.split(delimiter)
            main[r[0]] = {a: b.decode('utf-8') for a, b in zip(sub_keys, r[1:])}

    return(main)