if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from classes import GUI, clicker, presser
    else:
        from ..classes import GUI, clicker, presser
    window = GUI.Interface()
    window.main()



