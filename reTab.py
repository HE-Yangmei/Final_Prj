# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:20:34 2019

@author: Administrator
"""

#-*- coding:utf-8 -*-
import sys
import os
 
if __name__ == '__main__':
 
    #sys.argv[0]这个参数是脚本名称.
    try:
        sourceFilePath = sys.argv[1];   #参数1
        outFilePath    = sys.argv[2];   #参数2
        ifExists = os.path.exists(sourceFilePath)
        if not ifExists:
            print "Error:The Source file not exists!~-";
            sys.exit();
        
        
        with open(sourceFilePath , "r") as f:
            sourceFileStr = f.read();
        #四个空格
        outFileStr = sourceFileStr.replace("\t","    ");
        
        with open(outFilePath,"a+") as w:
            w.write(outFileStr);
        
        print "replace success! , output path : " + outFilePath;
    except Exception as e:
        print e;
        print "Error:get args error,  ex: python xxx.py sourceFile  outFile  .....";