def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
        return result
    students = [[1,'Jeanney', 'V'],[2,'Desta', 'V']]
    print("\nOriginal list of lists:")
    print(students)
    print('\nConverted lists to a dictionary')
    print(test(students))
