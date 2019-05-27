import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    XML_URI = os.path.join(basedir, 'ui.xml')
    DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    # 解析xml的xpath规则，针对不同xml规则不同
    XPATH_QUESTION = '//node[@class="android.webkit.WebView"]/node/node[@index="2"]/node/node[@index="1"]/node[@index="0"]'
    XPATH_CONTENT = './node[@index="0"]/@content-desc'
    XPATH_OPTIONS = './node[@index="1"]//node/node[@index="1"]'
    XPATH_OPTOIN_DESC = './@content-desc'
    XPATH_OPTION_BOUNDES = './@bounds'
    HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}