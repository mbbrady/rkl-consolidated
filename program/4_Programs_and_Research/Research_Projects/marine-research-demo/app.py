"""
Marine Research AI-Enabled Story Map
Streamlit Demo Application

Demonstration of AI-enabled interactive story map with natural language querying
for marine research data.
"""

import streamlit as st
import pandas as pd
from pathlib import Path
import json
from datetime import datetime
import folium
from streamlit_folium import st_folium

# Page config
st.set_page_config(
    page_title="Marine Research Story Map Demo",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #0F4C81;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #6C757D;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #F8F9FA;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #0F4C81;
    }
    .query-example {
        background-color: #E7F3FF;
        padding: 0.5rem 1rem;
        border-radius: 0.3rem;
        margin: 0.5rem 0;
        cursor: pointer;
    }
    .stButton>button {
        background-color: #0F4C81;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🌊 Marine Research AI Story Map</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Demonstration • Natural language querying • Interactive mapping</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/300x100/0F4C81/FFFFFF?text=RKL+Logo", use_column_width=True)

    st.markdown("### About This Demo")
    st.info("""
    This prototype demonstrates how marine research organizations can use AI to query
    their expedition data naturally—without exposing sensitive research data to cloud services.

    **Key Features:**
    - 🗺️ Interactive mapping
    - 💬 Natural language queries
    - 🔒 Local processing capability
    - 📊 Sample expedition data structure
    """)

    st.markdown("### Demo Mode")
    demo_mode = st.radio(
        "LLM Backend:",
        ["API (OpenAI/Claude)", "Local LLM (Llama 3.1)", "Placeholder"],
        index=2,
        help="In production, choose between cloud API or fully local processing"
    )

    if demo_mode == "API (OpenAI/Claude)":
        st.warning("⚠️ API mode requires key (not included in public demo)")
    elif demo_mode == "Local LLM (Llama 3.1)":
        st.info("💻 Local LLM would run on your infrastructure")
    else:
        st.success("✅ Using placeholder responses for demo")

    st.markdown("---")
    st.markdown("### About RKL")
    st.markdown("""
    **Resonant Knowledge Lab** is a 501(c)(3) nonprofit creating open infrastructure
    for responsible AI use with organizational data.

    - Website: [resonantknowledgelab.org](https://resonantknowledgelab.org)
    - Email: info@resonantknowledgelab.org
    """)

# Load sample data
@st.cache_data
def load_sample_data():
    """Load sample marine research data"""
    # Sample data structure for demonstration
    data = {
        'sample_id': [f'MR-2023-{i:04d}' for i in range(25)],
        'station_name': [
            'Station A1', 'Station A2', 'Station A3', 'Station A4', 'Station A5',
            'Station B1', 'Station B2', 'Station B3', 'Station B4', 'Station B5',
            'Station C1', 'Station C2', 'Station C3', 'Station C4', 'Station C5',
            'Station D1', 'Station D2', 'Station D3', 'Station D4', 'Station D5',
            'Station E1', 'Station E2', 'Station E3', 'Station E4', 'Station E5'
        ],
        'latitude': [
            36.849, 36.987, 36.941, 37.292, 37.238,
            37.611, 38.076, 38.785, 37.835, 38.314,
            38.908, 38.407, 38.845, 38.063, 39.004,
            39.173, 39.242, 39.298, 39.316, 39.347,
            39.434, 39.533, 38.963, 38.613, 38.513
        ],
        'longitude': [
            -76.215, -76.192, -76.090, -76.203, -76.398,
            -76.532, -76.987, -76.421, -76.186, -76.543,
            -76.271, -76.138, -76.364, -76.487, -76.221,
            -76.354, -76.287, -76.419, -76.502, -76.324,
            -76.072, -76.154, -76.443, -76.574, -76.321
        ],
        'microplastic_count': [
            245, 189, 312, 278, 423,
            156, 267, 334, 201, 289,
            178, 245, 312, 267, 234,
            298, 356, 412, 389, 334,
            278, 423, 267, 198, 245
        ],
        'temperature': [
            18.5, 19.2, 18.9, 19.5, 18.3,
            20.1, 19.8, 18.7, 19.3, 19.6,
            20.3, 19.9, 19.2, 19.7, 20.0,
            19.4, 18.8, 19.1, 19.5, 19.9,
            20.2, 19.6, 19.3, 19.8, 20.1
        ],
        'salinity': [
            28.5, 27.8, 29.2, 28.1, 26.9,
            27.3, 28.9, 26.5, 28.4, 27.6,
            28.2, 29.0, 27.4, 28.6, 27.9,
            28.3, 29.1, 27.7, 28.0, 28.8,
            27.5, 28.4, 29.3, 27.1, 28.7
        ],
        'date': ['2023-10-15'] * 25
    }

    df = pd.DataFrame(data)
    return df

df = load_sample_data()

# Main tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🗺️ Map View", "💬 Natural Language Query", "📊 Data Explorer", "ℹ️ About", "🚀 Deploy Your Own"])

with tab1:
    st.markdown("### Interactive Station Map")
    st.caption("Sample marine research sampling stations")

    # Create folium map
    m = folium.Map(
        location=[38.5, -76.5],
        zoom_start=8,
        tiles='CartoDB dark_matter'
    )

    # Add markers
    for idx, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=6,
            popup=f"""
            <b>{row['station_name']}</b><br>
            Sample ID: {row['sample_id']}<br>
            Microplastics: {row['microplastic_count']} particles/m³<br>
            Temperature: {row['temperature']}°C<br>
            Salinity: {row['salinity']} PSU
            """,
            color='#E36F5C',
            fillColor='#E36F5C',
            fillOpacity=0.7,
            weight=2
        ).add_to(m)

    # Display map
    st_folium(m, width=700, height=600)

    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Stations", len(df))
    with col2:
        st.metric("Avg Microplastics", f"{df['microplastic_count'].mean():.0f} /m³")
    with col3:
        st.metric("Avg Temperature", f"{df['temperature'].mean():.1f}°C")
    with col4:
        st.metric("Avg Salinity", f"{df['salinity'].mean():.1f} PSU")

