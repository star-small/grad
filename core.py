class Vector:
    def __init__(self, val):
        self.val = val

    def __add__(self, Vec2):
        return Vector([self.val[i] + Vec2.val[i] for i in range(len(Vec2.val))])

    def __repr__(self):
        return f"{self.val}"
