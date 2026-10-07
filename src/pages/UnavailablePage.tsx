import type { AppRoute } from "../layouts/AppLayout";
import { StatePanel } from "../components/common/StatePanel";

const labels: Record<Exclude<AppRoute, "dashboard" | "inbox" | "settings">, string> = {
  campaigns: "Chiến dịch", keywords: "Từ khóa", groups: "Nhóm & Fanpage", messages: "Tin nhắn & Comment",
  templates: "Mẫu phản hồi", ai: "AI Assistant", analytics: "Thống kê", activity: "Nhật ký hoạt động",
};

export function UnavailablePage({ route }: { route: Exclude<AppRoute, "dashboard" | "inbox" | "settings"> }) {
  return (
    <section>
      <header className="page-header"><div><h1>{labels[route]}</h1><p>Workspace foundation</p></div></header>
      <StatePanel title="Not available yet" message="This workspace will become available when its backend contract is implemented." />
    </section>
  );
}
