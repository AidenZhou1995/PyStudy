class Man:
    """ Here are some instruction """

    def __init__(self, name, x):
        self.name = name
        self.x = x
        print("hh")

    def speak(self):
        print("My name is %s, and I'm a %s" % (self.name, self.x))


class Student:
    """ a student """

    def __init__(self, lesson):
        self.lesson = lesson
        print(self.lesson)

    def study(self):
        print("I am studying %s" % self.lesson)


class Boy(Man, Student):

    def __init__(self, n, x, less, age):
        Man.__init__(self, n, x)
        Student.__init__(self, less)
        self.age = age

    def my_age(self):
        print("My age is %d, and I'm a %s" % (self.age, self.x))


class Boy2(Man):
    """ test super: 先尝试从一个开始 """

    def __init__(self, name, x):
        super(Man, self).__init__(name, x)
        print("OK")

# ken = Boy("ken", "man", "math", 18)
# ken.speak()
# ken.my_age()
# ken.study()

if __name__ == '__main__':
    A = Boy2("a", "b")