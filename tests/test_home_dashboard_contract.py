import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read_css() -> str:
    return (ROOT / "app" / "app.css").read_text(encoding="utf-8")


def _section_between(css: str, start_marker: str, end_marker: str) -> str:
    return css.split(start_marker, 1)[1].split(end_marker, 1)[0]


def _rule_body(css: str, selector: str) -> str:
    pattern = re.compile(re.escape(selector) + r"\s*\{([^}]*)\}", re.S)
    match = pattern.search(css)
    assert match, f"missing selector: {selector}"
    return match.group(1)


def test_home_dashboard_uses_a_two_by_two_desktop_grid():
    css = _read_css()
    section = _section_between(css, "/* 首页仪表盘卡片 */", "/* 侧边栏字体放大 */")

    grid_rule = _rule_body(section, ".markdown-section .dpr-home-dashboard-grid")
    assert "display: grid" in grid_rule
    assert "grid-template-columns: repeat(2, minmax(0, 1fr))" in grid_rule
    assert "grid-template-rows: repeat(2, minmax(0, 1fr))" in grid_rule
    assert "align-items: stretch" in grid_rule


def test_home_dashboard_cards_keep_a_quiet_equal_height_surface():
    css = _read_css()
    section = _section_between(css, "/* 首页仪表盘卡片 */", "/* 侧边栏字体放大 */")

    shared_selector = ".markdown-section .dpr-home-dashboard-card"
    shared_rule = _rule_body(section, shared_selector)
    assert "display: flex" in shared_rule
    assert "flex-direction: column" in shared_rule
    assert "height: 100%" in shared_rule
    assert "background: #ffffff" in shared_rule
    assert "border: 1px solid #d9dee3" in shared_rule
    assert "border-radius: 8px" in shared_rule
    assert "box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04)" in shared_rule
    assert "border-left" not in shared_rule
    assert "gradient" not in shared_rule.lower()


def test_home_dashboard_variants_only_use_semantic_accent_colors():
    css = _read_css()
    section = _section_between(css, "/* 首页仪表盘卡片 */", "/* 侧边栏字体放大 */")

    title_rule = _rule_body(section, ".markdown-section .dpr-home-dashboard-title")
    count_rule = _rule_body(section, ".markdown-section .dpr-home-dashboard-count")
    assert "color: var(--dpr-home-dashboard-accent)" in title_rule
    assert "color: var(--dpr-home-dashboard-accent)" in count_rule

    assert "--dpr-home-dashboard-accent: #2563eb" in _rule_body(
        section, ".markdown-section .dpr-home-report-card"
    )
    assert "--dpr-home-dashboard-accent: #17805c" in _rule_body(
        section, ".markdown-section .dpr-home-brief-card"
    )
    assert "--dpr-home-dashboard-accent: #c44f45" in _rule_body(
        section, ".markdown-section .dpr-home-deep-card"
    )
    assert "--dpr-home-dashboard-accent: #966b00" in _rule_body(
        section, ".markdown-section .dpr-home-skim-card"
    )
    shared_rule_start = section.index(".markdown-section .dpr-home-dashboard-card {")
    shared_rule_end = section.index("}", shared_rule_start)
    for selector in (
        ".markdown-section .dpr-home-report-card",
        ".markdown-section .dpr-home-brief-card",
        ".markdown-section .dpr-home-deep-card",
        ".markdown-section .dpr-home-skim-card",
    ):
        assert section.index(f"{selector} {{") > shared_rule_end


def test_home_dashboard_stats_are_not_nested_cards():
    css = _read_css()
    section = _section_between(css, "/* 首页仪表盘卡片 */", "/* 侧边栏字体放大 */")
    stat_rule = _rule_body(section, ".markdown-section .dpr-home-dashboard-stat")
    assert "background" not in stat_rule
    assert "border-radius" not in stat_rule
    assert "border: 1px" not in stat_rule
    assert "flex-direction: column" in stat_rule


def test_home_dashboard_layout_keeps_footer_links_and_wrapped_tags():
    css = _read_css()
    section = _section_between(css, "/* 首页仪表盘卡片 */", "/* 侧边栏字体放大 */")

    body_rule = _rule_body(section, ".markdown-section .dpr-home-dashboard-body")
    tags_rule = _rule_body(section, ".markdown-section .dpr-home-dashboard-tags")
    link_rule = _rule_body(section, ".markdown-section .dpr-home-dashboard-link")
    title_rule = _rule_body(section, ".markdown-section .dpr-home-dashboard-title")
    paper_link_rule = _rule_body(
        section, ".markdown-section .dpr-home-dashboard-paper-list a"
    )

    assert "flex: 1 1 auto" in body_rule
    assert "min-width: 0" in body_rule
    assert "display: flex" in tags_rule
    assert "flex-wrap: wrap" in tags_rule
    assert "margin-top: auto" in link_rule
    assert "overflow: hidden" in title_rule
    assert "text-overflow: ellipsis" in title_rule
    assert "white-space: nowrap" in title_rule
    assert "display: block" in paper_link_rule
    assert "min-width: 0" in paper_link_rule
    assert "overflow: hidden" in paper_link_rule
    assert "text-overflow: ellipsis" in paper_link_rule


def test_home_dashboard_hover_motion_stays_subtle_and_respects_reduced_motion():
    css = _read_css()
    section = _section_between(css, "/* 首页仪表盘卡片 */", "/* 侧边栏字体放大 */")

    hover_rule = _rule_body(
        section,
        ".markdown-section .dpr-home-dashboard-card:hover,\n"
        ".markdown-section .dpr-home-dashboard-card:focus-within",
    )
    assert "transform: translateY(-1px)" in hover_rule

    base_rule = _rule_body(section, ".markdown-section .dpr-home-dashboard-card")
    assert "transition: transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease" in base_rule

    reduced_motion = _section_between(
        section,
        "@media (prefers-reduced-motion: reduce)",
        "@media (max-width: 760px)",
    )
    reduced_rule = _rule_body(reduced_motion, ".markdown-section .dpr-home-dashboard-card")
    assert "transition: none" in reduced_rule
    hover_reduced_rule = _rule_body(
        reduced_motion,
        ".markdown-section .dpr-home-dashboard-card:hover,\n"
        "  .markdown-section .dpr-home-dashboard-card:focus-within",
    )
    assert "transform: none" in hover_reduced_rule


def test_home_dashboard_switches_to_single_column_on_small_screens():
    css = _read_css()
    section = _section_between(css, "/* 首页仪表盘卡片 */", "/* 侧边栏字体放大 */")

    mobile = section.split("@media (max-width: 760px)", 1)[1]
    grid_rule = _rule_body(mobile, ".markdown-section .dpr-home-dashboard-grid")
    assert "grid-template-columns: minmax(0, 1fr)" in grid_rule
    assert "grid-template-rows: none" in grid_rule


def test_current_and_init_homepages_render_exactly_four_dashboard_cards():
    for path in (ROOT / "docs" / "README.md", ROOT / "docs_init" / "README.md"):
        content = path.read_text(encoding="utf-8")
        assert content.count('class="dpr-home-dashboard-card ') == 4, path
        assert content.count('class="dpr-home-dashboard-grid"') == 1, path
