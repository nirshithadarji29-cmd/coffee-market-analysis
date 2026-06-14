import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# =====================================================
# DATABASE CONNECTION
# =====================================================

DATABASE_URL = "postgresql://neondb_owner:npg_m6BzOKYuklo5@ep-long-fire-aoze56xh-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Coffee Market Expansion Strategy",
    page_icon="☕",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

market_df = pd.read_sql("""
SELECT *
FROM market_score
ORDER BY market_score DESC
""", engine)

# =====================================================
# HEADER
# =====================================================

st.title("☕ Coffee Market Expansion Strategy")

st.info("""
### Executive Summary

This dashboard identifies the most attractive countries for coffee market expansion using:

✅ Coffee Consumption

✅ Population Size

✅ Per-Capita Demand

The final Market Score ranks countries based on their overall business attractiveness.
""")

# =====================================================
# KPI CARDS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Countries Analyzed",
        market_df["country_name"].nunique()
    )

with col2:
    st.metric(
        "Top Market",
        market_df.iloc[0]["country_name"]
    )

with col3:
    st.metric(
        "Highest Score",
        f"{market_df.iloc[0]['market_score']:.3f}"
    )

with col4:
    st.metric(
        "Recommended Markets",
        "Top 3"
    )

st.divider()

# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📈 Executive Summary",
        "🏆 Market Ranking",
        "🌍 Country Explorer",
        "📋 Methodology"
    ]
)

# =====================================================
# TAB 1 - EXECUTIVE SUMMARY
# =====================================================

with tab1:

    st.header("Top Recommended Markets")

    top3 = market_df.head(3)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success(
            f"""
🥇 #1 Market

{top3.iloc[0]['country_name']}

Score: {top3.iloc[0]['market_score']:.3f}
"""
        )

    with c2:
        st.info(
            f"""
🥈 #2 Market

{top3.iloc[1]['country_name']}

Score: {top3.iloc[1]['market_score']:.3f}
"""
        )

    with c3:
        st.warning(
            f"""
🥉 #3 Market

{top3.iloc[2]['country_name']}

Score: {top3.iloc[2]['market_score']:.3f}
"""
        )

    st.header("Business Recommendation")

    st.write(f"""
Based on the market scoring model, the highest ranked countries are:

**1. {top3.iloc[0]['country_name']}**

**2. {top3.iloc[1]['country_name']}**

**3. {top3.iloc[2]['country_name']}**

These markets demonstrate the strongest combination of:

- Coffee Consumption
- Population Scale
- Per-Capita Demand

and represent the most attractive opportunities for expansion.
""")

# =====================================================
# TAB 2 - MARKET RANKING
# =====================================================

with tab2:

    st.header("Top 10 Market Ranking")

    top10 = market_df.head(10)

    fig = px.bar(
        top10,
        x="market_score",
        y="country_name",
        orientation="h",
        text=top10["market_score"].round(3),
        title="Top 10 Markets by Market Score"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        yaxis_title="Country",
        xaxis_title="Market Score",
        height=650
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Market Score Distribution")

    dist_fig = px.histogram(
        market_df,
        x="market_score",
        nbins=20,
        title="Distribution of Market Scores"
    )

    st.plotly_chart(
        dist_fig,
        use_container_width=True
    )

    st.subheader("Market Ranking Data")

    with st.expander("View Full Ranking Table"):
        st.dataframe(
            market_df,
            use_container_width=True
        )

# =====================================================
# TAB 3 - COUNTRY EXPLORER
# =====================================================

with tab3:

    st.header("Country Explorer")

    selected_country = st.selectbox(
        "Select Country",
        sorted(market_df["country_name"].unique())
    )

    try:

        country_query = f"""
        SELECT *
        FROM vw_market_analysis
        WHERE country_name = '{selected_country}'
        ORDER BY market_year
        """

        country_df = pd.read_sql(
            country_query,
            engine
        )

        if len(country_df) > 0:

            st.subheader(f"{selected_country} Market Overview")

            k1, k2, k3 = st.columns(3)

            with k1:
                st.metric(
                    "Latest Population",
                    f"{country_df['population'].max():,.0f}"
                )

            with k2:
                st.metric(
                    "Average Consumption",
                    f"{country_df['domestic_consumption'].mean():,.2f}"
                )

            with k3:
                st.metric(
                    "Average Per Capita",
                    f"{country_df['consumption_per_capita'].mean():.4f}"
                )

            st.subheader("Coffee Consumption Trend")

            consumption_fig = px.line(
                country_df,
                x="market_year",
                y="domestic_consumption",
                markers=True
            )

            st.plotly_chart(
                consumption_fig,
                use_container_width=True
            )

            st.subheader("Coffee Production Trend")

            production_fig = px.line(
                country_df,
                x="market_year",
                y="production",
                markers=True
            )

            st.plotly_chart(
                production_fig,
                use_container_width=True
            )

            st.subheader("Imports vs Exports")

            trade_df = country_df[
                [
                    "market_year",
                    "imports",
                    "exports"
                ]
            ].melt(
                id_vars="market_year",
                var_name="Trade Type",
                value_name="Value"
            )

            trade_fig = px.line(
                trade_df,
                x="market_year",
                y="Value",
                color="Trade Type",
                markers=True
            )

            st.plotly_chart(
                trade_fig,
                use_container_width=True
            )

            st.subheader("Population Growth Trend")

            pop_fig = px.line(
                country_df,
                x="market_year",
                y="population",
                markers=True
            )

            st.plotly_chart(
                pop_fig,
                use_container_width=True
            )

    except Exception as e:
        st.error(str(e))

# =====================================================
# TAB 4 - METHODOLOGY
# =====================================================

with tab4:

    st.header("Methodology")

    st.subheader("Data Sources")

    st.markdown("""
- USDA Coffee Production & Consumption Dataset
- World Bank Population Dataset
- ISO Country Code Mapping Dataset
""")

    st.subheader("Data Engineering Process")

    st.markdown("""
1. Extracted Coffee Market Data

2. Extracted Population Data

3. Standardized Country Codes

4. Built Star Schema

5. Loaded Data into PostgreSQL (Neon)

6. Created Analytical Views

7. Calculated Market Scores
""")

    st.subheader("Market Score Logic")

    st.markdown("""
Market Score combines:

- Coffee Consumption
- Population Size
- Per-Capita Demand

All metrics were normalized and weighted to produce a final market attractiveness score.
""")

    st.subheader("Data Quality Checks")

    st.success("✓ Population data cleaned")

    st.success("✓ Coffee data standardized")

    st.success("✓ Country mappings validated")

    st.success("✓ Missing values handled")

    st.warning("""
A small number of country mapping anomalies were identified during validation
and should be reviewed before production deployment.
""")

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption("""
Coffee Market Expansion Analysis

Built Using:
• PostgreSQL (Neon)
• Python
• SQL
• Streamlit
• Plotly

Prepared as a Business Intelligence & Data Analytics Case Study
""")