"""Streamlit app: embeds the Architechs FTC site (HTML + CSS + JS) for Streamlit Cloud."""

from pathlib import Path

import streamlit as st


def _bundle_html() -> str:
    root = Path(__file__).resolve().parent
    html = (root / "index.html").read_text(encoding="utf-8")
    css = (root / "styles.css").read_text(encoding="utf-8")
    js = (root / "main.js").read_text(encoding="utf-8")
    html = html.replace(
        '<link rel="stylesheet" href="styles.css" />',
        f"<style>\n{css}\n</style>",
    )
    html = html.replace(
        '<script src="main.js"></script>',
        f"<script>\n{js}\n</script>",
    )
    return html


def main() -> None:
    st.set_page_config(
        page_title="Architechs | FTC Robotics",
        page_icon="🔧",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.markdown(
        """
<style>
    header[data-testid="stHeader"] { display: none !important; }
    div[data-testid="stToolbar"] { display: none !important; }
    div[data-testid="stDecoration"] { display: none !important; }
    footer { visibility: hidden !important; height: 0 !important; }
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        max-width: none !important;
    }
    section[data-testid="stMain"] > div {
        padding-top: 0 !important;
        width: 100% !important;
    }
</style>
""",
        unsafe_allow_html=True,
    )
    st.html(_bundle_html(), width="stretch")


if __name__ == "__main__":
    main()
