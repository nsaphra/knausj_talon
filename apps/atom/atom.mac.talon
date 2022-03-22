os: mac
app: atom
-
tag(): user.find_and_replace
tag(): user.line_commands
tag(): user.multiple_cursors
tag(): user.snippets
tag(): user.splits
tag(): user.tabs
# tag(): user.code_operators

# Navigation, searching

compal [<user.text>]:
	key(cmd-shift-p)
	insert(user.text or "")

search:
	key(cmd-f)

(maxed | match next):
	key(f3)

search in files:
	key(cmd-shift-f)

go any:
	key(cmd-p)

go line:
	key(ctrl-g)

go <number>:
	key(ctrl-g)
	insert("{number}")
	key(enter)

# Go to a tab using a list (Tab Filter package)
go tab:
	key("cmd-shift-x")
	key("cmd-p")

# Go to a code symbol match in the project
go symbol:
	key("cmd-shift-r")

# Go to a definition
go def:
    key("cmd-shift-x")
    key("cmd-shift-d")

# Go to mark: swap current position with the mark
go ark:
    key(cmd-k)
    key(cmd-x)

# Switch to the neighboring group (either left or right)
swig:
	key("cmd-shift-x")
	key("cmd-shift-x")

# Toggle sidebar
sidebar:
	key("cmd-k")
	key("cmd-b")

focus sidebar: key("cmd-0")

# Switch to single column layout
single column: key("alt-shift-1")

# Switch to two-column layout
two columns: key("alt-shift-2")

# Operating on Tabs
# close file tab
tab close: app.tab_close()
tab back:
    key(cmd-shift-tab)

# Jumping about
jump back: key(alt--)
jump for: key("alt-shift--")

# Re-center the view (watch out: conflicts with Origami)
recenter:
	key("cmd-k")
	key("cmd-c")

bookmark set: key(cmd-f2)
bookmark next: key(f2)

# For use with multi-cursors: select word.
sword:
	key(cmd-d)

# For use with multi-cursors: unselect word, select the next one.
dross:
    key(cmd-k)
    key(cmd-d)

# Soft undo
soft undo:
    key(cmd-u)

# Indentation
action(edit.indent_less):
	key("cmd-[")

action(edit.indent_more):
	key(cmd-])

reindent:
	key(cmd-shift-x)
	key(cmd-r)

no indent:
	key(cmd-[:7)

# Miscellaneous editing

(uppercase | upcase):
	key(cmd-k)
	key(cmd-u)

(lower | lowercase | downcase):
	key(cmd-k)
	key(cmd-l)

(titlecase | titcase):
        key(cmd-k)
        key(cmd-t)

reflow:
	key(cmd-shift-x)
	key(cmd-shift-alt-q)

dupe line:
	key(cmd-shift-d)

# Swap line up or down
scoot up:
	key(cmd-shift-up)

scoot down:
	key(cmd-shift-down)

# Complete Julia code</description>
completion:
	key(cmd-space)

# Expand the selection to the interior between brackets
ex kets:
	key(cmd-shift-m)

# Expand the selection to line
ex line:
	key(cmd-l)

# Expand the selection to scope
ex cope:
	key(cmd-shift-space)

# The following two commands work together to set a mark, move the point
# to somewhere else, and then extend the selection between the current
# position of the point and the mark.
(set mark | sark):
	key(cmd-k)
	key(cmd-space)

(select to mark | ex ark):
	key(cmd-k)
	key(cmd-a)

# Evaluate code
eval:
    key(cmd-enter)

# Evaluate file using the build system
build:
    key(cmd-b)

# Copy name of the file to the clipboard
clip name:
	key("cmd-shift-x")
	key("cmd-alt-c")

# Store the path of the current file in the clipboard
clip path:
	key("cmd-shift-x")
	key("cmd-shift-alt-c")

# Change the working folder
to folder:
    key("cmd-shift-x")
    key("cmd-f")
