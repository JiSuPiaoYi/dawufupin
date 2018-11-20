$(function () {
    $('#id_content').before('<div id="editor" style="display: inline-block;"><p>'+$("#id_content").val()+'</p></div>');
    var E = window.wangEditor;
    var editor = new E('#editor');
    editor.customConfig.onchange = function (html) {
    	$("#id_content").val(html);
    }
    editor.create();
});