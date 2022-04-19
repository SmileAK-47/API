def test(a, *args, **kwargs):
    print(a)
    # print b
    # print c
    print(args)

    print(kwargs)



test(1, 2, 3, d='4', e=5)