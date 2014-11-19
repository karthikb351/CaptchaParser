unirest = require("unirest");
captcha = require("../CaptchaParser");
fs = require("fs");
var captchaUri = 'https://academics.vit.ac.in/parent/captcha.asp';
var getPixelMapFromBuffer = function (bitmapBuffer) {
    var pixelMap = [];
    var subArray = [];
    var row = 0;
    for (var i = bitmapBuffer.length - (25 * 132), r = 0; i < bitmapBuffer.length; ++i, ++r) {
        if (Math.floor(r / 132) !== row) {
            row = Math.floor(r / 132);
            pixelMap.push(subArray);
            subArray = [];
        }
        subArray.push(bitmapBuffer.readUInt8(i));
    }
    pixelMap.push(subArray);
    pixelMap.reverse();
    return pixelMap;
};

var onRequest = function (response) {
    if (response.error) {
        console.log('VIT Academics connection failed');
    }
    else {
    	pixMap = getPixelMapFromBuffer(response.body);
    	fs.writeFileSync("captcha.bmp", response.body);
    	//console.log(pixMap[3][14]);
        console.log(captcha.getCaptcha(pixMap));
    }
};
unirest.get(captchaUri)
    .encoding(null)
    .set('Content-Type', 'image/bmp')
    .end(onRequest);