from .tokens import TokenType

CFG = {
    "<program>": [
        [
            "<global>",
            TokenType.HOME,
            TokenType.OPAR,
            TokenType.CPAR,
            TokenType.COLON,
            "<newline>",
            "<code_block>",
            "<global>",
        ],
    ],
    "<global>": [
        [
            "<frozen_var>",
            "<data_type>",
            TokenType.IDENTIFIER,
            TokenType.ASSIGN,
            "<value>",
            "<newline>",
            "<next_global>",
        ],
        [
            "<function>",
            "<next_global>",
        ],
        [
            "<group>",
            "<next_global>",
        ],
        [
            None,
        ],
    ],
    "<next_global>": [
        [
            "<global>",
        ],
        [
            None,
        ],
    ],
    "<function>": [
        [
            "<return_type>",
            TokenType.IDENTIFIER,
            TokenType.OPAR,
            "<parameter>",
            TokenType.CPAR,
            TokenType.COLON,
            "<newline>",
            "<code_block>",
        ],
    ],
    "<method>": [
        [
            "<access_specifier>",
            "<return_type>",
            TokenType.IDENTIFIER,
            TokenType.OPAR,
            "<parameter>",
            TokenType.CPAR,
            TokenType.COLON,
            "<newline>",
            "<code_block>",
        ],
    ],
    "<code_block>": [
        [
            "<tab>",
            "<statement>",
            "<newline>",
            "<next_code_block>",
        ],
    ],
    "<next_code_block>": [
        [
            "<code_block>",
        ],
        [
            None,
        ],
    ],
    "<return_type>": [
        [
            "<data_type>",
        ],
        [
            TokenType.EMPTY,
        ],
    ],
    "<data_type>": [
        [
            TokenType.WORD,
            "<collection_suffix>",
        ],
        [
            TokenType.NUM,
            "<collection_suffix>",
        ],
        [
            TokenType.DECI,
            "<collection_suffix>",
        ],
        [
            TokenType.CHOICE,
            "<collection_suffix>",
        ],
        [
            TokenType.IDENTIFIER,
            "<collection_suffix>",
        ],
    ],
    "<collection_suffix>": [
        [
            TokenType.OBRACK,
            TokenType.CBRACK,
        ],
        [
            None,
        ],
    ],
    "<parameter>": [
        [
            "<data_type>",
            TokenType.IDENTIFIER,
            "<next_parameter>",
        ],
        [
            None,
        ],
    ],
    "<next_parameter>": [
        [
            TokenType.COMMA,
            "<parameter>",
        ],
        [
            None,
        ],
    ],
    "<group>": [
        [
            TokenType.GROUP,
            TokenType.IDENTIFIER,
            "<inheritance>",
            TokenType.COLON,
            "<newline>",
            "<group_body>",
        ]
    ],
    "<inheritance>": [
        [
            TokenType.INHERITS,
            TokenType.IDENTIFIER,
        ],
        [
            None,
        ],
    ],
    "<group_body>": [
        [
            "<group_global>",
            "<initializer>",
            "<next_group_global>",
        ],
        [
            "<next_group_global>",
            "<initializer>",
            "<group_global>",
        ],
    ],
    "<group_global>": [
        [
            "<tab>",
            "<field>",
            "<newline>",
            "<next_group_global>",
        ],
        [
            "<tab>",
            "<method>",
            "<next_group_global>",
        ],
    ],
    "<next_group_global>": [
        [
            "<group_global>",
        ],
        [
            None,
        ],
    ],
    "<initializer>": [
        [
            "<tab>",
            TokenType.INITIALIZE,
            TokenType.OPAR,
            "<parameter>",
            TokenType.CPAR,
            TokenType.COLON,
            "<newline>",
            "<code_block>",
        ],
        [
            None,
        ],
    ],
    "<field>": [
        [
            "<access_specifier>",
            "<data_type>",
            TokenType.IDENTIFIER,
            "<field_value>",
        ],
        [
            "<access_specifier>",
            TokenType.FROZEN,
            "<data_type>",
            TokenType.IDENTIFIER,
            TokenType.ASSIGN,
            "<value>",
        ],
    ],
    "<field_value>": [
        [
            TokenType.ASSIGN,
            "<value>",
        ],
        [
            None,
        ],
    ],
    "<access_specifier>": [
        [
            TokenType.VISIBLE,
        ],
        [
            TokenType.HIDDEN,
        ],
        [
            TokenType.RESTRICTED,
        ],
    ],
    "<expression>": [
        [
            "<operand>",
            "<next_operand>",
        ],
        [
            TokenType.NOT,
            "<expression>",
        ],
    ],
    "<next_operand>": [
        [
            None,
        ],
        [
            "<operator>",
            "<expression>",
        ],
    ],
    "<operand>": [
        [
            "<function_call>",
        ],
        [
            TokenType.MINUS,
            "<numeric>",
        ],
        [
            TokenType.OPAR,
            "<expression>",
            TokenType.CPAR,
        ],
        [
            "<variable>",
        ],
        [
            "<numeric>",
        ],
        [
            TokenType.WORD_LITERAL,
        ],
        [
            TokenType.YES,
        ],
        [
            TokenType.NO,
        ],
    ],
    "<numeric>": [
        [
            TokenType.NUM_LITERAL,
        ],
        [
            TokenType.DECI_LITERAL,
        ],
    ],
    "<operator>": [
        [
            TokenType.PLUS,
        ],
        [
            TokenType.MINUS,
        ],
        [
            TokenType.MULTIPLY,
        ],
        [
            TokenType.DIVIDE,
        ],
        [
            TokenType.FLOOR,
        ],
        [
            TokenType.MODULO,
        ],
        [
            TokenType.POWER,
        ],
        [
            TokenType.GREATER_THAN,
        ],
        [
            TokenType.LESS_THAN,
        ],
        [
            TokenType.GREATER_THAN_EQUAL,
        ],
        [
            TokenType.LESS_THAN_EQUAL,
        ],
        [
            TokenType.EQUAL_TO,
        ],
        [
            TokenType.NOT_EQUAL,
        ],
        [
            TokenType.AND,
        ],
        [
            TokenType.OR,
        ],
    ],
    "<statement>": [
        [
            "<function_call>",
        ],
        [
            "<frozen_var>",
            "<data_type>",
            TokenType.IDENTIFIER,
            TokenType.ASSIGN,
            "<value>",
        ],
        [
            "<variable>",
            "<assign_operator>",
            "<value>",
        ],
        [
            TokenType.INCASE,
            "<expression>",
            TokenType.COLON,
            "<newline>",
            "<code_block>",
            "<unless>",
            "<instead>",
        ],
        [
            TokenType.GIVEN,
            "<variable>",
            TokenType.COLON,
            "<newline>",
            "<event>",
            "<default>",
        ],
        [
            TokenType.EVERY,
            "<data_type>",
            TokenType.IDENTIFIER,
            TokenType.IN,
            "<iterable>",
            TokenType.COLON,
            "<newline>",
            "<code_block>",
        ],
        [
            TokenType.DURING,
            "<expression>",
            TokenType.COLON,
            "<newline>",
            "<code_block>",
        ],
        [
            TokenType.GO,
            TokenType.COLON,
            "<newline>",
            "<code_block>",
            TokenType.DURING,
            "<expression>",
        ],
    ],
    "<frozen_var>": [
        [
            TokenType.FROZEN,
        ],
        [
            None,
        ],
    ],
    "<assign_operator>": [
        [
            TokenType.ASSIGN,
        ],
        [
            TokenType.PLUS_ASSIGN,
        ],
        [
            TokenType.MINUS_ASSIGN,
        ],
        [
            TokenType.MULTIPLY_ASSIGN,
        ],
        [
            TokenType.DIVIDE_ASSIGN,
        ],
        [
            TokenType.FLOOR_ASSIGN,
        ],
        [
            TokenType.POWER_ASSIGN,
        ],
        [
            TokenType.MODULO_ASSIGN,
        ],
    ],
    "<unless>": [
        [
            TokenType.UNLESS,
            "<expression>",
            TokenType.COLON,
            "<newline>",
            "<code_block>",
            "<next_unless>",
        ],
        [
            None,
        ],
    ],
    "<next_unless>": [
        [
            "<unless>",
        ],
        [
            None,
        ],
    ],
    "<instead>": [
        [
            TokenType.INSTEAD,
            TokenType.COLON,
            "<newline>",
            "<code_block>",
        ],
        [
            None,
        ],
    ],
    "<default>": [
        [
            TokenType.DEFAULT,
            TokenType.COLON,
            "<newline>",
            "<code_block>",
        ],
        [
            None,
        ],
    ],
    "<event>": [
        [
            TokenType.EVENT,
            "<event_value>",
            TokenType.COLON,
            "<newline>",
            "<code_block>",
            "<next_event>",
        ],
    ],
    "<event_value>": [
        [
            TokenType.WORD_LITERAL,
        ],
        [TokenType.NUM_LITERAL],
        [
            TokenType.DECI_LITERAL,
        ],
    ],
    "<next_event>": [
        [
            "<event>",
        ],
        [
            None,
        ],
    ],
    "<iterable>": [
        [
            "<collection_value>",
        ],
        [
            "<variable>",
        ],
        [
            "<function_call>",
        ],
    ],
    "<variable>": [
        [
            "<normal_variable>",
        ],
        [
            "<object>",
            "<next_variable>",
        ],
    ],
    "<normal_variable>": [
        [
            TokenType.IDENTIFIER,
            "<next_variable>",
        ],
    ],
    "<next_variable>": [
        [
            TokenType.PERIOD,
            "<normal_variable>",
            "<next_variable>",
        ],
        [
            None,
        ],
    ],
    "<object>": [
        [
            TokenType.PARENT,
        ],
        [
            TokenType.SELF,
        ],
    ],
    "<value>": [
        [
            "<expression>",
        ],
        [
            "<collection_value>",
        ],
        [
            "<wiki_value>",
        ],
        [
            TokenType.NEW,
            TokenType.IDENTIFIER,
            TokenType.OPAR,
            "<argument>",
            TokenType.CPAR,
        ],
    ],
    "<collection_value>": [
        [
            TokenType.OBRACK,
            "<opt_newline_tab>",
            "<value>",
            "<next_item>",
            "<opt_newline_tab>",
            TokenType.CBRACK,
        ],
    ],
    "<next_item>": [
        [
            TokenType.COMMA,
            "<opt_newline_tab>",
            "<expression>",
            "<next_item>",
        ],
        [
            None,
        ],
    ],
    "<wiki_value>": [
        [
            TokenType.OBRACE,
            "<opt_newline_tab>",
            "<key>",
            TokenType.COLON,
            "<value>",
            "<next_pair>",
            "<opt_newline_tab>",
            TokenType.CBRACE,
        ],
    ],
    "<key>": [
        [
            TokenType.WORD_LITERAL,
        ],
        [
            "<variable>",
        ],
    ],
    "<next_pair>": [
        [
            TokenType.COMMA,
            "<opt_newline_tab>",
            "<key>",
            TokenType.COLON,
            "<expression>",
            "<next_pair>",
        ],
        [
            None,
        ],
    ],
    "<function_call>": [
        [
            TokenType.IDENTIFIER,
            TokenType.OPAR,
            "<argument>",
            TokenType.CPAR,
        ],
        [
            "<variable>",
            TokenType.PERIOD,
            "<function_call>",
        ],
        [
            "<object>",
            TokenType.PERIOD,
            TokenType.INITIALIZE,
            TokenType.OPAR,
            "<argument>",
            TokenType.CPAR,
        ],
        [
            TokenType.RANGE,
            TokenType.OPAR,
            "<argument>",
            TokenType.CPAR,
        ],
        [
            TokenType.INP,
            TokenType.OPAR,
            "<argument>",
            TokenType.CPAR,
        ],
        [
            TokenType.OUT,
            TokenType.OPAR,
            "<argument>",
            TokenType.CPAR,
        ],
        [
            TokenType.WORD,
            TokenType.OPAR,
            "<argument>",
            TokenType.CPAR,
        ],
        [
            TokenType.NUM,
            TokenType.OPAR,
            "<argument>",
            TokenType.CPAR,
        ],
        [
            TokenType.DECI,
            TokenType.OPAR,
            "<argument>",
            TokenType.CPAR,
        ],
    ],
    "<argument>": [
        [
            "<expression>",
            "<next_argument>",
        ],
        [
            None,
        ],
    ],
    "<next_argument>": [
        [
            TokenType.COMMA,
            "<argument>",
        ],
        [
            None,
        ],
    ],
    "<newline>": [
        [
            TokenType.NEWLINE,
            "<next_newline>",
        ],
        [
            TokenType.EOF,
        ],
    ],
    "<next_newline>": [
        [
            TokenType.NEWLINE,
            "<next_newline>",
        ],
        [
            None,
        ],
    ],
    "<tab>": [
        [
            TokenType.TAB,
            "<next_tab>",
        ],
    ],
    "<next_tab>": [
        [
            "<tab>",
        ],
        [
            None,
        ],
    ],
    "<opt_newline_tab>": [
        [
            TokenType.NEWLINE,
            "<tab>",
        ],
        [
            None,
        ],
    ],
}

