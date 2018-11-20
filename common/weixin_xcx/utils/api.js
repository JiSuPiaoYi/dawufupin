/**
 * time:2018-07-07
 * author:许志文
 * comment:存放后台api请求
 */

const app = new getApp();
const api_host = app.globalData.globalUrl;
const wxapi = require("./wxapi.js");


//判断是否完成了微信帐号绑定
function is_account_bind(params, successCall) {
    let url = api_host + '/weixin_xcx/is_account_bind/';
    wxapi.request(url, "POST", params, successCall);
}

//小程序微信登录后帐号绑定
function account_bind(params, successCall) {
    let url = api_host + '/weixin_xcx/account_bind/';
    wxapi.request(url, "POST", params, successCall);
}

//通告列表
function annunciate_list(params, successCall) {
    let url = api_host + '/weixin_xcx/annunciate_list/';
    wxapi.request(url, "GET", params, successCall);
}

//通告详情
function annunciate_info(params, successCall) {
    let url = api_host + '/weixin_xcx/annunciate_info/';
    wxapi.request(url, "GET", params, successCall);
}

//政令列表
function governmentdecree_list(params, successCall) {
    let url = api_host + '/weixin_xcx/governmentdecree_list/';
    wxapi.request(url, "GET", params, successCall);
}

//政令详情
function governmentdecree_info(params, successCall) {
    let url = api_host + '/weixin_xcx/governmentdecree_info/';
    wxapi.request(url, "GET", params, successCall);
}

//用户信息
function user_info(params, successCall) {
    let url = api_host + '/weixin_xcx/user_info/';
    wxapi.request(url, "GET", params, successCall);
}

//修改密码
function change_password(params, successCall) {
    let url = api_host + '/weixin_xcx/change_password/';
    wxapi.request(url, "POST", params, successCall);
}

//获取贫困户列表
function poorhouse_list(params, successCall) {
    let url = api_host + '/weixin_xcx/poorhouse_list/';
    wxapi.request(url, "GET", params, successCall);
}

//获取贫困户详情
function poorhouse_detail(params, successCall) {
    let url = api_host + '/weixin_xcx/poorhouse_detail/';
    wxapi.request(url, "GET", params, successCall);
}

//账号解绑
function relieve_bind(params, successCall) {
    let url = api_host + '/weixin_xcx/relieve_bind/';
    wxapi.request(url, "POST", params, successCall);
}

//意见反馈
function feedback(params, successCall) {
    let url = api_host + '/weixin_xcx/feedback/';
    wxapi.request(url, "POST", params, successCall);
}

module.exports = {
    is_account_bind: is_account_bind,
    account_bind: account_bind,
    annunciate_list: annunciate_list,
    annunciate_info: annunciate_info,
    governmentdecree_list: governmentdecree_list,
    governmentdecree_info: governmentdecree_info,
    user_info: user_info,
    change_password: change_password,
    poorhouse_list: poorhouse_list,
    poorhouse_detail: poorhouse_detail,
    relieve_bind: relieve_bind,
    feedback: feedback
}