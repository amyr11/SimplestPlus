from src.grammar_helper import GrammarHelper

grammar_helper = GrammarHelper()
# grammar_helper.display_cfg()
# grammar_helper.display_first_set()
# grammar_helper.display_follow_set()
grammar_helper.export_cfg_first_follow_predict("./dump/cfg_first_follow.txt")
grammar_helper.export_all_md("./dump/cfg_first_follow.md")
