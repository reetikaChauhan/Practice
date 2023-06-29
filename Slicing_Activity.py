

def exchange_first_last(seq):
    if len(seq) < 2:
        return seq
    return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq):
    return seq[::2]

def remove_first_last_four(seq):
    return seq[4:-4:2]

def reverse_sequence(seq):
    return seq[::-1]

def rearrange_thirds(seq):
    third = len(seq) // 3
    return seq[-third:] + seq[:third] + seq[third:-third]


if __name__ == "__main__":
    l=(1,2,3,4,5,6)
    print(reverse_sequence(l))
    print(remove_every_other(l))

    

    




    
