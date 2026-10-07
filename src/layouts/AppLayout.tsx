import type { ReactNode } from "react";
import { ShieldCheck } from "lucide-react";
import { Sidebar } from "../components/navigation/Sidebar";

export type AppRoute =
  | "dashboard" | "campaigns" | "keywords" | "groups" | "inbox"
  | "messages" | "templates" | "ai" | "analytics" | "activity" | "settings";

interface AppLayoutProps {
  route: AppRoute;
  onNavigate: (route: AppRoute) => void;
  children: ReactNode;
}

export function AppLayout({ route, onNavigate, children }: AppLayoutProps) {
  return (
    <div className="app">
      <Sidebar route={route} onNavigate={onNavigate} />
      <main className="main">
        <div className="desktop-status">
          <span><ShieldCheck size={14} /> Approval boundary active</span>
          <span className="system-ready"><i /> API boundary ready</span>
        </div>
        {children}
      </main>
    </div>
  );
}
