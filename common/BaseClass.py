#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_user_info(self):
        return self.name + str(self.age)
