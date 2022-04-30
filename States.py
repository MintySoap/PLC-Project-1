class States:

    def __init__(self,T):
        self.marked = False
        self.state = T
        self.category = "delta"
    
    def get_marked(self):
        return self.marked

    def get_state(self):
        return self.state

    def get_category(self):
        return self.category

    def set_state(self,T):
        self.state = T

    def set_category(self,cat):
        self.category=cat
    
    def set_marked(self, mark):
        self.marked = mark

    def __str__(self):
        return (self.category+"\("+str(self.state))