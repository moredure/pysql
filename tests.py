from pysql import sqli

def var_test():
    assert 1337 == sqli.var
