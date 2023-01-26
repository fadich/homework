import re


def validation(sample):

    pattern1 = r"(\-\d+|\d+) (\+|\-|\*|\/|\**|\//) (\-\d+|\d+)"
    pattern2 = r"abs (\-\d+|\d+)"
    pattern3 = r"\-\d+|\d+"

    match1 = re.fullmatch(pattern1, sample)
    match2 = re.fullmatch(pattern2, sample)
    match3 = re.fullmatch(pattern3, sample)

    if match1 or match2 or match3 or sample == "":
        return True
    else:
        return False
