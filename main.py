import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def colormap2pal(color_name: str = "tab10"):
    # 创建一个简单的colormap
    color_name = color_name
    cmap = plt.get_cmap(color_name)

    # 获取colormap的颜色值
    num_colors = cmap.N
    colors = cmap(np.linspace(0, 1, num_colors))
    colors_255 = (colors[:, :3] * 255).astype(np.uint8)

    # 准备文件头
    header = "JASC-PAL\n0100\n{}\n".format(num_colors)
    header = header.encode("utf-8")
    # 导出到.pal文件
    cwd = Path.cwd() / "PalFile"
    cwd.mkdir(exist_ok=True)
    oth_file_path = f"./PalFile/{color_name}.pal"
    with open(oth_file_path, "wb") as f:
        f.write(header)
        for color in colors_255:
            line = f"{color[0]} {color[1]} {color[2]}\n".encode("utf-8")
            f.write(line)
    print(f"Colormap exported to {oth_file_path}")


def main():
    print("Hello from pythoncolor2origin!")
    colormap2pal()


if __name__ == "__main__":
    main()
