import sublime, sublime_plugin


def shorten_hex(hex_):
    """Shorten a hex string to a single digit, if possible.

    For CSS colors, a hex string that is a repetition of the same digit can be
    shortened to just that digit.

    """

    a, b, c, d, e, f = hex_
    # Only shorten if all components can be shortened.
    if a == b and c == d and e == f:
        return a + c + e
    return hex_


class ColorBrightnessCommand(sublime_plugin.TextCommand):
    """Adds a value to each component of an RGB color.

    The color should be a hexadecimal value currently under the cursor.

    Example:
    - Open console: ctrl + `
    - Put cursor over RGB hexadecimal value
    - Execute: view.run_command('color_brightness', {'amount': -10})

    """

    def run(self, edit, amount):
        """Add an amount to the nearest hex color value."""

        amount = float(amount)
        word_range = self.view.word(self.view.sel()[0])
        text = self.view.substr(word_range)
        text_len = len(text)
        if text_len != 3 and text_len != 6:
            return
        if text_len == 3:
            text = ''.join([i * 2 for i in text])
        components = (text[0:2], text[2:4], text[4:6])
        components = [int(int(c, 16) + amount) for c in components]
        components = [max(min(c, 255), 0) for c in components]
        components = ['{0:02x}'.format(c) for c in components]
        new_color = shorten_hex(''.join(components))
        self.view.sel().add(word_range)
        self.view.replace(edit, word_range, new_color)
