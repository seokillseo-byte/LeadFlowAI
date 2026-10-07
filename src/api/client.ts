import axios from "axios";

const baseURL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export const apiClient = axios.create({
  baseURL,
  headers: { "Content-Type": "application/json" },
  timeout: 15000,
});

export function getApiError(error: unknown, fallback = "Không thể hoàn tất yêu cầu.") {
  if (axios.isAxiosError(error)) {
    const detail = error.response?.data?.detail;
    if (typeof detail === "object" && detail !== null) {
      return {
        code: typeof detail.code === "string" ? detail.code : undefined,
        message: typeof detail.message === "string" ? detail.message : fallback,
        requestId: typeof error.response?.headers?.["x-request-id"] === "string"
          ? error.response.headers["x-request-id"]
          : undefined,
      };
    }
    if (typeof detail === "string") return { message: detail };
    if (error.message) return { message: error.message };
  }
  return { message: fallback };
}
