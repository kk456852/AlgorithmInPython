from abc import ABC, abstractmethod

# 抽象工厂
class AbastractFactory(ABC):
    
    @abstractmethod
    def product_phone(self):
        pass

# 苹果工厂
class AppleFactory(AbastractFactory):
    
    def product_phone(self):
        return Apple().make()

# 小米工厂
class XiaomiFactory(AbastractFactory):
    
    def product_phone(self):
        return XiaoMi().make()
 

# 生产线
class ProductLine(ABC):
    
    @abstractmethod
    def make(self):
        pass

# 苹果生产线
class Apple(ProductLine):
    
    def make(self):
        print("make apple")

# 小米生产线
class XiaoMi(ProductLine):
    
    def make(self):
        print("make xiaomi")

def client_product(factory:AbastractFactory):
    return factory

if __name__ == '__main__':
    xiaomi = client_product(XiaomiFactory())
    xiaomi.product_phone()
    apple = client_product(AppleFactory())
    apple.product_phone()