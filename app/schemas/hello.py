class Hello ():

    def __init__ (self, content: str):
        
        import json
        
        if type(content) == str:
            content = json.loads(content)
            
        self.content = content
        
    def get_content (self):
        return self.content