# Unfuck Interpreter v-1.0


# The MIT License (MIT)
#
# Copyright (c) 2015 Andrew Melrose
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--run", type=argparse.FileType("r"), required=True,
    help="Specify the Unfuck program to execute.")
parser.add_argument("input", nargs="*", default="",
    help="Type the input that your Unfuck program expects.")
args = parser.parse_args()

p = args.run.read()
args.run.close()
pPtr = 0
op = ""
tape = [0]
tPtr = 0
inps = " ".join(args.input) or sys.stdin.read().strip()
iPtr = 0

pard = 0
parp = 1
ptrd = 1

def invall():
  global ptrd
  invparp()
  invpard()
  ptrd = -ptrd

def invparp():
  global parp
  parp = -parp

def invpard():
  global pard
  pard = -pard

def condSkip():
  global pPtr
  if tape[tPtr] > 0:
    pPtr += ptrd

def backCell():
  global tPtr
  if tPtr > 0:
    tPtr -= 1

def forwCell():
  global tPtr
  tPtr += 1
  if tPtr == len(tape):
    tape.append(0)

def decrCell():
  global tape
  tape[tPtr] = (tape[tPtr] + 255) % 256

def incrCell():
  global tape
  tape[tPtr] = (tape[tPtr] + 1) % 256

def outp():
  sys.stdout.write(chr(tape[tPtr]))

def inp():
  global tape, iPtr
  if iPtr < len(inps):
    tape[tPtr] = ord(inps[iPtr])
    iPtr = iPtr + 1
  else:
    tape[tPtr] = 0


ops = {
  "^" : invall,
  "~" : invparp,
  "!" : invpard,
  "?" : condSkip,
  "<" : backCell,
  ">" : forwCell,
  "-" : decrCell,
  "+" : incrCell,
  "." : outp,
  "," : inp
}

def Main():
  global pPtr, pard, parp
  while pPtr < len(p):
    if pPtr < 0:
      raise Exception("Unfuck program pointer is running into negative indices!")
    op = p[pPtr]
    if op == "(":
      pard += parp
    elif op == ")":
      pard -= parp;
    elif pard < 1:
      if op in ops:
        ops[op]()
    pPtr += ptrd

if __name__ == "__main__":
  Main()
