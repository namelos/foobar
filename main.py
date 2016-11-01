class Container(object):
    def __init__(self, val):
        self.val = val

def mapContainer(f):
    return lambda container: f(container.val)



"""
Maybe = Some(val) | None
"""

class Some(object):
    def __init__(self, val):
        self.val = val

