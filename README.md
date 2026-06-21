# 顺聊 (ShunLiao)

<div align="center">

💬 **一款简洁、快速的即时通讯应用**

[![GitHub release](https://img.shields.io/github/v/release/你的用户名/shunliao-app?style=flat-square)](https://github.com/你的用户名/shunliao-app/releases)
[![GitHub downloads](https://img.shields.io/github/downloads/你的用户名/shunliao-app/total?style=flat-square)](https://github.com/你的用户名/shunliao-app/releases)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

</div>

---

## ✨ 功能特性

- 🚀 **快速聊天** - 实时消息推送
- 👥 **通讯录管理** - 轻松管理联系人
- 🔍 **发现页** - 朋友圈、扫一扫等功能
- 👤 **个人中心** - 完善的个人资料管理
- 📱 **跨平台** - 支持 Android、iOS、Web
- 🎨 **简洁界面** - 绿色主题，清新舒适

---

## 📱 下载安装

### 方法一：从 Release 下载（推荐）

1. 访问 [Releases](https://github.com/你的用户名/shunliao-app/releases) 页面
2. 下载最新版本的 `app-debug.apk` 或 `app-release.apk`
3. 在 Android 手机上安装（需要允许"安装未知来源应用"）

### 方法二：从源码构建

```bash
# 克隆项目
git clone https://github.com/你的用户名/shunliao-app.git
cd shunliao-app

# 安装依赖
npm install

# 同步到 Android
npx cap sync android

# 构建 APK
cd android
./gradlew assembleDebug
```

---

## 🛠️ 技术栈

- **前端**: HTML5 + CSS3 + JavaScript
- **跨平台框架**: Capacitor
- **即时通讯**: 腾讯云 IM（可选）
- **构建工具**: GitHub Actions（自动打包）

---

## 🚀 开发计划

- [x] 基础聊天功能
- [x] 通讯录管理
- [x] 发现页
- [x] 个人中心
- [ ] 图片/语音消息
- [ ] 群聊功能
- [ ] 好友系统
- [ ] 视频通话

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 👨‍💻 作者

**顺聊团队**

- GitHub: [@你的用户名](https://github.com/你的用户名)
- 邮箱: your-email@example.com

---

<div align="center">

⭐ 如果这个项目对你有帮助，请给它一个 Star！

</div>
