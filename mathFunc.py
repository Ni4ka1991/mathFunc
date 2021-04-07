#!/usr/bin/env
from os import system

def mul( a, b ):
  m =  a * b
  return m

def div( a, b ):
    d = a / b
    return d

def add( a, b ):
    ad = a + b
    return ad

def sub( a, b ):
    s = a - b
    return s

system(" clear" )
print()
print( f"The result of mul func = {mul( 3, 5 )}" )
print( f"The result of div func = {div( 14, 2 )}" )
print( f"The result of add func = {add( 234, 567 )}" )
print( f"The result of sub func = {sub( 117, 18 )}" )
print( f"The result of my functions: {mul( add( 1, 2 ), div( 3, 4 ))}" )
