from datetime import datetime
import hashlib
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class CreateBranch:
    def __init__(self,text):
        self.text = text
    
    def create_log(self):
        self.dt = datetime.now()
        seed = str(self.dt)
        self.hash = hashlib.sha256(seed.encode())
        self.hash_16 = self.hash.hexdigest()
        return [self.text,self.dt,self.hash_16]