import os
from file import *


def restore_hotbar(save_path, game_path, version, restore, backup_date) -> None:
    path = set_fold_name(save_path, game_path, version)
    os.makedirs(path, exist_ok=True)

    try:
        # noinspection PyTypeChecker
        with open(os.path.join(path, f'{backup_date}.nbt'), 'rb') as f:
            with open(os.path.join(restore, 'hotbar.nbt'), 'wb') as c:
                c.write(f.read())
    except Exception as e:
        print(f'发生错误：{e}')
