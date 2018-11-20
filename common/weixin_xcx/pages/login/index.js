// pages/login/index.js

const app = getApp();
const api = require('../../utils/api.js');
const util = require('../../utils/util.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
      progress_percent:0,
      hasUserInfo: true,
      canIUse: wx.canIUse('button.open-type.getUserInfo')
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
      var that = this;


      that.setData({
          progress_percent: 5
      });//设置进度条百分比

      var system_info = wx.getSystemInfoSync();
      var is_can_sdk = util.compareVersion(system_info.SDKVersion,'1.9.0');
      if (is_can_sdk === -1){
          wx.showModal({
              title: '提示',
              showCancel:false,
              content: '当前微信版本过低，请升级到最新微信版本后重试。'
          });
          return;
      }


      // 获取用户信息
      wx.getSetting({
          success: res => {
              that.setData({
                  progress_percent: 20
              });//设置进度条百分比
              if (res.authSetting['scope.userInfo']) {
                  // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框

                  wx.getUserInfo({
                      success: userInfoRes => {
                          that.setData({
                              progress_percent: 40
                          });//设置进度条百分比

                          // 可以将 res 发送给后台解码出 unionId
                          app.globalData.userInfo = userInfoRes.userInfo;

                          that.setData({
                              hasUserInfo: true
                          });
                          that.query_user();
                      }
                  });

              }else{
                  //没有授权
                  that.setData({
                      hasUserInfo: false
                  }); 
                  if (!that.data.canIUse) {
                      // 在没有 open-type=getUserInfo 版本的兼容处理
                      wx.getUserInfo({
                          success: userInfoRes => {
                              that.setData({
                                  progress_percent: 40
                              });//设置进度条百分比

                              app.globalData.userInfo = userInfoRes.userInfo
                              that.setData({
                                  hasUserInfo: true
                              });
                              that.query_user();
                          }
                      })
                  }else{
                      that.setData({
                          progress_percent: 40
                      });//设置进度条百分比
                  }
              }
          }
      });
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },
  getUserInfo: function (e) {
      console.log(e)
      app.globalData.userInfo = e.detail.userInfo
      this.setData({
          hasUserInfo: true
      });
      this.query_user();
  },
  query_user:function(){
      var that = this;
      that.setData({
          progress_percent: 60
      });//设置进度条百分比
      // 登录
      wx.login({
          success: loginRes => {
              that.setData({
                  progress_percent: 80
              });//设置进度条百分比

              // 发送 res.code 到后台换取 openId, sessionKey, unionId
              api.is_account_bind({
                "code":loginRes.code
              },function(res){
                  that.setData({
                      progress_percent: 100
                  });//设置进度条百分比

                    var code = res.data.code;
                    var openid = res.data.data.openid;
                    var url;
                    if(code === '200'){
                        wx.setStorageSync('token', res.data.data.token);
                        wx.setStorageSync('user_info', res.data.data);
                        wx.reLaunch({
                            url: '/pages/annunciate/index'
                        })
                    } else if (code === '40001'){
                        wx.reLaunch({
                            url: '/pages/account_bind/index?openid='+openid
                        })
                    }else{
                        wx.showModal({
                            title: '提示',
                            content: res.message,
                            showCancel:false
                        })
                    }
              });
                
          }
      })
  }
})