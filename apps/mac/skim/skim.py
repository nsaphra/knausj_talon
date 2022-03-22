from talon import ctrl, ui, Module, Context, actions, clip, app

ctx = Context()
ctx.matches = r"""
bundle: net.sourceforge.skim-app.skim
"""

# ctx = Context()
# mod = Module()
# apps = mod.apps
# mod.apps.skim = """
# os: mac
# and app.bundle: net.sourceforge.skim-app.skim
# """
#
# ctx.matches = r"""
# app: safari
# """
# @ctx.action_class("user")
#
# keymap = {
#   "highlight": Key("cmd-ctrl-h"),
#   "anchor": Key("cmd-ctrl-n"),
# }
#
#
# ctx.keymap(keymap)
