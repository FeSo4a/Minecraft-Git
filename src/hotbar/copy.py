def hotbar_copy(game_path, copy) -> None:
    try:
        with open(f'{game_path}/hotbar.nbt', 'rb') as f:
            with open(f'{copy}/hotbar.nbt', 'wb') as c:
                c.write(f.read())
    except Exception as e:
        print(f'发生错误：{e}')
