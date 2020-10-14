
import argparse
import cmd

from . import InteractiveOMC


class OMCShell(
    cmd.Cmd,
):
    omc: InteractiveOMC

    prompt = "|omc| >>> "

    def __init__(
        self,
        *args,
        omc: InteractiveOMC,
        **kwrds,
    ):
        super(OMCShell, self).__init__(*args, **kwrds)

        self.omc = omc

    def do_shell(self, arg):
        print(self.omc.evaluate(arg), end="")

    def do_quit(self, arg):
        return True


def main():
    parser = argparse.ArgumentParser(
        prog="OMCSessionDebug"
    )
    parser.add_argument(
        "--omc",
        help="omc executable",
        default=None,
    )
    args = parser.parse_args()

    with InteractiveOMC.open(omc_command=args.omc) as omc:
        OMCShell(
            omc=omc
        ).cmdloop()


main()
