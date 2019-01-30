class Instructions():
    def __init__(self):
        self.string = ""

    def get(self, name):
        getattr(self, name.lower())()
        return self

    def double07(self):
        self.string = """
            Insert Instructions Here
        """

    def hot_potato(self):
        self.string = """
            Insert Instructions Here
        """

    def match(self):
        self.string = """
            Insert Instructions Here
        """

    def fragments(self):
        self.string = """
            Insert Instructions Here
        """

    def multigame(self):
        self.string = """
            Insert Instructions Here
        """