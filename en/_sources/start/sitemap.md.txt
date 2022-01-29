# 网站地图

Sphinx 扩展 [jdillard/sphinx-sitemap](https://github.com/jdillard/sphinx-sitemap) 为你的 Sphinx 文档的 HTML 版本生成多版本和多语言 [sitemaps.org](https://www.sitemaps.org/protocol.html) 兼容的网站地图。

## 配置

安装：

```sh
pip install sphinx-sitemap
```

添加到 {confval}`extensions`：

```sh
extensions = ['sphinx_sitemap']
```

### 基础配置

在你的 Sphinx `conf.py` 中设置 {confval}`html_baseurl` 的值为当前文档的 base URL。比如说：

```sh
html_baseurl = 'https://my-site.com/docs/'
```

在 HTML 构建完成后，`sphinx-sitemap` 会输出网站地图的位置：

```sh
sitemap.xml was generated for URL https://my-site.com/docs/ in /path/to/_build/sitemap.xml
```

```{tip}
确保在安装和升级后确认网站地图的准确性。
```

## 更改文件名

在 `conf.py` 中设置 {confval}`sitemap_filename` 为需要的文件名，例如：

```sh
sitemap_filename = "sitemap.xml"
```

### 版本配置

对于多版本网站地图，需要为每个版本生成一个网站地图，然后手动将其位置添加到 [网站地图索引文件](https://support.google.com/webmasters/answer/75712?hl=en) 中。

该扩展将查看当前正在构建的版本的 {confval}`version` 配置值，所以要确保该值被设置。

````{hint}
当使用多个版本时，最好的做法是将所有版本的主题布局中的 canonical URL 设置为该页面的最新版本：

```html
<link rel="canonical" href="https://my-site.com/docs/latest/index.html"/>
```
````

### 多语言配置

对于多语言网站地图，每一种语言/地区生成一个网站地图，然后手动将其位置添加到网站地图索引文件中。

主语言是由 {confval}`language` 配置值设置的。替代语言是由 `sitemap_locales` 选项手动设置的，或者由扩展的 {confval}`locale_dirs` 配置值自动检测的，所以要确保其中一个被设置。

`sitemap_locales` 配置是指定一个在 `sitemap` 中包含的 `locales` 的列表。例如，如果一个第三方扩展添加不支持的语言到 `locale_dirs`，或者允许 `locale` 达到一定的翻译百分比后再公开。例如，如果主要语言是 `zh_CN`，并且指定了 `en` 和 `fr` 的翻译列表，那么 `sitemap` 看起来是这样的：

```xml
<?xml version="1.0" encoding="utf-8"?>
  <urlset xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
      <loc>https://my-site.com/docs/zh_CN/index.html</loc>
      <xhtml:link href="https://my-site.com/docs/es/index.html" hreflang="en" rel="alternate"/>
      <xhtml:link href="https://my-site.com/docs/fr/index.html" hreflang="fr" rel="alternate"/>
      <xhtml:link href="https://my-site.com/docs/en/index.html" hreflang="zh_CN" rel="alternate"/>
    </url>
    <url>
        <loc>https://my-site.com/docs/zh_CN/about.html</loc>
        <xhtml:link href="https://my-site.com/docs/es/about.html" hreflang="en" rel="alternate"/>
        <xhtml:link href="https://my-site.com/docs/fr/about.html" hreflang="fr" rel="alternate"/>
        <xhtml:link href="https://my-site.com/docs/en/about.html" hreflang="zh_CN" rel="alternate"/>
    </url>
  </urlset>
```

当网站地图的地域性受到限制时：

```python
sitemap_locales = ['zh_CN', 'en']
```

最终的结果是，每种语言/版本的构建都类似于以下内容：

```xml
<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://my-site.com/docs/zh_CN/index.html</loc>
    <xhtml:link href="https://my-site.com/docs/en/index.html" hreflang="es" rel="alternate"/>
  </url>
  <url>
    <loc>https://my-site.com/docs/zh_CN/about.html</loc>
    <xhtml:link href="https://my-site.com/docs/en/about.html" hreflang="es" rel="alternate"/>
  </url>
</urlset>
```

当特殊值设置为 `[None]` 时：

```xml
sitemap_locales = [None]
```

只生成主语言：

```xml
<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://my-site.com/docs/zh_CN/index.html</loc>
  </url>
  <url>
    <loc>https://my-site.com/docs/zh_CN/about.html</loc>
  </url>
</urlset>
```

### 定制 URL 方案

如果同时设置了 {confval}`language` 和 {confval}`version`，默认的 `URL` 格式是 `{version}{lang}{link}`。要改变默认行为，请在 `conf.py` 中设置 {confval}`sitemap_url_scheme` 的值为所需格式。比如说：

```python
sitemap_url_scheme = "{lang}{version}subdir/{link}"
```

```{note}
该扩展目前是 opinionated，因为它自动给语言和版本值加上尾部的斜线。你也可以从方案中省略所需行为的值。
```

## 充分发挥网站地图的作用

1. 在源目录中添加一个 `robots.txt` 文件，其中包含一个指向网站地图或网站地图索引的链接。比如说：

    ```
    User-agent: *

    Sitemap: https://my-site.com/docs/sitemap.xml
    ```

    然后，将 `robots.txt` 添加到 {confval}`html_extra_path` 配置值中：

    ```python
    html_extra_path = ['robots.txt']
    ```

2. 将网站地图或网站地图索引提交给适当的搜索引擎工具。

