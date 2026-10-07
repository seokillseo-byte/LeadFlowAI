import type { ReactNode } from "react";

interface StatePanelProps {
  title: string;
  message: string;
  action?: ReactNode;
  tone?: "neutral" | "error";
}

export function StatePanel({ title, message, action, tone = "neutral" }: StatePanelProps) {
  return (
    <div className={`state-panel ${tone === "error" ? "state-error" : ""}`}>
      <strong>{title}</strong>
      <p>{message}</p>
      {action}
    </div>
  );
}
