#!/usr/bin/python

class Replacee(object):
  def __init__(self, value):
    self.value = value

  def GetValue(self):
    return self.value

r = Replacee(2)
print r.value
print r.GetValue()

Replacee.GetValue = lambda _: 3

print r.value
print r.GetValue()
