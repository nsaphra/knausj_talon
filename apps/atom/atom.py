from talon import actions, Context, Module, app, clip

is_mac = app.platform == "mac"

ctx = Context()
mod = Module()

apps = mod.apps
apps.atom = "app.name: Atom"
apps.atom = "app.name: atom"
apps.atom = """
os: windows
and app.name: Atom
os: windows
and app.exe: atom.exe
"""
apps.atom = """
os: mac
and app.bundle: com.github.atom'
"""

ctx.matches = r"""
app: Atom
"""

@ctx.action_class("user")
class UserActions:
    # find_and_replace.py support begin

    def find(text: str):
        """Triggers find in current editor"""
        if is_mac:
            actions.key("cmd-f")
        else:
            actions.key("ctrl-f")

        if text:
            actions.insert(text)

    def find_next():
        actions.user.vscode("cmd-g")

    def find_previous():
        actions.user.vscode("cmd-shift-g")

    def find_everywhere(text: str):
        """Triggers find across project"""
        if is_mac:
            actions.key("cmd-shift-f")
        else:
            actions.key("ctrl-shift-f")

        if text:
            actions.insert(text)

    def find_toggle_match_by_case():
        """Toggles find match by case sensitivity"""
        if is_mac:
            actions.key("alt-cmd-c")
        else:
            actions.key("alt-c")

    # def find_toggle_match_by_word():
    #     """Toggles find match by whole words"""
    #     if is_mac:
    #         actions.key("cmd-alt-w")
    #     else:
    #         actions.key("alt-w")
    #
    # def find_toggle_match_by_regex():
    #     """Toggles find match by regex"""
    #     if is_mac:
    #         actions.key("cmd-alt-r")
    #     else:
    #         actions.key("alt-r")

    def replace(text: str):
        """Search and replaces in the active editor"""
        if is_mac:
            actions.key("alt-cmd-f")
        else:
            actions.key("ctrl-h")

        if text:
            actions.insert(text)

    def replace_everywhere(text: str):
        """Search and replaces in the entire project"""
        if is_mac:
            actions.key("cmd-shift-h")
        else:
            actions.key("ctrl-shift-h")

        if text:
            actions.insert(text)

    def replace_confirm():
        """Confirm replace at current position"""
        if is_mac:
            actions.key("shift-cmd-1")
        else:
            actions.key("ctrl-shift-1")

    def replace_confirm_all():
        """Confirm replace all"""
        if is_mac:
            actions.key("cmd-enter")
        else:
            actions.key("ctrl-alt-enter")

    def select_next_occurrence(text: str):
        actions.key("cmd-d")

