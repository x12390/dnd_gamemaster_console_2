class MultiValueDict(dict):
    """An extended dictionary, that does not overwrite values for the same key. It creates an array of all values instead."""
    def __setitem__(self, key, value):
        if type(value) is str:
            listval = []
            listval.append(value)

        if key in self:
            listval = []
            old_values = list(self[key])
            for i in old_values:
                listval.append(i)
            listval.append(value)

        super().__setitem__(key, listval)


# dict = MultiValueDict()
# dict["1"] = "1Value1"
# dict["1"] = "1Value2"
# dict["1"] = "1Value3"
# dict["2"] = "2Value1"
# dict["2"] = "2Value2"
# dict["2"] = "2Value3"
# dict["2"] = "2Value4"
# dict["3"] = "3Value1"
# print(dict)