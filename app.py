import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Cyberattack Analytics Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# DARK THEME
# =========================================================

st.markdown(
    """
    <style>

    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #050b14 0%, #0b1120 100%);
        color: #e2e8f0;
    }

    .main {
        background: transparent;
    }

    .dashboard-title {
        text-align: center;
        padding: 30px 0 20px 0;
        animation: fadeIn 1s ease-in-out;
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-10px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .dashboard-title h1 {
        color: #f8fafc;
        font-size: 46px;
        font-weight: 800;
        margin-bottom: 8px;
        letter-spacing: -1px;
    }

    .dashboard-title h1 span {
        color: #38bdf8;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
    }

    .dashboard-title p {
        color: #94a3b8;
        font-size: 18px;
        font-weight: 400;
        margin-top: 0;
        letter-spacing: 0.5px;
    }

    .section-title {
        color: #f8fafc;
        font-size: 26px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 8px;
        border-left: 4px solid #38bdf8;
        padding-left: 12px;
        text-shadow: 0 0 10px rgba(56,189,248,0.2);
    }

    .section-description {
        color: #94a3b8;
        font-size: 15px;
        margin-bottom: 25px;
        padding-left: 16px;
    }

    .kpi-card {
        background: rgba(17, 24, 39, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(56, 189, 248, 0.15);
        border-radius: 16px;
        padding: 24px 16px;
        min-height: 130px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }

    .kpi-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(56, 189, 248, 0.15);
        border-color: rgba(56, 189, 248, 0.5);
    }

    .kpi-title {
        color: #94a3b8;
        font-size: 15px;
        font-weight: 600;
        margin-bottom: 12px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    .kpi-value {
        color: #38bdf8;
        font-size: 36px;
        font-weight: 800;
        line-height: 1.2;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
    }

    /* Filters / Inputs */
    div[data-baseweb="select"] > div {
        background-color: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid #1e293b !important;
        border-radius: 10px !important;
        transition: border-color 0.3s ease;
    }

    div[data-baseweb="select"] > div:hover {
        border-color: #38bdf8 !important;
    }

    div[data-baseweb="select"] span {
        color: #f8fafc !important;
    }

    /* Reset Button */
    .stButton > button {
        background: linear-gradient(90deg, #0ea5e9, #2563eb);
        color: #ffffff;
        border: none;
        border-radius: 10px;
        height: 42px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(14, 165, 233, 0.3);
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #2563eb, #0ea5e9);
        box-shadow: 0 6px 20px rgba(14, 165, 233, 0.5);
        transform: translateY(-2px);
    }

    /* Download Button */
    .stDownloadButton > button {
        background: rgba(30, 41, 59, 0.7);
        color: #f8fafc;
        border: 1px solid #334155;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stDownloadButton > button:hover {
        background: rgba(56, 189, 248, 0.1);
        border-color: #38bdf8;
        color: #38bdf8;
        transform: translateY(-2px);
    }

    label {
        color: #94a3b8 !important;
        font-weight: 600 !important;
    }

    hr {
        border-color: rgba(51, 65, 85, 0.5);
        margin: 30px 0;
    }
    
    /* Metrics for Automated Insights */
    [data-testid="stMetricValue"] {
        color: #38bdf8 !important;
        font-size: 32px !important;
        font-weight: 800 !important;
        text-shadow: 0 0 15px rgba(56, 189, 248, 0.3) !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 15px !important;
        color: #94a3b8 !important;
        font-weight: 600 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# COMMON CHART STYLE
# =========================================================

def style_chart(fig, height=450):

    fig.update_layout(
        template="plotly_dark",
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            color="#cbd5e1",
            family="Inter, sans-serif"
        ),
        margin=dict(
            l=55,
            r=30,
            t=75,
            b=65
        ),
        hoverlabel=dict(
            bgcolor="rgba(15, 23, 42, 0.95)",
            font_size=14,
            font_color="#f8fafc",
            bordercolor="#38bdf8",
            font_family="Inter, sans-serif"
        ),
        colorway=["#38bdf8", "#818cf8", "#34d399", "#fbbf24", "#f472b6", "#a78bfa"]
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        automargin=True,
        tickfont=dict(color="#94a3b8")
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(51, 65, 85, 0.4)",
        zeroline=False,
        tickformat=",",
        automargin=True,
        tickfont=dict(color="#94a3b8")
    )

    return fig


# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("cyberattacks_cleaned.csv")


# =========================================================
# DATA CLEANING
# =========================================================

df["Year"] = pd.to_numeric(
    df["Year"],
    errors="coerce"
)

df["Counts of Attack"] = pd.to_numeric(
    df["Counts of Attack"],
    errors="coerce"
)

df = df.dropna(
    subset=[
        "Year",
        "Counts of Attack"
    ]
)

df["Year"] = df["Year"].astype(int)


# =========================================================
# MONTH NUMBER
# =========================================================

month_map = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

df["Month Number"] = df["Month"].map(month_map)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="dashboard-title">
        <h1><span>🛡️</span> Cyberattack Analytics</h1>
        <p>India Cyber Threat Intelligence Dashboard<br>Analysis Period: <span>2023 – 2025</span></p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# FILTER OPTIONS
# =========================================================

years = sorted(
    df["Year"].unique().tolist()
)

states = sorted(
    df["State"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

attack_types = sorted(
    df["Type of Attacks"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)


# =========================================================
# RESET FILTERS
# =========================================================

def reset_filters():

    st.session_state["year_filter"] = "All"
    st.session_state["state_filter"] = "All"
    st.session_state["type_filter"] = "All"


# =========================================================
# FILTER SECTION
# =========================================================

st.markdown(
    '<div class="section-title">🔎 Explore Cyberattack Data</div>',
    unsafe_allow_html=True
)

filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(
    [1, 1.6, 1.6, 1]
)

with filter_col1:

    selected_year = st.selectbox(
        "📅 Year",
        ["All"] + [
            str(year)
            for year in years
        ],
        key="year_filter"
    )

with filter_col2:

    selected_state = st.selectbox(
        "📍 State",
        ["All"] + states,
        key="state_filter"
    )

with filter_col3:

    selected_type = st.selectbox(
        "🛡️ Attack Type",
        ["All"] + attack_types,
        key="type_filter"
    )

with filter_col4:

    st.write("")

    st.button(
        "🔄 Reset Filters",
        use_container_width=True,
        on_click=reset_filters
    )

st.divider()


# =========================================================
# APPLY FILTERS
# =========================================================

filtered_df = df.copy()

if selected_year != "All":

    filtered_df = filtered_df[
        filtered_df["Year"].astype(str)
        == selected_year
    ]

if selected_state != "All":

    filtered_df = filtered_df[
        filtered_df["State"].astype(str)
        == selected_state
    ]

if selected_type != "All":

    filtered_df = filtered_df[
        filtered_df["Type of Attacks"].astype(str)
        == selected_type
    ]


# =========================================================
# FILTER STATUS
# =========================================================

active_filters = []

if selected_year != "All":
    active_filters.append(
        f"Year: {selected_year}"
    )

if selected_state != "All":
    active_filters.append(
        f"State: {selected_state}"
    )

if selected_type != "All":
    active_filters.append(
        f"Attack Type: {selected_type}"
    )

if active_filters:

    st.info(
        "🔎 Active Filters: "
        + " | ".join(active_filters)
    )

else:

    st.success(
        "Showing data for all years, states and attack types."
    )


# =========================================================
# KPI CALCULATIONS
# =========================================================

if len(filtered_df) > 0:

    total_attacks = int(
        filtered_df["Counts of Attack"].sum()
    )

    average_attack = int(
        filtered_df["Counts of Attack"].mean()
    )

    total_records = len(filtered_df)

    total_states = filtered_df["State"].nunique()

    total_attack_types = (
        filtered_df["Type of Attacks"].nunique()
    )

else:

    total_attacks = 0
    average_attack = 0
    total_records = 0
    total_states = 0
    total_attack_types = 0


# =========================================================
# KPI SECTION
# =========================================================

st.markdown(
    '<div class="section-title">📌 Key Performance Indicators</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Summary of cyberattack activity for the selected filters.'
    '</div>',
    unsafe_allow_html=True
)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(
        f'''
        <div class="kpi-card">
            <div class="kpi-title">🛡️ Total Attacks</div>
            <div class="kpi-value">{total_attacks:,}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with kpi2:
    st.markdown(
        f'''
        <div class="kpi-card">
            <div class="kpi-title">📍 Total States</div>
            <div class="kpi-value">{total_states:,}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with kpi3:
    st.markdown(
        f'''
        <div class="kpi-card">
            <div class="kpi-title">🔐 Attack Types</div>
            <div class="kpi-value">{total_attack_types:,}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with kpi4:
    st.markdown(
        f'''
        <div class="kpi-card">
            <div class="kpi-title">📋 Dataset Records</div>
            <div class="kpi-value">{total_records:,}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

st.divider()

# =========================================================
# ATTACK OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">📊 Attack Overview</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Overall cyberattack distribution across years and attack categories.'
    '</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


# =========================================================
# YEAR CHART
# =========================================================

with col1:

    yearly_analysis = (
        filtered_df
        .groupby(
            "Year",
            as_index=False
        )["Counts of Attack"]
        .sum()
        .rename(
            columns={
                "Counts of Attack":
                "Total Attacks"
            }
        )
        .sort_values("Year")
    )

    fig_year = px.bar(
        yearly_analysis,
        x="Year",
        y="Total Attacks",
        title="Total Cyberattacks by Year",
        text="Total Attacks"
    )

    fig_year.update_traces(
        texttemplate="%{text:,}",
        textposition="outside",
        hovertemplate=
        "<b>Year:</b> %{x}<br>"
        "<b>Total Attacks:</b> %{y:,}"
        "<extra></extra>"
    )

    fig_year.update_layout(
        xaxis_title="Year",
        yaxis_title="Total Attacks"
    )

    fig_year = style_chart(
        fig_year,
        450
    )

    st.plotly_chart(
        fig_year,
        use_container_width=True,
        key="year_chart"
    )


# =========================================================
# ATTACK TYPE CHART
# =========================================================

with col2:

    attack_type_analysis = (
        filtered_df
        .groupby(
            "Type of Attacks",
            as_index=False
        )["Counts of Attack"]
        .sum()
        .rename(
            columns={
                "Counts of Attack":
                "Total Attacks"
            }
        )
        .sort_values(
            "Total Attacks",
            ascending=False
        )
    )

    fig_type = px.bar(
        attack_type_analysis,
        x="Type of Attacks",
        y="Total Attacks",
        title="Cyberattacks by Attack Type",
        text="Total Attacks"
    )

    fig_type.update_traces(
        texttemplate="%{text:,}",
        textposition="outside",
        hovertemplate=
        "<b>Attack Type:</b> %{x}<br>"
        "<b>Total Attacks:</b> %{y:,}"
        "<extra></extra>"
    )

    fig_type.update_layout(
        xaxis_title="Attack Type",
        yaxis_title="Total Attacks"
    )

    fig_type = style_chart(
        fig_type,
        450
    )

    st.plotly_chart(
        fig_type,
        use_container_width=True,
        key="attack_type_chart"
    )

st.divider()

# =========================================================
# REGIONAL THREAT ANALYSIS
# =========================================================

st.markdown(
    '<div class="section-title">🌍 Regional Threat Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Geographic distribution and states with the highest cyberattack counts.'
    '</div>',
    unsafe_allow_html=True
)

map_col, top5_col = st.columns(2)

with map_col:
    state_map_data = (
        filtered_df
        .groupby(
            "State",
            as_index=False
        )["Counts of Attack"]
        .sum()
        .rename(
            columns={
                "Counts of Attack":
                "Total Attacks"
            }
        )
    )

    state_coordinates = {
        "Andhra Pradesh": (15.9129, 79.7400),
        "Arunachal Pradesh": (28.2180, 94.7278),
        "Assam": (26.2006, 92.9376),
        "Bihar": (25.0961, 85.3131),
        "Chhattisgarh": (21.2787, 81.8661),
        "Goa": (15.2993, 74.1240),
        "Gujarat": (22.2587, 71.1924),
        "Haryana": (29.0588, 76.0856),
        "Himachal Pradesh": (31.1048, 77.1734),
        "Jharkhand": (23.6102, 85.2799),
        "Karnataka": (15.3173, 75.7139),
        "Kerala": (10.8505, 76.2711),
        "Madhya Pradesh": (22.9734, 78.6569),
        "Maharashtra": (19.7515, 75.7139),
        "Manipur": (24.6637, 93.9063),
        "Meghalaya": (25.4670, 91.3662),
        "Mizoram": (23.1645, 92.9376),
        "Nagaland": (26.1584, 94.5624),
        "Odisha": (20.9517, 85.0985),
        "Punjab": (31.1471, 75.3412),
        "Rajasthan": (27.0238, 74.2179),
        "Sikkim": (27.5330, 88.5122),
        "Tamil Nadu": (11.1271, 78.6569),
        "Telangana": (18.1124, 79.0193),
        "Tripura": (23.9408, 91.9882),
        "Uttar Pradesh": (26.8467, 80.9462),
        "Uttarakhand": (30.0668, 79.0193),
        "West Bengal": (22.9868, 87.8550),
        "Delhi": (28.7041, 77.1025),
        "Jammu and Kashmir": (33.7782, 76.5762),
        "Ladakh": (34.1526, 77.5771),
        "Puducherry": (11.9416, 79.8083),
        "Chandigarh": (30.7333, 76.7794),
        "Dadra and Nagar Haveli and Daman and Diu": (20.1809, 73.0169),
        "Andaman and Nicobar Islands": (11.7401, 92.6586),
        "Lakshadweep": (10.5667, 72.6417)
    }

    map_df = state_map_data.copy()
    map_df["Latitude"] = map_df["State"].map(lambda x: state_coordinates.get(x, (None, None))[0])
    map_df["Longitude"] = map_df["State"].map(lambda x: state_coordinates.get(x, (None, None))[1])
    map_df = map_df.dropna(subset=["Latitude", "Longitude"])

    if len(map_df) > 0:
        fig_map = px.scatter_geo(
            map_df,
            lat="Latitude",
            lon="Longitude",
            size="Total Attacks",
            color="Total Attacks",
            hover_name="State",
            hover_data={
                "Total Attacks": ":,",
                "Latitude": False,
                "Longitude": False
            },
            projection="natural earth",
            title="State-wise Cyberattack Distribution",
            size_max=45,
            color_continuous_scale=["#1e293b", "#0ea5e9", "#38bdf8", "#a5f3fc"]
        )

        fig_map.update_geos(
            scope="asia",
            showcountries=True,
            countrycolor="rgba(51, 65, 85, 0.5)",
            showsubunits=True,
            subunitcolor="rgba(51, 65, 85, 0.5)",
            showland=True,
            landcolor="rgba(15, 23, 42, 0.5)",
            showocean=True,
            oceancolor="rgba(0,0,0,0)",
            bgcolor="rgba(0,0,0,0)"
        )

        fig_map.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                color="#cbd5e1",
                family="Inter, sans-serif"
            ),
            height=650,
            margin=dict(
                l=10,
                r=10,
                t=70,
                b=10
            )
        )

        st.plotly_chart(
            fig_map,
            use_container_width=True,
            key="india_map"
        )
    else:
        st.warning("No geographic data available for the selected filters.")

with top5_col:
    top5_analysis = (
        filtered_df
        .groupby(
            "State",
            as_index=False
        )["Counts of Attack"]
        .sum()
        .rename(
            columns={
                "Counts of Attack":
                "Total Attacks"
            }
        )
        .sort_values(
            "Total Attacks",
            ascending=False
        )
        .head(5)
    )

    fig_top5 = px.bar(
        top5_analysis,
        x="State",
        y="Total Attacks",
        title="Top 5 States by Cyberattacks",
        text="Total Attacks"
    )

    fig_top5.update_traces(
        texttemplate="%{text:,}",
        textposition="outside",
        hovertemplate=
        "<b>State:</b> %{x}<br>"
        "<b>Total Attacks:</b> %{y:,}"
        "<extra></extra>"
    )

    fig_top5.update_layout(
        xaxis_title="State",
        yaxis_title="Total Attacks",
        xaxis_tickangle=-35
    )

    fig_top5 = style_chart(
        fig_top5,
        450
    )

    st.plotly_chart(
        fig_top5,
        use_container_width=True,
        key="top5_chart"
    )

st.divider()

# =========================================================
# TEMPORAL ANALYSIS
# =========================================================

st.markdown(
    '<div class="section-title">📅 Temporal Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Monthly cyberattack trends over the selected period.'
    '</div>',
    unsafe_allow_html=True
)

monthly_analysis = (
    filtered_df
    .groupby(
        ["Month", "Month Number"],
        as_index=False
    )["Counts of Attack"]
    .sum()
    .rename(
        columns={
            "Counts of Attack":
            "Total Attacks"
        }
    )
    .sort_values("Month Number")
)

fig_month = px.line(
    monthly_analysis,
    x="Month Number",
    y="Total Attacks",
    markers=True,
    title="Monthly Cyberattack Trend"
)

fig_month.update_traces(
    hovertemplate=
    "<b>Month:</b> %{x}<br>"
    "<b>Total Attacks:</b> %{y:,}"
    "<extra></extra>"
)

fig_month.update_layout(
    xaxis_title="Month",
    yaxis_title="Total Attacks",
    xaxis=dict(
        tickmode="array",
        tickvals=list(range(1, 13)),
        ticktext=[
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
    )
)

fig_month = style_chart(
    fig_month,
    450
)

st.plotly_chart(
    fig_month,
    use_container_width=True,
    key="monthly_chart"
)

st.divider()

# =========================================================
# ATTACK PATTERN ANALYSIS
# =========================================================

st.markdown(
    '<div class="section-title">🔍 Attack Pattern Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Comparison of attack categories across different time periods.'
    '</div>',
    unsafe_allow_html=True
)

type_year_col, type_month_col = st.columns(2)

with type_year_col:
    type_year_analysis = (
        filtered_df
        .groupby(
            ["Year", "Type of Attacks"],
            as_index=False
        )["Counts of Attack"]
        .sum()
        .rename(
            columns={
                "Counts of Attack":
                "Total Attacks"
            }
        )
        .sort_values("Year")
    )

    fig_type_year = px.bar(
        type_year_analysis,
        x="Year",
        y="Total Attacks",
        color="Type of Attacks",
        barmode="group",
        title="Cyberattack Types by Year"
    )

    fig_type_year.update_traces(
        hovertemplate=
        "<b>Year:</b> %{x}<br>"
        "<b>Total Attacks:</b> %{y:,}<br>"
        "<b>Attack Type:</b> %{fullData.name}"
        "<extra></extra>"
    )

    fig_type_year.update_layout(
        xaxis_title="Year",
        yaxis_title="Total Attacks"
    )

    fig_type_year = style_chart(
        fig_type_year,
        500
    )

    st.plotly_chart(
        fig_type_year,
        use_container_width=True,
        key="type_year_chart"
    )

with type_month_col:
    type_month_analysis = (
        filtered_df
        .groupby(
            [
                "Month",
                "Month Number",
                "Type of Attacks"
            ],
            as_index=False
        )["Counts of Attack"]
        .sum()
        .rename(
            columns={
                "Counts of Attack":
                "Total Attacks"
            }
        )
        .sort_values(
            "Month Number"
        )
    )

    fig_type_month = px.line(
        type_month_analysis,
        x="Month Number",
        y="Total Attacks",
        color="Type of Attacks",
        markers=True,
        title="Attack Type Trends by Month"
    )

    fig_type_month.update_traces(
        hovertemplate=
        "<b>Month:</b> %{x}<br>"
        "<b>Total Attacks:</b> %{y:,}<br>"
        "<b>Attack Type:</b> %{fullData.name}"
        "<extra></extra>"
    )

    fig_type_month.update_layout(
        xaxis_title="Month",
        yaxis_title="Total Attacks",
        xaxis=dict(
            tickmode="array",
            tickvals=list(range(1, 13)),
            ticktext=[
                "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
            ]
        )
    )

    fig_type_month = style_chart(
        fig_type_month,
        500
    )

    st.plotly_chart(
        fig_type_month,
        use_container_width=True,
        key="type_month_chart"
    )


st.divider()


# =========================================================
# SUBTYPE & CITY ANALYSIS
# =========================================================

st.markdown(
    '<div class="section-title">🏙️ Subtype & City Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Deep dive into specific attack subtypes and affected cities.'
    '</div>',
    unsafe_allow_html=True
)

sub_col, city_col = st.columns(2)

with sub_col:
    subtype_analysis = (
        filtered_df
        .groupby(
            "Subtype",
            as_index=False
        )["Counts of Attack"]
        .sum()
        .rename(
            columns={
                "Counts of Attack":
                "Total Attacks"
            }
        )
        .sort_values(
            "Total Attacks",
            ascending=False
        )
        .head(15)
    )

    fig_subtype = px.bar(
        subtype_analysis,
        x="Subtype",
        y="Total Attacks",
        title="Top 15 Cyberattack Subtypes",
        text="Total Attacks"
    )

    fig_subtype.update_traces(
        texttemplate="%{text:,}",
        textposition="outside",
        hovertemplate=
        "<b>Subtype:</b> %{x}<br>"
        "<b>Total Attacks:</b> %{y:,}"
        "<extra></extra>"
    )

    fig_subtype.update_layout(
        xaxis_title="Attack Subtype",
        yaxis_title="Total Attacks",
        xaxis_tickangle=-45
    )

    fig_subtype = style_chart(
        fig_subtype,
        550
    )

    st.plotly_chart(
        fig_subtype,
        use_container_width=True,
        key="subtype_chart"
    )


with city_col:
    city_analysis = (
        filtered_df
        .groupby(
            ["State", "City"],
            as_index=False
        )["Counts of Attack"]
        .sum()
        .rename(
            columns={
                "Counts of Attack":
                "Total Attacks"
            }
        )
        .sort_values(
            "Total Attacks",
            ascending=False
        )
        .head(15)
    )

    fig_city = px.bar(
        city_analysis,
        x="City",
        y="Total Attacks",
        title="Top 15 Cities by Cyberattacks",
        text="Total Attacks",
        hover_data=["State"]
    )

    fig_city.update_traces(
        texttemplate="%{text:,}",
        textposition="outside",
        hovertemplate=
        "<b>City:</b> %{x}<br>"
        "<b>State:</b> %{customdata[0]}<br>"
        "<b>Total Attacks:</b> %{y:,}"
        "<extra></extra>"
    )

    fig_city.update_layout(
        xaxis_title="City",
        yaxis_title="Total Attacks",
        xaxis_tickangle=-45
    )

    fig_city = style_chart(
        fig_city,
        550
    )

    st.plotly_chart(
        fig_city,
        use_container_width=True,
        key="city_chart"
    )

st.divider()

# =========================================================
# STATE-WISE YEAR ANALYSIS
# =========================================================

st.markdown(
    '<div class="section-title">📅 State-wise Year Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Comparison of state-level cyberattack counts across years.'
    '</div>',
    unsafe_allow_html=True
)

year_state_analysis = (
    filtered_df
    .groupby(
        ["Year", "State"],
        as_index=False
    )["Counts of Attack"]
    .sum()
    .rename(
        columns={
            "Counts of Attack":
            "Total Attacks"
        }
    )
    .sort_values("Year")
)

fig_year_state = px.bar(
    year_state_analysis,
    x="Year",
    y="Total Attacks",
    color="State",
    barmode="group",
    title="Cyberattacks by State and Year"
)

fig_year_state.update_traces(
    hovertemplate=
    "<b>Year:</b> %{x}<br>"
    "<b>Total Attacks:</b> %{y:,}<br>"
    "<b>State:</b> %{fullData.name}"
    "<extra></extra>"
)

fig_year_state.update_layout(
    xaxis_title="Year",
    yaxis_title="Total Attacks"
)

fig_year_state = style_chart(
    fig_year_state,
    550
)

st.plotly_chart(
    fig_year_state,
    use_container_width=True,
    key="year_state_chart"
)

st.divider()

# =========================================================
# AUTOMATED CYBERATTACK INSIGHTS
# =========================================================

st.markdown(
    '<div class="section-title">💡 Automated Cyberattack Insights</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Automatically generated observations based on the selected filters.'
    '</div>',
    unsafe_allow_html=True
)

if len(filtered_df) > 0:

    insight_state = filtered_df.groupby("State")["Counts of Attack"].sum().sort_values(ascending=False)
    highest_state = insight_state.index[0]
    highest_state_count = int(insight_state.iloc[0])

    insight_city = filtered_df.groupby(["State", "City"])["Counts of Attack"].sum().sort_values(ascending=False)
    highest_city_state = insight_city.index[0][0]
    highest_city = insight_city.index[0][1]
    highest_city_count = int(insight_city.iloc[0])

    insight_type = filtered_df.groupby("Type of Attacks")["Counts of Attack"].sum().sort_values(ascending=False)
    highest_type = insight_type.index[0]
    highest_type_count = int(insight_type.iloc[0])

    insight_year = filtered_df.groupby("Year")["Counts of Attack"].sum().sort_values(ascending=False)
    highest_year = int(insight_year.index[0])
    highest_year_count = int(insight_year.iloc[0])

    insight_month = filtered_df.groupby(["Month", "Month Number"])["Counts of Attack"].sum().sort_values(ascending=False)
    highest_month = insight_month.index[0][0]
    highest_month_count = int(insight_month.iloc[0])

    type_percentage = (highest_type_count / total_attacks * 100 if total_attacks > 0 else 0)

    insight1, insight2, insight3 = st.columns(3)

    with insight1:
        st.metric(label="📍 Highest Attack State", value=highest_state, delta=f"{highest_state_count:,} attacks")

    with insight2:
        st.metric(label="🏙️ Highest Attack City", value=highest_city, delta=f"{highest_city_count:,} attacks")
        st.caption(f"State: {highest_city_state}")

    with insight3:
        st.metric(label="🛡️ Most Frequent Attack Type", value=highest_type, delta=f"{highest_type_count:,} attacks")
        st.caption(f"{type_percentage:.1f}% of selected attacks")

    insight4, insight5, insight6 = st.columns(3)

    with insight4:
        st.metric(label="📅 Highest Attack Year", value=str(highest_year), delta=f"{highest_year_count:,} attacks")

    with insight5:
        st.metric(label="📈 Highest Attack Month", value=highest_month, delta=f"{highest_month_count:,} attacks")

    with insight6:
        st.metric(label="📊 Dataset Records", value=f"{total_records:,}", delta="Selected records")

else:
    st.warning("No data available for the selected filters.")

st.divider()

# =========================================================
# DATA EXPLORER
# =========================================================

st.markdown(
    '<div class="section-title">📋 Data Explorer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Detailed records based on the currently selected filters.'
    '</div>',
    unsafe_allow_html=True
)

display_columns = [
    "Year",
    "Month",
    "Type of Attacks",
    "Subtype",
    "State",
    "City",
    "Counts of Attack"
]

detail_df = filtered_df[display_columns].copy()

st.dataframe(
    detail_df,
    use_container_width=True,
    height=500
)

st.markdown(
    '<div class="section-title">⬇️ Download Filtered Data</div>',
    unsafe_allow_html=True
)

csv_data = detail_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered CSV",
    data=csv_data,
    file_name="filtered_cyberattack_analysis.csv",
    mime="text/csv"
)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        padding:20px;
        color:#64748b;
        font-size:14px;
    ">
        🛡️ Cyberattack Analytics Dashboard |
        Big Data Analysis Project |
        India | 2023–2025
    </div>
    """,
    unsafe_allow_html=True
)