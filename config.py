#from qutebrowser.api import interceptor

## General
c.auto_save.session = True
c.editor.command = ["/usr/local/bin/alacritty", "-e", "/usr/local/bin/nvim -f {file}"]

## Appearance
c.tabs.show = "switching"
c.downloads.position = "bottom"

# colors
# Normal colors
colour_normal_black = '#3B4252'
colour_normal_red = '#BF616A'
colour_normal_green = '#A3BE8C'
colour_normal_yellow = '#EBCB8B'
colour_normal_blue = '#81A1C1'
colour_normal_magenta = '#B48EAD'
colour_normal_cyan = '#88C0D0'
colour_normal_white = '#E5E9F0'

# Bright colors
colour_bright_black = '#4C566A'
colour_bright_red = '#BF616A'
colour_bright_green = '#A3BE8C'
colour_bright_yellow = '#EBCB8B'
colour_bright_blue = '#81A1C1'
colour_bright_magenta = '#B48EAD'
colour_bright_cyan = '#8FBCBB'
colour_bright_white = '#ECEFF4'

c.colors.statusbar.normal.bg = colour_normal_black
c.colors.statusbar.normal.fg = colour_bright_white

c.colors.tabs.selected.even.bg = colour_normal_black
c.colors.tabs.selected.odd.bg  = colour_normal_black

c.colors.tabs.even.bg = colour_normal_blue
c.colors.tabs.even.fg = colour_normal_black

c.colors.tabs.odd.bg = colour_normal_cyan
c.colors.tabs.odd.fg = colour_bright_black

## Bindings
config.bind(";p", "spawn pass_menu")

## Ad Blocking
## TODO Fix to block ads
#def g4g_adblock(info: interceptor.Request):
#    url = info.request_url
#    if (
#        url.host() == "https://www.geeksforgeeks.org"
#        ):
#        info.block()

#interceptor.register(g4g_adblock)
