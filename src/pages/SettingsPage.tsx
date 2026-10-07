import { StatePanel } from "../components/common/StatePanel";

export function SettingsPage() {
  return (
    <section>
      <header className="page-header"><div><h1>Cài đặt</h1><p>Foundation only — không lưu cấu hình giả.</p></div></header>
      <StatePanel title="Cấu hình chưa khả dụng" message="Sprint 0 chưa có backend contract cho settings persistence. Không có nút Save giả và không ghi dữ liệu cục bộ." />
    </section>
  );
}
