# Unfuck Programming Langauge

### What is Unfuck?

Unfuck is an esoteric programming langugage, designed by Andrew Melrose
in early 2015 and implemented in mid 2015. The language itself is based
on an earlier esoteric programming language called [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck)
which was designed by Urban Muller in 1993.
Unfuck differs slightly from  Brainfuck, in that there are no loop instructions.
That doesn't mean to say you can't loop in Unfuck, you just have to build
the control flow structures yourself.

### Usage

Unfuck was written in Python 2.7, so you'll need a compatible version of Python to execute Unfuck.

Unfuck is intended to be run from the command line.

To run an Unfuck without input:
```sh
python unfuck.py -r yourprogram.uf
```
Unfuck only accepts raw data passed to it as an argument or through standard input from another process:
```sh
python unfuck.py -r yourprogram.uf Some input to be processed
```
and:
```sh
TYPE somefile.txt | python unfuck.py -r yourprogram.uf
```

### What are the instructions?

Unfuck maintains the same instructions for manipulating data on the tape as well as those
for traversing the tape and inputting and outputting data. The square brackets **[** and **]** are gone
and have been replaced with a new set of instructions, which when used in combination, can achieve the same
effect of the while loops in Brainfuck.

Those instructions are;

| Instruction | Description
:---: | ---
( | Increment the parenthesis depth counter (default)
) | Decrement the parenthesis depth counter (default)
! | Invert the parenthesis depth counter
~ | Invert the parenthesis polarity flag
^ | Same as the two instructions above, plus reverse program pointer direction
? | If the current cell is non-zero, skip the next instruction

**Note:**
```
All instructions for the exception of '(' and ')' will only execute
as long as the pard (parenthesis depth counter) is less than 1. Otherwise,
they will simply be ignored. With this in mind, '(' and ')' can be used
to comment out code.
```

### What does an Unfuck while loop look like?

This is what it looks like:
```
(^~)~(~?!)((
  Other code goes here
))(^)
```

Here are some tables showing what happens when we execute the code.

Current cell is 0:

<table>
  <tr>
    <td>Program</td>
    <td>(</td>
    <td>^</td>
    <td>~</td>
    <td>)</td>
    <td>~</td>
    <td>(</td>
    <td>~</td>
    <td>?</td>
    <td>!</td>
    <td>)</td>
    <td>(</td>
    <td>(</td>
    <td>c</td>
    <td>)</td>
    <td>)</td>
    <td>(</td>
    <td>^</td>
    <td>)</td>
  </tr>
  <tr>
    <td>pard</td>
    <td>1</td>
    <td></td>
    <td></td>
    <td>0</td>
    <td></td>
    <td>-1</td>
    <td></td>
    <td></td>
    <td></td>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td></td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td></td>
    <td>0</td>
  </tr>
  <tr>
    <td>parp</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><strong>-</strong></td>
    <td></td>
    <td><strong>+</strong></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Direction</td>
    <td>=&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  
</table>

Current cell is greater than 0 (Step 1):

<table>
  <tr>
    <td>Program</td>
    <td>(</td>
    <td>^</td>
    <td>~</td>
    <td>)</td>
    <td>~</td>
    <td>(</td>
    <td>~</td>
    <td>?</td>
    <td>!</td>
    <td>)</td>
    <td>(</td>
    <td>(</td>
    <td>c</td>
    <td>)</td>
    <td>)</td>
    <td>(</td>
    <td>^</td>
    <td>)</td>
  </tr>
  <tr>
    <td>pard</td>
    <td>1</td>
    <td></td>
    <td></td>
    <td>0</td>
    <td></td>
    <td>-1</td>
    <td></td>
    <td></td>
    <td></td>
    <td>-2</td>
    <td>-1</td>
    <td>0</td>
    <td></td>
    <td>-1</td>
    <td>-2</td>
    <td>-1</td>
    <td><strong>1</strong></td>
    <td></td>
  </tr>
  <tr>
    <td>parp</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><strong>-</strong></td>
    <td></td>
    <td><strong>+</strong></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><strong>-</strong></td>
    <td></td>
  </tr>
  <tr>
    <td>Direction</td>
    <td>=&gt;</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><strong>&lt;</strong></td>
    <td></td>
  </tr>
</table>

Current cell is greater than 0 (Step 2):

<table>
  <tr>
    <td>Program</td>
    <td>(</td>
    <td>^</td>
    <td>~</td>
    <td>)</td>
    <td>~</td>
    <td>(</td>
    <td>~</td>
    <td>?</td>
    <td>!</td>
    <td>)</td>
    <td>(</td>
    <td>(</td>
    <td>c</td>
    <td>)</td>
    <td>)</td>
    <td>(</td>
    <td>^</td>
    <td>)</td>
  </tr>
  <tr>
    <td>pard</td>
    <td></td>
    <td><strong>1</strong></td>
    <td></td>
    <td>-1</td>
    <td></td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td></td>
    <td>2</td>
    <td>1</td>
    <td>0</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>parp</td>
    <td></td>
    <td><strong>+</strong></td>
    <td><strong>-</strong></td>
    <td></td>
    <td><strong>+</strong></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Direction</td>
    <td></td>
    <td><strong>&gt;</strong></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>&lt;=</td>
    <td></td>
  </tr>
</table>

### So, why the name?

```
The language has gone through a few ideas for names. However, the name that was chosen made more sense for
a couple of reasons; It is based on Brainfuck, hence the last four
letters of the name. Also, while I was designing the language,
I noticed a resemblence of the code I was writting in Unfuck to that
of Underload.
```

### License

See the license file.
