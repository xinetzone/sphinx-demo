# 创作

分支 `old` 已经废弃。

仅仅需要修改文件夹 `_sphinx/` 以及 `docs/` 便可完成配置。

```{rubric} 生成文档
```

```shell
invoke docs
```

```{rubric} 清空文档
```

```shell
invoke docs.clean
```

```{rubric} 创建贡献者文档
```

```shell
invoke write.clean
```

```{toctree}
:maxdepth: 2
:hidden:

start/index
about/index
```

# 索引与表格

* {ref}`genindex`
* {ref}`modindex`
* {ref}`search`
