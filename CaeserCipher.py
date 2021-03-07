class CaeserCipher:

    def decode(string, shift):
        shifted_decimals = [ord(x) for x in string]
        unshifted_decimals = [x - shift for x in shifted_decimals]
        newStr = [chr(x) for x in unshifted_decimals]
        strings = ""
        for x in newStr:
            strings += x
        return strings

    def encode(string, shift):
        
        decimals = [ord(x) for x in string]
        shifted = [x + shift for x in decimals]
        shifted_string = [chr(x) for x in shifted]
        ret = ""
        for x in shifted_string:
            ret += x
        return ret

