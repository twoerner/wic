"""
Minimal subset of BitBake's bb.utils used by standalone wic.
"""
import os

def mkdirhier(path):
    os.makedirs(path, exist_ok=True)
