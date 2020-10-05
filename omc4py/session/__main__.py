
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
        print(self.omc.execute(arg), end="")

    def do_quit(self, arg):
        return True


def main():
    with InteractiveOMC.open() as omc:
        OMCShell(
            omc=omc
        ).cmdloop()


main()
