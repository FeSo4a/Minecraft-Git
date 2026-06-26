import os


def restore_hotbar(save_path, game_path, version, restore) -> None:
    # 将用户输入的路径中的斜杠替换为.，版本号中去掉v，把.换成_
    result = game_path.replace('/', '.').replace('\\', '.').replace(':', '')
    version = version.replace('.', '_')
    if version.startswith('v'):
        version = version[1:]
    os.makedirs(f'{save_path}/{result}', exist_ok=True)

    try:
        with open(f'{save_path}/{result}/{version}.nbt', 'rb') as f:
            with open(f'{restore}/hotbar.nbt', 'wb') as c:
                c.write(f.read())
    except Exception as e:
        print(f'发生错误：{e}')