# CFG = {
#     "<relational_expression>": [
#         [
#             "<relational_operand>",
#             "<relational_operator>",
#             "<relational_operand>",
#         ],
#         [
#             TokenType.OPAR,
#             "<relational_expression>",
#             TokenType.CPAR,
#         ]
#     ],
#     "<relational_operand>": [
#         [TokenType.IDENTIFIER],
#         [
#             TokenType.MINUS,
#             TokenType.NUM_LITERAL,
#         ],
#         [
#             TokenType.MINUS,
#             TokenType.DECI_LITERAL,
#         ],
#         [TokenType.NUM_LITERAL],
#         [TokenType.DECI_LITERAL],
#         [TokenType.WORD_LITERAL],
#         ["<arithmetic_expression>"],
#     ],
#     "<relational_operator>": [
#         [TokenType.EQUAL_TO],
#         [TokenType.NOT_EQUAL],
#         [TokenType.LESS_THAN],
#         [TokenType.GREATER_THAN],
#         [TokenType.LESS_THAN_EQUAL],
#         [TokenType.GREATER_THAN_EQUAL],
#     ],
#     "<logical_expression>": [
#         [
#             "<logical_operand>",
#             "<logical_operator>",
#             "<logical_operand>",
#             "<next_logical>",
#         ],
#         [
#             TokenType.NOT,
#             "<logical_expression>",
#         ],
#         [
#             TokenType.NOT,
#             "<relational_expression>",
#         ],
#         [
#             TokenType.OPAR,
#             "<logical_expression>",
#             TokenType.CPAR,
#         ],
#     ],
#     "<next_logical>": [
#         [None],
#         [
#             "<logical_operator>",
#             "<logical_operand>",
#             "<next_logical>",
#         ],
#     ],
#     "<logical_operand>": [
#         ["<relational_expression>"],
#         ["<logical_expression>"],
#         [TokenType.IDENTIFIER],
#         [TokenType.YES],
#         [TokenType.NO],
#     ],
#     "<logical_operator>": [
#         [TokenType.AND],
#         [TokenType.OR],
#     ],
#     "<arithmetic_expression>": [
#         [
#             "<term>",
#             "<next_term>",
#         ],
#         [
#             TokenType.OPAR,
#             "<arithmetic_expression>",
#             TokenType.CPAR,
#         ],
#     ],
#     "<next_term>": [
#         [None],
#         [
#             "<term_operator>",
#             "<arithmetic_expression>",
#         ],
#     ],
#     "<term>": [
#         [
#             "<factor>",
#             "<next_factor>",
#         ],
#     ],
#     "<next_factor>": [
#         [None],
#         [
#             "<factor_operator>",
#             "<term>",
#         ],
#     ],
#     "<term_operator>": [
#         [TokenType.PLUS],
#         [TokenType.MINUS],
#     ],
#     "<factor>": [
#         [TokenType.IDENTIFIER],
#         [
#             TokenType.MINUS,
#             TokenType.NUM_LITERAL,
#         ],
#         [
#             TokenType.MINUS,
#             TokenType.DECI_LITERAL,
#         ],
#         [TokenType.NUM_LITERAL],
#         [TokenType.DECI_LITERAL],
#         ["<arithmetic_expression>"],
#     ],
#     "<factor_operator>": [
#         [TokenType.MULTIPLY],
#         [TokenType.DIVIDE],
#     ],
# }

