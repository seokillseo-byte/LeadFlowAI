# LeadFlow AI UI Blueprint & Design System

## Master visual reference

- docs/blueprints/leadflow-ai-dashboard.svg

The master SVG is a detailed product mockup and visual contract for the desktop shell. It should be treated as the visual reference for spacing, information hierarchy, navigation, cards, tables, statuses and action placement.

## Product direction
Modern desktop SaaS, professional, clean, high information density, optimized for Windows desktop workflows.

## Layout
- Dark navy left navigation
- Bright content canvas
- Header/system-status strip
- KPI cards
- Main analytics area
- Lead Inbox table
- Right-side activity/AI/campaign rail
- Bottom connection and safety status bar
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
- Facebook/provider status
- API/database status
- Global pause
- Campaign management

## Interaction principles
- Human approval is visible and easy to understand.
- High-risk/outbound actions require explicit confirmation.
- Scores are supportive signals, not automatic truth.
- Empty, loading, error, permission and paused states must be designed.
- The interface must remain usable without AI suggestions.
- Status colors and labels must be consistent across screens.

## Screen contracts

Before implementing a screen, read its specification under docs/ui/. At minimum:
- dashboard.md
- campaigns.md
- keywords.md
- groups-pages.md
- lead-inbox.md
- messages-comments.md
- templates.md
- ai-assistant.md
- analytics.md
- activity-log.md
- settings.md
- states-and-interactions.md

## UI implementation rule

When implementing a screen, use the blueprint as the visual contract. If the product needs a meaningful deviation, update this document, the relevant screen spec and the blueprint before merging.
