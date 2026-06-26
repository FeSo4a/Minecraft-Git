import argparse

from config import *
from hotbar import *


def main() -> None:
    save_path, game_path, version = new_config()

    parser = argparse.ArgumentParser(
        description='一个MC hotbar文件管理工具 | By FeSo4a | MIT许可证'
    )
    # 设置操作
    parser.add_argument('-v', '--version', type=str, help='设置当前游戏版本号')
    parser.add_argument('-g', '--gamepath', type=str, help='设置.minecraft文件夹路径')
    parser.add_argument('-s', '--setpath', type=str, help='设置保存文件的路径')
    # 显示信息
    parser.add_argument('-sh', '--showhotbar', action='store_true', help='显示保存文件的路径')
    parser.add_argument('-sp', '--showpath', action='store_true', help='显示目前指向的.minecraft文件夹路径')
    parser.add_argument('-sv', '--showversion', action='store_true', help='显示目前指向的版本号')
    # 核心操作
    parser.add_argument('-hb', '--hotbarbackup', action='store_true', help='备份当前版本的hotbar文件')
    parser.add_argument('-hs', '--hotbarstore', action='store_true', help='恢复当前版本的hotbar文件')
    parser.add_argument('-c', '--copy', type=str, help='将当前指向的.minecraft文件夹下的hotbar文件转移到指定位置')
    parser.add_argument('-r', '--restore', type=str, help='将当前hotbar文件的备份转移到当前指定的.minecraft文件夹下')

    args = parser.parse_args()

    # 显示.minecraft文件夹路径
    if args.showpath:
        if game_path is None:
            print('未设置.minecraft文件夹路径')
        else:
            print(f'当前指向的.minecraft文件夹路径为：\n{game_path}')
    # 显示保存文件路径
    if args.showhotbar:
        print(f'当前的保存文件路径为：\n{save_path}')
    # 显示版本号
    if args.showversion:
        if version is None:
            print('未设置当前游戏版本号')
        else:
            print(f'当前游戏版本号为：\n{version}')

    # 设置路径，版本
    flag = False
    if args.gamepath:
        game_path = args.gamepath
        flag = True
    if args.setpath:
        save_path = args.setpath
        flag = True
    if args.version:
        version = args.version
        flag = True
    # 实时写入
    if flag:
        write_in(save_path, game_path, version)

    # 备份和恢复hotbar
    flag = not None in [save_path, game_path, version]
    if args.hotbarbackup:
        if flag:
            backup_hotbar(game_path, save_path, version)
        else:
            print('请先设置.minecraft文件夹路径和版本号')
    if args.hotbarstore:
        if flag:
            store_hotbar(game_path, save_path, version)
        else:
            print('请先设置.minecraft文件夹路径和版本号')

    # 复制hotbar文件
    if args.copy:
        if flag:
            hotbar_copy(game_path, args.copy)
        else:
            print('请先设置.minecraft文件夹路径和版本号')
    if args.restore:
        if flag:
            restore_hotbar(save_path, game_path, version, args.restore)
        else:
            print('请先设置.minecraft文件夹路径和版本号')


if __name__ == '__main__':
    main()