#
# atom_hotkey = 'cmd-shift-ctrl-alt-t'
#
# class Struct:
#     def __init__(self, **entries):
#         self.__dict__.update(entries)
#
# # NB! These command names are duplicated in commands.js
# COMMANDS = Struct(
#     DELETE_TO_BOL = 'b',
#     DELETE_TO_EOL = 'e',
#     SELECT_LINES = 's',
#     FIND_NEXT = 'f',
#     FIND_PREVIOUS = 'p',
#     COPY_LINE = 'c',
#     MOVE_LINE = 'm',
#     SELECT_UNTIL = 'u',
# )
#
# ############## support for parsing numbers as command postfix
#
# numeral_map = dict((str(n), n) for n in range(0, 20))
# for n in [20, 30, 40, 50, 60, 70, 80, 90]:
#     numeral_map[str(n)] = n
# numeral_map["oh"] = 0 # synonym for zero
#
# numerals          = ' (' + ' | '.join(sorted(numeral_map.keys())) + ')+'
# optional_numerals = ' (' + ' | '.join(sorted(numeral_map.keys())) + ')*'
#
# def text_to_number(m):
#
#     tmp = [str(s).lower() for s in m._words]
#     words = [parse_word(word) for word in tmp]
#
#     result = 0
#     factor = 1
#     for word in reversed(words):
#         if word not in numerals:
#             # we consumed all the numbers and only the command name is left.
#             break
#
#         result = result + factor * int(numeral_map[word])
#         factor = 10 * factor
#
#     return result
#
#
# def parse_word(word):
#     word = word.lstrip('\\').split('\\', 1)[0]
#     return word
#
#
# ######### actions and helper functions
# # def jump_to_bol(m):
# #     line = text_to_number(m)
# #     actions.key('ctrl-g')
# #     Str(str(line))(None)
# #     actions.key('enter')
#
# def jump_to_end_of_line():
#     actions.key('cmd-right')
#
# def jump_to_beginning_of_text():
#     actions.key('cmd-left')
#
# def jump_to_nearly_end_of_line():
#     actions.key('left')
#
# # def jump_to_bol_and(then):
# #     def fn(m):
# #         if len(m._words) > 1:
# #             jump_to_bol(m)
# #         else:
# #             actions.key('ctrl-a')
# #             actions.key('cmd-left')
# #         then()
# #     return fn
# #
# # def jump_to_eol_and(then):
# #     def fn(m):
# #         if len(m._words) > 1:
# #             jump_to_bol(m)
# #         actions.key('cmd-right')
# #         then()
# #     return fn
#
#
# def toggle_comments(*unneeded):
#    actions.key('cmd-/')
#
# def snipline():
#     actions.key('shift-cmd-right')
#     actions.key('delete')
#     actions.key('delete')
#     actions.key('ctrl-a')
#     actions.key('cmd-left')
#
#
# def get_first_word(m):
#     return str(m.dgndictation[0]._words[0])
#
# def execute_atom_command(command, parameters=None):
#     actions.key(atom_hotkey)
#     actions.key(command)
#     if parameters:
#         Str(parameters)(None)
#         actions.key('enter')
#
# def find_next(m):
#     execute_atom_command(COMMANDS.FIND_NEXT, get_first_word(m))
#
# def find_previous(m):
#     execute_atom_command(COMMANDS.FIND_PREVIOUS, get_first_word(m))
#
# def copy_line(m):
#     line = text_to_number(m)
#     execute_atom_command(COMMANDS.COPY_LINE, str(line))
#
# def move_line(m):
#     line = text_to_number(m)
#     execute_atom_command(COMMANDS.MOVE_LINE, str(line))
#
# def select_lines(m):
#     # NB: line_range is e.g. 99102, which is parsed in
#     #  the atom package as lines 99..102
#     line_range = text_to_number(m)
#     execute_atom_command(COMMANDS.SELECT_LINES, str(line_range))
#
# def select_until(m):
#     line = text_to_number(m)
#     execute_atom_command(COMMANDS.SELECT_UNTIL, str(line))

# keymap = {
    # # 'sprinkle' + optional_numerals: jump_to_bol,
    # 'spring' + optional_numerals: jump_to_eol_and(jump_to_beginning_of_text),
    # # 'sprinkler'
    # 'dear' + optional_numerals: jump_to_eol_and(lambda: None),
    # 'smear' + optional_numerals: jump_to_eol_and(jump_to_nearly_end_of_line),
    # 'trundle': toggle_comments,
    # # 'trundle' + numerals: jump_to_bol_and(toggle_comments),
    # 'jolt': actions.key('cmd-x cmd-v cmd-v'),
    #
    # # 'snipline' + optional_numerals: jump_to_bol_and(snipline),
    #
    # 'snipple': [actions.key(atom_hotkey), actions.key(COMMANDS.DELETE_TO_BOL)],
    # 'snipper': [actions.key(atom_hotkey), actions.key(COMMANDS.DELETE_TO_EOL)],
    #
    # # needs bracket-matcher atom package; still a bit poor.
    # 'bracken': [actions.key('cmd-ctrl-m')],
    #
    # 'copy line' + numerals: copy_line,
    # 'move line' + numerals: move_line,
    #
    # 'crew <dgndictation>': find_next,
    # 'trail <dgndictation>': find_previous,
    #
    # 'shackle': actions.key('cmd-l'),
    # 'selrang' + numerals: select_lines,
    # 'salty' + numerals: select_until,
    #
    # 'shockey': actions.key('cmd-shift-enter'),
    # 'shockoon': actions.key('cmd-right enter'),
    # 'sprinkoon' + numerals: jump_to_eol_and(lambda: actions.key('enter')),
# }
#
# ctx.keymap(keymap)
