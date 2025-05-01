import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from RelatioLangLexer import RelatioLangLexer
from RelatioLangParser import RelatioLangParser
from RelatioLangParserListener import RelatioLangParserListener


def get_original_token_text(ctx):
    start_token = ctx.start
    stop_token = ctx.stop
    text_with_spaces = start_token.getInputStream().getText(start_token.start, stop_token.stop)
    return text_with_spaces


class RelatioLangListener(RelatioLangParserListener):
    def exitGraph_source_stmt(self, ctx:RelatioLangParser.Graph_source_stmtContext):
        print("GRAPH SOURCE:")
        print(f"\ttable is \"{ctx.table_name().getText()}\"")
        if ctx.expr() is not None:
            print(f"\twhere statement is \"{get_original_token_text(ctx.expr())}\"")
        print()

    def exitNo_enter_stmt(self, ctx:RelatioLangParser.No_enter_stmtContext):
        print("NO ENTER:")
        print(f"\ttable is \"{ctx.table_name().getText()}\"")
        print()

    def exitNo_exit_stmt(self, ctx:RelatioLangParser.No_exit_stmtContext):
        print("NO EXIT:")
        print(f"\ttable is \"{ctx.table_name().getText()}\"")
        print()

    def exitLimit_distance_stmt(self, ctx:RelatioLangParser.Limit_distance_stmtContext):
        print("LIMIT DISTANCE:")
        print(f"\tdistance is \"{ctx.INTEGER_LITERAL().getText()}\"")
        print(f"\ttable is \"{ctx.table_name().getText()}\"")
        print()


def main(argv):
    filename = input()
    input_stream = FileStream(filename)
    lexer = RelatioLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RelatioLangParser(stream)
    tree = parser.parse()

    relatio_lang_listiner = RelatioLangListener()
    walker = ParseTreeWalker()
    walker.walk(relatio_lang_listiner, tree)

if __name__ == '__main__':
    main(sys.argv)
