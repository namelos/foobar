class Container(object):
    def __init__(self, val):
        self.val = val

def mapContainer(f):
    return lambda container: f(container.val)

"""
Maybe = Some(val) | None
"""

"""
Some value
"""
class Some(object):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "Some %s" % self.val

"""
map_maybe :: (a -> b) -> Maybe a -> Maybe b
"""
def map_maybe(f):
    def apply(maybe):
        if maybe is None:
            return None
        else:
            return Some(f(maybe.val))
    return apply