import functools

class BFList(list):
  """
  BFList is a extension of Python's standard list with some useful functional methods (map, filter, reduce, etc) on the instance objects.
  """
  
  # Override so that we return a BFList
  def __add__(self, other):
    return BFList(super(BFList, self).__add__(other))
  
  def foreach(self, f):
    for i in self:
      f(i)
      
  def filter(self, f):
    return BFList(i for i in self if f(i))
  
  def map(self, f):
    return BFList(f(i) for i in self)
    
  def reduceLeft(self, f):
    return functools.reduce(f, self)
    
  def reduce(self, f):
    return self.reduceLeft(f)
    
  def foldLeft(self, f, initial):
    return functools.reduce(f, self, initial)
    
  def reverse(self):
    return BFList(self[::-1])
    
  def reduceRight(self, f):
    return functools.reduce(f, self.reverse())
  
  def foldRight(self, f, initial):
    return functools.reduce(f, self.reverse(), initial)