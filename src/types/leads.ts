export interface Lead {
  id: number;
  post_id: number;
  campaign_id: number;
  score: number | null;
  intent: string | null;
  fit: string | null;
  need: string | null;
  confidence: number | null;
  status: string | null;
}
export type LeadStatus = Lead["status"];
export interface ApiError {
  code?: string;
  message: string;
  requestId?: string;
}
