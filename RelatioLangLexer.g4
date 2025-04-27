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

IDENTIFIER:
    '"' (~'"' | '""')* '"'
    | '`' (~'`' | '``')* '`'
    | '[' ~']'* ']'
    | [A-Z_\u007F-\uFFFF] [A-Z_0-9\u007F-\uFFFF]*
;

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