# CFG = {
#     "<relational_expression>": [
#         [
#             "<arithmetic_expression>",
#             "<relational_operator>",
#             "<arithmetic_expression>",
#         ]
#     ],
#     "<relational_operator>": [
#         [TokenType.EQUAL_TO],
#         [TokenType.NOT_EQUAL],
#         [TokenType.LESS_THAN],
#         [TokenType.GREATER_THAN],
#         [TokenType.LESS_THAN_EQUAL],
#         [TokenType.GREATER_THAN_EQUAL],
#     ],
#     "<logical_expression>": [
#         [
#             "<logical_operand>",
#             "<logical_operator>",
#             "<logical_operand>",
#             "<next_logical>",
#         ]
#     ],
#     "<next_logical>": [
#         [None],
#         [
#             "<logical_operator>",
#             "<logical_operand>",
#             "<next_logical>",
#         ],
#     ],
#     "<logical_operand>": [
#         [
#             TokenType.OPAR,
#             "<logical_expression>",
#             TokenType.CPAR,
#         ],
#         ["<relational_expression>"],
#         [TokenType.IDENTIFIER],
#         [TokenType.YES],
#         [TokenType.NO],
#     ],
#     "<logical_operator>": [
#         [TokenType.AND],
#         [TokenType.OR],
#     ],
#     "<arithmetic_expression>": [
#         [
#             "<term>",
#             "<next_term>",
#         ],
#     ],
#     "<next_term>": [
#         [None],
#         [
#             "<term_operator>",
#             "<arithmetic_expression>",
#         ],
#     ],
#     "<term>": [
#         [
#             "<factor>",
#             "<next_factor>",
#         ],
#     ],
#     "<next_factor>": [
#         [None],
#         [
#             "<factor_operator>",
#             "<term>",
#         ],
#     ],
#     "<term_operator>": [
#         [TokenType.PLUS],
#         [TokenType.MINUS],
#     ],
#     "<factor>": [
#         [TokenType.IDENTIFIER],
#         ["<numeric>"],
#         [
#             TokenType.MINUS,
#             "<numeric>",
#         ],
#         [
#             TokenType.OPAR,
#             "<arithmetic_expression>",
#             TokenType.CPAR,
#         ],
#     ],
#     "<factor_operator>": [
#         [TokenType.MULTIPLY],
#         [TokenType.DIVIDE],
#     ],
#     "<numeric>": [
#         [TokenType.NUM_LITERAL],
#         [TokenType.DECI_LITERAL],
#     ],
# }

