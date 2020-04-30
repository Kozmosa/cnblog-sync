import logging


class PreProcessor:
    def __init__(self):
        self.fhandler = logging.FileHandler(
            "log/preprocess.log", mode='w', encoding=None, delay=False)
        self.flogger = logging.getLogger("preprocessor")
        self.flogger.addHandler(self.fhandler)
        self.flogger.setLevel(logging.INFO)

    def process(self, content, options={}):
        self.flogger.info("Processing Mathjax")
        try:
            content = self.mathjax(content)
        except:
            self.flogger.error("Mathjax Processed Error")
        
        self.flogger.info("Processing Front matter")
        try:
            content = self.front_matter(content, options)
        except:
            self.flogger.error("Front Matter Processed Error")

        return content

    def mathjax(self, content):
        # content = content.replace("$frac", "{% raw %} $frac")
        # content = content.replace("}$", "}$ {% endraw %}")
        content = content.replace("{", "\{")
        content = content.replace("}", "\}")
        return content

    def front_matter(self, content, options={}):
        template = """---
title: TITLE
author: AUTHOR
date: DATE
mathjax: true
---
"""
        result = template.replace("TITLE", options['title'])
        result = result.replace("AUTHOR", options['author'])
        result = result.replace("DATE", options['date'])
        content = result + content
        return content
