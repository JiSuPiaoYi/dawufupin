// pages/poor_house_detail/index.js
const api = require('../../utils/api.js');
var sliderWidth = 96; // 需要设置slider的宽度，用于计算中间位置
Page({

  /**
   * 页面的初始数据
   */
  data: {
    data_id:null,
    detail:{},
    policy_list:[],

    tabs: ["基本信息", "享受政策"],
    activeIndex: 0,
    sliderOffset: 0,
    sliderLeft: 0,

    select_date_index:0,
    select_date_list:[],
      policy_list_dict:{},
      policy_list_display_dict:{}
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
        data_id:options.id,
        home_location: options.home_location
    });

    var that = this;
    wx.getSystemInfo({
        success: function (res) {
            that.setData({
                sliderLeft: (res.windowWidth / that.data.tabs.length - sliderWidth) / 2,
                sliderOffset: res.windowWidth / that.data.tabs.length * that.data.activeIndex
            });
        }
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
      this.get_poorhouse_detail();
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
  tabClick: function (e) {
      this.setData({
          sliderOffset: e.currentTarget.offsetLeft,
          activeIndex: e.currentTarget.id
      });
  },
  //获取贫困户详情
  get_poorhouse_detail:function(){
      wx.showLoading({
          title: '玩命加载中',
      });
      var that = this;
      api.poorhouse_detail({
          "id": that.data.data_id
      },function(res){
          wx.hideLoading();
          var policy_list = res.data.data.policy_list;
          var four_one_list = res.data.data.four_one_list;
          var select_date_array = [];
          for (var i = 0; i < policy_list.length;i++){
              select_date_array.push(policy_list[i].date_year);
          }
          var select_date_set = new Set(select_date_array);
          var select_date_list = Array.from(select_date_set);
          select_date_list.sort();
          select_date_list.unshift("所有");

            var policy_list_dict = {};
          for (var i in policy_list) {

          }
            for(var i in policy_list){
                var layer_list = [];
                if (policy_list[i].policy_first_layer){
                    layer_list.push(policy_list[i].policy_first_layer);
                }
                if (policy_list[i].policy_second_layer){
                    layer_list.push(policy_list[i].policy_second_layer);
                }
                if (policy_list[i].policy_third_layer) {
                    layer_list.push(policy_list[i].policy_third_layer);
                }
                if (!policy_list_dict[layer_list.join(',')]){
                    policy_list_dict[layer_list.join(',')] = []
                }
                policy_list_dict[layer_list.join(',')].push(policy_list[i]);
            }
          if (four_one_list.length > 0){
              policy_list_dict['健康扶起来.重病兜底保障一批.“四位一体”一站式服务'] = four_one_list;
          } console.log(four_one_list)
        
        that.setData({
            detail:res.data.data.detail,
            policy_list: policy_list,
            select_date_list: select_date_list,
            policy_list_dict: policy_list_dict,
            policy_list_dict_copy: policy_list_dict
        });
      });
  },
  select_date: function (event){
      var that = this;
      var index = event.detail.value;
      var year = that.data.select_date_list[index];
      var policy_list_dict_copy = that.data.policy_list_dict_copy;
      var policy_list_dict = {};
      for (var i in policy_list_dict_copy){
          if (policy_list_dict[i] === undefined){
              policy_list_dict[i] = []
          }
          for (var j in policy_list_dict_copy[i]){
              if (policy_list_dict_copy[i][j].date_year == year) {
                  policy_list_dict[i].push(policy_list_dict_copy[i][j]);
              }
          }
          
      }
      var policy_list_dict_ = {};
      for (var i in policy_list_dict){
          if (policy_list_dict[i].length){
              policy_list_dict_[i] = policy_list_dict[i];
          }
      }
      that.setData({
          select_date_index: index,
          policy_list_dict: policy_list_dict_
      });
  },
    policy_list_display_func:function(event){
        var policy_name = event.currentTarget.dataset.policy_name;
        var policy_list_display_dict = this.data.policy_list_display_dict;
        policy_list_display_dict[policy_name] = !policy_list_display_dict[policy_name];
        this.setData({
            policy_list_display_dict: policy_list_display_dict
        });
    }
})