tag: browser
win.title: /overleaf.com/
-

go line: key(cmd-l)

new line: "\\newline",

sightee:
    insert("\\citet{}")
    key(left)
citepee:
    insert("~\\citep{}")
    key(left)
reference:
    insert("~\\ref{}")
    key(left)
text:
    insert("\\textrm{}")
    key(left)
fraction:
    insert("\\frac{}{}")
    key(left:3)
