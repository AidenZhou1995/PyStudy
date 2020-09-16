class FooParent:
    def __init__(self, x):
        self.parent = 'I\'m the parent.'
        print('Parent%s' % x)

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self, x):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild, self).__init__(x)
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild("x")
    fooChild.bar('HelloWorld')