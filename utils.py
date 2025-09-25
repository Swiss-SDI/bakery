# coding=utf-8
""" Utility functions for the bakery Streamlit app """
# Copyright 2023, Swiss Statistical Design & Innovation Sàrl

import streamlit as st


def render_swiss_sdi_footer():
    """
    Renders the Swiss-SDI footer component with logo and website link.
    This function can be called from any page to display consistent branding.
    Follows Streamlit footer best practices with proper styling and layout.
    """
    # Footer with Swiss-SDI and Streamlit branding - Normal flow, no gap
    # Remove default margins and padding that create gaps
    st.markdown(
        """
        <style>
        .main .block-container {
            padding-bottom: 0px; /* Remove default bottom padding */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Create a clean footer that sits at the bottom of content without gaps
    footer_html = f"""
    <style>
        .content-footer {{
            margin-top: 30px;
            margin-bottom: 0;
            padding: 20px 0 0 0;
            text-align: center;
            background-color: transparent;
            border-top: 1px solid #e6e6e6;
        }}
        .footer-content {{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
            margin-bottom: 10px;
        }}
        .footer-logo {{
            height: 50px;
            vertical-align: middle;
            transition: opacity 0.3s ease;
        }}
        .footer-logo:hover {{
            opacity: 0.8;
        }}
        .footer-text {{
            color: #666;
            font-size: 13px;
            margin: 0;
            padding-bottom: 0;
        }}
        .footer-link {{
            color: #D80707 !important;
            text-decoration: none !important;
            font-weight: 500;
        }}
        .footer-link:hover {{
            color: #D80707 !important;
            text-decoration: underline !important;
        }}
        .footer-streamlit {{
            color: #D80707 !important;
            text-decoration: none !important;
            font-weight: 500;
        }}
        .footer-streamlit:hover {{
            color: #D80707 !important;
            text-decoration: underline !important;
        }}
        .content-footer a {{
            color: #D80707 !important;
            text-decoration: none !important;
        }}
        .content-footer a:hover {{
            color: #D80707 !important;
            text-decoration: underline !important;
        }}
        .content-footer a:visited {{
            color: #D80707 !important;
        }}
        @media (max-width: 768px) {{
            .footer-content {{
                flex-direction: column;
                gap: 10px;
            }}
            .footer-logo {{
                height: 40px;
            }}
            .footer-text {{
                font-size: 12px;
            }}
        }}
    </style>
    <div class="content-footer">
        <div class="footer-content">
            <a href="https://swiss-sdi.ch" target="_blank" style="text-decoration: none;">
                <img src="data:image/png;base64,{_get_ssdi_logo_base64()}" alt="Swiss-SDI Logo" class="footer-logo">
            </a>
            <img src="data:image/png;base64,{_get_streamlit_logo_base64()}" alt="Streamlit Logo" class="footer-logo">
        </div>
        <p class="footer-text">
            Powered by <a href="https://swiss-sdi.ch" target="_blank" class="footer-link">Swiss Statistical Design & Innovation</a> 
            and <a href="https://streamlit.io" target="_blank" class="footer-streamlit">Streamlit</a>
        </p>
    </div>
    """
    
    st.markdown(footer_html, unsafe_allow_html=True)


def _get_ssdi_logo_base64():
    """
    Convert the Swiss-SDI logo to base64 for embedding in HTML.
    Returns the base64 encoded string of the logo.
    """
    import base64
    try:
        with open("assets/ssdi.png", "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        # Fallback if logo file is not found
        return ""


def _get_streamlit_logo_base64():
    """
    Convert the Streamlit logo to base64 for embedding in HTML.
    Returns the base64 encoded string of the logo.
    """
    import base64
    try:
        with open("assets/streamlit.png", "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        # Fallback if logo file is not found
        return ""
