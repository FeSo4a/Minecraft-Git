import os


def hotbar_copy(game_path, copy) -> None:
    try:
        with open(os.path.join(game_path, 'hotbar.nbt'), 'rb') as f:
            with open(os.path.join(copy, 'hotbar.nbt'), 'wb') as c:
                c.write(f.read())
    except Exception as e:
        print(f'发生错误：{e}')
