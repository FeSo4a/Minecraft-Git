import os

from file import *


def backup_hotbar(game_path, save_path, version, max_files) -> None:
    """
    备份hotbar.nbt文件
    :param max_files: 最多支持保存几个nbt文件
    :param game_path: 游戏路径
    :param save_path: 保存路径
    :param version: 版本号
    :return: 无
    """
    # 将用户输入的路径中的斜杠替换为.，版本号中去掉v，把.换成_
    path = set_fold_name(save_path, game_path, version)
    os.makedirs(path, exist_ok=True)

    try:
        with open(os.path.join(game_path, 'hotbar.nbt'), 'rb') as f:
            save_latest_nbt(path, f.read())
    except Exception as e:
        print(f'发生错误：{e}')

    cleanup_old_nbt_files(path, max_files)
