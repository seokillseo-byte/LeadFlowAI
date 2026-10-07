import { useState } from "react";
import { AppLayout, type AppRoute } from "./layouts/AppLayout";
import { DashboardPage } from "./pages/DashboardPage";
import { LeadInboxPage } from "./pages/LeadInboxPage";
import { SettingsPage } from "./pages/SettingsPage";
import { UnavailablePage } from "./pages/UnavailablePage";

export default function App() {
  const [route, setRoute] = useState<AppRoute>("dashboard");

  const page = route === "dashboard"
    ? <DashboardPage />
    : route === "inbox"
      ? <LeadInboxPage />
      : route === "settings"
        ? <SettingsPage />
        : <UnavailablePage route={route} />;

  return <AppLayout route={route} onNavigate={setRoute}>{page}</AppLayout>;
}
