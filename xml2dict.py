
def xml2dict(xml):
    """ Converts an XML document to a dictionary. Keys based on the tag names. XML file has to 
        begin with <root>.

        Options:

        xml: string
            Local xml file.
    """

    import xml.etree.ElementTree as et

    tree = et.parse(xml)
    main_dict = dict()

    for elem in list(tree.getroot()):
        sub_dict = dict()
        for i in elem:
            sub_dict[i.attrib[i.attrib.keys()[0]]] = i.text.strip()

        main_dict[elem.attrib[elem.attrib.keys()[0]]] = sub_dict
    return(main_dict)
