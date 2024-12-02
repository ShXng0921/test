import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Agg')  # 使用Agg后端进行图像保存

# 设置合适的字体，避免警告
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置matplotlib的字体
mpl.rcParams['font.family'] = 'DejaVu Sans'

from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter, BSPlotter, BSPlotterProjected, DosPlotter
import os

# 设置文件路径
vasprun_path = os.path.join('band', 'vasprun.xml')  # 确保路径正确指向band文件夹

# 读取vasprun.xml，获取带结构和DOS数据
bs_vasprun = Vasprun(vasprun_path, parse_projected_eigen=True)
bs_data = bs_vasprun.get_band_structure(line_mode=True)

dos_vasprun = Vasprun(vasprun_path)
dos_data = dos_vasprun.complete_dos

# 设置图形参数并绘制图形
banddos_fig = BSDOSPlotter(
    bs_projection='elements', 
    dos_projection='elements', 
    vb_energy_range=4, 
    fixed_cb_energy=4
)

# 获取并绘制图形
fig = banddos_fig.get_plot(bs=bs_data, dos=dos_data)

# 保存图像到band文件夹中
output_path = os.path.join('band', 'banddos_fig.png')
plt.savefig(output_path)
print(f"图像已保存至 {output_path}")
