from llm.llm_interface import LLMInterface

def expand(keyword: str) -> list:
    llm = LLMInterface()
    return llm.expand_keywords(keyword)
