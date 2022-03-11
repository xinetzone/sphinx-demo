import sys
from pathlib import Path

# 载入自定义模块
DOC_ROOT = Path(__file__).parent.absolute()
sys.path.extend([
    str(DOC_ROOT.parent/'_sphinx'),
    str(DOC_ROOT.parent/'src'),
])

from share_conf import *