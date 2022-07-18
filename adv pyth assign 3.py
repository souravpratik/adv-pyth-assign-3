#!/usr/bin/env python
# coding: utf-8

# # Adv. Python Assignment-03
Question 1: What is the concept of an abstract superclass?

Solution : The class whose properties gets inherited by another class is known as superclass or parent class and the class                which inherits the properties of another class is known as the subclass. A subclass inherits all data and behavior              of parent class. But we can also add more information and behavior to the subclass and also override its behavior.Question 2: What happens when a class statement's top level contains a basic assignment statement?

Solution :  Any top-level statement in modu.py will be executed, including other imports if any, means: "Things that are                     interpreted at import time". 
            
             the def and the class. These are both executed at import time. These definitions are compound statements .                      
            Question 3: Why does a class need to manually call a superclass's __init__ method?

Solution :  A class need to manually call a superclass's __init__ method, since Python does not automatically call this method             if it exists. 
            Often, we want to call a method on an instance (or class) if and only if that method exists. Otherwise, we do                   nothing or default to another action. For example, this often applies to the _ _init_ _ method of superclasses.Question 4: How can you augment, instead of completely replacing, an inherited method?

Solution :  To augment an inherited method involves forwarding. Message forwarding allows to augment an inherited method in                 such a way that it can perform its inherited action and some new action. All three method types can be forwarded               (Procedure, Procedure Set and Function).
Question 5 : How is the local scope of a class different from that of a function?

Solution :  Local scope is the area between an { and it's closing }. Function scope is the area between the opening { of a                 function and its closing }, which may contain more "local" scopes. A label is visible in the entirety of the                   function within which it is defined, e.g.
            
            int f( int a ) 
            {
               int b = 8;
               if ( a > 14 )
               {
                   int c = 50;
                   label:
                   return c - a - b;
                }
                if ( a > 7 ) goto label;
                return -99;
            }
            
            here, 'int c' is not visible outside its enclosing block. label is visible outside its enclosing block, but only to             function scope.