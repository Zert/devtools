#!/usr/bin/python

import getopt, sys
import urllib


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:l:t:d:v",
                                   ["help", "input=", "output=",
                                    "language=", "title=",
                                    "description=", "langlist"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)
    input = None
    output = None
    verbose = False
    title = ""
    description = ""
    language = "text"
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i", "--input"):
            input = a
        elif o in ("-o", "--output"):
            output = a
        elif o in ("-l", "--language"):
            language = a
        elif o in ("-t", "--title"):
            title = a
        elif o in ("-d", "--description"):
            description = a
        elif o == "--langlist":
            language_list()
            sys.exit(2)
        else:
            assert False, "unhandled option"
    pastedata(input, output, title, description, language, verbose)

def usage():
    print("Usage: " + sys.argv[0]
          + " [-l|--language language]"
          + " [-t|--title title]"
          + " [-d|--description]"
          + " [--langlist]"
          + " < content")

all_languages = [
    "actionscript", "actionscript3", "apacheconf", "applescript", "assembly",
    "basemake", "bash", "console", "bat", "bbcode", "befunge", "boo", "brainfuck",
    "c", "c#", "c++", "c++-objdumb", "c-objdump", "cheetah", "clojure", "common-lisp",
    "css", "d", "d-objdump", "delphi", "diff", "django", "dylan", "erb", "erlang",
    "erl", "fortran", "gas", "genshi", "po", "gnuplot", "groff", "haskell", "html",
    "ini", "io", "irc", "java", "javascript", "jinja", "jsp", "latex", "lighty",
    "lisp", "lhs", "llvm", "logtalk", "lua", "make", "mako", "matlab", "matlabsession",
    "minid", "moin", "moocode", "mupad", "mupad", "myghty", "mysql", "nasm", "nginx",
    "numpy", "objdump", "objectivec", "ocaml", "glsl", "pascal", "perl", "php", "pov",
    "prolog", "python", "pycon", "pytb", "python3", "py3tb", "r", "redcode", "rst",
    "rhtml", "ruby", "rbcon", "s", "scala", "scheme", "smalltalk", "smarty", "sql",
    "sqlite3", "squidconf", "tcl", "tcsh", "text", "vim", "basic", "vbnet", "xml",
    "xslt", "yaml"
    ]
all_languages.sort()

def language_list():
    print "Supported languages: " + ", ".join(all_languages)


def pastedata(input, output, title, description, language, verbose):
    if language not in all_languages:
        print "Language '" + language + "' not supported"
        language_list()
        sys.exit(2)

    if input == None:
        content = ""
        for line in sys.stdin:
            content += line
    else:
        print "Input from file not realised"
        sys.exit(2)

    if content == "":
        print "Null content. Exiting..."
        sys.exit(2)

    if verbose:
        print "Content:\n" + content

    f = urllib.urlopen(
        "http://showmecode.com/code/add/",
        "content=" + urllib.quote(content)
        + "&title=" + urllib.quote(title)
        + "&lexer=" + language
        + "&description=" + urllib.quote(description)
        )
    print f.geturl()

if __name__ == "__main__":
    main()
