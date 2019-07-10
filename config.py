import os
BASE_DIRS = os.path.dirname(__file__)

# 参数
options = {
    "port": 8090
}

settings = {
    "static_path": os.path.join(BASE_DIRS, "static"),
    "template_path": os.path.join(BASE_DIRS, "templates"),
    # "debug": True,
    "autoreload": False,
    # 关闭当前项目的自动转义，一般不建义使用
    # "autoescape": None

}

