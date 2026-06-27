from .set_fold import *


def list_nbt_filenames(folder_path) -> list[str]:
    """
    获取指定文件夹中所有 .nbt 文件的文件名（不包含 .nbt 后缀）。

    :param folder_path: 目标文件夹路径

    :return: 包含所有 .nbt 文件名（无后缀）的列表，按字母顺序排序
    """
    # 获取文件夹中所有文件
    all_files = os.listdir(folder_path)

    # 筛选 .nbt 文件并去除后缀
    nbt_filenames = []
    for filename in all_files:
        # 检查是否为 .nbt 文件
        if filename.lower().endswith(".nbt"):
            # 去除 .nbt 后缀
            name_without_ext = filename[:-4]  # ".nbt" 长度为 4
            nbt_filenames.append(name_without_ext)

    # 按字母顺序排序（可选，根据需要调整）
    nbt_filenames.sort()

    return nbt_filenames


def show_all_nbt(game_path, save_path, version) -> None:
    fix_path = set_fold_name(save_path, game_path, version)
    nbt_filenames = list_nbt_filenames(fix_path)
    print(f'当前的备份有：')
    for file_name in nbt_filenames:
        print(file_name)
