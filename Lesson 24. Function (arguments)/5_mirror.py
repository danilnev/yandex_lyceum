def mirror(arr):
    mirrored_part = arr.copy()
    mirrored_part.reverse()  # arr.reverse() изменяла массив, а возвращала None
    # теперь мы копируем массив, а потом его переворачиваем
    arr += mirrored_part
