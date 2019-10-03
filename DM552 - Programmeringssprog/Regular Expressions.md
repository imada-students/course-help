Regular Expressions
===================

Grep\[Mode\] \[Regular Expression\] \[Filename\]

Modes:
------

-   -h (Do not display filenames)

-   -i (Ignore case)

-   -l (List only filenames containing matching lines

-   -n (Precede each matching line with its line number

-   -v (Negate matches)

-   -x Match whole line only (fgrep only)

-   -e (expression - specify expression as option)

-   -f filename

Regular Expressions:
--------------------

+-----------------------+-----------------------+-----------------------+
| Regular Expression    | Meaning               | Example               |
+=======================+=======================+=======================+
| .                     | The dot expression    | "o.o" matches any     |
|                       | matches any           | line with a character |
|                       | character.            | in between two o's    |
+-----------------------+-----------------------+-----------------------+
| \[\]                  | Character classes can | b\[eor\]at matches    |
|                       | be used to match any  | beat, brat, boat      |
|                       | specific set of       |                       |
|                       | characters.           |                       |
+-----------------------+-----------------------+-----------------------+
| \[\^\]                | Character classes can | b\[\^eor\]at matches  |
|                       | be negated.           | all lines not         |
|                       |                       | containing beat,      |
|                       |                       | brat, boat            |
+-----------------------+-----------------------+-----------------------+
| \^                    | Is an anchor, and     | \^b\[eor\]at would    |
|                       | means beginning of    | only match if         |
|                       | the line              | beat,breat, or boat   |
|                       |                       | was in the start of   |
|                       |                       | the line.             |
+-----------------------+-----------------------+-----------------------+
| \$                    | Is an anchor, means   | b\[eor\]at\$ would    |
|                       | end of the line.      | only match if the 3   |
|                       |                       | words where in the    |
|                       |                       | end of the line.      |
+-----------------------+-----------------------+-----------------------+
| \^\$                  | Empty lines           |                       |
+-----------------------+-----------------------+-----------------------+
| \^word\$              | Only matches if the   |                       |
|                       | word is alone on a    |                       |
|                       | line                  |                       |
+-----------------------+-----------------------+-----------------------+
| \*                    | The \* is used to     | Ya\*y matches         |
|                       | define zero or more   | yaaaaaaay, and yy.    |
|                       | occurrences.          |                       |
+-----------------------+-----------------------+-----------------------+
| \+                    | The plus (+) means    | abc+d will match      |
|                       | "one or more".        | 'abcd' , 'abccd' , or |
|                       |                       | 'abccccccd' but will  |
|                       | Equivalent to {1,}    | not match 'abd'.      |
+-----------------------+-----------------------+-----------------------+
| ?                     | The '?' (question     | July? will match      |
|                       | mark) specifies an    | 'Jul' or 'July'       |
|                       | optional character,   |                       |
|                       | the single character  |                       |
|                       | that immediately      |                       |
|                       | precedes it           |                       |
|                       |                       |                       |
|                       | Equivalent to {0,1}   |                       |
+-----------------------+-----------------------+-----------------------+
| \\n                   | Backreference         | For example, to find  |
|                       | specifier, where n is | if the first word of  |
|                       | a number. Looks for   | a line is the same as |
|                       | nth subexpression     | the last:             |
|                       |                       |                       |
|                       |                       | \^\\(\[\[:alpha:\]\]\ |
|                       |                       | \{1,\\}\\)            |
|                       |                       | .\* \\1\$             |
+-----------------------+-----------------------+-----------------------+

\*, ?, and + are known as quantifiers

Quantifiers can be used with subexpressions.

-   (a\*c)+ will match 'c' , 'ac' , 'aac' or 'aacaacac' but will not
    match 'a' or a blank line

More about character classes:
=============================

![](media/image1.png){width="4.104166666666667in"
height="2.550877077865267in"}

Named character classes are: alpha, lower, upper, alnum, digit, punct,
cntrl.

  \[\[:alpha:\]\] - Named character classes   \[a-zA-Z\]
  ------------------------------------------- -------------
  \[\[:alnum:\]\]                             \[a-zA-Z0-9
  \[45\[:lower:\]\]                           \[45a-z\]

Repetition ranges
=================

  {}      notation can specify a range of repetitions for the immediately preceding regex
  ------- ---------------------------------------------------------------------------------
  {n}     Means exactly n occurrences
  {n,}    Means at least n occurrences
  {n,m}   means at least n occurrences but no more than m occurrences

.{0,} same as .\*

a{2,} same as aaa\*

Subexpressions
==============

If you want to group part of an expression so that \* or { } applies to
more than just the previous character, use ( ) notation

Subexpresssions are treated like a single character

a\* matches 0 or more occurrences of a

abc\* matches ab, abc, abcc, abccc, ...

(abc)\* matches abc, abcabc, abcabcabc, ...

(abc){2,3} matches abcabc or abcabcabc
