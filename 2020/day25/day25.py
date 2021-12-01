
card_test = 5764801
door_test = 17807724

card_public = 5290733
door_public = 15231938

def get_loop_size(key):
    n = 7
    i = 1
    while n != key:
        n *= 7
        n = n % 20201227
        i += 1
        
    return i

def get_encryption_key(loop_num, subject_num):
    n = 1
    for _ in range(loop_num):
        n *= subject_num
        n = n % 20201227
    return n



card_loop = get_loop_size(card_public)
door_loop = get_loop_size(door_public)

print(get_encryption_key(card_loop, door_public))
# print(get_encryption_key(door_loop, card_public))