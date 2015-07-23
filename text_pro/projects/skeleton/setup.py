try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description'：'My Project',
	'author':'Jake',
	'url':'http://www.baidu.com',
	'download_url':'Where to download it.',
	'author_email':'liujingjieyear@163.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['NAME'],
	'scripts':[],
	'name':'projactname'
}
setup(**config)