// pages/feedback/index.js
const api = require('../../utils/api.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
      select_list: [
          { "id": 1, "name": "建议" },
          { "id": 2, "name": "贫困户基本信息数据问题" },
          { "id": 3, "name": "贫困户享受政策数据问题" },
          { "id": 4, "name": "其他问题" },
      ],
      about_objects: ["请选择","贫困户户主姓名", "贫困户户主身份证号", "贫困人口姓名","贫困人口身份证号"],
      about_index:null,
      select_feedback_type: null,//选择的建议类型id
      select_feedback_type_index:null,
      content: null,
      files:[]
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

  write_content: function (event) {
      this.setData({
          content: event.detail.value
      });
  },
  //选择建议类型
  select_feedback_type_func: function (event) {
      var index = event.detail.value;
      var select_feedback_type_id = this.data.select_list[index].id;
      this.setData({
          select_feedback_type_id: select_feedback_type_id,
          select_feedback_type_index:index
      });
  },
  formSubmit: function (e) {
      var that = this;
      console.log('form发生了submit事件，携带数据为：', e.detail.value)

      var content = e.detail.value.content;
      var about_object_content = e.detail.value.about_object_content;
      var about_object = '';

      if (that.data.about_index && that.data.about_index != 0){
          about_object = that.data.about_objects[that.data.about_index];
      }else{
          about_object = null;
      }

      if ((about_object && !about_object_content) || (!about_object && about_object_content)) {
          wx.showToast({
              title: '请补全涉及对象相关资料',
              icon: 'none'
          });
          return;
      }

      if (content === '' || !that.data.select_feedback_type_id) {
          return;
      }

      var type = '';
      var select_list = that.data.select_list;
      for (var i = 0; i < select_list.length; i++) {
          if (select_list[i].id == that.data.select_feedback_type_id) {
              type = select_list[i].name;
              break
          }
      }


      const app = new getApp();
      const api_host = app.globalData.globalUrl;
      let token = wx.getStorageSync("token");
      wx.showLoading({
          title: '提交中',
          mask:true
      });
      if (that.data.files.length > 0){
          wx.uploadFile({
              url: api_host + '/weixin_xcx/feedback/',
              filePath: that.data.files[0],
              name: 'file',
              formData: {
                  "token": token,
                  "type": type,
                  "content": content,
                  "about_object": about_object,
                  "about_object_content": about_object_content
              },
              success: function (res) {
                  wx.hideLoading();
                  if (res.statusCode === 200){
                      wx.showModal({
                          title: '提示',
                          content: '感谢您的建议和反馈！',
                          confirmText: '继续建议',
                          cancelText: '关闭',
                          success: function (res) {
                              if (res.confirm) {
                                  wx.reLaunch({
                                      url: '/pages/feedback/index'
                                  });
                              } else if (res.cancel) {

                              }
                          }
                      })
                  }
              }
          })
      }else{
          api.feedback({
              "type": type,
              "content": content,
              "about_object": about_object,
              "about_object_content": about_object_content
          }, function (res) {
              wx.hideLoading();
              if(res.data.code === '200'){
                  wx.showModal({
                      title: '提示',
                      content: '感谢您的建议和反馈！',
                      confirmText: '继续建议',
                      cancelText: '关闭',
                      success: function (res) {
                          if (res.confirm) {
                              wx.reLaunch({
                                  url: '/pages/feedback/index'
                              });
                          } else if (res.cancel) {

                          }
                      }
                  })
              }
          });
      }

  },
  chooseImage: function (e) {
      var that = this;
      wx.chooseImage({
          sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
          sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
          success: function (res) {
              // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
              that.setData({
                  //files: that.data.files.concat(res.tempFilePaths)
                  files: [res.tempFilePaths[0]]
              });
          }
      })
  },
  previewImage: function (e) {
      wx.previewImage({
          current: e.currentTarget.id, // 当前显示图片的http链接
          urls: this.data.files // 需要预览的图片http链接列表
      })
  },
    bindAboutIndexChange:function(e){
        this.setData({
            about_index: e.detail.value
        })
    }
})