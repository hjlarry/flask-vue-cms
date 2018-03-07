DEBUG = False
SITE_URL = 'http://localhost:8100/'
STATIC_FOLDER = 'static'
STATIC_URL = SITE_URL+STATIC_FOLDER+'/'
UPLOAD_FOLDER = STATIC_FOLDER + '/upload/'

# 导入本地配置
try:
    from local_setting import *
except:
    pass