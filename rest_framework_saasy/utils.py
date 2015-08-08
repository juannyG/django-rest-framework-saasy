#-*- coding: utf-8 -*-

__all__ = ['classproperty']


class classproperty(classmethod):
    """Subclass classmethod to make classmethod properties possible"""
    def __get__(self, instance, owner):
        return super(classproperty, self).__get__(instance, owner)()
