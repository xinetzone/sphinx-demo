# Pytorch 环境搭建

```{seealso}
更多精彩见：
- 知乎 [win11 配置 Pytorch GPU](https://www.zhihu.com/zvideo/1458194846603767808)
- 简书 [搭建一个友好的可塑性计算机视觉工具集](https://www.jianshu.com/p/1577b65fd5b4)
```

{guilabel}`环境配置`：学习 [Anaconda3 教程](anaconda3.md)，然后配置 PyTorch。

## 本地服务器支持 GPU

1. 替换 [本地服务器 GPU 配置](gpu) 中的环境 `ai` 为 `torch`。
2. 安装 PyTorch GPU 支持：

    ```sh
    conda install pytorch torchvision torchaudio -c pytorch
    ```

3. 添加 Jupyter 内核支持：

    ```sh
    conda install ipykernel
    python -m ipykernel install --user --name torch --display-name "PyTorch"
    ```

4. 更多内容见 {guilabel}`预览`：[pytorch-demo](https://xinetzone.github.io/pytorch-demo)。
