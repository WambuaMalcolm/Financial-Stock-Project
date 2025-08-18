import streamlit as st
from src.query_engine import create_query_engine  # your module

# Create the query engine once
query_engine = create_query_engine()

st.title("📊 Financial Stock Assistant")

report_type = st.selectbox(
    'What type of report do you want?',
    ('Single Stock Outlook', 'Competitor Analysis')
)

if report_type == 'Single Stock Outlook':
    symbol = st.text_input("Stock Symbol")

    if symbol:
        with st.spinner(f'Generating report for {symbol}...'):
            response = query_engine.query(
                f"Write a report on the outlook for {symbol} stock from 2023 to 2027. "
                f"Be sure to include potential risks and headwinds."
            )

            # Show the answer
            st.subheader("📄 Report")
            st.write(str(response))

            # Show the sources
            if hasattr(response, "source_nodes"):
                st.subheader("🔍 Sources")
                for node in response.source_nodes:
                    st.markdown(f"**File:** {node.node.metadata.get('file_name', 'N/A')}")
                    st.write(node.node.text[:300] + "...")


elif report_type == 'Competitor Analysis':
    symbol1 = st.text_input("Stock Symbol 1")
    symbol2 = st.text_input("Stock Symbol 2")

    if symbol1 and symbol2:
        with st.spinner(f'Generating report for {symbol1} vs. {symbol2}...'):
            response = query_engine.query(
                f"Write a report on the competition between {symbol1} stock and {symbol2} stock."
            )

            # Show the answer
            st.subheader("📄 Report")
            st.write(str(response))

            # Show the sources
            if hasattr(response, "source_nodes"):
                st.subheader("🔍 Sources")
                for node in response.source_nodes:
                    st.markdown(f"**File:** {node.node.metadata.get('file_name', 'N/A')}")
                    st.write(node.node.text[:300] + "...")
