import { X } from "lucide-react";
import type { Lead } from "../../types/leads";

export function LeadDetail({ lead, loading, onClose }: { lead: Lead; loading: boolean; onClose: () => void }) {
  return (
    <aside className="detail-panel">
      <div className="detail-head">
        <div><small>Lead detail</small><h2>Lead #{lead.id}</h2></div>
        <button className="icon-button" onClick={onClose} aria-label="Đóng"><X size={18} /></button>
      </div>
      {loading && <div className="detail-loading">Đang tải dữ liệu…</div>}
      <dl>
        <dt>Post ID</dt><dd>{lead.post_id}</dd>
        <dt>Campaign ID</dt><dd>{lead.campaign_id}</dd>
        <dt>Score</dt><dd>{lead.score ?? "Unavailable"}</dd>
        <dt>Intent</dt><dd>{lead.intent || "Unavailable"}</dd>
        <dt>Fit</dt><dd>{lead.fit || "Unavailable"}</dd>
        <dt>Need</dt><dd>{lead.need || "Unavailable"}</dd>
        <dt>Confidence</dt><dd>{lead.confidence === null ? "Unavailable" : `${Math.round(lead.confidence * 100)}%`}</dd>
        <dt>Status</dt><dd>{lead.status || "Unavailable"}</dd>
      </dl>
      <div className="detail-note">Post content, author, source and suggested reply are not present in the Sprint 0 Lead API response, so the UI does not fabricate them.</div>
    </aside>
  );
}
