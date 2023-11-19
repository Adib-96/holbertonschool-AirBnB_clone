#!/usr/bin/python3
"""the __init__ method for the initialization of an instance"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
