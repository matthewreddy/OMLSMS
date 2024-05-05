import omldb

if __name__ == "__main__":
    # Run normally (not as test environment)
    import sys
    omldb.main(False, *sys.argv[1:])