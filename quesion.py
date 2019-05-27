import re
from lxml import etree
from config import Config

class Option(object):
    def __init__(self, desc, pos, counter):
        self.desc = desc
        self.pos = pos
        self.counter = counter

    def __repr__(self):
        return '<class Option>'

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
        
    def __eq__(self, other):
        return self.content == other.content

    @classmethod
    def from_xml(cls, filename):
        xml = etree.parse(filename)
        root = xml.getroot()
        xml_question = root.xpath(Config.XPATH_QUESTION)[0]
        content = xml_question.xpath(Config.XPATH_CONTENT)[0]
        xml_options = xml_question.xpath(Config.XPATH_OPTIONS)
        # options = [str(x.xpath(Config.XPATH_OPTOIN_DESC)[0]).strip() for x in xml_options]
        options = []
        for o in xml_options:
            desc = o.xpath(Config.XPATH_OPTOIN_DESC)[0]
            bound_str = o.xpath(Config.XPATH_OPTION_BOUNDES)[0]
            bound = [int(x) for x in re.findall(r'\d+', bound_str)]
            pos = ((bound[0]+bound[1])//2, (bound[1]+bound[3])//2)
            options.append(Option(desc, pos, 0))

        return cls(content, options)

if __name__ == "__main__":
    obj = Question.from_xml('./xmls/ui.xml')
    print(obj)

        
