import { useCallback, useEffect, useState } from "react";
import { getApiError } from "../../api/client";
import { approveLead, getLead, listLeads } from "../../api/leads";
import type { ApiError, Lead } from "../../types/leads";

export function useLeads() {
  const [items, setItems] = useState<Lead[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<ApiError | null>(null);
  const [approvalError, setApprovalError] = useState<ApiError | null>(null);
  const [approvingId, setApprovingId] = useState<number | null>(null);
  const [selected, setSelected] = useState<Lead | null>(null);
  const [detailLoading, setDetailLoading] = useState(false);

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      setItems(await listLeads());
    } catch (err) {
      setError(getApiError(err, "Không thể tải Lead Inbox."));
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { void load(); }, [load]);

  const openLead = useCallback(async (lead: Lead) => {
    setDetailLoading(true);
    try {
      setSelected(await getLead(lead.id));
    } catch {
      setSelected(lead);
    } finally {
      setDetailLoading(false);
    }
  }, []);

  const approve = useCallback(async (lead: Lead) => {
    setApprovalError(null);
    setApprovingId(lead.id);
    try {
      const approved = await approveLead(lead.id);
      setItems((current) => current.map((item) => item.id === approved.id ? approved : item));
      setSelected((current) => current?.id === approved.id ? approved : current);
      return true;
    } catch (err) {
      setApprovalError(getApiError(err, "Duyệt Lead thất bại. Trạng thái chưa được thay đổi."));
      return false;
    } finally {
      setApprovingId(null);
    }
  }, []);

  return {
    items, loading, error, approvalError, approvingId, selected, detailLoading,
    load, openLead, approve,
    clearApprovalError: () => setApprovalError(null),
    closeDetail: () => setSelected(null),
  };
}
