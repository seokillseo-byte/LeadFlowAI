import { CheckCircle2, Eye, LoaderCircle } from "lucide-react";
import type { Lead } from "../../types/leads";

interface LeadListProps {
  leads: Lead[];
  approvingId: number | null;
  onOpen: (lead: Lead) => void;
  onApprove: (lead: Lead) => void;
}

function statusLabel(status: string | null) {
  if (status === "approved") return "Approved";
  if (status === "new") return "Awaiting approval";
  return status || "Status unavailable";
}

export function LeadList({ leads, approvingId, onOpen, onApprove }: LeadListProps) {
  return (
    <div className="lead-list">
      {leads.map((lead) => {
        const approved = lead.status === "approved";
        return (
          <article className="lead-row" key={lead.id}>
            <div className="score">{lead.score ?? "—"}<small>{lead.score === null ? "" : "/100"}</small></div>
            <div className="lead-content">
              <div className="lead-meta">Lead #{lead.id} · Post #{lead.post_id} · Campaign #{lead.campaign_id}</div>
              <div className="lead-facts">
                <span><b>Intent</b> {lead.intent || "Unavailable"}</span>
                <span><b>Fit</b> {lead.fit || "Unavailable"}</span>
                <span><b>Need</b> {lead.need || "Unavailable"}</span>
                <span><b>Confidence</b> {lead.confidence === null ? "Unavailable" : `${Math.round(lead.confidence * 100)}%`}</span>
              </div>
            </div>
            <div className="lead-actions">
              <span className={approved ? "badge approved" : "badge"}>{statusLabel(lead.status)}</span>
              <button className="secondary small" onClick={() => onOpen(lead)} disabled={approvingId === lead.id}><Eye size={14} /> Open</button>
              {!approved && (
                <button className="primary small" onClick={() => onApprove(lead)} disabled={approvingId === lead.id}>
                  {approvingId === lead.id ? <LoaderCircle className="spin" size={14} /> : <CheckCircle2 size={14} />}
                  {approvingId === lead.id ? "Đang duyệt…" : "Duyệt"}
                </button>
              )}
            </div>
          </article>
        );
      })}
    </div>
  );
}
