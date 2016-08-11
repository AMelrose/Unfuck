# Unfuck Interpreter v-1.0


# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>


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
    elif op in ops:
      if pard < 1:
        ops[op]()
    pPtr += ptrd

if __name__ == "__main__":
  Main()
