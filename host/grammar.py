#!/usr/bin/python3

import abc

# interfaces
class Grammar(abc.ABC):
  # prints the following grammar
  @abc.abstractmethod
  def print(self):
    pass

  # emits the following grammar to raw data
  @abc.abstractmethod
  def emit(self):
    pass

  # load from raw
  @abc.abstractmethod
  def load(self, data):
    pass

# manager
class GrammarManager():
  

# grammars
