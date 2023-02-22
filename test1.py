import tester

for i in range(0, 100):
  if tester.fsum(i, i) != i+i:
    raise Exception("Sorry, no numbers below zero!")
