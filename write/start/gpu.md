# 本地服务器 GPU 配置

支持 Windows10+ 以及 Ubuntu20.04+

1. [安装 CUDA](https://developer.nvidia.cn/cuda-downloads)。
2. 安装 `ai` 环境，并使用 `conda` 安装 CUDA（即 `cudatoolkit`）与 `cudnn`：

    ```sh
    conda create -n ai python=3.9
    conda activate ai
    conda install cudatoolkit=11.5
    conda install cudnn
    ```

    这里 `11.5` 应该换成对应的 CUDA 版本。