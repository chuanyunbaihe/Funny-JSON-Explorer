from Product import *


# 抽象工厂和建造者
class AbstractJsonFactory(ABC):
    @abstractmethod
    def container(self):  # 创建JSON树中的容器节点
        pass

    @abstractmethod
    def leaf(self):  # 创建JSON树中的叶子节点
        pass

    @abstractmethod
    def result(self):  # 获取JSON树
        pass


class TreeFactory(AbstractJsonFactory):
    def __init__(self):
        self.product = TreeProduct()

    def container(self):
        self.product.set_container()

    def leaf(self):
        self.product.set_leaf()

    def result(self):
        return self.product


class RectangleFactory(AbstractJsonFactory):
    def __init__(self):
        self.product = RectangleProduct()

    def container(self):
        self.product.set_container()

    def leaf(self):
        self.product.set_leaf()

    def result(self):
        return self.product
