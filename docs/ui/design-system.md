# LeadFlow AI UI Blueprint & Design System

The canonical visual reference is:
- docs/blueprints/leadflow-ai-dashboard.svg

## Product direction
Modern desktop SaaS, professional, clean, high information density, optimized for Windows desktop workflows.

## Layout
- Dark navy left navigation
- Bright content canvas
- Three-column dashboard composition where useful
- Rounded cards
- Subtle borders and shadows
- Compact tables for lead operations
- Clear status chips and score badges

## Primary navigation
- Tổng quan
- Chiến dịch
- Từ khóa
- Nhóm & Fanpage
- Lead Inbox
- Tin nhắn & Comment
- Mẫu phản hồi
- AI Assistant
- Thống kê
- Nhật ký hoạt động
- Cài đặt

## Dashboard
The dashboard should make these states visible immediately:
- Bài viết đã quét
- Lead tiềm năng
- Đã gửi comment
- Đã gửi tin nhắn
- Hiệu suất 7 ngày
- Tỷ lệ chuyển đổi
- Hoạt động gần đây
- AI Assistant
- Chiến dịch đang chạy
- Lead Inbox

## Interaction principles
- Human approval is visible and easy to understand.
- High-risk/outbound actions require an explicit confirmation state.
- Scores are supportive signals, not automatic truth.
- Empty, loading, error and permission states must be designed.
- The interface must remain usable without AI suggestions.

## UI implementation rule

When implementing a screen, use the blueprint as the visual contract. If the product needs a meaningful deviation, update this document and the blueprint before merging.
