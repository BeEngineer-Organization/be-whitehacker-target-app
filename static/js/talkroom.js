'use strict';

// テキスト内のURLをリンクに置き換える関数
function replaceURLWithLink(text) {
    // URLを検出する正規表現
    var urlRegex = /(https?:\/\/[^\s]+)/g;
    return text.replace(urlRegex, function(url) {
        return '<a href="' + url + '">' + url + '</a>';
    });
}

// 対象の要素を取得し、テキストを取得して置き換える
var contentDivs = document.getElementsByClassName('replace');

for(var i = 0; i < contentDivs.length; i++) {
    contentDivs[i].innerHTML = replaceURLWithLink(contentDivs[i].innerHTML); 
}