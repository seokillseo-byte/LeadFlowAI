from dataclasses import dataclass
@dataclass
class ScoreResult: score:int; label:str; reasons:list[str]
def score_post(content:str,include_keywords:list[str],exclude_keywords:list[str])->ScoreResult:
 text=content.lower()
 if any(k.lower() in text for k in exclude_keywords): return ScoreResult(0,"not_fit",["Matched an excluded keyword"])
 hits=[k for k in include_keywords if k.lower() in text]
 if not hits:return ScoreResult(10,"low",["No target keyword matched"])
 score=min(60+len(hits)*10,95); return ScoreResult(score,"high" if score>=80 else "medium",[f"Matched: {', '.join(hits)}"])