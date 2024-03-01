# import pysimplestplus

# CFG = {
#     "<program>": [
#         [
#             "<global>",
#             pysimplestplus.TT_HOME,
#             pysimplestplus.TT_OPAR,
#             pysimplestplus.TT_CPAR,
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#             "<global>",
#         ],
#     ],
#     "<global>": [
#         [
#             pysimplestplus.TT_FROZEN,
#             "<fr_primitive_or_object>",
#             "<newline>",
#             "<next_global>",
#         ],
#         [
#             "<data_type>",
#             pysimplestplus.TT_IDENTIFIER,
#             "<init_or_func>",
#             "<next_global>",
#         ],
#         [
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_IDENTIFIER,
#             "<init_or_func>",
#             "<next_global>",
#         ],
#         [
#             pysimplestplus.TT_EMPTY,
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_OPAR,
#             "<parameter>",
#             pysimplestplus.TT_CPAR,
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#             "<next_global>",
#         ],
#         [
#             pysimplestplus.TT_GROUP,
#             pysimplestplus.TT_IDENTIFIER,
#             "<inheritance>",
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<group_body>",
#             "<next_global>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<next_global>": [
#         [
#             "<global>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<init_or_func>": [
#         [
#             pysimplestplus.TT_ASSIGN,
#             "<value>",
#             "<newline>",
#         ],
#         [
#             pysimplestplus.TT_OPAR,
#             "<parameter>",
#             pysimplestplus.TT_CPAR,
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#     ],
#     "<inheritance>": [
#         [
#             pysimplestplus.TT_INHERITS,
#             pysimplestplus.TT_IDENTIFIER,
#         ],
#         [
#             None,
#         ],
#     ],
#     "<group_body>": [
#         [
#             "<tab>",
#             "<initializer_or_group_global>",
#         ],
#     ],
#     "<initializer_or_group_global>": [
#         [
#             "<required_initializer>",
#             "<optional_group_global>",
#         ],
#         [
#             "<required_group_global>",
#             "<optional_initializer>",
#         ],
#     ],
#     "<required_group_global>": [
#         [
#             "<access_specifier>",
#             "<group_global>",
#             "<optional_group_global>",
#         ],
#     ],
#     "<group_global>": [
#         [
#             pysimplestplus.TT_FROZEN,
#             "<fr_primitive_or_object>",
#             "<newline>",
#         ],
#         [
#             "<data_type>",
#             pysimplestplus.TT_IDENTIFIER,
#             "<group_init_or_func>",
#         ],
#         [
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_IDENTIFIER,
#             "<group_init_or_func>",
#         ],
#         [
#             pysimplestplus.TT_EMPTY,
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_OPAR,
#             "<parameter>",
#             pysimplestplus.TT_CPAR,
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#     ],
#     "<group_init_or_func>": [
#         [
#             pysimplestplus.TT_ASSIGN,
#             "<value>",
#             "<newline>",
#         ],
#         [
#             pysimplestplus.TT_OPAR,
#             "<parameter>",
#             pysimplestplus.TT_CPAR,
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<optional_group_global>": [
#         [
#             "<tab>",
#             "<required_group_global>",
#             "<optional_group_global>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<required_initializer>": [
#         [
#             pysimplestplus.TT_INITIALIZE,
#             pysimplestplus.TT_OPAR,
#             "<parameter>",
#             pysimplestplus.TT_CPAR,
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#     ],
#     "<optional_initializer>": [
#         [
#             "<tab>",
#             "<initializer_or_group_global>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<access_specifier>": [
#         [
#             pysimplestplus.TT_VISIBLE,
#         ],
#         [
#             pysimplestplus.TT_HIDDEN,
#         ],
#         [
#             pysimplestplus.TT_RESTRICTED,
#         ],
#     ],
#     "<code_block>": [
#         [
#             "<tab>",
#             "<block_definition>",
#         ],
#     ],
#     "<block_definition>": [
#         [
#             "<statements>",
#             "<next_code_block>",
#         ],
#         [
#             pysimplestplus.TT_BACK,
#             "<expression>",
#             "<newline>",
#         ],
#     ],
#     "<statements>": [
#         [
#             "<single_block_statements>",
#             "<newline>",
#         ],
#         [
#             "<multi_block_statements>",
#         ],
#     ],
#     "<next_code_block>": [
#         [
#             "<code_block>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<single_block_statements>": [
#         [
#             pysimplestplus.TT_GLOBAL,
#             pysimplestplus.TT_IDENTIFIER,
#         ],
#         [
#             pysimplestplus.TT_STOP,
#         ],
#         [
#             pysimplestplus.TT_SKIP,
#         ],
#         [
#             pysimplestplus.TT_FROZEN,
#             "<fr_primitive_or_object>",
#         ],
#         [
#             pysimplestplus.TT_IDENTIFIER,
#             "<init_assign_call>",
#         ],
#         [
#             "<castable_type>",
#             "<typecast_or_init>",
#         ],
#         [
#             pysimplestplus.TT_WIKI,
#             "<collectin_suffix>",
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_ASSIGN,
#             "<value>",
#         ],
#         [
#             pysimplestplus.TT_CHOICE,
#             "<collectin_suffix>",
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_ASSIGN,
#             "<value>",
#         ],
#     ],
#     "<fr_primitive_or_object>": [
#         [
#             "<data_type>",
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_ASSIGN,
#             "<value>",
#         ],
#         [
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_ASSIGN,
#             "<value>",
#         ],
#     ],
#     "<typecast_or_init>": [
#         [
#             pysimplestplus.TT_OPAR,
#             "<argument>",
#             pysimplestplus.TT_CPAR,
#         ],
#         [
#             "<collection_suffix>",
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_ASSIGN,
#             "<value>",
#         ],
#     ],
#     "<init_assign_call>": [
#         [pysimplestplus.TT_IDENTIFIER, "<assign_operator>", "<value>"],
#         [
#             "<assign_call>",
#         ],
#     ],
#     "<assign_call>": [
#         [
#             "<dot_tail>",
#         ],
#         [
#             "<assign_operator>",
#             "<value>",
#         ],
#         [
#             pysimplestplus.TT_OPAR,
#             "<argument>",
#             pysimplestplus.TT_CPAR,
#             "<dot_tail>",
#         ],
#         [
#             "<slice_suffix>",
#             "<dot_or_assign>",
#         ],
#     ],
#     "<dot_tail>": [
#         [
#             pysimplestplus.TT_PERIOD,
#             "<id_or_coll_func>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<id_or_coll_func>": [
#         [
#             pysimplestplus.TT_IDENTIFIER,
#             "<assign_call>",
#         ],
#         [
#             pysimplestplus.TT_INITIALIZE,
#             pysimplestplus.TT_OPAR,
#             "<argument>",
#             pysimplestplus.TT_CPAR,
#         ],
#     ],
#     "<dot_or_assign>": [
#         [
#             pysimplestplus.TT_PERIOD,
#             "<id_or_coll_func>",
#         ],
#         [
#             "<assign_operator>",
#             "<value>",
#         ],
#     ],
#     "<multi_block_statements>": [
#         [
#             pysimplestplus.TT_INCASE,
#             "<expression>",
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#             "<unless_instead>",
#         ],
#         [
#             pysimplestplus.TT_GIVEN,
#             "<given_value>",
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<event>",
#             "<default>",
#         ],
#         [
#             pysimplestplus.TT_EVERY,
#             "<data_type>",
#             pysimplestplus.TT_IDENTIFIER,
#             "<opt_pair>",
#             pysimplestplus.TT_IN,
#             "<iterable>",
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#         [
#             pysimplestplus.TT_GO,
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#             "<tab>",
#             pysimplestplus.TT_DURING,
#             "<expression>",
#             "<newline>",
#         ],
#         [
#             pysimplestplus.TT_DURING,
#             "<expression>",
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#     ],
#     "<unless_instead>": [
#         [
#             "<tab>",
#             "<block_stmt_or_unless_instead>",
#         ],
#     ],
#     "<block_stmt_or_unless_instead>": [
#         [
#             "<unless>",
#             "<block_stmt_or_unless_instead>",
#         ],
#         [
#             "<instead>",
#         ],
#         [
#             "<block_definition>",
#         ],
#     ],
#     "<unless>": [
#         [
#             pysimplestplus.TT_UNLESS,
#             "<expression>",
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#     ],
#     "<instead>": [
#         [
#             pysimplestplus.TT_INSTEAD,
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#     ],
#     "<given_value>": [
#         [
#             pysimplestplus.TT_IDENTIFIER,
#             "<variable_tail>",
#         ],
#         [
#             pysimplestplus.TT_OPAR,
#             pysimplestplus.TT_IDENTIFIER,
#             "<variable_tail>",
#             pysimplestplus.TT_CPAR,
#         ],
#     ],
#     "<event>": [
#         [
#             "<tab>",
#             pysimplestplus.TT_EVENT,
#             "<event_value>",
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#             "<next_event>",
#         ],
#     ],
#     "<event_value>": [
#         [
#             pysimplestplus.TT_WORD_LITERAL,
#         ],
#         [pysimplestplus.TT_NUM_LITERAL],
#         [
#             pysimplestplus.TT_DECI_LITERAL,
#         ],
#         [
#             pysimplestplus.TT_YES,
#         ],
#         [
#             pysimplestplus.TT_NO,
#         ],
#     ],
#     "<next_event>": [
#         [
#             "<event>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<default>": [
#         [
#             "<tab>",
#             "<block_stmt_or_default>",
#         ],
#     ],
#     "<block_stmt_or_default>": [
#         [
#             pysimplestplus.TT_DEFAULT,
#             pysimplestplus.TT_COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#         [
#             "<block_definition>",
#         ],
#     ],
#     "<opt_pair>": [
#         [
#             pysimplestplus.TT_COMMA,
#             "<data_type>",
#             pysimplestplus.TT_IDENTIFIER,
#         ],
#         [
#             None,
#         ],
#     ],
#     "<iterable>": [
#         [
#             "<collection_value>",
#         ],
#         [
#             "<wiki_value>",
#         ],
#         [
#             "<func_or_var>",
#         ],
#         [
#             pysimplestplus.TT_WORD_LITERAL,
#         ],
#     ],
#     "<data_type>": [
#         [
#             pysimplestplus.TT_NUM,
#             "<collection_suffix>",
#         ],
#         [
#             pysimplestplus.TT_WORD,
#             "<collection_suffix>",
#         ],
#         [
#             pysimplestplus.TT_DECI,
#             "<collection_suffix>",
#         ],
#         [
#             pysimplestplus.TT_CHOICE,
#             "<collection_suffix>",
#         ],
#         [
#             pysimplestplus.TT_WIKI,
#             "<collection_suffix>",
#         ],
#     ],
#     "<castable_type>": [
#         [
#             pysimplestplus.TT_NUM,
#         ],
#         [
#             pysimplestplus.TT_WORD,
#         ],
#         [
#             pysimplestplus.TT_DECI,
#         ],
#     ],
#     "<return_type>": [
#         [
#             pysimplestplus.TT_EMPTY,
#         ],
#         [
#             "<data_type>",
#         ],
#     ],
#     "<collection_suffix>": [
#         [
#             pysimplestplus.TT_OBRACK,
#             "<collection_index>",
#             pysimplestplus.TT_CBRACK,
#             "<next_collection_suffix>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<next_collection_suffix>": [
#         [
#             "<collection_suffix>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<collection_index>": [
#         [
#             pysimplestplus.TT_NUM_LITERAL,
#         ],
#         [
#             "<func_or_var>",
#         ],
#         [
#             pysimplestplus.TT_OBRACK,
#             "<value>",
#             "<next_item>",
#             pysimplestplus.TT_CBRACK,
#         ],
#     ],
#     "<collection_value>": [
#         [
#             pysimplestplus.TT_OBRACK,
#             "<value>",
#             "<next_item>",
#             pysimplestplus.TT_CBRACK,
#         ],
#     ],
#     "<next_item>": [
#         [
#             pysimplestplus.TT_COMMA,
#             "<value>",
#             "<next_item>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<predefined_func>": [
#         [
#             pysimplestplus.TT_WORD,
#             pysimplestplus.TT_OPAR,
#             "<argument>",
#             pysimplestplus.TT_CPAR,
#         ],
#         [
#             pysimplestplus.TT_NUM,
#             pysimplestplus.TT_OPAR,
#             "<argument>",
#             pysimplestplus.TT_CPAR,
#         ],
#         [
#             pysimplestplus.TT_DECI,
#             pysimplestplus.TT_OPAR,
#             "<argument>",
#             pysimplestplus.TT_CPAR,
#         ],
#     ],
#     "<slice_suffix>": [
#         [
#             pysimplestplus.TT_OBRACK,
#             "<slice_operand>",
#             "<slice>",
#             pysimplestplus.TT_CBRACK,
#         ],
#     ],
#     "<slice>": [
#         [
#             pysimplestplus.TT_COLON,
#             "<slice_operand>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<slice_operand>": [
#         [
#             pysimplestplus.TT_NUM_LITERAL,
#         ],
#         [
#             "<func_or_var>",
#         ],
#     ],
#     "<func_or_var>": [
#         [
#             pysimplestplus.TT_IDENTIFIER,
#             "<func_or_var_tail>",
#         ],
#     ],
#     "<func_or_var_tail>": [
#         [
#             "<variable_tail>",
#         ],
#         [pysimplestplus.TT_OPAR, "<argument>", pysimplestplus.TT_CPAR, "<func_or_var_tail>"],
#         [
#             None,
#         ],
#     ],
#     "<variable_tail>": [
#         [
#             pysimplestplus.TT_PERIOD,
#             pysimplestplus.TT_IDENTIFIER,
#             "<variable_tail>",
#         ],
#         [
#             "<slice_suffix>",
#             "<variable_tail>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<parameter>": [
#         [
#             "<data_type>",
#             pysimplestplus.TT_IDENTIFIER,
#             "<next_parameter>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<next_parameter>": [
#         [
#             pysimplestplus.TT_COMMA,
#             "<parameter>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<argument>": [
#         [
#             "<expression>",
#             "<next_argument>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<next_argument>": [
#         [
#             pysimplestplus.TT_COMMA,
#             "<argument>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<newline>": [
#         [
#             pysimplestplus.TT_NEWLINE,
#             "<next_newline>",
#         ],
#     ],
#     "<next_newline>": [
#         [
#             pysimplestplus.TT_NEWLINE,
#             "<next_newline>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<tab>": [
#         [
#             pysimplestplus.TT_TAB,
#             "<next_tab>",
#         ],
#     ],
#     "<next_tab>": [
#         [
#             "<tab>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<value>": [
#         [
#             "<expression>",
#         ],
#         [
#             "<collection_value>",
#         ],
#         [
#             "<wiki_value>",
#         ],
#     ],
#     "<expression>": [
#         [
#             "<disjunction>",
#         ],
#     ],
#     "<disjunction>": [
#         [
#             "<conjunction>",
#             "<next_disjunction>",
#         ],
#     ],
#     "<next_disjunction>": [
#         [
#             pysimplestplus.TT_OR,
#             "<disjunction>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<conjunction>": [
#         [
#             "<inversion>",
#             "<next_conjunction>",
#         ],
#     ],
#     "<next_conjunction>": [
#         [
#             pysimplestplus.TT_AND,
#             "<conjunction>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<inversion>": [
#         [
#             pysimplestplus.TT_NOT,
#             "<inversion>",
#         ],
#         [
#             "<comparison>",
#         ],
#     ],
#     "<comparison>": [
#         [
#             "<sum>",
#             "<comparison_operand>",
#         ],
#     ],
#     "<comparison_operand>": [
#         [
#             "<comparison_operator>",
#             "<sum>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<comparison_operator>": [
#         [
#             pysimplestplus.TT_LESS_THAN,
#         ],
#         [
#             pysimplestplus.TT_LESS_THAN_EQUAL,
#         ],
#         [
#             pysimplestplus.TT_GREATER_THAN,
#         ],
#         [
#             pysimplestplus.TT_GREATER_THAN_EQUAL,
#         ],
#         [
#             pysimplestplus.TT_NOT_EQUAL,
#         ],
#         [
#             pysimplestplus.TT_EQUAL_TO,
#         ],
#     ],
#     "<sum>": [
#         [
#             "<term>",
#             "<next_term>",
#         ],
#     ],
#     "<term>": [
#         [
#             "<factor>",
#             "<next_factor>",
#         ],
#     ],
#     "<next_term>": [
#         ["<term_operator>", "<sum>"],
#         [
#             None,
#         ],
#     ],
#     "<term_operator>": [
#         [
#             pysimplestplus.TT_PLUS,
#         ],
#         [
#             pysimplestplus.TT_MINUS,
#         ],
#     ],
#     "<factor>": [
#         [
#             "<atom>",
#             "<exponentiation>",
#         ],
#     ],
#     "<next_factor>": [
#         [
#             "<factor_operator>",
#             "<term>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<factor_operator>": [
#         [
#             pysimplestplus.TT_MULTIPLY,
#         ],
#         [
#             pysimplestplus.TT_DIVIDE,
#         ],
#         [
#             pysimplestplus.TT_FLOOR,
#         ],
#         [
#             pysimplestplus.TT_MODULO,
#         ],
#     ],
#     "<exponentiation>": [
#         [
#             pysimplestplus.TT_POWER,
#             "<factor>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<atom>": [
#         [
#             pysimplestplus.TT_WORD_LITERAL,
#         ],
#         [
#             "<numeric>",
#         ],
#         [
#             pysimplestplus.TT_MINUS,
#             "<numeric>",
#         ],
#         [
#             pysimplestplus.TT_YES,
#         ],
#         [
#             pysimplestplus.TT_NO,
#         ],
#         [
#             pysimplestplus.TT_NEW,
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_OPAR,
#             "<argument>",
#             pysimplestplus.TT_CPAR,
#         ],
#         [
#             pysimplestplus.TT_OPAR,
#             "<expresson>",
#             pysimplestplus.TT_CPAR,
#         ],
#         [
#             pysimplestplus.TT_BLANK,
#         ],
#         [
#             "<func_or_var>",
#         ],
#     ],
#     "<numeric>": [
#         [
#             pysimplestplus.TT_NUM_LITERAL,
#         ],
#         [
#             pysimplestplus.TT_DECI_LITERAL,
#         ],
#     ],
#     "<type_cast_tail>": [
#         [
#             pysimplestplus.TT_OPAR,
#             "<argument>",
#             pysimplestplus.TT_CPAR,
#         ],
#     ],
#     "<wiki_value>": [
#         [
#             pysimplestplus.TT_OBRACE,
#             pysimplestplus.TT_WORD_LITERAL,
#             pysimplestplus.TT_COLON,
#             "<value>",
#             "<next_pair>",
#             pysimplestplus.TT_CBRACE,
#         ],
#     ],
#     "<next_pair>": [
#         [
#             pysimplestplus.TT_COMMA,
#             pysimplestplus.TT_WORD_LITERAL,
#             pysimplestplus.TT_COLON,
#             "<expression>",
#             "<next_pair>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<assign_operator>": [
#         [
#             pysimplestplus.TT_ASSIGN,
#         ],
#         [
#             pysimplestplus.TT_PLUS_ASSIGN,
#         ],
#         [
#             pysimplestplus.TT_MINUS_ASSIGN,
#         ],
#         [
#             pysimplestplus.TT_MULTIPLY_ASSIGN,
#         ],
#         [
#             pysimplestplus.TT_DIVIDE_ASSIGN,
#         ],
#         [
#             pysimplestplus.TT_FLOOR_ASSIGN,
#         ],
#         [
#             pysimplestplus.TT_POWER_ASSIGN,
#         ],
#         [
#             pysimplestplus.TT_MODULO_ASSIGN,
#         ],
#     ],
# }


