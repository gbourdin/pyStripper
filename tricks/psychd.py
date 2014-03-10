# coding=utf-8
import re


def psychd_trick(data):
    """
    Removes psychd logo from data
                                              oooo              .o8
                                              `888             "888
    oo.ooooo.   .oooo.o oooo    ooo  .ooooo.   888 .oo.    .oooo888
     888' `88b d88(  "8  `88.  .8'  d88' `"Y8  888P"Y88b  d88' `888
     888   888 `"Y88b.    `88..8'   888        888   888  888   888
     888   888 o.  )88b    `888'    888   .o8  888   888  888   888
     888bod8P' 8""888P'     .8'     `Y8bod8P' o888o o888o `Y8bod88P"
     888                .o..P'
    o888o               `Y8P'
    """

    psychd_logo = re.compile(
        "\s*oooo              \.o8(.*)(\r*\n)" +
        "\s*`888             \"888(.*)(\r*\n)" +
        "\s*oo\.ooooo\.   \.oooo\.o oooo    ooo  \.ooooo\.   888 \.oo\.    \.oooo888(.*)(\r*\n)" +
        "\s*888' `88b d88\(  \"8  `88\.  \.8'  d88' `\"Y8  888P\"Y88b  d88' `888(.*)(\r*\n)" +
        "\s*888   888 `\"Y88b\.    `88\.\.8\'   888        888   888  888   888(.*)(\r*\n)" +
        "\s*888   888 o\.  \)88b    `888\'    888   \.o8  888   888  888   888(.*)(\r*\n)" +
        "\s*888bod8P\' 8\"\"888P'     \.8'     `Y8bod8P\' o888o o888o `Y8bod88P\"(.*)(\r*\n)"+
        "\s*888                \.o\.\.P'(.*)(\r*\n)" +
        "\s*o888o               `Y8P\'(.*)(\r*\n)",
        re.M
    )

    data = re.sub(psychd_logo, '', data)
    return data
