# 顺聊 - 上架指南

## 📱 应用信息

- **应用名称**: 顺聊
- **包名**: com.shunliao.app
- **版本**: 1.0.0
- **开发者**: 顺聊团队

## 🏪 上架准备清单

### ✅ 必需文件

- [x] 隐私政策 (PRIVACY.md)
- [x] 用户协议 (TERMS.md)
- [x] 开源许可证 (LICENSE)
- [ ] 应用图标（各种尺寸）
- [ ] 应用截图（手机+平板）
- [ ] 宣传视频（可选）

### ✅ 法律要求

- [ ] 软件著作权登记（中国）
- [ ] ICP备案（如果服务器在中国）
- [ ] 网络安全评估（中国）

### ✅ 技术准备

- [x] Android 版本（APK/AAB）
- [ ] iOS 版本（需要 Mac + Xcode）
- [ ] 后端服务器（如果使用真实 IM）
- [ ] 域名 + SSL 证书

## 📦 打包命令

### Android Debug 版本（测试用）
```bash
cd android
./gradlew assembleDebug
# 输出: android/app/build/outputs/apk/debug/app-debug.apk
```

### Android Release 版本（上架用）
```bash
cd android
./gradlew assembleRelease
# 输出: android/app/build/outputs/apk/release/app-release.apk
```

### 生成签名密钥（首次必须）
```bash
keytool -genkey -v -keystore shunliao-key.keystore -alias shunliao -keyalg RSA -keysize 2048 -validity 10000
```

## 🚀 上架流程

### Google Play Store

1. 注册 Google Play 开发者账号（$25 一次性）
2. 创建应用
3. 填写应用信息
4. 上传 APK/AAB
5. 提交审核（通常 1-3 天）

### 华为应用市场

1. 注册华为开发者联盟
2. 实名认证
3. 上传 APK
4. 填写应用信息
5. 提交审核（通常 3-7 天）

### 小米应用商店

1. 注册小米开发者
2. 软件著作权登记
3. 上传 APK
4. 提交审核

### 应用宝（腾讯）

1. 注册腾讯开放平台
2. 企业认证（必须）
3. 上传 APK
4. 提交审核

## 💡 建议

- 先上架 Google Play（审核最快）
- 准备好软件著作权（国内必须）
- 测试各种屏幕尺寸
- 优化应用启动速度

---

**顺聊团队**
**2026年6月22日**