# import pysimplestplus

# CFG = {
#     "<initialization>": [
#         [
#             "<optional_frozen>",
#             "<data_type>",
#             "<optional_coll_suffix>",
#             pysimplestplus.TT_IDENTIFIER,
#             pysimplestplus.TT_ASSIGN,
#             "<expression>",
#         ],
#     ],
#     "<optional_frozen>": [
#         [
#             pysimplestplus.TT_FROZEN,
#         ],
#         [
#             None,
#         ],
#     ],
#     "<data_type>": [
#         [
#             pysimplestplus.TT_NUM,
#         ],
#         [
#             pysimplestplus.TT_DECI,
#         ],
#         [
#             pysimplestplus.TT_WORD,
#         ],
#         [
#             pysimplestplus.TT_LETTER,
#         ],
#         [
#             pysimplestplus.TT_CHOICE,
#         ],
#         [
#             pysimplestplus.TT_WIKI,
#         ],
#         [
#             pysimplestplus.TT_IDENTIFIER,
#         ],
#     ],
#     "<optional_coll_suffix>": [
#         [
#             pysimplestplus.TT_OBRACK,
#             pysimplestplus.TT_CBRACK,
#             "<optional_coll_suffix>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<expression>": [
#         [
#             "<and_expr>",
#             "<next_and_expr>",
#         ],
#         [
#             pysimplestplus.TT_OBRACK,
#             "<optional_coll_values>",
#             pysimplestplus.TT_CBRACK,
#         ],
#         [
#             pysimplestplus.TT_OBRACE,
#             "<optional_wiki_values>",
#             pysimplestplus.TT_CBRACE,
#         ],
#     ],
#     "<and_expr>": [
#         [
#             "<comp_expr>",
#             "<next_comp_expr>",
#         ],
#     ],
#     "<next_and_expr>": [
#         [
#             pysimplestplus.TT_OR,
#             "<and_expr>",
#             "<next_and_expr>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<optional_coll_values>": [
#         [
#             "<expression>",
#             "<next_coll_value>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<next_coll_value>": [
#         [
#             pysimplestplus.TT_COMMA,
#             "<expression>",
#             "<next_coll_value>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<optional_wiki_values>": [
#         [
#             "<key_value_pair>",
#             "<next_key_value_pair>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<key_value_pair>": [
#         [
#             "<key>",
#             pysimplestplus.TT_COLON,
#             "<expression>",
#         ],
#     ],
#     "<key>": [
#         [
#             pysimplestplus.TT_NUM_LITERAL,
#         ],
#         [
#             pysimplestplus.TT_DECI_LITERAL,
#         ],
#         [
#             pysimplestplus.TT_WORD_LITERAL,
#         ],
#         [
#             pysimplestplus.TT_LETTER_LITERAL,
#         ],
#         [
#             pysimplestplus.TT_YES,
#         ],
#         [
#             pysimplestplus.TT_NO,
#         ],
#     ],
#     "<next_key_value_pair>": [
#         [
#             pysimplestplus.TT_COMMA,
#             "<key_value_pair>",
#             "<next_key_value_pair>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<comp_expr>": [
#         [
#             pysimplestplus.TT_NOT,
#             "<comp_expr>",
#         ],
#         [
#             "<arith_expr>",
#             "<next_arith_expr>",
#         ],
#     ],
#     "<next_comp_expr>": [
#         [pysimplestplus.TT_AND, "<comp_expr>", "<next_comp_expr>"],
#         [None],
#     ],
#     "<next_arith_expr>": [
#         [
#             "<comp_operator>",
#             "<arith_expr>",
#             "<next_arith_expr>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<comp_operator>": [
#         [
#             pysimplestplus.TT_EQUAL_TO,
#         ],
#         [
#             pysimplestplus.TT_NOT_EQUAL,
#         ],
#         [
#             pysimplestplus.TT_LESS_THAN,
#         ],
#         [
#             pysimplestplus.TT_GREATER_THAN,
#         ],
#         [
#             pysimplestplus.TT_LESS_THAN_EQUAL,
#         ],
#         [
#             pysimplestplus.TT_GREATER_THAN_EQUAL,
#         ],
#     ],
#     "<arith_expr>": [
#         [
#             "<term>",
#             "<next_term>",
#         ]
#     ],
#     "<term>": [
#         [
#             "<factor>",
#             "<next_factor>",
#         ]
#     ],
#     "<next_term>": [
#         [
#             "<term_operator>",
#             "<term>",
#             "<next_term>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<term_operator>": [
#         [
#             pysimplestplus.TT_PLUS,
#         ],
#         [
#             pysimplestplus.TT_MINUS,
#         ],
#     ],
#     "<factor>": [
#         [
#             pysimplestplus.TT_WORD_LITERAL,
#         ],
#         [
#             pysimplestplus.TT_LETTER_LITERAL,
#         ],
#         [
#             pysimplestplus.TT_YES,
#         ],
#         [
#             pysimplestplus.TT_NO,
#         ],
#         [
#             pysimplestplus.TT_BLANK,
#         ],
#         [
#             pysimplestplus.TT_IDENTIFIER,
#             "<optional_call_tail>",
#         ],
#         [
#             pysimplestplus.TT_MINUS,
#             "<numeric_literal>",
#         ],
#         [
#             "<numeric_literal>",
#         ],
#         [
#             pysimplestplus.TT_OPAR,
#             "<expression>",
#             pysimplestplus.TT_CPAR,
#         ],
#     ],
#     "<next_factor>": [
#         [
#             "<factor_operator>",
#             "<factor>",
#             "<next_factor>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<factor_operator>": [
#         [
#             pysimplestplus.TT_MULTIPLY,
#         ],
#         [
#             pysimplestplus.TT_DIVIDE,
#         ],
#         [
#             pysimplestplus.TT_FLOOR,
#         ],
#         [
#             pysimplestplus.TT_MODULO,
#         ],
#     ],
#     "<optional_call_tail>": [
#         [
#             pysimplestplus.TT_OPAR,
#             "<optional_argument>",
#             pysimplestplus.TT_CPAR,
#         ],
#         [
#             None,
#         ],
#     ],
#     "<optional_argument>": [
#         [
#             "<expression>",
#             "<next_argument>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<next_argument>": [
#         [
#             pysimplestplus.TT_COMMA,
#             "<expression>",
#             "<next_argument>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<numeric_literal>": [
#         [
#             pysimplestplus.TT_NUM_LITERAL,
#         ],
#         [
#             pysimplestplus.TT_DECI_LITERAL,
#         ],
#     ],
# }


import pysimplestplus

CFG = {
    "<program>": [
        [],
    ],
    "<global>": [
        [],
    ],
    "<func_def>": [
        [],
    ],
    "<group_def>": [
        [],
    ],
}
