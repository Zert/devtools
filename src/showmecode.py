#!/usr/bin/python

from optparse import OptionParser
import sys
import urllib


def main():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input",
                      help="Read content from INPUTFILE", metavar="INPUTFILE")
##    parser.add_option("-o", "--output", dest="output",
##                      help="Write HTML-reply to OUTFILE", metavar="OUTFILE")
    parser.add_option("-l", "--language", dest="language", default="text",
                      help="Language for highlighting (default plain text)")
    parser.add_option("--langlist", action="store_true", dest="langlist",
                      default=False, help="List supported languages")
    parser.add_option("-t", "--title", dest="title", default="",
                      help="Title of code")
    parser.add_option("-d", "--description", dest="description", default="",
                      help="Description of code")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
                      default=False, help="List supported languages")

    (options, args) = parser.parse_args()

    input = options.input
    ##output = options.output
    output = None,
    verbose = options.verbose
    title = options.title
    description = options.description
    language = options.language
    if options.langlist:
            language_list()
            sys.exit(2)

    pastedata(input, output, title, description, language, verbose)

def usage():
    print("Usage: " + sys.argv[0]
          + " [-i|--input inputfile]"
          + " [-l|--language language]"
          + " [-t|--title title]"
          + " [-d|--description]"
          + " [--langlist]"
          + " [< content]")

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
    print "Supported languages: " + str.join(", ", all_languages)


def pastedata(input, output, title, description, language, verbose):
    if language not in all_languages:
        print "Language '" + language + "' not supported"
        language_list()
        sys.exit(2)

    if input == None:
        content = sys.stdin.read()
    else:
        content = open(input, 'r').read()

    if content == "":
        print "Null content. Exiting..."
        sys.exit(2)

    if verbose:
        print "Content:\n" + content


    params = urllib.urlencode({'content':content,
                               'title':title,
                               'lexer':language,
                               'description':description})
    f = urllib.urlopen("http://showmecode.com/code/add/", params)
    print(f.geturl())

if __name__ == "__main__":
    main()
