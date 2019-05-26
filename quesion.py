import re
from lxml import etree
from config import Config



class Question(object):
    def __init__(self, content, options, answer=''):
        self.content = content
        self.options = options
        self.answer = answer
    
    def __repr__(self):
        return '<class Question> %r' %self.content
    
    def __str__(self):
        op = " ".join(self.options)
        return f'{self.content}\n{op}'

    @classmethod
    def from_xml(cls, filename):
        xml = etree.parse(filename)
        root = xml.getroot()
        xml_question = root.xpath(Config.XPATH_QUESTION)[0]
        content = xml_question.xpath(Config.XPATH_CONTENT)[0]
        xml_options = xml_question.xpath(Config.XPATH_OPTIONS)

        options = [str(x.xpath(Config.XPATH_OPTOIN_DESC)[0]).strip() for x in xml_options]
        return cls(content, options)

if __name__ == "__main__":
    obj = Question.from_xml('./xmls/ui.xml')
    print(obj)

        