with tab2:
    st.markdown("### Natural Language Query Interface")
    st.caption("Ask questions about the marine research data in plain English")

    # Example queries
    st.markdown("#### Try These Example Queries:")
    examples = [
        "Which station had the highest microplastic count?",
        "What's the average temperature across all stations?",
        "Show me stations with salinity below 28 PSU",
        "Which stations have more than 300 microplastics per cubic meter?",
        "What's the temperature range in the survey area?",
        "Compare microplastic levels in the northern vs southern stations",
        "Which station had the lowest contamination?",
        "What's the correlation between temperature and microplastic count?",
        "Show stations with both high temperature and high microplastics",
        "What's the median salinity value?"
    ]

    for i, example in enumerate(examples):
        if st.button(example, key=f"example_{i}"):
            st.session_state.selected_query = example

    # Query input
    query = st.text_input("Or type your own question:", value=st.session_state.get('selected_query', ''))

    if query:
        st.markdown("---")
        st.markdown("#### AI Response:")

        # Generate response based on query
        response = ""
        if "highest microplastic" in query.lower():
            max_row = df.loc[df['microplastic_count'].idxmax()]
            response = f"**{max_row['station_name']}** had the highest microplastic count with **{max_row['microplastic_count']} particles/m³**."

        elif "average temperature" in query.lower():
            avg_temp = df['temperature'].mean()
            response = f"The average temperature across all stations is **{avg_temp:.1f}°C**."

        elif "salinity below 28" in query.lower():
            low_sal = df[df['salinity'] < 28]
            stations = ", ".join(low_sal['station_name'].tolist())
            response = f"There are **{len(low_sal)} stations** with salinity below 28 PSU: {stations}."

        elif "more than 300 microplastics" in query.lower():
            high_mp = df[df['microplastic_count'] > 300]
            stations = ", ".join(high_mp['station_name'].tolist())
            response = f"**{len(high_mp)} stations** have more than 300 microplastics per cubic meter: {stations}."

        elif "temperature range" in query.lower():
            min_temp = df['temperature'].min()
            max_temp = df['temperature'].max()
            response = f"The temperature range is **{min_temp:.1f}°C to {max_temp:.1f}°C** (range of {max_temp - min_temp:.1f}°C)."

        elif "northern vs southern" in query.lower():
            median_lat = df['latitude'].median()
            northern = df[df['latitude'] >= median_lat]['microplastic_count'].mean()
            southern = df[df['latitude'] < median_lat]['microplastic_count'].mean()
            response = f"Northern stations (latitude ≥ {median_lat:.2f}°): average **{northern:.0f} particles/m³**. Southern stations: average **{southern:.0f} particles/m³**."

        elif "lowest contamination" in query.lower():
            min_row = df.loc[df['microplastic_count'].idxmin()]
            response = f"**{min_row['station_name']}** had the lowest contamination with **{min_row['microplastic_count']} particles/m³**."

        elif "correlation" in query.lower():
            corr = df['temperature'].corr(df['microplastic_count'])
            if abs(corr) < 0.3:
                strength = "weak"
            elif abs(corr) < 0.7:
                strength = "moderate"
            else:
                strength = "strong"
            direction = "positive" if corr > 0 else "negative"
            response = f"There is a **{strength} {direction} correlation** (r = {corr:.3f}) between temperature and microplastic count."

        elif "high temperature and high microplastics" in query.lower():
            high_temp = df[df['temperature'] > df['temperature'].quantile(0.75)]
            high_both = high_temp[high_temp['microplastic_count'] > high_temp['microplastic_count'].quantile(0.75)]
            stations = ", ".join(high_both['station_name'].tolist())
            response = f"**{len(high_both)} stations** have both high temperature (>75th percentile) and high microplastics: {stations}."

        elif "median salinity" in query.lower():
            median_sal = df['salinity'].median()
            response = f"The median salinity value is **{median_sal:.1f} PSU**."

        else:
            response = "I can answer questions about the marine research data. Try one of the example queries above, or ask about stations, microplastic counts, temperature, or salinity."

        st.success(response)

        # Show sample data context
        with st.expander("📊 Sample data being queried"):
            st.dataframe(df.head(10))

