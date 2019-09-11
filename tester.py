import unittest
import student

class TestStudent(unittest.TestCase):
    # Part 2b test cases
    # s1 == s2 for all (should be false)
    def test1_lt(self):
        s1 = student.Student(3.5, "Fred", 19)
        s2 = student.Student(3.5, "Fred", 19)
        self.assertFalse(s1 < s2)  
    
    # s1 < s2 for gpa
    def test2_lt(self):
        s1 = student.Student(3.5, "Fred", 19)
        s2 = student.Student(4.0, "Julie", 20)
        self.assertTrue(s1 < s2)

    # s1 > s2 for gpa
    def test3_lt(self):
        s1 = student.Student(3.5, "Fred", 19)
        s2 = student.Student(2.1, "Jack", 18)
        self.assertFalse(s1 < s2)

    # s1 < s2 for name (gpa is equal)
    def test4_lt(self):
        s1 = student.Student(3.5, "Fred", 19)
        s2 = student.Student(3.5, "Zack", 22)
        self.assertTrue(s1 < s2)

    # s1 > s2 for name (gpa is equal)
    def test5_lt(self):
        s1 = student.Student(3.0, "Mallory", 22)
        s2 = student.Student(3.0, "Brett", 20)
        self.assertFalse(s1 < s2)

    # s1 < s2 for age (gpa and name are equal)
    def test6_lt(self):
        s1 = student.Student(2.7, "Jess", 19)
        s2 = student.Student(2.7, "Jess", 22)
        self.assertTrue(s1 < s2)

    # s1 > s2 for age (gpa and name are equal)
    def test7_lt(self):
        s1 = student.Student(1.8, "Cassie", 20)
        s2 = student.Student(1.8, "Cassie", 19)
        self.assertFalse(s1 < s2)

    # s1 == s2
    def test1_eq(self):
        s1 = student.Student(3.8, "Frank", 22)
        s2 = student.Student(3.8, "Frank", 22)
        self.assertTrue(s1 == s2)

    # s1 != s2
    def test2_eq(self):
        s1 = student.Student(4.0, "Anne", 22)
        s2 = student.Student(3.8, "Frank", 22)
        self.assertFalse(s1 == s2)

    # s1 == s2
    def test1_str(self):
        o1 = student.Student(1.8, "Cassie", 20)
        o2 = student.Student(1.8, "Cassie", 20)
        s1 = str(o1)
        s2 = str(o2)
        self.assertTrue(s1 == s2)

    # s1 != s2
    def test2_str(self):
        o1 = student.Student(1.8, "Cassie", 20)
        o2 = student.Student(1.9, "Cassie", 19)
        s1 = str(o1)
        s2 = str(o2)
        self.assertFalse(s1 == s2)

    # h1 == h2
    def test1_hash(self):
        o1 = student.Student(2.3, "Joe", 20)
        o2 = student.Student(2.3, "Joe", 20)
        h1 = hash(o1)
        h2 = hash(o2)
        self.assertTrue(h1 == h2)

    # h1 != h2
    def test2_hash(self):
        o1 = student.Student(3.8, "Frank", 20)
        o2 = student.Student(3.9, "Frank", 19)
        h1 = hash(o1)
        h2 = hash(o2)
        self.assertFalse(h1 == h2)

    # sort with sorted function (by GPA)
    def test1_sorted(self):
        testlist = [student.Student(3.3, "Hether", 18),
                student.Student(4.0, "Anne", 22),
                student.Student(2.4, "Frank", 22),
                student.Student(2.8, "Joe", 19),
                student.Student(3.7, "Rhyan", 20),
                student.Student(1.9, "Zach", 20),
                student.Student(3.3, "Beth", 21)]
        sortedlist = [testlist[5],
                    testlist[2],
                    testlist[3],
                    testlist[6],
                    testlist[0],
                    testlist[4],
                    testlist[1]]
        self.assertTrue(sorted(testlist) == sortedlist)

    # sort with sorted function (by Name)
    def test2_sorted(self):
        testlist = [student.Student(3.3, "Hether", 18),
                student.Student(3.3, "Anne", 22),
                student.Student(3.3, "Frank", 22),
                student.Student(3.3, "Joe", 19),
                student.Student(3.3, "Rhyan", 20),
                student.Student(3.3, "Zach", 20),
                student.Student(3.3, "Beth", 21)]
        sortedlist = [testlist[1],
                    testlist[6],
                    testlist[2],
                    testlist[0],
                    testlist[3],
                    testlist[4],
                    testlist[5]]
        self.assertTrue(sorted(testlist) == sortedlist)

    # sort with sorted function (by age)
    def test3_sorted(self):
        testlist = [student.Student(3.3, "Heather", 18),
                student.Student(3.3, "Heather", 19),
                student.Student(3.3, "Heather", 15),
                student.Student(3.3, "Heather", 23),
                student.Student(3.3, "Heather", 20),
                student.Student(3.3, "Heather", 22),
                student.Student(3.3, "Heather", 21)]
        sortedlist = [testlist[2],
                    testlist[0],
                    testlist[1],
                    testlist[4],
                    testlist[6],
                    testlist[5],
                    testlist[3]]
        self.assertTrue(sorted(testlist) == sortedlist)

    # sort with sorted function (by GPA)
    def test4_sorted(self):
        testlist = [student.Student(3.3, "Hether", 18),
                student.Student(4.0, "Anne", 22),
                student.Student(2.4, "Frank", 22),
                student.Student(2.8, "Joe", 19),
                student.Student(3.7, "Rhyan", 20),
                student.Student(1.9, "Zach", 20),
                student.Student(3.3, "Beth", 21)]
        sortedlist = [testlist[5],
                    testlist[2],
                    testlist[3],
                    testlist[6],
                    testlist[0],
                    testlist[4],
                    testlist[1]]
        sortedlist.reverse()
        self.assertTrue(sorted(testlist, reverse=True) == sortedlist)

    # sort with sorted function (by Name)
    def test5_sorted(self):
        testlist = [student.Student(3.3, "Hether", 18),
                student.Student(3.3, "Anne", 22),
                student.Student(3.3, "Frank", 22),
                student.Student(3.3, "Joe", 19),
                student.Student(3.3, "Rhyan", 20),
                student.Student(3.3, "Zach", 20),
                student.Student(3.3, "Beth", 21)]
        sortedlist = [testlist[1],
                    testlist[6],
                    testlist[2],
                    testlist[0],
                    testlist[3],
                    testlist[4],
                    testlist[5]]
        sortedlist.reverse()
        self.assertTrue(sorted(testlist, reverse=True) == sortedlist)

    # sort with sorted function (by age)
    def test6_sorted(self):
        testlist = [student.Student(3.3, "Heather", 18),
                student.Student(3.3, "Heather", 19),
                student.Student(3.3, "Heather", 15),
                student.Student(3.3, "Heather", 23),
                student.Student(3.3, "Heather", 20),
                student.Student(3.3, "Heather", 22),
                student.Student(3.3, "Heather", 21)]
        sortedlist = [testlist[2],
                    testlist[0],
                    testlist[1],
                    testlist[4],
                    testlist[6],
                    testlist[5],
                    testlist[3]]
        sortedlist.reverse()
        self.assertTrue(sorted(testlist, reverse=True) == sortedlist)

    # multiple different hashes
    def test1_dict(self):
        dict1 = {}
        o1 = student.Student(3.8, "Frank", 20)
        o2 = student.Student(3.9, "Anne", 19)
        o3 = student.Student(2.5, "Jill", 20)
        o4 = student.Student(1.9, "Howard", 22)
        dict1[o1] = 1
        dict1[o2] = 1
        dict1[o3] = 1
        dict1[o4] = 1
        self.assertTrue(dict1[o1] == 1 and dict1[o2] == 1 and dict1[o3] == 1 and dict1[o4] == 1)

    # mix of multiple different and multiple grouped hashes
    def test2_dict(self):
        dict2 = {}
        o1 = student.Student(3.8, "Frank", 20)
        o2 = student.Student(3.9, "Anne", 19)
        o3 = student.Student(2.2, "Beth", 19)
        o4 = student.Student(4.0, "Jack", 21)
        o5 = student.Student(4.0, "Jack", 21)
        o6 = student.Student(2.2, "Beth", 19)
        o7 = student.Student(3.5, "Haley", 21)
        o8 = student.Student(4.0, "Jack", 21)
        dict2[o1] = 1
        dict2[o2] = 1
        dict2[o3] = 1
        dict2[o4] = 1
        dict2[o5] = dict2[o5] + 1
        dict2[o6] = dict2[o6] + 1
        dict2[o7] = 1
        dict2[o8] = dict2[o8] + 1
        self.assertTrue(len(dict2.keys()) == 5)
        self.assertTrue(dict2[o8] == 3)
        self.assertTrue(dict2[o6] == 2)
        self.assertTrue(dict2[o1] == 1 and dict2[o2] == 1 and dict2[o7] == 1)

    # multiple different hashes (using dict())
    def test3_dict(self):
        o1 = student.Student(3.8, "Frank", 20)
        o2 = student.Student(3.9, "Anne", 19)
        o3 = student.Student(2.5, "Jill", 20)
        o4 = student.Student(1.9, "Howard", 22)
        dict1 = dict([(o1, 1), (o2, 1), (o3, 1), (o4, 1)])
        self.assertTrue(dict1[o1] == 1 and dict1[o2] == 1 and dict1[o3] == 1 and dict1[o4] == 1)

    # mix of multiple different and multiple grouped hashes (using dict())
    def test4_dict(self):
        dict2 = {}
        o1 = student.Student(3.8, "Frank", 20)
        o2 = student.Student(3.9, "Anne", 19)
        o3 = student.Student(2.2, "Beth", 19)
        o4 = student.Student(4.0, "Jack", 21)
        o5 = student.Student(4.0, "Jack", 21)
        o6 = student.Student(2.2, "Beth", 19)
        o7 = student.Student(3.5, "Haley", 21)
        o8 = student.Student(4.0, "Jack", 21)
        dict2[o1] = 1
        dict2[o2] = 1
        dict2[o3] = 1
        dict2[o4] = 1
        dict2[o5] = dict2[o5] + 1
        dict2[o6] = dict2[o6] + 1
        dict2[o7] = 1
        dict2[o8] = dict2[o8] + 1
        dict1 = dict([(o1, 1), (o2, 1), (o3, 1), (o4, 1), (o5, 2), (o6, 2), (o7, 1), (o8, 3)])
        self.assertTrue(len(dict2.keys()) == 5)
        self.assertTrue(dict2[o8] == 3)
        self.assertTrue(dict2[o6] == 2)
        self.assertTrue(dict2[o1] == 1 and dict2[o2] == 1 and dict2[o7] == 1)

    # Part 2c test case
    # lambda sort (using sorted) (gpa)
    def test1_lambda(self):
        testlist = [student.Student(3.3, "Hether", 18),
                student.Student(4.0, "Anne", 22),
                student.Student(2.4, "Frank", 22),
                student.Student(2.8, "Joe", 19),
                student.Student(3.7, "Rhyan", 20)]
        sortedlist = [testlist[2],
                    testlist[3],
                    testlist[0],
                    testlist[4],
                    testlist[1]]
        self.assertTrue(sorted(testlist, key=lambda x: x.gpa) == sortedlist)

    # lambda sort (using sorted) (name)
    def test2_lambda(self):
        testlist = [student.Student(3.3, "Hether", 18),
                student.Student(4.0, "Anne", 22),
                student.Student(4.0, "Frank", 22),
                student.Student(4.0, "Joe", 19),
                student.Student(3.7, "Rhyan", 20)]
        sortedlist = [testlist[0],
                    testlist[4],
                    testlist[1],
                    testlist[2],
                    testlist[3]]
        self.assertTrue(sorted(testlist, key=lambda x: x.gpa) == sortedlist)

    # lambda sort (using sorted) (age)
    def test3_lambda(self):
        testlist = [student.Student(3.3, "Hether", 18),
                student.Student(4.0, "Anne", 22),
                student.Student(2.8, "Frank", 22),
                student.Student(2.8, "Frank", 19),
                student.Student(2.8, "Frank", 20)]
        sortedlist = [testlist[3],
                    testlist[4],
                    testlist[2],
                    testlist[0],
                    testlist[1]]
        self.assertTrue(sorted(testlist, key=lambda s: (s.gpa, s.name, s.age)) == sortedlist)

if __name__ == '__main__':
    unittest.main()