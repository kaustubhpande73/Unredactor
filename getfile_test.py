import pandas as pd
import unredactor
import pytest
import sys
import os

def get_data(): #Function for importing data
        file = 'unredactor.tsv'
        df = pd.read_csv(file,sep='\t',header=None,error_bad_lines=False,names=['username','file_type','names','redacted_text'])
        return df    
        assert df != None
