from dataclasses import dataclass
@dataclass
class SocialPost:
    external_id:str
    source:str
    author:str
    content:str
    url:str|None=None
class MetaProvider:
    """Official Meta integration boundary. No cookie scraping, CAPTCHA bypass, stealth automation or bulk unsolicited outreach."""
    def discover_posts(self,keywords:list[str])->list[SocialPost]: raise NotImplementedError("Connect an approved Meta API flow.")
    def publish_comment(self,post_id:str,text:str)->str: raise NotImplementedError("Connect an approved Meta API flow.")
    def send_message(self,recipient_id:str,text:str)->str: raise NotImplementedError("Connect an approved Meta API flow.")