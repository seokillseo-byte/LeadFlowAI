from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app=FastAPI(title="LeadFlow AI API",version="0.1.0")
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173","http://127.0.0.1:5173"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
class Lead(BaseModel):
 id:int; source:str; author:str; content:str; score:int; status:str; suggested_reply:str|None=None
LEADS=[Lead(id=1,source="Facebook Group",author="Nguyễn Minh",content="Mình đang tìm đơn vị làm website bán hàng cho shop, cần tư vấn trong tuần này.",score=94,status="new",suggested_reply="Chào bạn Minh, bên mình có thể tư vấn nhanh nhu cầu website bán hàng. Nếu bạn muốn, mình gửi bạn vài phương án phù hợp để tham khảo nhé."),Lead(id=2,source="Facebook Group",author="Trần An",content="Có ai biết bên nào chạy quảng cáo Facebook hiệu quả cho spa không?",score=82,status="new",suggested_reply="Chào bạn, bên mình có hỗ trợ quảng cáo cho mô hình dịch vụ. Bạn có thể chia sẻ quy mô spa và khu vực hoạt động để mình tư vấn hướng phù hợp.")]
@app.get("/health")
def health(): return {"ok":True,"service":"leadflow-api"}
@app.get("/api/leads",response_model=list[Lead])
def list_leads(): return LEADS
@app.post("/api/leads/{lead_id}/approve")
def approve_lead(lead_id:int):
 for lead in LEADS:
  if lead.id==lead_id:
   lead.status="approved"; return {"ok":True,"lead_id":lead_id,"status":lead.status}
 return {"ok":False,"error":"lead_not_found"}
@app.post("/api/scan")
def scan(): return {"ok":True,"message":"Scan job queued"}