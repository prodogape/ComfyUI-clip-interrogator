#### [English](./README.md) | 中文

# ComfyUI-clip-interrogator
Unofficial ComfyUI extension of clip-interrogator

_作者刚玩这个，如果发现问题欢迎提issue_

### 安装
- 先安装pythongosssss/ComfyUI-Custom-Scripts：`https://github.com/pythongosssss/ComfyUI-Custom-Scripts`
- 到ComfyUI项目根目录下的`custom_nodes/`文件夹下：`cd path/to/ComfyUI/custom_nodes`
- git clone本项目: `git clone https://github.com/unanan/ComfyUI-clip-interrogator.git`
- 到`ComfyUI-clip-interrogator/`文件夹下: `cd path/to/ComfyUI/custom_nodes/ComfyUI-clip-interrogator`
- 运行 `python install.py`

**注：连不上huggingface的机器记得设置`HF_ENDPOINT`全局变量（只能提醒到这里了）**

### 使用示意
![](./assets/1.png)
![](./assets/2.png)
![](./assets/3.png)

#### Verbose: 代码结构说明（希望对一些跟我一样刚入门的想写custom_nodes的小白有一点帮助）
- `node_mappings.py`里是到ComfyUI界面上的一些名称的映射
- `nodes.py`里定义的是ComfyUI的节点类，有些方法和变量是特定的必须写的，`FUNCTION`里要写调用模型预测的代码
- `inference.py`里是具体模型加载、预测等等的代码
