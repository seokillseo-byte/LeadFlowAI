import { apiClient } from "./client";
import type { Lead } from "../types/leads";

export async function listLeads(): Promise<Lead[]> {
  const response = await apiClient.get<Lead[]>("/api/leads");
  return response.data;
}

export async function getLead(leadId: number): Promise<Lead> {
  const response = await apiClient.get<Lead>(`/api/leads/${leadId}`);
  return response.data;
}

export async function approveLead(leadId: number): Promise<Lead> {
  const response = await apiClient.post<Lead>(`/api/leads/${leadId}/approve`);
  return response.data;
}
