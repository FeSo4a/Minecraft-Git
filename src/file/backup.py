import datetime
import os


def save_latest_nbt(folder_path, binary_data: bytes) -> None:
    """
    处理指定文件夹中的 latest.nbt 文件：
    1. 若 latest.nbt 存在，将其重命名为「当前日期-当前时间.nbt」
    2. 将传入的二进制数据保存为新的 latest.nbt

    :param folder_path: 目标文件夹路径（需已存在）
    :param binary_data: 要保存的二进制数据

    :return: 无返回值
    """
    # 构造 latest.nbt 的完整路径
    latest_path = os.path.join(folder_path, 'latest.nbt')

    # 检查 latest.nbt 是否存在
    if os.path.isfile(latest_path):
        # 获取当前时间并格式化（避免文件名非法字符，用横杠替代冒号）
        current_time = datetime.datetime.now()
        timestamp: str = current_time.strftime('%Y-%m-%d_%H-%M-%S')
        new_filename: str = f'{timestamp}.nbt'
        new_path = os.path.join(folder_path, new_filename)

        # 重命名旧文件
        try:
            os.rename(latest_path, new_path)
        except Exception as e:
            print(f"重命名文件失败: {e}")

    # 保存新的 latest.nbt（覆盖或新建）
    try:
        with open(latest_path, "wb") as f:
            f.write(binary_data)
    except Exception as e:
        print(f"保存文件失败: {e}")
