import json
import os

DEFAULT_CONFIG = {
    'save_path': '../save'
}


def new_config() -> tuple[str, str | None, str | None]:
    """
    自动创建config文件和目录，若已经存在，则读取config文件
    :return:
        依次返回 save_path, game_path, version
    """
    os.makedirs('../config', exist_ok=True)
    # noinspection PyBroadException
    try:
        with open('../config/config.json', 'r', encoding='utf-8') as f:
            config: dict = json.load(f)
            save_path = config.get('save_path', '../path')
            game_path = config.get('game_path', None)
            version = config.get('version', None)

            return save_path, game_path, version

    except:
        with open('../config/config.json', 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_CONFIG, f, indent=2)
            return DEFAULT_CONFIG['save_path'], None, None
