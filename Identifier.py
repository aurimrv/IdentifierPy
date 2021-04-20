#!/usr/bin/env python
""" generated source for module Identifier """

# package: identifier
class Identifier(object):
    """ generated source for class Identifier """

    def valid_s(self, ch):
        """ generated source for method valid_s """
        if ((ch >= 'A') and (ch <= 'Z')) or ((ch >= 'a') and (ch <= 'z')):
            return True
        else:
            return False

    def valid_f(self, ch):
        """ generated source for method valid_f """
        if ((ch >= 'A') and (ch <= 'Z')) or ((ch >= 'a') and (ch <= 'z')) or ((ch >= '0') and (ch <= '9')):
            return True
        else:
            return False

    def validateIdentifier(self, s):
        """ generated source for method validateIdentifier """
        achar = str()
        valid_id = False
        achar = s[0]
        valid_id = self.valid_s(achar)
        if len(s) > 1:
            achar = s[1]
            i = 1
            while i < len(s) - 1:
                achar = s[i]
                if not self.valid_f(achar):
                    valid_id = False
                i += 1
        if valid_id and (len(s) >= 1) and (len(s) < 6):
            return True
        else:
            return False