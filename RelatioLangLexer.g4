/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2020 by Martin Mirchev
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
 * associated documentation files (the "Software"), to deal in the Software without restriction,
 * including without limitation the rights to use, copy, modify, merge, publish, distribute,
 * sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
 * NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 * DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 * Project : sqlite-parser; an ANTLR4 grammar for SQLite https://github.com/bkiers/sqlite-parser
 * Developed by : Bart Kiers, bart@big-o.nl
 */

// $antlr-format alignTrailingComments on, columnLimit 150, maxEmptyLinesToKeep 1, reflowComments off, useTab off
// $antlr-format allowShortRulesOnASingleLine on, alignSemicolons ownLine

lexer grammar RelatioLangLexer;

options {
    caseInsensitive = true;
}

SCOL      : ';';
DOT       : '.';
OPEN_PAR  : '(';
CLOSE_PAR : ')';
COMMA     : ',';
ASSIGN    : '=';
STAR      : '*';
PLUS      : '+';
MINUS     : '-';
TILDE     : '~';
PIPE2     : '||';
DIV       : '/';
MOD       : '%';
LT2       : '<<';
GT2       : '>>';
AMP       : '&';
PIPE      : '|';
LT        : '<';
LT_EQ     : '<=';
GT        : '>';
GT_EQ     : '>=';
EQ        : '==';
NOT_EQ1   : '!=';
NOT_EQ2   : '<>';


OPEN_CUR  : '{';
CLOSE_CUR : '}';
OPEN_SQR  : '[';
CLOSE_SQR : ']';
COLON     : ':';

ALL_               : 'ALL';
AND_               : 'AND';
AS_                : 'AS';
ASC_               : 'ASC';
BETWEEN_           : 'BETWEEN';
BY_                : 'BY';
CASE_              : 'CASE';
COLLATE_           : 'COLLATE';
CROSS_             : 'CROSS';
CURRENT_DATE_      : 'CURRENT_DATE';
CURRENT_TIME_      : 'CURRENT_TIME';
CURRENT_TIMESTAMP_ : 'CURRENT_TIMESTAMP';
DESC_              : 'DESC';
DISTINCT_          : 'DISTINCT';
ELSE_              : 'ELSE';
END_               : 'END';
ESCAPE_            : 'ESCAPE';
EXCEPT_            : 'EXCEPT';
EXISTS_            : 'EXISTS';
FROM_              : 'FROM';
FULL_              : 'FULL';
GLOB_              : 'GLOB';
GROUP_             : 'GROUP';
HAVING_            : 'HAVING';
IF_                : 'IF';
IN_                : 'IN';
INDEXED_           : 'INDEXED';
INNER_             : 'INNER';
INTERSECT_         : 'INTERSECT';
IS_                : 'IS';
ISNULL_            : 'ISNULL';
JOIN_              : 'JOIN';
LEFT_              : 'LEFT';
LIKE_              : 'LIKE';
LIMIT_             : 'LIMIT';
MATCH_             : 'MATCH';
NATURAL_           : 'NATURAL';
NO_                : 'NO';
NOT_               : 'NOT';
NOTNULL_           : 'NOTNULL';
NULL_              : 'NULL';
OFFSET_            : 'OFFSET';
ON_                : 'ON';
OR_                : 'OR';
ORDER_             : 'ORDER';
OUTER_             : 'OUTER';
RIGHT_             : 'RIGHT';
RECURSIVE_         : 'RECURSIVE';
ROW_               : 'ROW';
ROWS_              : 'ROWS';
SELECT_            : 'SELECT';
THEN_              : 'THEN';
UNION_             : 'UNION';
USING_             : 'USING';
VALUES_            : 'VALUES';
WHEN_              : 'WHEN';
WHERE_             : 'WHERE';
WITH_              : 'WITH';
FIRST_VALUE_       : 'FIRST_VALUE';
OVER_              : 'OVER';
PARTITION_         : 'PARTITION';
RANGE_             : 'RANGE';
PRECEDING_         : 'PRECEDING';
UNBOUNDED_         : 'UNBOUNDED';
CURRENT_           : 'CURRENT';
FOLLOWING_         : 'FOLLOWING';
CUME_DIST_         : 'CUME_DIST';
DENSE_RANK_        : 'DENSE_RANK';
LAG_               : 'LAG';
LAST_VALUE_        : 'LAST_VALUE';
LEAD_              : 'LEAD';
NTH_VALUE_         : 'NTH_VALUE';
NTILE_             : 'NTILE';
PERCENT_RANK_      : 'PERCENT_RANK';
RANK_              : 'RANK';
ROW_NUMBER_        : 'ROW_NUMBER';
TRUE_              : 'TRUE';
FALSE_             : 'FALSE';
WINDOW_            : 'WINDOW';
NULLS_             : 'NULLS';
FIRST_             : 'FIRST';
LAST_              : 'LAST';
FILTER_            : 'FILTER';
GROUPS_            : 'GROUPS';
EXCLUDE_           : 'EXCLUDE';
TIES_              : 'TIES';
OTHERS_            : 'OTHERS';

GRAPH_             : 'GRAPH';
SOURCE_            : 'SOURCE';
INCLUDE_           : 'INCLUDE';
EDGE_              : 'EDGE';
ENTER_             : 'ENTER';
EXIT_              : 'EXIT';
VISITS_            : 'VISITS';
FOR_               : 'FOR';
DISTANCE_          : 'DISTANCE';
TRANSFORMER_       : 'TRANSFORMER';
SET_               : 'SET';
GENERATION_        : 'GENERATION';
AMOUNT_            : 'AMOUNT';

IDENTIFIER:
    '"' (~'"' | '""')* '"'
    | '`' (~'`' | '``')* '`'
    | '[' ~']'* ']'
    | [A-Z_\u007F-\uFFFF] [A-Z_0-9\u007F-\uFFFF]*
;

INTEGER_LITERAL: DIGIT+;

NUMERIC_LITERAL: ((DIGIT+ ('.' DIGIT*)?) | ('.' DIGIT+)) ('E' [-+]? DIGIT+)? | '0x' HEX_DIGIT+;

BIND_PARAMETER: '?' DIGIT* | [:@$] IDENTIFIER;

STRING_LITERAL: '\'' ( ~'\'' | '\'\'')* '\'';

BLOB_LITERAL: 'X' STRING_LITERAL;

SINGLE_LINE_COMMENT: '--' ~[\r\n]* (('\r'? '\n') | EOF) -> channel(HIDDEN);

MULTILINE_COMMENT: '/*' .*? '*/' -> channel(HIDDEN);

SPACES: [ \u000B\t\r\n] -> channel(HIDDEN);

UNEXPECTED_CHAR: .;

fragment HEX_DIGIT : [0-9A-F];
fragment DIGIT     : [0-9];
