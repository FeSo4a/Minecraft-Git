import os

from file import *


def store_hotbar(game_path, save_path, version, backup_date) -> None:
    """
        恢复hotbar.nbt文件
        :param backup_date: 保存日期（即文件名）
        :param game_path: 游戏路径
        :param save_path: 保存路径
        :param version: 版本号
        :return: 无
    """
    path = set_fold_name(save_path, game_path, version)
    os.makedirs(path, exist_ok=True)

    try:
        with open(os.path.join(game_path, 'hotbar.nbt'), 'wb') as f:
            # noinspection PyTypeChecker
            with open(os.path.join(path, f'{backup_date}.nbt'), 'rb') as c:
                f.write(c.read())
    except Exception as e:
        print(f'发生错误：{e}')
