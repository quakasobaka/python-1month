def thesaurus(*args):
    out_list = {}
    for name in args:
        if out_list.get(name[0]):
            out_list[name[0]].append(name)
        else:
            out_list[name[0]] = [name]
    return out_list