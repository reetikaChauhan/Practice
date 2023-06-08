def alt_longest_common_prefix(strs: list) -> str:
    res = ''
    print(list(zip(*strs)))
    # zip *strs zips each element separately - this loop automatically stops after 
    # the shortest length string is exhausted.
    for vals in zip(*strs):
        print('vals',vals)
        char = vals[0]
        print('char',char)
        if all(val == char for val in vals[1:]): # check for character equality 
            res += char
            print('res',res)
        else:
            break
    return res
print(alt_longest_common_prefix(["flower","flow","flight"]))