with tab3:
    st.markdown("### Data Explorer")
    st.caption("Filter and explore the marine research dataset")

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        mp_range = st.slider("Microplastic Count (particles/m³)",
                            int(df['microplastic_count'].min()),
                            int(df['microplastic_count'].max()),
                            (int(df['microplastic_count'].min()), int(df['microplastic_count'].max())))
    with col2:
        temp_range = st.slider("Temperature (°C)",
                              float(df['temperature'].min()),
                              float(df['temperature'].max()),
                              (float(df['temperature'].min()), float(df['temperature'].max())))
    with col3:
        sal_range = st.slider("Salinity (PSU)",
                             float(df['salinity'].min()),
                             float(df['salinity'].max()),
                             (float(df['salinity'].min()), float(df['salinity'].max())))

    # Apply filters
    filtered_df = df[
        (df['microplastic_count'] >= mp_range[0]) & (df['microplastic_count'] <= mp_range[1]) &
        (df['temperature'] >= temp_range[0]) & (df['temperature'] <= temp_range[1]) &
        (df['salinity'] >= sal_range[0]) & (df['salinity'] <= sal_range[1])
    ]

    st.markdown(f"**Showing {len(filtered_df)} of {len(df)} stations**")
    st.dataframe(filtered_df, use_container_width=True)

    # Download button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name="marine_research_filtered.csv",
        mime="text/csv"
    )

with tab4:
    st.markdown("### About This Project")

    st.markdown("""
    #### Technology Demonstration

    This interactive story map demonstrates how marine research organizations can leverage AI
    to make their expedition data more accessible and queryable through natural language.

    **Key Capabilities:**
    - **Natural Language Querying**: Ask questions in plain English instead of writing complex database queries
    - **Interactive Visualization**: Explore sampling locations and data patterns on an interactive map
    - **Data Sovereignty**: Options for both cloud-based and fully local AI processing
    - **Integration Ready**: Can be embedded in existing websites or WordPress installations

    #### Sample Use Cases
    - Rapid data exploration during expeditions
    - Public engagement with research findings
    - Educational demonstrations
    - Grant proposal visualizations
    - Partner collaboration tools

    #### Technology Stack
    - **Frontend**: Streamlit (Python web framework)
    - **Mapping**: Folium/Leaflet with CartoDB Dark Matter theme
    - **Data Processing**: pandas, geopandas
    - **AI Options** (not active in demo):
      - LangChain RAG pipeline
      - Local LLM support (Llama 3.1) or cloud APIs (GPT-4, Claude)
      - ChromaDB vector store for semantic search

    #### About Resonant Knowledge Lab

    Resonant Knowledge Lab is a 501(c)(3) nonprofit organization creating open infrastructure
    for responsible AI use with organizational data.

    We help research organizations and institutions:
    - Apply AI to protected data without exposure
    - Maintain data sovereignty and control
    - Build verifiable and auditable AI systems
    - Implement ethical AI governance frameworks

    **Contact**: info@resonantknowledgelab.org
    **Website**: [resonantknowledgelab.org](https://resonantknowledgelab.org)

    ---

    *This is a demonstration with sample data. Contact RKL for implementation assistance.*
    """)

