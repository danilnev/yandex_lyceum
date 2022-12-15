num = int(input())
views = dict()
string = input().split()
views[string[0]] = [string[-1], []]
main_post = string[0]
for i in range(num - 1):
    string = input().split()
    repost = string[0]
    post = string[4][:-1]
    view = string[-1]
    array = [post]
    for poster in views[post][1]:
        array.append(poster)
    views[repost] = [view, array]
    for poster in views[repost][1]:
        views[poster][0] = str(int(views[poster][0]) + int(view))
for value in views.values():
    print(value[0])
