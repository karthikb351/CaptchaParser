unirest = require("unirest");
captcha = require("../CaptchaParser");
fs = require("fs");
var captchaUri = 'https://academics.vit.ac.in/parent/captcha.asp';

var onRequest = function (response) {
    if (response.error) {
        console.log('VIT Academics connection failed');
    }
    else {
    	pixMap = getPixelMapFromBuffer(response.body);
    	fs.writeFileSync("captcha.bmp", response.body);
        console.log(captcha.getCaptcha(pixMap));
    }
};
unirest.get(captchaUri)
    .encoding(null)
    .set('Content-Type', 'image/bmp')
    .end(onRequest);