with tab5:
    st.markdown("### Deploy Your Own Story Map")

    st.markdown("""
    This is an open-source demo that you can customize and deploy for your own organization.
    All code is available on GitHub under an MIT license.
    """)

    # Source Code
    st.markdown("---")
    st.markdown("#### 📦 Source Code")

    github_url = "https://github.com/mbbrady/marine-research-demo"

    st.markdown(f"""
    **GitHub Repository:** [{github_url}]({github_url})

    The repository includes:
    - Complete Streamlit application code (`app.py`)
    - Sample data structure
    - Requirements and dependencies (`requirements.txt`)
    - README with project information
    - MIT License for free use and modification

    **To access the source code:**
    1. Visit the GitHub repository above
    2. Browse files or click "Code" → "Download ZIP"
    3. Clone the repository using git
    """)

    st.code(f"""# Clone from GitHub
git clone {github_url}
cd marine-research-demo

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
""", language='bash')

    # Deployment Options
    st.markdown("---")
    st.markdown("#### 🚀 Deployment Options")

    st.markdown("""
    **Option 1: Hugging Face Spaces (Easiest)**
    - Free hosting for public demos
    - Automatic deployment from GitHub
    - No server management required
    - Perfect for prototypes and demos

    **Steps:**
    1. Create a free account at [huggingface.co](https://huggingface.co)
    2. Create a new Space with Streamlit template
    3. Connect your GitHub repository
    4. Push your code and it deploys automatically

    **Option 2: Self-Hosted**
    - Full control over data and infrastructure
    - Can run on-premises or cloud servers
    - Ideal for production deployments
    - Supports local data sovereignty

    **Requirements:**
    - Linux/Mac/Windows server
    - Python 3.8+
    - 1GB RAM minimum
    - Port 8501 accessible
    """)

    # Embedding in Website
    st.markdown("---")
    st.markdown("#### 🔗 Embed in Your Website")

    st.markdown("""
    Once deployed, you can embed the story map in any website using an iframe:
    """)

    embed_code = f'''<iframe
    src="https://huggingface.co/spaces/rkl-org/marine-research-demo"
    width="100%"
    height="800"
    frameborder="0"
    style="border: none; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
</iframe>'''

    st.code(embed_code, language='html')

    st.markdown("""
    **For WordPress:**
    - Add a "Custom HTML" block
    - Paste the iframe code above
    - Replace the URL with your deployment URL
    - Adjust height as needed

    **For other CMS:**
    - Most content management systems support iframe embeds
    - Look for "Custom HTML" or "Embed" options
    - Paste the iframe code in HTML mode
    """)

    # Customization
    st.markdown("---")
    st.markdown("#### 🎨 Customization")

    st.markdown("""
    **Easy to customize for your data:**
    - Replace sample data with your research data
    - Update station names, coordinates, and measurements
    - Modify colors and branding
    - Add your organization's logo and information
    - Customize query responses for your specific use case

    **Data format:**
    - CSV or pandas DataFrame
    - Columns: station_name, latitude, longitude, measurements
    - Date field for temporal data (optional)
    - Any additional metadata fields

    **Need help customizing?**
    Contact RKL for implementation assistance: info@resonantknowledgelab.org
    """)

    # Advanced Features
    st.markdown("---")
    st.markdown("#### 🔬 Add Advanced Features")

    st.markdown("""
    The demo shows basic functionality. RKL can help you add:

    **Real AI Integration:**
    - Local LLM processing (Llama, Mistral, etc.)
    - Cloud AI APIs (GPT-4, Claude, etc.)
    - RAG pipeline for semantic search
    - Vector database for efficient querying

    **Data Governance:**
    - Access control and authentication
    - Audit logging for queries
    - Data sovereignty compliance
    - CARE principles implementation

    **Advanced Visualization:**
    - Time-series animations
    - Heat maps and clustering
    - Multi-layer map overlays
    - Custom data visualizations

    **Contact us:** info@resonantknowledgelab.org
    **Website:** [resonantknowledgelab.org](https://resonantknowledgelab.org)
    """)
