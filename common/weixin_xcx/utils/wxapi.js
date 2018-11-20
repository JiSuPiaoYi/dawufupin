/**
 * time:2018-07-07
 * author:许志文
 * comment:存放微信api请求
 */

function request(url, method = 'GET', params, successCall, failCall) {
    if (!('token' in params)) {
        let token = wx.getStorageSync("token");
        params['token'] = token;
    }

    var content_type;
    if(method === 'GET'){
        content_type = 'application/json'
    }else{
        content_type = 'application/x-www-form-urlencoded'
    }

    wx.request({
        url: url,
        method: method,
        data: params,
        header: {
            'content-type': content_type // 默认值
        },
        success: successCall,
        fail: function () {
            console.log('请求接口失败' + method + ':' + url + ';\n参数：' + JSON.stringify(params))
        }
    })
}



module.exports = {
    request: request,
}