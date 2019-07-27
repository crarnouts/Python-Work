# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:33:36 2019

@author: arnou
"""

class PandasChain:
    # 5 pts - Complete this constructor
    def __init__(self, name): 
        self.__name = name.upper() # Convert name to upper case and store it here

    def add_transaction(self,s,r,v): 
        if self.__current_block.get_size() >= 10:
            self.__commit_block(self.__current_block)
        self.__current_block.add_transaction(s,r,v)
    
    
class Block:
    # 5 pts for constructor
    def __init__(self,seq_id,prev_hash): 
        self.__seq_id = seq_id
        self.__prev_hash = prev_hash
        self.__col_names = ['Timestamp','Sender','Receiver','Value','TxHash']
        self.__transactions = # Create a new blank DataFrame with set headers
        self.__status = # Initial status. This will be a string.
        self.__block_hash = None
        self.__merkle_tx_hash = None