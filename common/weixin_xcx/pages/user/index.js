// pages/user/index.js
const app = getApp();
const api = require('../../utils/api.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
      userInfo:{},
      user_info:{}
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
    this.setData({
        userInfo: app.globalData.userInfo
    });
    var user_info = wx.getStorageSync('user_info');
    this.setData({
        user_info: user_info
    });
    //this.get_user_info();
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

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  },
  //获取用户信息
  get_user_info:function(){
      var that = this;
    api.user_info({},function(res){
        that.setData({
            user_info:res.data.data
        });
    });
  },
  //账号解绑
  relieve_bind:function(){
      var that = this;
      var token = wx.getStorageSync('token');
      wx.showModal({
          title: '提示',
          content: '确定要退出登录吗？',
          success: function (res) {
              if (res.confirm) {
                  api.relieve_bind({
                      "token": token
                  }, function (res) {
                      if (res.data.code === '200') {
                          wx.setStorageSync('token', '');
                          wx.showToast({
                              title: res.data.message,
                              icon: 'success',
                              duration: 2000,
                              complete: function (toastRes) {
                                  wx.reLaunch({
                                      url: '/pages/login/index'
                                  });
                              }
                          });
                      } else {
                          wx.showToast({
                              title: res.data.message,
                              icon: 'none',
                              duration: 2000
                          })
                      }
                  });
              } else if (res.cancel) {
                  console.log('取消解绑')
              }
          }
      });

  }
})