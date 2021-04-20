#!/usr/bin/env python
""" generated source for module IdentifierMain """
# package: identifier
from Identifier import Identifier

class IdentifierMain(object):
    """ generated source for class IdentifierMain """

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        if len(args) == 1:
            print("Uso: IdentifierMain <string>")
        else:
            id = Identifier()
            if id.validateIdentifier(args[1]):
                print("Valido")
            else:
                print("Invalido")

if __name__ == '__main__':
    import sys
    IdentifierMain.main(sys.argv)
