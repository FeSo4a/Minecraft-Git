import json


def write_in(save_path, game_path, version, max_backup) -> None:
    """
    写入保存路径，游戏路径，游戏版本。
    :param max_backup: 最多保存多少文件
    :param save_path: 保存路径
    :param game_path: 游戏路径
    :param version: 游戏版本

    :return:
        无
    """
    if max_backup < 1:
        max_backup = 1

    config: dict = {
        'save_path': save_path,
        'game_path': game_path,
        'version': version,
        'max_backup': max_backup
    }

    with open('../config/config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
