# Access Modifiers
# =================

# public modifier
class ABC:
    def __init__(self):
        self.public_attribute = None # This is a public attribute
    
    def public_function():  # this is a public function
        pass
    

# Private modifier
class ABC:
    def __init__(self):
        self._private_attribute = None # this is a private attribute
          
    def _private_fuction(): # This is a private function      
        pass    
    
# Protected Access Modifier
class ABC:
    def _protected_method(self):
        self.__protected_attribute = 10 # This is a protected attribute
        
    def __protected_function(): # this is a protected function
        pass          
