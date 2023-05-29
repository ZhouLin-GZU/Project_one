# 作者；lin.zhou
for selenium import webdriver

# 第一层：Base_Page层
class BasePage:
    def _init_(self):
        self.driver = webdriver.Chrom();
        self.driver.get("http://qyapi.weixin.qq.com/cqi-bin/user/create");

    def locator_ele(self,args):
        ele = self.driver.find_element(*args)
        return ele


