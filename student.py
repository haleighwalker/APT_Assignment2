# Part 1, student class definition with __str__, __lt__,
# __hash__, and __eq__ implemented

class Student:
    def __init__(self, g, n, a):
        self.gpa = g
        self.name = n
        self.age = a

    def __str__(self):
        return ("[%s %s %s]" % (self.gpa, self.name, self.age))

    def __lt__(self, other):
        if self.gpa < other.gpa:
            return True
        elif other.gpa < self.gpa:
            return False
        else:
            if self.name < other.name:
                return True
            elif other.name < self.name:
                return False
            else:
                if self.age < other.age:
                    return True
                else:
                    return False
    
    def __eq__(self, other):
        return (self.age == other.age and self.name == other.name and self.gpa == other.gpa)
    
    def __hash__(self):
        name_count = 0
        for s in self.name:
            name_count += ord(s)
        return (int(self.gpa + name_count + self.age))