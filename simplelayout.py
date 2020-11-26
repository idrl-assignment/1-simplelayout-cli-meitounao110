import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="Demo of simplelayout")
    parser.add_argument('--board_grid', help=' Layout panel resolution ', type=int)
    parser.add_argument('--unit_grid', help=' Rectangular component resolution ',type=int)
    parser.add_argument('--unit_n', help=' Numbers of component ', type=int)
    parser.add_argument('--positions', help=' position serial number of component ', \
                        nargs='+', type=int)
    parser.add_argument('-o', '--outdir', help=' directory of output ', default='./example_dir', type=str)
    parser.add_argument('--file_name', help=' file name of output ', default='example', type=str)
    args = parser.parse_args()
#检验是否被整除
    if args.board_grid % args.unit_grid != 0:
        return
    uplimit = (args.board_grid / args.unit_grid) ** 2
#检验长度是否标准
    if len(args.positions) != args.unit_n:
        return
    else:
        for i in range(0,len(args.positions)):
            if 1 < args.positions[i] or args.positions[i] > uplimit:
                return
            else:
                print(i)
    path = transpath(args.outdir)
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(rf'{path}')
    full_path = path + args.file_name + '.jpg'
    file = open(full_path, 'w')
    file.write()
# os.mknod()

def transpath(path):
    path = path.replace('/', 'os.sep')
    path = path.replace('\\', 'os.sep')
    return path



if __name__ == "__main__":
    main()
