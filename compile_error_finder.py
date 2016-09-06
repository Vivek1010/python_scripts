#!/usr/bin/env python

import re
err = open("jamlog.txt", "r")

for line in err:
    if re.match("(.*)ERROR:(.*) |\
                 (undeclared)|\
                 (syntax error)|\
                 (implicit declaration)|\
                 (unterminated string)|\
                 (character constant too long)|\
                 (initialization makes integer from pointer without a cast)|\
                 (dereferencing pointer to incomplete type)|\
                 (unknown escape sequence)|\
                 (suggest parentheses around assignment used as truth value)|\
                 (control reaches end of non-void functio)|\
                 (unused variable)|\
                 (passing arg of ... as ... due to prototype)|\
                 (assignment of read-only location)|\
                 (cast discards qualifiers from pointer target type)|\
                 (assignment discards qualifiers)|\
                 (initialization discards qualifiers)|\
                 (return discards qualifiers)|\
                 (initializer element is not a constant)|\
                 (parse error) ", line):
            print line,
