Project Euler
=============

A Flask application runs solutions of [Project Euler][projecteuler] with GAE (Google App Engine).

util.py
-------
1. prime_factors()
  return prime factors (can be used to identify prime)
    e.g. 
      prime_factors(20) returns [2, 2, 5]
      prime_factors(3) returns [3] a prime
    special value
      prime_factors(0) returns [0]
      prime_factors(1) returns [1]
  
2. divisors()
    return all divisors, including itself
    e.g. 
      divisors(220) returns [1, 2, 4, 5, 10, 20]
  
3. digits()
    return number of digits and ditis list
    e.g. 
      digits(1092) returns [4, [1, 0, 9, 2]]

4. is_prime()
5. primes_less_than()
6. factorGenerator()

Flask application with GAE
--------------------------
This repository comes with a simple setting making a Flask application work with GAE

C++ codes
---------
There several solutions solved by C++ codes.


[projecteuler] http://projecteuler.net/