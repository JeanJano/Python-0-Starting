from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
list = []
dict = {}
tuple = ()
set = set()

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found(Fake))
print(NULL_not_found("Brian"))
NULL_not_found(list)
NULL_not_found(dict)
NULL_not_found(tuple)
NULL_not_found(set)
NULL_not_found([1, 2, 3])