# from tokens import TokenType

# CFG = {
#     "<program>": [
#         [
#             "<global>",
#             TokenType.HOME,
#             TokenType.OPAR,
#             TokenType.CPAR,
#             TokenType.COLON,
#             "<newline>",
#             "<code_block>",
#             "<global>",
#         ],
#     ],
#     "<global>": [
#         [
#             "<frozen_var>",
#             "<data_type>",
#             TokenType.IDENTIFIER,
#             TokenType.ASSIGN,
#             "<value>",
#             "<newline>",
#             "<next_global>",
#         ],
#         [
#             "<function>",
#             "<next_global>",
#         ],
#         [
#             "<group>",
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
#     "<function>": [
#         [
#             "<return_type>",
#             TokenType.IDENTIFIER,
#             TokenType.OPAR,
#             "<parameter>",
#             TokenType.CPAR,
#             "<newline>",
#             "<code_block>",
#         ],
#     ],
#     "<method>": [
#         [
#             "<access_specifier>",
#             "<return_type>",
#             TokenType.IDENTIFIER,
#             TokenType.OPAR,
#             "<parameter>",
#             TokenType.CPAR,
#             "<newline>",
#             "<code_block>",
#         ],
#     ],
#     "<code_block>": [
#         [
#             "<tab>",
#             "<statement>",
#             "<newline>",
#             "<next_code_block>",
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
#     "<return_type>": [
#         [
#             "<data_type>",
#         ],
#         [
#             TokenType.EMPTY,
#         ],
#     ],
#     "<data_type>": [
#         [
#             TokenType.WORD,
#             "<collection_suffix>",
#         ],
#         [
#             TokenType.NUM,
#             "<collection_suffix>",
#         ],
#         [
#             TokenType.DECI,
#             "<collection_suffix>",
#         ],
#         [
#             TokenType.CHOICE,
#             "<collection_suffix>",
#         ],
#         [
#             TokenType.IDENTIFIER,
#             "<collection_suffix>",
#         ],
#     ],
#     "<collection_suffix>": [
#         [
#             TokenType.OBRACK,
#             TokenType.CBRACK,
#         ],
#         [
#             None,
#         ],
#     ],
#     "<parameter>": [
#         [
#             "<data_type>",
#             TokenType.IDENTIFIER,
#             "<next_parameter>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<next_parameter>": [
#         [
#             TokenType.COMMA,
#             "<data_type>",
#             TokenType.IDENTIFIER,
#             "<next_parameter>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<group>": [
#         [
#             TokenType.GROUP,
#             TokenType.IDENTIFIER,
#             "<inheritance>",
#             TokenType.COLON,
#             "<newline>",
#             "<group_global>",
#             "<initializer>",
#             "<next_group_global>",
#         ]
#     ],
#     "<inheritance>": [
#         [
#             TokenType.INHERITS,
#             TokenType.IDENTIFIER,
#         ],
#         [
#             None,
#         ]
#     ],
#     "<group_global>": [
#         [
#             "<tab>",
#             "<field>",
#             "<newline>",
#             "<next_group_global>",
#         ],
#         [
#             "<tab>",
#             "<method>",
#             "<next_group_global>",
#         ],
#     ],
#     "<next_group_global>": [
#         [
#             "<group_global>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<initializer>": [
#         [
#             "<tab>",
#             TokenType.INITIALIZE,
#             TokenType.OPAR,
#             "<parameter>",
#             TokenType.CPAR,
#             TokenType.COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#         [
#             None,
#         ]
#     ],
#     "<field>": [
#         [
#             "<access_specifier>",
#             "<data_type>",
#             TokenType.IDENTIFIER,
#             "<field_value>",
#         ],
#         [
#             "<access_specifier>",
#             TokenType.FROZEN,
#             "<data_type>",
#             TokenType.IDENTIFIER,
#             TokenType.ASSIGN,
#             "<value>",
#         ],
#     ],
#     "<field_value>": [
#         [
#             TokenType.ASSIGN,
#             "<value>",
#         ],
#         [
#             None,
#         ]
#     ],
#     "<access_specifier>": [
#         [
#             TokenType.VISIBLE,
#         ],
#         [
#             TokenType.HIDDEN,
#         ],
#         [
#             TokenType.RESTRICTED,
#         ],
#     ],
#     "<expression>": [
#         [
#             "<operand>",
#             "<next_operand>",
#         ],
#     ],
#     "<next_operand>": [
#         [
#             "<operator>",
#             "<expression>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<operand>": [
#         [
#             "<function_call>",
#         ],
#         [
#             TokenType.MINUS,
#             "<numeric>",
#         ],
#         [
#             TokenType.NOT,
#             "<expression>",
#         ],
#         [
#             TokenType.OPAR,
#             "<expression>",
#             TokenType.CPAR,
#         ],
#         [
#             "<variable>",
#         ],
#         [
#             "<numeric>",
#         ],
#         [
#             TokenType.WORD_LITERAL,
#         ],
#         [
#             TokenType.YES,
#         ],
#         [
#             TokenType.NO,
#         ],
#     ],
#     "<numeric>": [
#         [
#             TokenType.NUM_LITERAL,
#         ],
#         [
#             TokenType.DECI_LITERAL,
#         ],
#     ],
#     "<operator>": [
#         [
#             TokenType.PLUS,
#         ],
#         [
#             TokenType.MINUS,
#         ],
#         [
#             TokenType.MULTIPLY,
#         ],
#         [
#             TokenType.DIVIDE,
#         ],
#         [
#             TokenType.FLOOR,
#         ],
#         [
#             TokenType.MODULO,
#         ],
#         [
#             TokenType.POWER,
#         ],
#         [
#             TokenType.GREATER_THAN,
#         ],
#         [
#             TokenType.LESS_THAN,
#         ],
#         [
#             TokenType.GREATER_THAN_EQUAL,
#         ],
#         [
#             TokenType.LESS_THAN_EQUAL,
#         ],
#         [
#             TokenType.EQUAL_TO,
#         ],
#         [
#             TokenType.NOT_EQUAL,
#         ],
#         [
#             TokenType.AND,
#         ],
#         [
#             TokenType.OR,
#         ],
#     ],
#     "<statement>": [
#         [
#             "<frozen_var>",
#             "<data_type>",
#             TokenType.IDENTIFIER,
#             TokenType.ASSIGN,
#             "<value>",
#         ],
#         [
#             "<variable>",
#             "<assign_operator>",
#             "<value>",
#         ],
#         [
#             TokenType.INCASE,
#             "<expression>",
#             TokenType.COLON,
#             "<newline>",
#             "<code_block>",
#             "<unless>",
#             "<instead>",
#         ],
#         [
#             TokenType.GIVEN,
#             "<variable>",
#             TokenType.COLON,
#             "<newline>",
#             "<event>",
#             "<default>",
#         ],
#         [
#             TokenType.EVERY,
#             "<data_type>",
#             TokenType.IDENTIFIER,
#             TokenType.IN,
#             "<iterable>",
#             TokenType.COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#         [
#             TokenType.DURING,
#             "<expression>",
#             TokenType.COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#         [
#             TokenType.GO,
#             TokenType.COLON,
#             "<newline>",
#             "<code_block>",
#             TokenType.DURING,
#             "<expression>",
#         ],
#     ],
#     "<frozen_var>": [
#         [
#             TokenType.FROZEN,
#         ],
#         [
#             None,
#         ],
#     ],
#     "<assign_operator>": [
#         [
#             TokenType.ASSIGN,
#         ],
#         [
#             TokenType.PLUS_ASSIGN,
#         ],
#         [
#             TokenType.MINUS_ASSIGN,
#         ],
#         [
#             TokenType.MULTIPLY_ASSIGN,
#         ],
#         [
#             TokenType.DIVIDE_ASSIGN,
#         ],
#         [
#             TokenType.FLOOR_ASSIGN,
#         ],
#         [
#             TokenType.POWER_ASSIGN,
#         ],
#         [
#             TokenType.MODULO_ASSIGN,
#         ],
#     ],
#     "<unless>": [
#         [
#             TokenType.UNLESS,
#             "<expression>",
#             TokenType.COLON,
#             "<newline>",
#             "<code_block>",
#             "<next_unless>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<next_unless>": [
#         [
#             "<unless>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<instead>": [
#         [
#             TokenType.INSTEAD,
#             TokenType.COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<default>": [
#         [
#             TokenType.DEFAULT,
#             TokenType.COLON,
#             "<newline>",
#             "<code_block>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<event>": [
#         [
#             TokenType.EVENT,
#             "<event_value>",
#             TokenType.COLON,
#             "<newline>",
#             "<code_block>",
#             "<next_event>",
#         ],

