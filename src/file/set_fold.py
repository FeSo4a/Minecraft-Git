import os
from typing import *


def set_fold_name(save_path, game_path, version) -> LiteralString | str | bytes:
    """
    设置保存文件夹名称
    :param save_path: 保存路径
    :param game_path: 游戏路径
    :param version: 版本号
    :return:
        fix_path: 最终经过修正的路径
    """
    fix_game_path = game_path.replace('/', '.').replace('\\', '.').replace(':', '')
    if version.startswith('v'):
        version = version[1:]
    fix_version = version.replace('.', '_')
    fix_path = os.path.join(save_path, fix_game_path, fix_version)
    return fix_path
