## 软件仓库

### 什么是软件仓库

在Linux中，软件仓库（Software Repository）是指一个集中存储软件包的地方，这些软件包可以被系统自动下载、安装和更新。软件仓库通常包含了大量的软件包，这些软件包可以用于安装和更新操作系统的组件、应用程序和工具。

软件仓库的作用包括：

1. **软件分发和管理**: 软件仓库提供了一个集中的地方，用户可以方便地获取软件包。用户可以通过软件仓库安装新的软件包，更新已安装的软件包，或者卸载不再需要的软件包。

2. **版本控制**: 软件仓库通常会存储软件包的不同版本，用户可以根据需要选择特定的版本进行安装或更新。

3. **依赖关系解决**: 软件仓库中的软件包通常会包含它们所依赖的其他软件包的信息。系统可以通过软件仓库自动解决软件包之间的依赖关系，确保安装或更新软件包时所需的依赖项也会被满足。

4. **安全性和可信度**: 官方的软件仓库通常会进行软件包的审核和验证，确保软件包的安全性和可信度。用户可以信任官方软件仓库，以获取经过验证的软件包。

在Linux中，不同的发行版（如Ubuntu、Debian、CentOS、Fedora等）通常会有各自的官方软件仓库，同时也可能存在第三方或社区维护的软件仓库。用户可以配置系统，指定使用哪些软件仓库，并通过包管理工具（如apt、yum、dnf等）来管理软件包的安装和更新。

通过使用软件仓库，Linux系统可以轻松地获取并管理各种软件包，从而提供了便利和灵活性，使用户能够轻松地扩展系统的功能和应用。

### 常见的仓库镜像

1. **Ubuntu镜像**: Ubuntu是一个流行的Linux发行版，它提供了官方的镜像仓库以及一些第三方镜像仓库。常见的Ubuntu镜像仓库包括官方的Ubuntu镜像站点（如archive.ubuntu.com）以及一些全球范围的镜像站点（如mirrors.ustc.edu.cn、mirrors.tuna.tsinghua.edu.cn等）。

2. **Debian镜像**: Debian是另一个广泛使用的Linux发行版，它也提供了官方的镜像仓库以及一些第三方镜像仓库。常见的Debian镜像仓库包括官方的Debian镜像站点（如deb.debian.org）以及一些全球范围的镜像站点（如mirrors.ustc.edu.cn、mirrors.tuna.tsinghua.edu.cn等）。

3. **CentOS镜像**: CentOS是一个基于Red Hat Enterprise Linux（RHEL）源代码构建的Linux发行版，它也提供了官方的镜像仓库以及一些第三方镜像仓库。常见的CentOS镜像仓库包括官方的CentOS镜像站点（如mirror.centos.org）以及一些全球范围的镜像站点（如mirrors.ustc.edu.cn、mirrors.tuna.tsinghua.edu.cn等）。

4. **Docker镜像**: Docker是一个流行的容器化平台，它提供了官方的Docker镜像仓库（Docker Hub），其中包含了各种操作系统、应用程序和工具的镜像。用户可以通过Docker Hub快速获取和部署所需的镜像。

5. **Python镜像**: Python是一种广泛使用的编程语言，它提供了官方的Python镜像仓库（Python Package Index，简称PyPI），其中包含了各种Python库和工具的镜像。用户可以通过PyPI快速下载和安装Python库。

