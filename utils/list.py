def chunk_list(target_list, size):
    for n in range(0, len(target_list), size):
        yield target_list[n:size + n]


