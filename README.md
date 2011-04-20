BFList is a extension of Python's standard list with some useful functional methods (map, filter, reduce, etc) on the instance objects.

# Examples

    >>> l = BFList([1, 2, 3])
    >>> l.reduceLeft(lambda a, b: a + b)
    6
    >>> l.foldLeft(lambda a, b: a + b, -1)
    5
    >>> l.filter(lambda a: a % 2 == 0)
    [2]
    >>> l.foreach(lambda a: sys.stdout.write(str(a)))
    123
    >>> l.reduceRight(lambda a, b: a - b)
    0