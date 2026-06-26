import os


def backup_hotbar(game_path, save_path, version) -> None:
    """
    备份hotbar.nbt文件
    :param game_path: 游戏路径
    :param save_path: 保存路径
    :param version: 版本号
    :return: 无
    """
    # 将用户输入的路径中的斜杠替换为.，版本号中去掉v，把.换成_
    result = game_path.replace('/', '.').replace('\\', '.').replace(':', '')
    version = version.replace('.', '_')
    if version.startswith('v'):
        version = version[1:]
    os.makedirs(f'{save_path}/{result}', exist_ok=True)

    try:
        with open(f'{game_path}/hotbar.nbt', 'rb') as f:
            with open(f'{save_path}/{result}/{version}.nbt', 'wb') as c:
                c.write(f.read())
    except Exception as e:
        print(f'发生错误：{e}')
