import re

# Luxembourg postcodes are four digits. Some put "L-" in front, but
# this is ignored here.
def is_valid_postcode(pc):
    if re.match('\d{4}$', pc):
        return True
    return False

# Should match one, two and three digits.
def is_valid_partial_postcode(pc):
    if re.match('\d{4}$', pc):
        return True
    return False

