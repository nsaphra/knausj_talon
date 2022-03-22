mode: user.markdown
mode: command
and code.language: markdown
-
tag(): user.code_operators
tag(): user.code_comment
tag(): user.code_generic

inside verbatim block:
    insert("```")
    key(enter)
    key(enter)
    insert("```")
    key(up)

inside verbatim:
    insert("``")
    key(left)