#     ],
#     "<event_value>": [
#         [
#             TokenType.WORD_LITERAL,
#         ],
#         [
#             TokenType.NUM_LITERAL
#         ],
#         [
#             TokenType.DECI_LITERAL,
#         ],
#     ],
#     "<next_event>": [
#         [
#             "<event>",
#         ],
#         [
#             None,
#         ]
#     ],
#     "<iterable>": [
#         [
#             "<collection_value>",
#         ],
#         [
#             "<variable>",
#         ],
#         [
#             "<function_call>",
#         ],
#     ],
#     "<variable>": [
#         [
#             "<normal_variable>",
#         ],
#         [
#             "<object>",
#             "<next_variable>",
#         ],
#     ],
#     "<normal_variable>": [
#         [
#             TokenType.IDENTIFIER,
#             "<next_variable>",
#         ],
#     ],
#     "<next_variable>": [
#         [
#             TokenType.PERIOD,
#             "<normal_variable>",
#             "<next_variable>",
#         ],
#         [
#             None,
#         ]
#     ],
#     "<object>": [
#         [
#             TokenType.PARENT,
#         ],
#         [
#             TokenType.SELF,
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
#         [
#             TokenType.NEW,
#             TokenType.IDENTIFIER,
#             TokenType.OPAR,
#             "<argument>",
#             TokenType.CPAR,
#         ],
#     ],
#     "<collection_value>": [
#         [
#             TokenType.OBRACK,
#             "<opt_newline_tab>",
#             "<value>",
#             "<next_item>",
#             "<opt_newline_tab>",
#             TokenType.CBRACK,
#         ],
#     ],
#     "<next_item>": [
#         [
#             TokenType.COMMA,
#             "<opt_newline_tab>",
#             "<expression>",
#             "<next_item>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<wiki_value>": [
#         [
#             TokenType.OBRACE,
#             "<opt_newline_tab>",
#             "<key>",
#             TokenType.COLON,
#             "<value>",
#             "<next_pair>",
#             "<opt_newline_tab>",
#             TokenType.CBRACE,
#         ],
#     ],
#     "<key>": [
#         [
#             TokenType.WORD_LITERAL,
#         ],
#         [
#             "<variable>",
#         ],
#     ],
#     "<next_pair>": [
#         [
#             TokenType.COMMA,
#             "<opt_newline_tab>",
#             "<key>",
#             TokenType.COLON,
#             "<expression>",
#             "<next_pair>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<function_call>": [
#         [
#             TokenType.IDENTIFIER,
#             TokenType.OPAR,
#             "<argument>",
#             TokenType.CPAR,
#         ],
#         [
#             "<variable>",
#             TokenType.PERIOD,
#             "<function_call>",
#         ],
#         [
#             "<object>",
#             TokenType.PERIOD,
#             TokenType.INITIALIZE,
#             TokenType.OPAR,
#             "<argument>",
#             TokenType.CPAR,
#         ],
#         [
#             TokenType.RANGE,
#             TokenType.OPAR,
#             "<argument>",
#             TokenType.CPAR,
#         ],
#         [
#             TokenType.INP,
#             TokenType.OPAR,
#             "<argument>",
#             TokenType.CPAR,
#         ],
#         [
#             TokenType.OUT,
#             TokenType.OPAR,
#             "<argument>",
#             TokenType.CPAR,
#         ],
#         [
#             TokenType.WORD,
#             TokenType.OPAR,
#             "<argument>",
#             TokenType.CPAR,
#         ],
#         [
#             TokenType.NUM,
#             TokenType.OPAR,
#             "<argument>",
#             TokenType.CPAR,
#         ],
#         [
#             TokenType.DECI,
#             TokenType.OPAR,
#             "<argument>",
#             TokenType.CPAR,
#         ],
#     ],
#     "<argument>": [
#         [
#             "<expression>",
#             "<next_argument>",
#         ],
#         [
#             None,
#         ]
#     ],
#     "<next_argument>": [
#         [
#             TokenType.COMMA,
#             "<argument>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<newline>": [
#         [
#             TokenType.NEWLINE,
#             "<next_newline>",
#         ],
#         [
#             TokenType.EOF,
#         ],
#     ],
#     "<next_newline>": [
#         [
#             TokenType.NEWLINE,
#             "<next_newline>",
#         ],
#         [
#             None,
#         ],
#     ],
#     "<tab>": [
#         [
#             TokenType.TAB,
#             "<next_tab>",
#         ],
#     ],
#     "<next_tab>": [
#         [
#             "<tab>",
#         ],
#         [
#             None,
#         ]
#     ],
#     "<opt_newline_tab>": [
#         [
#             TokenType.NEWLINE,
#             "<tab>",
#         ],
#         [
#             None,
#         ],
#     ],
# }
