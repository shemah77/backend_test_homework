

if len(alien_set) == window_sum:
    i_slice += 1
    max_len_sub_ok = len(alien_set)
else:
    if len(alien_set) > max_len_sub:
        max_len_sub = len(alien_set)
    break