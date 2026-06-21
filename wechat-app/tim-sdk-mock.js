/**
 * 顺聊 - 模拟 TIM SDK（开发测试用）
 * 当无法连接腾讯云时使用此模拟版本
 * 生产环境请使用真实 TIM SDK
 */

var TIM = window.TIM || {};

// 模拟事件类型
TIM.EVENT = {
  SDK_READY: 'sdk_ready',
  MESSAGE_RECEIVED: 'message_received',
  ERROR: 'error',
  CONVERSATION_LIST_UPDATED: 'conversation_list_updated',
  SDK_NOT_READY: 'sdk_not_ready',
};

TIM.TYPES = {
  MSG_TEXT: 'MSG_TEXT',
  CONV_C2C: 'C2C',
  CONV_GROUP: 'GROUP',
};

// 模拟 UserSig 验证（简单 base64 解码检查）
function parseUserSig(userSig) {
  try {
    var compressed = Buffer.from(userSig, 'base64');
    var jsonStr = require('zlib').unzipSync ? '' : '';
    // 浏览器环境简化处理
    return { valid: true };
  } catch (e) {
    return { valid: false };
  }
}

// 本地存储的会话数据
var localConversations = {};
var localMessages = {};

// 创建 TIM 实例
TIM.create = function (options) {
  var sdkAppID = options.SDKAppID;
  var isMock = true; // 模拟模式

  var eventListeners = {};

  var timInstance = {
    // 登录
    login: function (params) {
      return new Promise(function (resolve, reject) {
        var userID = params.userID;
        var userSig = params.userSig;

        if (!userID) {
          reject(new Error('userID is required'));
          return;
        }

        // 模拟登录验证
        setTimeout(function () {
          // 保存用户信息
          timInstance.currentUser = userID;
          
          // 触发 SDK_READY 事件
          setTimeout(function () {
            if (eventListeners[TIM.EVENT.SDK_READY]) {
              eventListeners[TIM.EVENT.SDK_READY].forEach(function (cb) {
                cb({});
              });
            }
          }, 500);

          resolve({
            data: {
              repeatLogin: false,
              userID: userID
            }
          });
        }, 800);
      });
    },

    // 退出登录
    logout: function () {
      return new Promise(function (resolve) {
        timInstance.currentUser = null;
        resolve({});
      });
    },

    // 获取会话列表
    getConversationList: function () {
      return new Promise(function (resolve) {
        var convList = Object.values(localConversations);
        resolve({
          data: {
            conversationList: convList
          }
        });
      });
    },

    // 创建文本消息
    createTextMessage: function (options) {
      return {
        type: 'MSG_TEXT',
        to: options.to,
        conversationType: options.conversationType,
        payload: options.payload,
        from: timInstance.currentUser,
        time: Date.now(),
        _options: options
      };
    },

    // 发送消息
    sendMessage: function (message) {
      return new Promise(function (resolve, reject) {
        if (!timInstance.currentUser) {
          reject(new Error('Not logged in'));
          return;
        }

        setTimeout(function () {
          // 存到本地消息记录
          var key = message.conversationType + '_' + message.to;
          if (!localMessages[key]) localMessages[key] = [];
          localMessages[key].push(message);

          // 模拟对方回复（如果是发给 user002，模拟 user002 回复）
          if (message.to === 'user002' && timInstance.currentUser !== 'user002') {
            setTimeout(function () {
              var replyMsg = {
                type: 'MSG_TEXT',
                from: 'user002',
                to: timInstance.currentUser,
                payload: { text: '收到！（模拟回复）' },
                time: Date.now()
              };
              if (eventListeners[TIM.EVENT.MESSAGE_RECEIVED]) {
                eventListeners[TIM.EVENT.MESSAGE_RECEIVED].forEach(function (cb) {
                  cb({ data: [replyMsg] });
                });
              }
            }, 1500);
          }

          resolve({ data: message });
        }, 300);
      });
    },

    // 获取消息列表
    getMessageList: function (options) {
      return new Promise(function (resolve) {
        var key = options.conversationType + '_' + options.to;
        var msgs = localMessages[key] || [];
        resolve({
          data: {
            messageList: msgs
          }
        });
      });
    },

    // 监听事件
    on: function (eventName, callback) {
      if (!eventListeners[eventName]) eventListeners[eventName] = [];
      eventListeners[eventName].push(callback);
    },

    // 取消监听
    off: function (eventName, callback) {
      if (eventListeners[eventName]) {
        eventListeners[eventName] = eventListeners[eventName].filter(function (cb) {
          return cb !== callback;
        });
      }
    },

    // 销毁实例
    destroy: function () {
      timInstance.currentUser = null;
      eventListeners = {};
      return Promise.resolve({});
    },

    currentUser: null
  };

  return timInstance;
};

// 导出
if (typeof module !== 'undefined' && module.exports) {
  module.exports = TIM;
}

window.TIM = TIM;
console.log('[顺聊] 模拟 TIM SDK 已加载（开发测试模式）');
