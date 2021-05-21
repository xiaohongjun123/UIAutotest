#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 16:41
# @Author  : hongjun.xiao
# @File    : Runner.py
# @system  : WenJiang

import os
def PtPath(script_path):
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+script_path

