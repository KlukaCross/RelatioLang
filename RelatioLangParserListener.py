# Generated from RelatioLangParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RelatioLangParser import RelatioLangParser
else:
    from RelatioLangParser import RelatioLangParser

# This class defines a complete listener for a parse tree produced by RelatioLangParser.
class RelatioLangParserListener(ParseTreeListener):

    # Enter a parse tree produced by RelatioLangParser#parse.
    def enterParse(self, ctx:RelatioLangParser.ParseContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#parse.
    def exitParse(self, ctx:RelatioLangParser.ParseContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#sql_stmt_list.
    def enterSql_stmt_list(self, ctx:RelatioLangParser.Sql_stmt_listContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#sql_stmt_list.
    def exitSql_stmt_list(self, ctx:RelatioLangParser.Sql_stmt_listContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#sql_stmt.
    def enterSql_stmt(self, ctx:RelatioLangParser.Sql_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#sql_stmt.
    def exitSql_stmt(self, ctx:RelatioLangParser.Sql_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#signed_number.
    def enterSigned_number(self, ctx:RelatioLangParser.Signed_numberContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#signed_number.
    def exitSigned_number(self, ctx:RelatioLangParser.Signed_numberContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#common_table_expression.
    def enterCommon_table_expression(self, ctx:RelatioLangParser.Common_table_expressionContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#common_table_expression.
    def exitCommon_table_expression(self, ctx:RelatioLangParser.Common_table_expressionContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#expr.
    def enterExpr(self, ctx:RelatioLangParser.ExprContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#expr.
    def exitExpr(self, ctx:RelatioLangParser.ExprContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#literal_value.
    def enterLiteral_value(self, ctx:RelatioLangParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#literal_value.
    def exitLiteral_value(self, ctx:RelatioLangParser.Literal_valueContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#value_row.
    def enterValue_row(self, ctx:RelatioLangParser.Value_rowContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#value_row.
    def exitValue_row(self, ctx:RelatioLangParser.Value_rowContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#values_clause.
    def enterValues_clause(self, ctx:RelatioLangParser.Values_clauseContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#values_clause.
    def exitValues_clause(self, ctx:RelatioLangParser.Values_clauseContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#graph_source_stmt.
    def enterGraph_source_stmt(self, ctx:RelatioLangParser.Graph_source_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#graph_source_stmt.
    def exitGraph_source_stmt(self, ctx:RelatioLangParser.Graph_source_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#include_edge_stmt.
    def enterInclude_edge_stmt(self, ctx:RelatioLangParser.Include_edge_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#include_edge_stmt.
    def exitInclude_edge_stmt(self, ctx:RelatioLangParser.Include_edge_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#exclude_edge_stmt.
    def enterExclude_edge_stmt(self, ctx:RelatioLangParser.Exclude_edge_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#exclude_edge_stmt.
    def exitExclude_edge_stmt(self, ctx:RelatioLangParser.Exclude_edge_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#no_enter_stmt.
    def enterNo_enter_stmt(self, ctx:RelatioLangParser.No_enter_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#no_enter_stmt.
    def exitNo_enter_stmt(self, ctx:RelatioLangParser.No_enter_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#no_exit_stmt.
    def enterNo_exit_stmt(self, ctx:RelatioLangParser.No_exit_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#no_exit_stmt.
    def exitNo_exit_stmt(self, ctx:RelatioLangParser.No_exit_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#limit_visits_stmt.
    def enterLimit_visits_stmt(self, ctx:RelatioLangParser.Limit_visits_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#limit_visits_stmt.
    def exitLimit_visits_stmt(self, ctx:RelatioLangParser.Limit_visits_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#limit_distance_stmt.
    def enterLimit_distance_stmt(self, ctx:RelatioLangParser.Limit_distance_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#limit_distance_stmt.
    def exitLimit_distance_stmt(self, ctx:RelatioLangParser.Limit_distance_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#transformer_stmt.
    def enterTransformer_stmt(self, ctx:RelatioLangParser.Transformer_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#transformer_stmt.
    def exitTransformer_stmt(self, ctx:RelatioLangParser.Transformer_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#set_generation_values_stmt.
    def enterSet_generation_values_stmt(self, ctx:RelatioLangParser.Set_generation_values_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#set_generation_values_stmt.
    def exitSet_generation_values_stmt(self, ctx:RelatioLangParser.Set_generation_values_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#set_generation_amount_stmt.
    def enterSet_generation_amount_stmt(self, ctx:RelatioLangParser.Set_generation_amount_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#set_generation_amount_stmt.
    def exitSet_generation_amount_stmt(self, ctx:RelatioLangParser.Set_generation_amount_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#select_stmt.
    def enterSelect_stmt(self, ctx:RelatioLangParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#select_stmt.
    def exitSelect_stmt(self, ctx:RelatioLangParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#join_clause.
    def enterJoin_clause(self, ctx:RelatioLangParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#join_clause.
    def exitJoin_clause(self, ctx:RelatioLangParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#select_core.
    def enterSelect_core(self, ctx:RelatioLangParser.Select_coreContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#select_core.
    def exitSelect_core(self, ctx:RelatioLangParser.Select_coreContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#simple_select_stmt.
    def enterSimple_select_stmt(self, ctx:RelatioLangParser.Simple_select_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#simple_select_stmt.
    def exitSimple_select_stmt(self, ctx:RelatioLangParser.Simple_select_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#compound_select_stmt.
    def enterCompound_select_stmt(self, ctx:RelatioLangParser.Compound_select_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#compound_select_stmt.
    def exitCompound_select_stmt(self, ctx:RelatioLangParser.Compound_select_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#table_or_subquery.
    def enterTable_or_subquery(self, ctx:RelatioLangParser.Table_or_subqueryContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#table_or_subquery.
    def exitTable_or_subquery(self, ctx:RelatioLangParser.Table_or_subqueryContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#result_column.
    def enterResult_column(self, ctx:RelatioLangParser.Result_columnContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#result_column.
    def exitResult_column(self, ctx:RelatioLangParser.Result_columnContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#join_operator.
    def enterJoin_operator(self, ctx:RelatioLangParser.Join_operatorContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#join_operator.
    def exitJoin_operator(self, ctx:RelatioLangParser.Join_operatorContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#join_constraint.
    def enterJoin_constraint(self, ctx:RelatioLangParser.Join_constraintContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#join_constraint.
    def exitJoin_constraint(self, ctx:RelatioLangParser.Join_constraintContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#compound_operator.
    def enterCompound_operator(self, ctx:RelatioLangParser.Compound_operatorContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#compound_operator.
    def exitCompound_operator(self, ctx:RelatioLangParser.Compound_operatorContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#column_name_list.
    def enterColumn_name_list(self, ctx:RelatioLangParser.Column_name_listContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#column_name_list.
    def exitColumn_name_list(self, ctx:RelatioLangParser.Column_name_listContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#filter_clause.
    def enterFilter_clause(self, ctx:RelatioLangParser.Filter_clauseContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#filter_clause.
    def exitFilter_clause(self, ctx:RelatioLangParser.Filter_clauseContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#window_defn.
    def enterWindow_defn(self, ctx:RelatioLangParser.Window_defnContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#window_defn.
    def exitWindow_defn(self, ctx:RelatioLangParser.Window_defnContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#over_clause.
    def enterOver_clause(self, ctx:RelatioLangParser.Over_clauseContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#over_clause.
    def exitOver_clause(self, ctx:RelatioLangParser.Over_clauseContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#frame_spec.
    def enterFrame_spec(self, ctx:RelatioLangParser.Frame_specContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#frame_spec.
    def exitFrame_spec(self, ctx:RelatioLangParser.Frame_specContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#frame_clause.
    def enterFrame_clause(self, ctx:RelatioLangParser.Frame_clauseContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#frame_clause.
    def exitFrame_clause(self, ctx:RelatioLangParser.Frame_clauseContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#simple_function_invocation.
    def enterSimple_function_invocation(self, ctx:RelatioLangParser.Simple_function_invocationContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#simple_function_invocation.
    def exitSimple_function_invocation(self, ctx:RelatioLangParser.Simple_function_invocationContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#aggregate_function_invocation.
    def enterAggregate_function_invocation(self, ctx:RelatioLangParser.Aggregate_function_invocationContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#aggregate_function_invocation.
    def exitAggregate_function_invocation(self, ctx:RelatioLangParser.Aggregate_function_invocationContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#window_function_invocation.
    def enterWindow_function_invocation(self, ctx:RelatioLangParser.Window_function_invocationContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#window_function_invocation.
    def exitWindow_function_invocation(self, ctx:RelatioLangParser.Window_function_invocationContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#common_table_stmt.
    def enterCommon_table_stmt(self, ctx:RelatioLangParser.Common_table_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#common_table_stmt.
    def exitCommon_table_stmt(self, ctx:RelatioLangParser.Common_table_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#order_by_stmt.
    def enterOrder_by_stmt(self, ctx:RelatioLangParser.Order_by_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#order_by_stmt.
    def exitOrder_by_stmt(self, ctx:RelatioLangParser.Order_by_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#limit_stmt.
    def enterLimit_stmt(self, ctx:RelatioLangParser.Limit_stmtContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#limit_stmt.
    def exitLimit_stmt(self, ctx:RelatioLangParser.Limit_stmtContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#ordering_term.
    def enterOrdering_term(self, ctx:RelatioLangParser.Ordering_termContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#ordering_term.
    def exitOrdering_term(self, ctx:RelatioLangParser.Ordering_termContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#asc_desc.
    def enterAsc_desc(self, ctx:RelatioLangParser.Asc_descContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#asc_desc.
    def exitAsc_desc(self, ctx:RelatioLangParser.Asc_descContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#frame_left.
    def enterFrame_left(self, ctx:RelatioLangParser.Frame_leftContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#frame_left.
    def exitFrame_left(self, ctx:RelatioLangParser.Frame_leftContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#frame_right.
    def enterFrame_right(self, ctx:RelatioLangParser.Frame_rightContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#frame_right.
    def exitFrame_right(self, ctx:RelatioLangParser.Frame_rightContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#frame_single.
    def enterFrame_single(self, ctx:RelatioLangParser.Frame_singleContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#frame_single.
    def exitFrame_single(self, ctx:RelatioLangParser.Frame_singleContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#window_function.
    def enterWindow_function(self, ctx:RelatioLangParser.Window_functionContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#window_function.
    def exitWindow_function(self, ctx:RelatioLangParser.Window_functionContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#offset.
    def enterOffset(self, ctx:RelatioLangParser.OffsetContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#offset.
    def exitOffset(self, ctx:RelatioLangParser.OffsetContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#default_value.
    def enterDefault_value(self, ctx:RelatioLangParser.Default_valueContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#default_value.
    def exitDefault_value(self, ctx:RelatioLangParser.Default_valueContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#partition_by.
    def enterPartition_by(self, ctx:RelatioLangParser.Partition_byContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#partition_by.
    def exitPartition_by(self, ctx:RelatioLangParser.Partition_byContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#order_by_expr.
    def enterOrder_by_expr(self, ctx:RelatioLangParser.Order_by_exprContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#order_by_expr.
    def exitOrder_by_expr(self, ctx:RelatioLangParser.Order_by_exprContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#order_by_expr_asc_desc.
    def enterOrder_by_expr_asc_desc(self, ctx:RelatioLangParser.Order_by_expr_asc_descContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#order_by_expr_asc_desc.
    def exitOrder_by_expr_asc_desc(self, ctx:RelatioLangParser.Order_by_expr_asc_descContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#expr_asc_desc.
    def enterExpr_asc_desc(self, ctx:RelatioLangParser.Expr_asc_descContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#expr_asc_desc.
    def exitExpr_asc_desc(self, ctx:RelatioLangParser.Expr_asc_descContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#unary_operator.
    def enterUnary_operator(self, ctx:RelatioLangParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#unary_operator.
    def exitUnary_operator(self, ctx:RelatioLangParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#column_alias.
    def enterColumn_alias(self, ctx:RelatioLangParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#column_alias.
    def exitColumn_alias(self, ctx:RelatioLangParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#function_call.
    def enterFunction_call(self, ctx:RelatioLangParser.Function_callContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#function_call.
    def exitFunction_call(self, ctx:RelatioLangParser.Function_callContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#set_of_values.
    def enterSet_of_values(self, ctx:RelatioLangParser.Set_of_valuesContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#set_of_values.
    def exitSet_of_values(self, ctx:RelatioLangParser.Set_of_valuesContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#range_of_values.
    def enterRange_of_values(self, ctx:RelatioLangParser.Range_of_valuesContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#range_of_values.
    def exitRange_of_values(self, ctx:RelatioLangParser.Range_of_valuesContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#keyword.
    def enterKeyword(self, ctx:RelatioLangParser.KeywordContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#keyword.
    def exitKeyword(self, ctx:RelatioLangParser.KeywordContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#name.
    def enterName(self, ctx:RelatioLangParser.NameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#name.
    def exitName(self, ctx:RelatioLangParser.NameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#function_name.
    def enterFunction_name(self, ctx:RelatioLangParser.Function_nameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#function_name.
    def exitFunction_name(self, ctx:RelatioLangParser.Function_nameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#schema_name.
    def enterSchema_name(self, ctx:RelatioLangParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#schema_name.
    def exitSchema_name(self, ctx:RelatioLangParser.Schema_nameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#table_name.
    def enterTable_name(self, ctx:RelatioLangParser.Table_nameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#table_name.
    def exitTable_name(self, ctx:RelatioLangParser.Table_nameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#column_name.
    def enterColumn_name(self, ctx:RelatioLangParser.Column_nameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#column_name.
    def exitColumn_name(self, ctx:RelatioLangParser.Column_nameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#collation_name.
    def enterCollation_name(self, ctx:RelatioLangParser.Collation_nameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#collation_name.
    def exitCollation_name(self, ctx:RelatioLangParser.Collation_nameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#index_name.
    def enterIndex_name(self, ctx:RelatioLangParser.Index_nameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#index_name.
    def exitIndex_name(self, ctx:RelatioLangParser.Index_nameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#table_alias.
    def enterTable_alias(self, ctx:RelatioLangParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#table_alias.
    def exitTable_alias(self, ctx:RelatioLangParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#transaction_name.
    def enterTransaction_name(self, ctx:RelatioLangParser.Transaction_nameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#transaction_name.
    def exitTransaction_name(self, ctx:RelatioLangParser.Transaction_nameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#window_name.
    def enterWindow_name(self, ctx:RelatioLangParser.Window_nameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#window_name.
    def exitWindow_name(self, ctx:RelatioLangParser.Window_nameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#alias.
    def enterAlias(self, ctx:RelatioLangParser.AliasContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#alias.
    def exitAlias(self, ctx:RelatioLangParser.AliasContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#filename.
    def enterFilename(self, ctx:RelatioLangParser.FilenameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#filename.
    def exitFilename(self, ctx:RelatioLangParser.FilenameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#base_window_name.
    def enterBase_window_name(self, ctx:RelatioLangParser.Base_window_nameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#base_window_name.
    def exitBase_window_name(self, ctx:RelatioLangParser.Base_window_nameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#simple_func.
    def enterSimple_func(self, ctx:RelatioLangParser.Simple_funcContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#simple_func.
    def exitSimple_func(self, ctx:RelatioLangParser.Simple_funcContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#aggregate_func.
    def enterAggregate_func(self, ctx:RelatioLangParser.Aggregate_funcContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#aggregate_func.
    def exitAggregate_func(self, ctx:RelatioLangParser.Aggregate_funcContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#table_function_name.
    def enterTable_function_name(self, ctx:RelatioLangParser.Table_function_nameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#table_function_name.
    def exitTable_function_name(self, ctx:RelatioLangParser.Table_function_nameContext):
        pass


    # Enter a parse tree produced by RelatioLangParser#any_name.
    def enterAny_name(self, ctx:RelatioLangParser.Any_nameContext):
        pass

    # Exit a parse tree produced by RelatioLangParser#any_name.
    def exitAny_name(self, ctx:RelatioLangParser.Any_nameContext):
        pass



del RelatioLangParser