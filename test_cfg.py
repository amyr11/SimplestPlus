from src.grammar_helper import GrammarHelper

grammar_helper = GrammarHelper()
grammar_helper.display_cfg()
grammar_helper.display_first_set()
grammar_helper.display_follow_set()
grammar_helper.export_cfg_first_follow("./dump/cfg_first_follow.txt")