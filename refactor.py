import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

def extract_section(start_marker, end_marker):
    start_idx = content.find(start_marker)
    if start_idx == -1: return ""
    end_idx = content.find(end_marker, start_idx) if end_marker else len(content)
    if end_idx == -1: end_idx = len(content)
    return content[start_idx:end_idx]

header_and_setup = content[:content.find('# =========================================================\n# FILTER OPTIONS')]
filters = extract_section('# =========================================================\n# FILTER OPTIONS', '# =========================================================\n# KPI CALCULATIONS')
kpi_calculations = extract_section('# =========================================================\n# KPI CALCULATIONS', '# =========================================================\n# KPI SECTION')
overview = extract_section('# =========================================================\n# OVERVIEW', '# =========================================================\n# TIME & REGIONAL OVERVIEW')
time_reg_overview = extract_section('# =========================================================\n# TIME & REGIONAL OVERVIEW', '# =========================================================\n# GEOGRAPHIC ANALYSIS')
india_map = extract_section('# =========================================================\n# INDIA CYBERATTACK MAP', '# =========================================================\n# AUTOMATED CYBERATTACK INSIGHTS')
insights = extract_section('# =========================================================\n# AUTOMATED CYBERATTACK INSIGHTS', '# =========================================================\n# ATTACK TYPE ANALYSIS')
attack_type_analysis = extract_section('# =========================================================\n# ATTACK TYPE ANALYSIS', '# =========================================================\n# SUBTYPE ANALYSIS')
subtype_analysis = extract_section('# =========================================================\n# SUBTYPE ANALYSIS', '# =========================================================\n# CITY LEVEL ANALYSIS')
city_analysis = extract_section('# =========================================================\n# CITY LEVEL ANALYSIS', '# =========================================================\n# STATE-WISE YEAR ANALYSIS')
state_year = extract_section('# =========================================================\n# STATE-WISE YEAR ANALYSIS', '# =========================================================\n# DETAILED DATA')
detailed_data = extract_section('# =========================================================\n# DETAILED DATA', "")

header_and_setup = re.sub(
    r'<div class="dashboard-title">.*?</div>',
    '<div class="dashboard-title">\\n        <h1><span>🛡️</span> Cyberattack Analytics</h1>\\n        <p>India Cyber Threat Intelligence Dashboard<br>Analysis Period: <span>2023 – 2025</span></p>\\n    </div>',
    header_and_setup,
    flags=re.DOTALL
)

filters = filters.replace('🎛️ Dashboard Filters', '🔎 Explore Cyberattack Data')

new_kpi_section = """# =========================================================
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

"""

overview = overview.replace('📊 Overview', '📊 Attack Overview')

def get_between(text, start, end):
    s = text.find(start)
    if s == -1: return ""
    e = text.find(end, s) if end else len(text)
    if e == -1: e = len(text)
    return text[s:e]

month_chart = get_between(time_reg_overview, '# =========================================================\n# MONTHLY CHART', '# =========================================================\n# TOP 5 STATES')
top5_states = get_between(time_reg_overview, '# =========================================================\n# TOP 5 STATES', "")
india_map_code = get_between(india_map, '# =========================================================\n# INDIA CYBERATTACK MAP', "")

def clean_and_indent(code, levels=1):
    lines = code.split('\\n')
    out = []
    skip = False
    for line in lines:
        if 'with col' in line: continue
        if line.startswith('st.divider()'): continue
        if '<div class="section-title">' in line or '<div class="section-description">' in line:
            skip = True
            continue
        if skip and 'unsafe_allow_html=True' in line:
            skip = False
            continue
        if skip: continue
        
        if line.startswith('    '): line = line[4:]
            
        if line.strip(): out.append('    ' * levels + line)
        else: out.append('')
    return '\\n'.join(out)

top5_clean = clean_and_indent(top5_states)
map_clean = clean_and_indent(india_map_code)

regional_analysis = """# =========================================================
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
""" + map_clean + """

with top5_col:
""" + top5_clean + """

st.divider()
"""

temporal_analysis = """# =========================================================
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

""" + clean_and_indent(month_chart, 0) + """

st.divider()
"""

attack_type_analysis = attack_type_analysis.replace('🛡️ Attack Type Analysis', '🔍 Attack Pattern Analysis')

subtype_clean = clean_and_indent(subtype_analysis)
city_clean = clean_and_indent(city_analysis)

subtype_city_analysis = """# =========================================================
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
""" + subtype_clean + """

with city_col:
""" + city_clean + """

st.divider()
"""

detailed_data = detailed_data.replace('📋 Detailed Analysis Data', '📋 Data Explorer')

new_content = (
    header_and_setup + 
    filters + 
    kpi_calculations + 
    new_kpi_section + 
    overview + 
    regional_analysis + 
    temporal_analysis + 
    attack_type_analysis + 
    subtype_city_analysis + 
    state_year + 
    insights + 
    detailed_data
)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Refactoring complete.")
