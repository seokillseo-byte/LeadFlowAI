import { Activity, BarChart3, Database, ShieldCheck } from "lucide-react";
import { StatePanel } from "../components/common/StatePanel";

const metrics = [
  ["Bài viết đã quét", "Unavailable", "Chưa có endpoint dashboard."],
  ["Lead tiềm năng", "Unavailable", "Chưa có endpoint dashboard."],
  ["Đã gửi comment", "Unavailable", "Chưa có endpoint action metrics."],
  ["Đã gửi tin nhắn", "Unavailable", "Chưa có endpoint action metrics."],
];

export function DashboardPage() {
  return (
    <section>
      <header className="page-header"><div><h1>Tổng quan</h1><p>Command center foundation theo canonical dashboard spec.</p></div><span className="system-pill"><i /> Backend metrics unavailable</span></header>
      <div className="metrics">{metrics.map(([title, value, note]) => <div className="metric" key={title}><div className="metric-icon"><Activity size={18} /></div><div><small>{title}</small><strong>{value}</strong><em>{note}</em></div></div>)}</div>
      <div className="dashboard-grid">
        <StatePanel title="Hiệu suất 7 ngày" message="Chưa có endpoint performance nên không hiển thị số liệu giả." />
        <StatePanel title="Conversion overview" message="Chưa có endpoint conversion nên không hiển thị số liệu giả." />
        <StatePanel title="Lead Inbox preview" message="Dùng Lead Inbox để xem dữ liệu Lead thực tế và approval boundary." action={<BarChart3 size={18} />} />
        <StatePanel title="Hệ thống & an toàn" message="Renderer không giữ secrets. Approval boundary vẫn do backend authoritative." action={<ShieldCheck size={18} />} />
        <StatePanel title="Database status" message="Không có endpoint status trong Sprint 0." action={<Database size={18} />} />
      </div>
    </section>
  );
}
