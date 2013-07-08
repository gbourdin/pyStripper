import re


def amiable_trick(data):
    """
    Strips the rose ascii art from amiable nfos leaving the rest of
    the text intact.
    """

    # These are ugly but we don't want to strip this text if it's not on
    # this drawing.
    data = re.sub("\|\|(.*)\n(.*)I loved you first(.*)\n(.*)\|\|(.*)",
                  r"\1\n\3\n\5", data)
    data = re.sub("\|\|(.*)\n(.*)sweetest downfall..(.*)\n(.*)\|\|,(.*)",
                  r"\1\n\3\n\5", data)

    data = re.sub("__ .---.(.*)", r"\1", data)
    data = re.sub("__ /  `  .-.7,--.(.*)", r"\1", data)
    data = re.sub("/  `. .-''. -,  , \\\(.*)", r"\1", data)
    data = re.sub("'--.-    -;   \| \) /(.*)", r"\1", data)
    data = re.sub(",` /   \\\ ,_\) /   '-.(.*)", r"\1", data)
    data = re.sub("/  \(  \(  \|   /  .' \) \\\(.*)", r"\1", data)
    data = re.sub("'.  `--,/   .---' ,-.\|(.*)", r"\1", data)
    data = re.sub("`--.  / '-, -' .'(.*)", r"\1", data)
    data = re.sub(".==,=; `-,.;--'(.*)", r"\1", data)
    data = re.sub("/ ,'  _;--;\|(.*)", r"\1", data)
    data = re.sub("/_...=' you are my(.*)", r"\1", data)
    data = re.sub("\|\| .==,=.(.*)", r"\1", data)
    data = re.sub("\|\|/    '.\\\(.*)", r"\1", data)
    data = re.sub(",\|\|`'=...__\\\(.*)", r"\1", data)

    # Only need one instance of these. Order matters.
    data = re.sub("\|\|,(.*)", r"\1", data)
    data = re.sub(",\|\|(.*)", r"\1", data)
    data = re.sub("\|\|(.*)", r"\1", data)

    return data
