'''
Created on 7/1/20

@author: dulanj
'''
import nltk


class MainClass(object):
    def __init__(self):
        self.grammar = nltk.data.load('file:mygrammar.cfg')
        print("=== My Grammar Rules ===")
        for p in self.grammar.productions():print(p)
        print("========================")

    def top_down(self, grammar, text):
        print("Text : {}".format(text))
        sent = text.split()
        rd_parser = nltk.RecursiveDescentParser(grammar)
        for tree in rd_parser.parse(sent):
            print(tree)
        print("------------------")

    def bottom_up(self, grammar, text):
        print("Text : {}".format(text))
        sent = text.split()
        sr_parser = nltk.ShiftReduceParser(grammar)
        for tree in sr_parser.parse(sent):
            print(tree)
        print("------------------")

    def bottom_up_left_corner(self, grammar, text):
        print("Text : {}".format(text))
        sent = text.split()
        parser = nltk.parse.BottomUpLeftCornerChartParser(grammar)
        for tree in parser.parse(sent):
            print(tree)
        print("------------------")

    def main(self):
        print("================= Top down =================")
        self.top_down(self.grammar, "book that flight")
        self.top_down(self.grammar, "can you book TWA flights")
        print("================= Bottom up ========================")
        self.bottom_up(self.grammar, "book that flight")
        self.bottom_up(self.grammar, "can you book TWA flights")
        print("================= Top Down & Bottom up ========================")
        self.bottom_up_left_corner(self.grammar, "book that flight")
        self.bottom_up_left_corner(self.grammar, "can you book TWA flights")


if __name__ == "__main__":
    obj = MainClass()
    obj.main()
