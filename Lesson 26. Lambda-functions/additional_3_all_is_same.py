def same_by(charac, objs):
    if not objs:
        return True
    results = list(map(charac, objs))
    if min(results) == max(results):
        return True
    return False


# values = [1, 2, 3, 4]
# if same_by(lambda x: x % 2, []):
#     print('same')
# else:
#     print('different')
