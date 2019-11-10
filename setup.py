try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from goby.version import version

# 多值的字典参数，setup是一个函数
setup(name="gobyapi",  # 包名
      version=version,  # 版本
      description="goby-api web api",  # 描述信息
      long_description="goby webapi接口",  # 完整描述信息
      author=["lidazhuang"],  # 作者
      author_email="becivells@qq.com",  # 作者邮箱
      keywords='goby',
      url="",  # 主页
      platforms=['any'],
      install_requires=[
          'requests',
      ],
      python_requires='>=3.4',
      py_modules=[
          "goby.v1.asset",
          "goby.v1.client",
          "goby.v1.data",
          "goby.v1.gobyapi",
          "goby.v1.__init__",
          "goby.v1.poc",
          "goby.version",
      ]
      )
