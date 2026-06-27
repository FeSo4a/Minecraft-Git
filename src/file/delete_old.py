import glob
import os


def cleanup_old_nbt_files(folder_path, max_backup: int) -> None:
    """
    清理文件夹中过旧的 .nbt 文件，确保文件总数不超过 max_files 个。
    规则：按文件修改时间排序，删除最旧的文件。

    :param folder_path: 目标文件夹路径
    :param max_backup: 最大保留文件数

    :return: 无返回值
    """
    # 获取文件夹中所有 .nbt 文件（排除子目录）
    nbt_files = glob.glob(os.path.join(folder_path, "*.nbt"))
    nbt_files = [f for f in nbt_files if os.path.isfile(f)]  # 确保是文件而非目录

    # 如果文件数量未超过限制，直接返回
    if len(nbt_files) <= max_backup:
        return

    # 按文件修改时间排序（最旧的在前）
    # 使用修改时间（mtime），比创建时间（ctime）兼容性更好
    nbt_files.sort(key=lambda x: os.path.getmtime(x))

    # 计算需要删除的文件数量
    files_to_delete = len(nbt_files) - max_backup

    # 删除最旧的文件
    for i in range(files_to_delete):
        old_file = nbt_files[i]
        try:
            os.remove(old_file)
        except Exception as e:
            print(f"删除文件 {old_file} 失败: {e}")
