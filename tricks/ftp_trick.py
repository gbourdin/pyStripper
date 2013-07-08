import re


def ftp_trick(data):
    """
    Removes FTP's logo from data.
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :::                                                                     :::
    :::  FFFFFFFFFFFFFFFFFFFFFFTTTTTTTTTTTTTTTTTTTTTTTPPPPPPPPPPPPPPPPP     :::
    :::  F::::::::::::::::::::FT:::::::::::::::::::::TP::::::::::::::::P    :::
    :::  F::::::::::::::::::::FT:::::::::::::::::::::TP::::::PPPPPP:::::P   :::
    :::  FF::::::FFFFFFFFF::::FT:::::TT:::::::TT:::::TPP:::::P     P:::::P  :::
    :::    F:::::F       FFFFFFTTTTTT  T:::::T  TTTTTT  P::::P     P:::::P  :::
    :::    F:::::F                     T:::::T          P::::P     P:::::P  :::
    :::    F::::::FFFFFFFFFF           T:::::T          P::::PPPPPP:::::P   :::
    :::    F:::::::::::::::F           T:::::T          P:::::::::::::PP    :::
    :::    F:::::::::::::::F           T:::::T          P::::PPPPPPPPP      :::
    :::    F::::::FFFFFFFFFF           T:::::T          P::::P              :::
    :::    F:::::F                     T:::::T          P::::P              :::
    :::    F:::::F                     T:::::T          P::::P              :::
    :::  FF:::::::FF                 TT:::::::TT      PP::::::PP            :::
    :::  F::::::::FF                 T:::::::::T      P::::::::P            :::
    :::  F::::::::FF                 T:::::::::T      P::::::::P            :::
    :::  FFFFFFFFFFF                 TTTTTTTTTTT      PPPPPPPPPP            :::
    :::                                                                     :::
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    """

    # Ugly re!

    ftp_logo = re.compile(
    "\s*:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::(.*)(\r*\n)" + \
    "\s*:::                                                                     :::(.*)(\r*\n)" + \
    "\s*:::  FFFFFFFFFFFFFFFFFFFFFFTTTTTTTTTTTTTTTTTTTTTTTPPPPPPPPPPPPPPPPP     :::(.*)(\r*\n)" + \
    "\s*:::  F::::::::::::::::::::FT:::::::::::::::::::::TP::::::::::::::::P    :::(.*)(\r*\n)" + \
    "\s*:::  F::::::::::::::::::::FT:::::::::::::::::::::TP::::::PPPPPP:::::P   :::(.*)(\r*\n)" + \
    "\s*:::  FF::::::FFFFFFFFF::::FT:::::TT:::::::TT:::::TPP:::::P     P:::::P  :::(.*)(\r*\n)" + \
    "\s*:::    F:::::F       FFFFFFTTTTTT  T:::::T  TTTTTT  P::::P     P:::::P  :::(.*)(\r*\n)" + \
    "\s*:::    F:::::F                     T:::::T          P::::P     P:::::P  :::(.*)(\r*\n)" + \
    "\s*:::    F::::::FFFFFFFFFF           T:::::T          P::::PPPPPP:::::P   :::(.*)(\r*\n)" + \
    "\s*:::    F:::::::::::::::F           T:::::T          P:::::::::::::PP    :::(.*)(\r*\n)" + \
    "\s*:::    F:::::::::::::::F           T:::::T          P::::PPPPPPPPP      :::(.*)(\r*\n)" + \
    "\s*:::    F::::::FFFFFFFFFF           T:::::T          P::::P              :::(.*)(\r*\n)" + \
    "\s*:::    F:::::F                     T:::::T          P::::P              :::(.*)(\r*\n)" + \
    "\s*:::    F:::::F                     T:::::T          P::::P              :::(.*)(\r*\n)" + \
    "\s*:::  FF:::::::FF                 TT:::::::TT      PP::::::PP            :::(.*)(\r*\n)" + \
    "\s*:::  F::::::::FF                 T:::::::::T      P::::::::P            :::(.*)(\r*\n)" + \
    "\s*:::  F::::::::FF                 T:::::::::T      P::::::::P            :::(.*)(\r*\n)" + \
    "\s*:::  FFFFFFFFFFF                 TTTTTTTTTTT      PPPPPPPPPP            :::(.*)(\r*\n)" + \
    "\s*:::                                                                     :::(.*)(\r*\n)" + \
    "\s*:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::(.*)(\r*\n)")


    data = re.sub(ftp_logo, '', data)

    return data
