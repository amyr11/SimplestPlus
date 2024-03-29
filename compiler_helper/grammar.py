import pysimplestplus.compiler as sp

CFG = {
    "<program>": [
        [
            "<extras>",
            "<global>",
            sp.TT_HOME,
            sp.TT_OPAR,
            sp.TT_CPAR,
            sp.TT_COLON,
            "<newline>",
            "<statements>",
            "<global>",
            "<extras>",
        ],
    ],
    "<extras>": [
        [
            sp.TT_NEWLINE,
            "<extras>",
        ],
        [
            sp.TT_TAB,
            sp.TT_NEWLINE,
            "<extras>",
        ],
        [
            None,
        ],
    ],
    "<global>": [
        [
            "<dec-stmt>",
            "<global>",
        ],
        [
            "<func-def>",
            "<global>",
        ],
        [
            "<group-def>",
            "<global>",
        ],
        [
            None,
        ],
    ],
    "<group-def>": [
        [
            sp.TT_GROUP,
            sp.TT_IDENTIFIER,
            "<inherits>",
            sp.TT_COLON,
            "<newline>",
            "<group-body>",
        ],
    ],
    "<inherits>": [
        [
            sp.TT_INHERITS,
            sp.TT_IDENTIFIER,
        ],
        [
            None,
        ],
    ],
    "<group-body>": [
        [
            "<group-constr>",
            "<group-global-opt>",
        ],
        [
            "<group-global-req>",
            "<group-constr-global-opt>",
        ],
    ],
    "<group-global-opt>": [
        [
            "<group-global>",
            "<group-global-opt>",
        ],
        [
            None,
        ],
    ],
    "<group-global-req>": [
        [
            "<group-global>",
            "<group-global-opt>",
        ],
    ],
    "<group-constr-global-opt>": [
        [
            "<group-constr>",
            "<group-global-opt>",
        ],
        [
            None,
        ],
    ],
    "<group-global>": [
        [
            sp.TT_TAB,
            "<access-spec>",
            "<dec-func-def>",
        ]
    ],
    "<dec-func-def>": [
        [
            "<dec-stmt>",
        ],
        [
            "<func-def>",
        ],
    ],
    "<access-spec>": [
        [
            sp.TT_VISIBLE,
        ],
        [
            sp.TT_HIDDEN,
        ],
        [
            sp.TT_RESTRICTED,
        ],
    ],
    "<group-constr>": [
        [
            sp.TT_TAB,
            sp.TT_IDENTIFIER,
            "<params>",
            sp.TT_COLON,
            "<newline>",
            "<statements>",
        ],
    ],
    "<func-def>": [
        [
            "<ret-type>",
            sp.TT_IDENTIFIER,
            "<params>",
            sp.TT_COLON,
            "<newline>",
            "<statements>",
        ],
    ],
    "<ret-type>": [
        [
            sp.TT_EMPTY,
        ],
        [
            "<type>",
        ],
    ],
    "<type>": [
        [
            "<data-struct>",
        ],
        [
            "<data-type>",
        ],
    ],
    "<data-struct>": [
        [
            sp.TT_COLLECTION,
            sp.TT_OBRACK,
            "<type>",
            sp.TT_CBRACK,
        ],
        [
            sp.TT_WIKI,
            sp.TT_OBRACK,
            "<data-type>",
            sp.TT_COMMA,
            "<type>",
            sp.TT_CBRACK,
        ],
    ],
    "<data-type>": [
        [
            sp.TT_NUM,
        ],
        [
            sp.TT_DECI,
        ],
        [
            sp.TT_WORD,
        ],
        [
            sp.TT_LETTER,
        ],
        [
            sp.TT_CHOICE,
        ],
        [
            sp.TT_IDENTIFIER,
        ],
    ],
    "<params>": [
        [
            sp.TT_OPAR,
            "<param-opt>",
            sp.TT_CPAR,
        ],
    ],
    "<param-opt>": [
        [
            "<type>",
            sp.TT_IDENTIFIER,
            "<param-tail>",
        ],
        [
            None,
        ],
    ],
    "<param-tail>": [
        [
            sp.TT_COMMA,
            "<param-opt>",
        ],
        [
            None,
        ],
    ],
    "<statements>": [
        [
            "<tab>",
            "<statement>",
            "<statement-opt>",
        ],
    ],
    "<statement-opt>": [
        [
            "<statements>",
        ],
        [
            None,
        ],
    ],
    "<statement>": [
        [
            sp.TT_BACK,
            "<expr>",
            "<newline>",
        ],
        [
            sp.TT_SKIP,
            "<newline>",
        ],
        [
            sp.TT_STOP,
            "<newline>",
        ],
        [
            sp.TT_GLOBAL,
            sp.TT_IDENTIFIER,
            "<newline>",
        ],
        [
            sp.TT_DEL,
            sp.TT_IDENTIFIER,
            "<newline>",
        ],
        [
            "<dec-stmt>",
        ],
        [
            "<assign-stmt>",
        ],
        [
            "<incase-stmt>",
        ],
        [
            "<given-stmt>",
        ],
        [
            "<every-stmt>",
        ],
        [
            "<during-stmt>",
        ],
        [
            "<go-during-stmt>",
        ],
        [
            "<expr>",
            "<newline>",
        ],
    ],
    "<dec-stmt>": [
        [
            "<type>",
            sp.TT_IDENTIFIER,
            "<assign-expr-opt>",
            "<dec-stmt-tail-1>",
            "<newline>",
        ],
        [
            sp.TT_FROZEN,
            "<type>",
            sp.TT_IDENTIFIER,
            sp.TT_ASSIGN,
            "<expr>",
            "<dec-stmt-tail-2>",
            "<newline>",
        ],
    ],
    "<assign-expr-opt>": [
        [
            sp.TT_ASSIGN,
            "<expr>",
        ],
        [
            None,
        ],
    ],
    "<dec-stmt-tail-1>": [
        [
            sp.TT_COMMA,
            sp.TT_IDENTIFIER,
            "<assign-expr-opt>",
            "<dec-stmt-tail-1>",
        ],
        [
            None,
        ],
    ],
    "<dec-stmt-tail-2>": [
        [
            sp.TT_COMMA,
            sp.TT_IDENTIFIER,
            sp.TT_ASSIGN,
            "<expr>" "<dec-stmt-tail-2>",
        ],
        [
            None,
        ],
    ],
    "<assign-stmt>": [
        [
            sp.TT_IDENTIFIER,
            "<dot_slice_tail>",
            "<assign-optr>",
            "<expr>",
            "<newline>",
        ],
    ],
    "<dot_slice_tail>": [
        [
            "<dot_slice>",
            "<dot_slice_tail>",
        ],
        [
            None,
        ],
    ],
    "<assign-optr>": [
        [
            sp.TT_ASSIGN,
        ],
        [
            sp.TT_PLUS_ASSIGN,
        ],
        [
            sp.TT_MINUS_ASSIGN,
        ],
        [
            sp.TT_MULTIPLY_ASSIGN,
        ],
        [
            sp.TT_DIVIDE_ASSIGN,
        ],
        [
            sp.TT_FLOOR_ASSIGN,
        ],
        [
            sp.TT_MODULO_ASSIGN,
        ],
        [
            sp.TT_POWER_ASSIGN,
        ],
    ],
    "<incase-stmt>": [
        [
            sp.TT_INCASE,
            "<expr>",
            sp.TT_COLON,
            "<newline>",
            "<statements>",
            "<unless-opt>",
            "<instead>",
        ],
    ],
    "<unless-opt>": [
        [
            "<unless>",
            "<unless-opt>",
        ],
        [
            None,
        ],
    ],
    "<unless>": [
        [
            "<tab>",
            sp.TT_UNLESS,
            "<expr>",
            sp.TT_COLON,
            "<newline>",
            "<statements>",
        ],
    ],
    "<instead>": [
        [
            "<tab>",
            sp.TT_INSTEAD,
            sp.TT_COLON,
            "<newline>",
            "<statements>",
        ],
        [
            None,
        ],
    ],
    "<given-stmt>": [
        [
            sp.TT_GIVEN,
            "<expr>",
            sp.TT_COLON,
            "<newline>",
            "<event-default>",
        ],
    ],
    "<event-default>": [
        [
            "<event-req>",
            "<default-event-opt>",
        ],
        [
            "<default>",
            "<event-opt>",
        ],
    ],
    "<event-req>": [
        [
            "<event>",
            "<event-opt>",
        ],
    ],
    "<event-opt>": [
        ["<event>", "<event-opt>"],
        [
            None,
        ],
    ],
    "<default-event-opt>": [
        [
            "<default>",
            "<event-opt>",
        ],
        [
            None,
        ],
    ],
    "<default>": [
        [
            "<tab>",
            sp.TT_DEFAULT,
            sp.TT_COLON,
            "<newline>",
            "<statements>",
        ],
    ],
    "<event>": [
        [
            "<tab>",
            sp.TT_EVENT,
            "<literals>",
            sp.TT_COLON,
            "<newline>",
            "<statements>",
        ],
    ],
    "<literals>": [
        [
            sp.TT_NUM_LITERAL,
        ],
        [
            sp.TT_DECI_LITERAL,
        ],
        [
            sp.TT_WORD_LITERAL,
        ],
        [
            sp.TT_LETTER_LITERAL,
        ],
        [
            sp.TT_YES,
        ],
        [
            sp.TT_NO,
        ],
        [
            sp.TT_BLANK,
        ],
    ],
    "<every-stmt>": [
        [
            sp.TT_EVERY,
            "<type>",
            sp.TT_IDENTIFIER,
            "<type-id-opt>",
            sp.TT_IN,
            "<expr>",
            sp.TT_COLON,
            "<newline>",
            "<statements>",
        ],
    ],
    "<type-id-opt>": [
        [
            sp.TT_COMMA,
            "<type>",
            sp.TT_IDENTIFIER,
        ],
        [
            None,
        ],
    ],
    "<during-stmt>": [
        [
            sp.TT_DURING,
            "<expr>",
            sp.TT_COLON,
            "<newline>",
            "<statements>",
        ],
    ],
    "<go-during-stmt>": [
        [
            sp.TT_GO,
            sp.TT_COLON,
            "<newline>",
            "<statements>",
            "<tab>",
            sp.TT_DURING,
            "<expr>",
            "<newline>",
        ],
    ],
    "<expr>": [
        [
            "<and-expr>",
            "<or-and-expr-tail>",
        ],
        [
            sp.TT_NEW,
            sp.TT_IDENTIFIER,
            "<args>",
        ],
    ],
    "<or-and-expr-tail>": [
        [
            sp.TT_OR,
            "<and-expr>",
            "<or-and-expr-tail>",
        ],
        [
            None,
        ],
    ],
    "<and-expr>": [
        [
            "<comp-expr>",
            "<and-comp-expr-tail>",
        ],
    ],
    "<and-comp-expr-tail>": [
        [
            sp.TT_AND,
            "<comp-expr>",
            "<and-comp-expr-tail>",
        ],
        [
            None,
        ],
    ],
    "<comp-expr>": [
        [
            sp.TT_NOT,
            "<comp-expr>",
        ],
        [
            "<arith-expr>",
            "<rel-tail>",
        ],
        [
            sp.TT_BLANK,
        ],
    ],
    "<rel-tail>": [
        [
            "<rel-optr>",
            "<arith-expr>",
            "<rel-tail>",
        ],
        [
            None,
        ],
    ],
    "<rel-optr>": [
        [
            sp.TT_EQUAL_TO,
        ],
        [
            sp.TT_NOT_EQUAL,
        ],
        [
            sp.TT_NOT_EQUAL,
        ],
        [
            sp.TT_LESS_THAN,
        ],
        [
            sp.TT_GREATER_THAN,
        ],
        [
            sp.TT_LESS_THAN_EQUAL,
        ],
        [
            sp.TT_GREATER_THAN_EQUAL,
        ],
    ],
    "<arith-expr>": [
        [
            "<term>",
            "<term-tail>",
        ]
    ],
    "<term-tail>": [
        [
            "<term-optr>",
            "<term>",
            "<term-tail>",
        ],
        [
            None,
        ],
    ],
    "<term-optr>": [
        [
            sp.TT_PLUS,
        ],
        [
            sp.TT_MINUS,
        ],
    ],
    "<term>": [
        [
            "<factor>",
            "<factor-tail>",
        ],
    ],
    "<factor-tail>": [
        [
            "<factor-optr>",
            "<factor>",
            "<factor-tail>",
        ],
        [
            None,
        ],
    ],
    "<factor-optr>": [
        [
            sp.TT_MULTIPLY,
        ],
        [
            sp.TT_DIVIDE,
        ],
        [
            sp.TT_FLOOR,
        ],
        [
            sp.TT_MODULO,
        ],
    ],
    "<factor>": [
        [
            sp.TT_MINUS,
            "<factor>",
        ],
        [
            "<power>",
        ],
    ],
    "<power>": [
        [
            "<atom>",
            "<power-tail>",
        ],
    ],
    "<power-tail>": [
        [
            sp.TT_POWER,
            "<factor>",
            "<power-tail>",
        ],
        [
            None,
        ],
    ],
    "<atom>": [
        [
            sp.TT_IDENTIFIER,
            "<dot_slice_arg_tail>",
        ],
        [
            sp.TT_WORD_LITERAL,
            "<args_opt>",
        ],
        [
            "<collection-expr>",
            "<args_opt>",
        ],
        [
            "<wiki-expr>",
            "<args_opt>",
        ],
        [
            sp.TT_OPAR,
            "<expr>",
            sp.TT_CPAR,
            "<args_opt>",
        ],
        [
            sp.TT_YES,
            "<slice_arg_opt>",
        ],
        [
            sp.TT_NO,
            "<slice_arg_opt>",
        ],
        [
            sp.TT_LETTER_LITERAL,
            "<slice_arg_opt>",
        ],
        [
            sp.TT_NUM_LITERAL,
        ],
        [
            sp.TT_DECI_LITERAL,
        ],
    ],
    "<dot_slice_arg>": [
        [
            "<dot_slice>",
        ],
        [
            "<args>",
        ],
    ],
    "<dot_slice_arg_tail>": [
        [
            "<dot_slice_arg>",
            "<dot_slice_arg_tail>",
        ],
        [
            None,
        ],
    ],
    "<args_opt>": [
        [
            "<dot_slice>",
            "<args_tail>",
            "<args_opt>",
        ],
        [
            None,
        ],
    ],
    "<args_tail>": [
        [
            "<args>",
            "<args_tail>",
        ],
        [
            None,
        ],
    ],
    "<slice_arg_opt>": [
        [
            "<dot>",
            "<slice_arg_tail>",
            "<slice_arg_opt>",
        ],
        [
            None,
        ],
    ],
    "<slice_arg_tail>": [
        [
            "<slice_arg>",
            "<slice_arg_tail>",
        ],
        [
            None,
        ],
    ],
    "<dot_slice>": [
        [
            "<dot>",
        ],
        [
            "<slice>",
        ],
    ],
    "<slice_arg>": [
        [
            "<slice>",
        ],
        [
            "<args>",
        ],
    ],
    "<dot>": [
        [
            sp.TT_PERIOD,
            sp.TT_IDENTIFIER,
        ],
    ],
    "<slice>": [
        [
            sp.TT_OBRACK,
            "<expr>",
            "<colon-expr-opt>",
            sp.TT_CBRACK,
        ],
    ],
    "<colon-expr-opt>": [
        [
            sp.TT_COLON,
            "<expr>",
        ],
        [
            None,
        ],
    ],
    "<args>": [
        [
            sp.TT_OPAR,
            "<expr-opt>",
            sp.TT_CPAR,
        ],
    ],
    "<expr-opt>": [
        [
            "<expr>",
            "<comma-expr-tail>",
        ],
        [
            None,
        ],
    ],
    "<comma-expr-tail>": [
        [
            sp.TT_COMMA,
            "<expr>",
            "<comma-expr-tail>",
        ],
        [
            None,
        ],
    ],
    "<collection-expr>": [
        [
            sp.TT_OBRACK,
            "<expr-opt>",
            sp.TT_CBRACK,
        ],
    ],
    "<wiki-expr>": [
        [
            sp.TT_OBRACE,
            "<key-value-opt>",
            sp.TT_CBRACE,
        ],
    ],
    "<key-value-opt>": [
        [
            "<keys>",
            sp.TT_COLON,
            "<expr>",
            "<key-value-tail>",
        ],
        [
            None,
        ],
    ],
    "<key-value-tail>": [
        [
            sp.TT_COMMA,
            "<keys>",
            sp.TT_COLON,
            "<expr>",
            "<key-value-tail>",
        ],
        [
            None,
        ],
    ],
    "<keys>": [
        [
            sp.TT_NUM_LITERAL,
        ],
        [
            sp.TT_DECI_LITERAL,
        ],
        [
            sp.TT_WORD_LITERAL,
        ],
        [
            sp.TT_LETTER_LITERAL,
        ],
        [
            sp.TT_YES,
        ],
        [
            sp.TT_NO,
        ],
    ],
    "<tab>": [
        [
            sp.TT_NEWLINE,
            "<tab-tail>",
        ]
    ],
    "<tab-tail>": [
        [
            "<tab>",
        ],
        [
            None,
        ],
    ],
    "<newline>": [
        [
            sp.TT_NEWLINE,
            "<newline-tail>",
        ]
    ],
    "<newline-tail>": [
        [
            "<newline>",
        ],
        [
            None,
        ],
    ],
}
