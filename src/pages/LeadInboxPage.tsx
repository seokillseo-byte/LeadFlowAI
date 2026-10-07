import { RefreshCw, Search } from "lucide-react";
import { LeadDetail } from "../components/leads/LeadDetail";
import { LeadList } from "../components/leads/LeadList";
import { StatePanel } from "../components/common/StatePanel";
import { useLeads } from "../features/leads/useLeads";

export function LeadInboxPage() {
  const leads = useLeads();

  return (
    <section>
      <header className="page-header">
        <div><h1>Lead Inbox</h1><p>Dữ liệu Lead từ API thật. Không dùng fixture trong production UI.</p></div>
        <button className="secondary" onClick={() => void leads.load()} disabled={leads.loading}><RefreshCw size={15} className={leads.loading ? "spin" : ""} /> Làm mới</button>
      </header>
      <div className="inbox-toolbar">
        <div className="search-box"><Search size={16} /><span>Search hiện được giữ ở trạng thái foundation</span></div>
        <span className="toolbar-note">Endpoint hiện hỗ trợ: list · view · approve</span>
      </div>
      {leads.error ? (
        <StatePanel tone="error" title="Không thể tải Lead Inbox" message={leads.error.message} action={<button className="primary" onClick={() => void leads.load()}>Thử lại</button>} />
      ) : leads.loading ? (
        <StatePanel title="Đang tải Lead Inbox" message="Đang lấy dữ liệu từ backend…" />
      ) : leads.items.length === 0 ? (
        <StatePanel title="Chưa có Lead" message="Backend trả về danh sách rỗng. Không có dữ liệu demo được chèn vào." />
      ) : (
        <div className="inbox-grid">
          <div className="panel">
            <div className="panel-head"><div><h2>Review queue</h2><small>Approval phải được backend xác nhận thành công.</small></div></div>
            <LeadList leads={leads.items} approvingId={leads.approvingId} onOpen={(lead) => void leads.openLead(lead)} onApprove={(lead) => void leads.approve(lead)} />
          </div>
          {leads.selected && <LeadDetail lead={leads.selected} loading={leads.detailLoading} onClose={leads.closeDetail} />}
        </div>
      )}
      {leads.approvalError && <div className="inline-error" role="alert">{leads.approvalError.message}<button onClick={leads.clearApprovalError}>Đóng</button></div>}
    </section>
  );
}
