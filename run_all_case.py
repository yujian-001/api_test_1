import unittest
import os
import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner
test_dir=os.getcwd() #获取执行test*.py的路径
# print(test_dir)

f=open(r"C:\Users\Administrator\PycharmProjects\discovertest\report\report.html","wb")

#discover自动识别目录下的所有test*.py文件
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py",top_level_dir=None)

# runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="testresult",description="unittestresult")
runner=HTMLTestRunner(stream=f,title="api test",description="unittest")
runner.run(discover)
f.close()