def title_case(title, minor_words=''):
    if len(title) == 0:
        return title
    else:
        title = title.split()
        minor_words = minor_words.split()
        new_list = []
        some_list = []
        for i in minor_words:
            i = i.capitalize()
            some_list.append(i)
        for i in title:
            i = i.capitalize()
            new_list.append(i)
        for i in new_list:
            if i in some_list:
                new_list[new_list.index(i)] = i.lower()
        counter = new_list[0]
        counter = counter.capitalize()
        new_list.insert(0, counter)
        counter_1 = new_list[1]
        new_list.remove(counter_1)
        return ' '.join(new_list)


print(title_case('a clash of KINGS', 'a an the of'))
