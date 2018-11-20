// pages/account_bind/index.js
const app = getApp();
const api = require('../../utils/api.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
      userInfo: {},
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
        this.setData({
            openid: options.openid
        });
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
      var that = this
      //调用应用实例的方法获取全局数据
      that.setData({
          userInfo: app.globalData.userInfo
      })
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

  formSubmit:function(e){
      var formdata = e.detail.value;
      formdata['openid'] = this.data.openid; 
      api.account_bind(formdata,function(res){
          if (res.data.code === '200') {
              wx.setStorageSync('token', res.data.data.token);
              wx.setStorageSync('user_info', res.data.data);
              wx.reLaunch({
                  url: '/pages/annunciate/index',
              });
          } else {
              wx.showToast({
                  title: res.data.message,
                  icon: 'none',
                  duration: 2000
              })

          }
      });
  }
})