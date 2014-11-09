# CaptchaParser

A simple Captcha parsing algorithm developed for VITacademics.

## Quickstart

### Python Usage

Include the ```CaptchaParser.py``` file in the directory you are working in, else install it globally so you can import it from anywhere.

```python
from CaptchaParser import CaptchaParser

img=Image.open("captcha.bmp")
parser=CaptchaParser()
captcha=parser.getCaptcha(img)
print captcha
```

### Nodejs Usage

Still under development.

## Bugs and feature requests

Have a bug or a feature request? If your problem or idea is not addressed yet, [please open a new issue](https://github.com/karthikb351/ProntoUsage/issues).

## Contributing and License

Contribute away. Let's see them PRs.

Code released under [the MIT license](LICENSE).