6. **Node.js镜像**: Node.js是一个流行的JavaScript运行时环境，它提供了官方的Node.js镜像仓库（Node.js Package Manager，简称npm），其中包含了各种Node.js模块和工具的镜像。用户可以通过npm快速获取和安装Node.js模

   附：

   相关镜像网站：

   1. **Ubuntu镜像**:
      - 官方Ubuntu镜像站点：[https://releases.ubuntu.com/](https://releases.ubuntu.com/)
      - 清华大学开源软件镜像站：[https://mirrors.tuna.tsinghua.edu.cn/ubuntu/](https://mirrors.tuna.tsinghua.edu.cn/ubuntu/)
      - 中国科学技术大学开源软件镜像站：[https://mirrors.ustc.edu.cn/ubuntu/](https://mirrors.ustc.edu.cn/ubuntu/)

   2. **Debian镜像**:
      - 官方Debian镜像站点：[https://www.debian.org/distrib/netinst](https://www.debian.org/distrib/netinst)
      - 清华大学开源软件镜像站：[https://mirrors.tuna.tsinghua.edu.cn/debian/](https://mirrors.tuna.tsinghua.edu.cn/debian/)
      - 中国科学技术大学开源软件镜像站：[https://mirrors.ustc.edu.cn/debian/](https://mirrors.ustc.edu.cn/debian/)

   3. **CentOS镜像**:
      - 官方CentOS镜像站点：[http://mirror.centos.org/](http://mirror.centos.org/)
      - 清华大学开源软件镜像站：[https://mirrors.tuna.tsinghua.edu.cn/centos/](https://mirrors.tuna.tsinghua.edu.cn/centos/)
      - 中国科学技术大学开源软件镜像站：[https://mirrors.ustc.edu.cn/centos/](https://mirrors.ustc.edu.cn/centos/)

   4. **Docker镜像**:
      - 官方Docker镜像站点（Docker Hub）：[https://hub.docker.com/](https://hub.docker.com/)

   5. **Python镜像**:
      - 官方Python镜像站点（PyPI）：[https://pypi.org/](https://pypi.org/)

   6. **Node.js镜像**:
      - 官方Node.js镜像站点（npm）：[https://www.npmjs.com/](https://www.npmjs.com/)


### 安装 vim wget 等常用工具

#### yum源

1.清华源

安装前，首先进行yum换源

以root用户或具有sudo权限的用户身份执行以下命令，备份当前的Yum源配置文件：

```
sudo cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
```

执行以下命令，使用文本编辑器（如vi或nano）打开 `/etc/yum.repos.d/CentOS-Base.repo` 文件：

```
sudo vi /etc/yum.repos.d/CentOS-Base.repo
```

在编辑器中，删除注释外的配置，以禁用官方源.

在文件的末尾添加以下内容，以添加清华大学的镜像源：

```
[base]
name=CentOS-$releasever - Base - Tsinghua
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/os/$basearch/
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/centos/RPM-GPG-KEY-CentOS-7

[updates]
name=CentOS-$releasever - Updates - Tsinghua
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/updates/$basearch/
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/centos/RPM-GPG-KEY-CentOS-7
```

这将添加两个新的 Yum 源，分别指向清华大学的镜像源，并包含了相应的GPG检查和密钥。

更改完配置如下图

![image-20240529160228887](D:/STUDY/CloudComputing/Essential/linux/3.配置软件仓库/D/image-20240529160228887.png)

保存并关闭文件（在vi中按下 `Esc` 键，然后输入 `:wq` 并按下 `Enter`）。

2.阿里源和163源

```
wget http://mirrors.aliyun.com/repo/Centos-7.repo
wget http://mirrors.163.com/.help/CentOS7-Base-163.repo
```





执行以下命令，清除Yum缓存并重建缓存：

```
sudo yum clean all
sudo yum makecache
```

这将清除旧的Yum缓存并重新生成基于新配置的Yum缓存。



vim-enhanced：vim编辑器工具包

net-tools：含有netstat、ifconfig、route、arp等命令

bash-completion：tab补全功能工具包

wget：下载软件包工具



#### 安装wget 

```
yum install wget -y
```

#### 安装vim

```
yum install vim-enhanced -y
```

#### 安装net-tools

```
yum install net-tools -y
```

#### 安装bash-completion

```
yum install bash-completion -y
```



### 相关文章：

Centos 常用软件安装：https://wlynxg.github.io/blog/Linux/Centos7%20%E5%B8%B8%E7%94%A8%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85/

[Centos安装完成后安装常用软件和工具包]：https://www.cnblogs.com/youngchaolin/p/10957814.html)https://cnblogs.com/youngchaolin/p/10957814.html