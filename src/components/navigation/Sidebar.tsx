import { Activity, BarChart3, Bot, FileText, FolderKanban, Inbox, LayoutDashboard, MessageSquare, Settings, Tags, UsersRound } from "lucide-react";
import type { AppRoute } from "../../layouts/AppLayout";

interface SidebarProps {
  route: AppRoute;
  onNavigate: (route: AppRoute) => void;
}

const items: Array<{ route: AppRoute; label: string; icon: typeof Inbox }> = [
  { route: "dashboard", label: "Tổng quan", icon: LayoutDashboard },
  { route: "campaigns", label: "Chiến dịch", icon: FolderKanban },
  { route: "keywords", label: "Từ khóa", icon: Tags },
  { route: "groups", label: "Nhóm & Fanpage", icon: UsersRound },
  { route: "inbox", label: "Lead Inbox", icon: Inbox },
  { route: "messages", label: "Tin nhắn & Comment", icon: MessageSquare },
  { route: "templates", label: "Mẫu phản hồi", icon: FileText },
  { route: "ai", label: "AI Assistant", icon: Bot },
  { route: "analytics", label: "Thống kê", icon: BarChart3 },
  { route: "activity", label: "Nhật ký hoạt động", icon: Activity },
  { route: "settings", label: "Cài đặt", icon: Settings },
];

export function Sidebar({ route, onNavigate }: SidebarProps) {
  return (
    <aside className="sidebar">
      <div className="brand"><div className="mark"><Bot size={18} /></div><div><b>LeadFlow</b> <span>AI</span></div></div>
      <nav>
        {items.map(({ route: itemRoute, label, icon: Icon }) => (
          <button key={itemRoute} className={route === itemRoute ? "nav active" : "nav"} onClick={() => onNavigate(itemRoute)}>
            <Icon size={17} /><span>{label}</span>
          </button>
        ))}
      </nav>
      <div className="approval-note"><span className="status-dot" /> Human approval enabled</div>
    </aside>
  );
}
