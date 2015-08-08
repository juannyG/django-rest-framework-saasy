#-*- coding: utf-8 -*-

__all__ = ['classproperty']


class classproperty(property):
    """Subclass property to make classmethod properties possible"""
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()
