// pages/poor_house/index.js
const api = require('../../utils/api.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
      user_info: null,
      page_type:2,//1为搜索，2为列表
      is_hide_search_modal:true,
      name:'',
      idcard:'',
      page: 0,
      count: 0,
      num_pages:0,
      every_page_number: 0,
      poorhouse_list:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
      var user_info = wx.getStorageSync('user_info');
      this.setData({
          user_info: user_info
      });
      if (user_info.department_id == 28){
          this.get_poorhouse_list();
          this.setData({
              page_type:2
          })
      }else{
          this.setData({
              page_type: 1
          })
      }
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
      var next_page = this.data.page+1;
      if (next_page > this.data.num_pages){
          return;
      }
    this.setData({
        page:next_page
    });
      this.get_poorhouse_list();
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  },
  //获取贫困户列表
  get_poorhouse_list:function(){
      var that = this;
    console.log(that.data.page);
      wx.showLoading({
          title: '玩命加载中',
      });
      api.poorhouse_list({
          "name":that.data.name,
          "idcard":that.data.idcard,
          "page": that.data.page+1,
          "token":that.data.user_info.token
      },function(res){
          wx.hideLoading();
          that.setData({
              page: res.data.page,
              count: res.data.count,
              num_pages: res.data.num_pages,
              every_page_number: res.data.every_page_number,
              poorhouse_list: that.data.poorhouse_list.concat(res.data.poorhouse_list)
          });
          if (that.data.poorhouse_list.length === 0){
              that.setData({
                  page:0
              });
          }else{
              that.setData({
                  is_hide_search_modal: true
              });
          }
      });
  },
  //显示搜索模态框
  show_search_modal: function () {
      this.setData({
          is_hide_search_modal: false
      });
  },
  //隐藏搜索模态框
  hide_search_modal:function(){
      this.setData({
          is_hide_search_modal: true
      });
  },
//   set_data:function(event){
//       var field = event.currentTarget.dataset.field;
//       var value = event.detail.value;
//     if(field === 'name'){
//         this.setData({
//             name: value
//         });
//     }else if(field === 'idcard'){
//         this.setData({
//             idcard: value
//         });
//     }
//   },
  formSubmit:function(event){
      var formdata = event.detail.value;
      var flag = false;//提交的表单是否有一项有值
      for (var key in formdata) {
          var value_trim = formdata[key].replace(/(^\s*)|(\s*$)/g, "");
          if (value_trim){
              flag = true;
          }
      }
      if(!flag){
          wx.showToast({
              title: "请输入搜索条件",
              icon: 'none',
              duration: 2000
          });
          return ;
      }

      this.setData({
          page:0,
          poorhouse_list: [],
          page_type:2
      });

      this.setData({
          name:formdata.name,
          idcard:formdata.idcard
      });
      this.get_poorhouse_list();
  }
})