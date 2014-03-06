# coding=utf-8
import re


def c4tv_trick(data):
    """
    Removes c4tv's logo from data.

    """

    # Ugly re!

    c4tv_logo = re.compile(
    r"\s*\.g8\"\"\"bgd        MMP\"\"MM\"\"YMM `7MMF\'   `7MF\'(.*)(\r*\n)" + \
    r"\s*\.dP\'     `M        P\'   MM   `7   `MA     ,V(.*)(\r*\n)" + \
    r"\s*dM\'       `     ,AM     MM         VM:   ,V(.*)(\r*\n)" + \
    r"\s*MM             AVMM     MM          MM\.  M\'(.*)(\r*\n)" + \
    r"\s*MM\.          ,W\' MM     MM          `MM A\'(.*)(\r*\n)" + \
    r"\s*`Mb\.     ,\',W\'   MM     MM           :MM;     ,-\. ,-\. ,-\. ,-\. ,-\. ,-\.-\|- ,-\.(.*)(\r*\n)" + \
    r"\s*`\"bmmmd\' AmmmmmMMmm \.JMML\.          VF      \| \| \|   \|-\' `-\. |-\' \| \| \|  `-\.(.*)(\r*\n)" + \
    r"\s*(.*)MM                           \|-\' \'   `-\' `-\' `-\' \' \' `\' `-\'(\r*\n)" + \
    r"\s*(.*)MM                           \|(\r*\n)" + \
    r"\s*(.*)\'(\r*\n)"
    )


    data = re.sub(c4tv_logo, '', data)

    return data
