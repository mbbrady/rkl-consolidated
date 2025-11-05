"""
ORP Marine Plastics AI-Enabled Story Map
Streamlit Demo Application

Ocean Research Project - Chesapeake Bay Plastic Survey
AI-enabled interactive story map with natural language querying.
"""

import streamlit as st
import pandas as pd
import geopandas as gpd
from pathlib import Path
import json
from datetime import datetime
import folium
from streamlit_folium import st_folium

# Page config
st.set_page_config(
    page_title="ORP Marine Plastics Story Map",
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
st.markdown('<div class="main-header">🌊 ORP Marine Plastics AI-Enabled Story Map</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Chesapeake Bay Plastic Survey • Natural language querying • Interactive mapping</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/300x100/0F4C81/FFFFFF?text=RKL+Logo", use_container_width=True)

    st.markdown("### About This Demo")
    st.info("""
    This prototype demonstrates how marine research organizations can use AI to query
    their expedition data naturally—without exposing sensitive research data to cloud services.

    **Key Features:**
    - 🗺️ Interactive mapping
    - 💬 Natural language queries
    - 🔒 Local processing capability
    - 📊 Real expedition data structure
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
    st.markdown("### About This Partnership")
    st.markdown("""
    **Ocean Research Project**
    Marine plastics research through expedition-based data collection aboard the SRV Marie Tharp.

    - Website: [oceanresearchproject.org](https://www.oceanresearchproject.org/)
    - [Marine Plastics Project](https://www.oceanresearchproject.org/about-6)
    """)

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
    """Load Chesapeake Bay sample data"""
    # This will be replaced with actual generated data
    data = {
        'sample_id': [f'ORP-2023-{i:04d}' for i in range(25)],
        'station_name': [
            'Elizabeth River', 'James River', 'Bay Mouth', 'Lower Bay', 'York River',
            'Rappahannock River', 'Potomac River 1', 'Potomac River 2', 'Lower Eastern Shore',
            'Patuxent River', 'Lower Western Shore', 'Mid Bay', 'Eastern Bay',
            'Magothy River', 'Upper Eastern Shore', 'Patapsco River', 'Back River',
            'Middle River', 'Gunpowder', 'Bush', 'C&D Canal', 'Susquehanna',
            'Severn River', 'Choptank River 1', 'Choptank River 2'
        ],
        'latitude': [
            36.849, 36.987, 36.941, 37.292, 37.238,
            37.611, 38.076, 38.785, 37.835, 38.314,
            38.908, 38.407, 38.845, 38.063, 39.004,
            39.173, 39.242, 39.298, 39.316, 39.347,
            39.438, 39.452, 38.974, 38.664, 38.664
        ],
        'longitude': [
            -76.300, -76.321, -76.139, -76.136, -76.504,
            -76.307, -76.445, -77.037, -75.954, -76.422,
            -76.483, -76.337, -76.322, -76.455, -76.173,
            -76.469, -76.405, -76.395, -76.307, -76.248,
            -75.998, -76.035, -76.467, -76.211, -76.228
        ],
        'microplastic_count': [
            45, 78, 34, 56, 67, 89, 123, 145, 23, 98,
            134, 76, 54, 187, 43, 234, 156, 112, 87, 65,
            34, 28, 198, 76, 82
        ],
        'water_temp_c': [
            18.5, 19.2, 17.8, 18.1, 18.9, 19.4, 20.1, 19.8, 18.3, 19.7,
            20.5, 19.1, 19.8, 21.2, 18.7, 21.8, 20.9, 20.3, 19.5, 19.2,
            18.1, 17.9, 20.8, 19.3, 19.4
        ],
        'salinity': [
            15.2, 14.8, 18.9, 16.7, 12.4, 10.8, 8.9, 5.2, 19.4, 11.3,
            6.7, 13.5, 8.2, 4.1, 9.8, 3.2, 4.5, 5.8, 7.2, 8.1,
            2.1, 1.5, 5.9, 9.7, 9.5
        ],
        'date': ['2023-10-23', '2023-10-23', '2023-10-24', '2023-10-24', '2023-10-24',
                 '2023-10-25', '2023-10-25', '2023-10-26', '2023-10-26', '2023-10-26',
                 '2023-10-27', '2023-10-27', '2023-10-27', '2023-10-28', '2023-10-28',
                 '2023-10-28', '2023-10-29', '2023-10-29', '2023-10-29', '2023-10-29',
                 '2023-10-30', '2023-10-30', '2023-10-30', '2023-10-31', '2023-10-31']
    }
    return pd.DataFrame(data)

df = load_sample_data()

# Main content tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🗺️ Interactive Map", "💬 Natural Language Queries", "📊 Data Explorer", "🔗 Integration", "ℹ️ About"])

with tab1:
    st.markdown("### Chesapeake Bay Sampling Locations")
    st.markdown("*Based on Ocean Research Project's Fall 2023 expedition (25 stations)*")

    # Create Folium map with dark minimalist theme
    m = folium.Map(
        location=[38.5, -76.5],
        zoom_start=8,
        tiles='CartoDB dark_matter',
        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
    )

    # Add markers for each sampling station
    for idx, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=8,
            popup=folium.Popup(f"""
                <b>{row['station_name']}</b><br>
                Sample ID: {row['sample_id']}<br>
                Microplastics: {row['microplastic_count']} particles/m³<br>
                Temperature: {row['water_temp_c']}°C<br>
                Salinity: {row['salinity']}<br>
                Date: {row['date']}
            """, max_width=300),
            color='#0F4C81',
            fill=True,
            fillColor='#4A90E2',
            fillOpacity=0.7,
            weight=2
        ).add_to(m)

    # Display map
    st_folium(m, width=None, height=500)

    # Summary statistics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Stations", len(df))
    with col2:
        st.metric("Avg Microplastics", f"{df['microplastic_count'].mean():.0f} /m³")
    with col3:
        st.metric("Avg Temperature", f"{df['water_temp_c'].mean():.1f}°C")
    with col4:
        st.metric("Date Range", "Oct 23-31, 2023")

with tab2:
    st.markdown("### Natural Language Queries")
    st.markdown("*Ask questions about the expedition data in plain English*")

    # Example queries
    st.markdown("#### Try These Example Queries:")
    example_queries = [
        "Show sites with highest microplastic concentrations",
        "Which tributaries have the most contamination?",
        "What was the average water temperature?",
        "Display all Potomac River sampling locations",
        "Compare sites with salinity above 15",
        "Show me samples from late October",
        "Which station had the warmest water?",
        "List all stations in order of plastic count",
        "What's the relationship between temperature and microplastics?",
        "Summarize the Chesapeake Bay findings"
    ]

    cols = st.columns(2)
    for idx, query in enumerate(example_queries):
        with cols[idx % 2]:
            if st.button(f"🔍 {query}", key=f"example_{idx}", use_container_width=True):
                st.session_state['selected_query'] = query

    st.markdown("---")

    # Query input
    query = st.text_input(
        "Or type your own question:",
        value=st.session_state.get('selected_query', ''),
        placeholder="e.g., Show me all sites with more than 100 microplastics per cubic meter"
    )

    if st.button("🚀 Run Query", type="primary"):
        if query:
            with st.spinner("Processing query..."):
                # Placeholder query processing
                st.success("✅ Query processed!")

                # Simple keyword-based responses for demo
                if "highest" in query.lower() and "microplastic" in query.lower():
                    st.markdown("#### Results:")
                    st.markdown("""
                    The highest microplastic concentrations were found at:
                    1. **Patapsco River** - 234 particles/m³
                    2. **Severn River** - 198 particles/m³
                    3. **Magothy River** - 187 particles/m³
                    4. **Potomac River 2** - 145 particles/m³
                    5. **Lower Western Shore** - 134 particles/m³
                    """)
                    top_5 = df.nlargest(5, 'microplastic_count')[['station_name', 'microplastic_count', 'water_temp_c', 'salinity']]
                    st.dataframe(top_5, use_container_width=True)

                elif "temperature" in query.lower() and "average" in query.lower():
                    avg_temp = df['water_temp_c'].mean()
                    st.markdown(f"""
                    #### Results:
                    The average water temperature across all 25 sampling stations was **{avg_temp:.2f}°C**.

                    - Minimum: {df['water_temp_c'].min():.1f}°C
                    - Maximum: {df['water_temp_c'].max():.1f}°C
                    - Standard deviation: {df['water_temp_c'].std():.1f}°C
                    """)
                    st.bar_chart(df.set_index('station_name')['water_temp_c'])

                elif "potomac" in query.lower():
                    potomac_data = df[df['station_name'].str.contains('Potomac', case=False)]
                    st.markdown(f"""
                    #### Results:
                    Found {len(potomac_data)} sampling locations in the Potomac River:
                    """)
                    st.dataframe(potomac_data[['station_name', 'microplastic_count', 'water_temp_c', 'salinity', 'date']], use_container_width=True)

                elif "salinity" in query.lower() and "15" in query:
                    high_salinity = df[df['salinity'] > 15]
                    st.markdown(f"""
                    #### Results:
                    Found {len(high_salinity)} stations with salinity above 15:
                    """)
                    st.dataframe(high_salinity[['station_name', 'salinity', 'microplastic_count']], use_container_width=True)

                else:
                    st.info("""
                    **This is a demo with placeholder responses.**

                    In the full version with RAG pipeline:
                    - Your query would be converted to a vector embedding
                    - Relevant data would be retrieved from the vector store
                    - A local LLM would generate a natural language response
                    - Supporting data and visualizations would be included

                    Try one of the example queries above to see sample responses!
                    """)
        else:
            st.warning("Please enter a query")

with tab3:
    st.markdown("### Data Explorer")
    st.markdown("*Browse the complete Chesapeake Bay expedition dataset*")

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        min_plastics = st.slider("Min microplastics (particles/m³)", 0, 250, 0)
    with col2:
        temp_range = st.slider("Water temperature (°C)", 15.0, 25.0, (15.0, 25.0))
    with col3:
        salinity_range = st.slider("Salinity", 0.0, 20.0, (0.0, 20.0))

    # Filter data
    filtered_df = df[
        (df['microplastic_count'] >= min_plastics) &
        (df['water_temp_c'] >= temp_range[0]) &
        (df['water_temp_c'] <= temp_range[1]) &
        (df['salinity'] >= salinity_range[0]) &
        (df['salinity'] <= salinity_range[1])
    ]

    st.markdown(f"**Showing {len(filtered_df)} of {len(df)} stations**")
    st.dataframe(
        filtered_df[['sample_id', 'station_name', 'microplastic_count', 'water_temp_c', 'salinity', 'date']],
        use_container_width=True
    )

    # Download option
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Filtered Data (CSV)",
        data=csv,
        file_name="chesapeake_bay_filtered_data.csv",
        mime="text/csv"
    )

with tab4:
    st.markdown("### WordPress Integration Guide")

    st.markdown("""
    This story map can be easily integrated into your WordPress website. Choose one of the methods below:
    """)

    # Test integration section
    st.markdown("---")
    st.markdown("#### 🧪 Test the Integration First")

    st.info("""
    **Want to see how this looks on your website before deploying?**

    We've created a test HTML file that mimics your site layout with the story map embedded.
    """)

    st.markdown("""
    **Download and test locally:**

    1. Download the test file: `test_integration.html` (included with source code)
    2. Make sure this Streamlit app is running locally (port 8501)
    3. Open `test_integration.html` in your web browser
    4. You'll see a mock ORP website page with the story map embedded

    **What you can test:**
    - How the iframe integrates with surrounding content
    - Responsive sizing and scrolling behavior
    - Visual appearance on your site
    - User interaction (clicking between tabs, queries, etc.)
    """)

    test_html_url = "https://github.com/YOUR-ORG/orp-marine-plastics/blob/main/test_integration.html"

    st.markdown(f"""
    📥 **[Download test_integration.html]({test_html_url})**

    The test file includes:
    - ORP-style header and navigation
    - Sample intro text about the Chesapeake Bay survey
    - Embedded story map (iframe)
    - Footer and additional content

    This lets you preview exactly how the integration will look on your actual website!
    """)

    # Method 1: Embed via iframe
    st.markdown("---")
    st.markdown("#### Method 1: Embed in WordPress (Recommended)")

    st.markdown("""
    **Perfect for:** Quick integration, no technical setup required

    **Steps:**
    1. Copy the embed code below
    2. In your WordPress editor, add a "Custom HTML" block
    3. Paste the embed code
    4. Publish or update your page
    """)

    # Get current URL dynamically (will work on Hugging Face)
    embed_url = "https://huggingface.co/spaces/YOUR-USERNAME/orp-marine-plastics"

    embed_code = f'''<iframe
    src="{embed_url}"
    width="100%"
    height="800"
    frameborder="0"
    style="border: none; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
</iframe>'''

    st.code(embed_code, language='html')

    st.info("💡 **Note:** Replace `YOUR-USERNAME` with your actual Hugging Face username after deployment")

    st.markdown("""
    **WordPress Block Editor:**
    - Click the **+** button to add a block
    - Search for "Custom HTML"
    - Paste the code above
    - Preview to see the embedded map

    **Classic Editor:**
    - Switch to "Text" mode (not "Visual")
    - Paste the embed code where you want the map
    - Switch back to "Visual" to preview
    """)

    # Method 2: Self-hosted
    st.markdown("---")
    st.markdown("#### Method 2: Self-Hosted Installation")

    st.markdown("""
    **Perfect for:** Full control, custom data, on-premise hosting

    **Requirements:**
    - Python 3.10+
    - Server with public IP (or localhost for testing)
    - Basic command line knowledge

    **Steps:**

    1. **Download the source code:**
    ```bash
    git clone https://github.com/YOUR-ORG/orp-marine-plastics.git
    cd orp-marine-plastics
    ```

    2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

    3. **Run the application:**
    ```bash
    streamlit run app.py --server.port 8501
    ```

    4. **Make it accessible:**
    - For production: Use nginx or Apache as reverse proxy
    - Point your domain to the server
    - Configure SSL certificate (Let's Encrypt)

    5. **Embed in WordPress:**
    ```html
    <iframe
        src="https://your-domain.com:8501"
        width="100%"
        height="800">
    </iframe>
    ```
    """)

    st.warning("⚠️ **Security Note:** When self-hosting, ensure proper firewall configuration and use HTTPS in production")

    # Method 3: GitHub + One-click deploy
    st.markdown("---")
    st.markdown("#### Method 3: Deploy Your Own Copy")

    st.markdown("""
    **Perfect for:** Customization, your own branding, multiple projects

    **Platforms (all free tier available):**

    1. **Hugging Face Spaces** (Easiest)
       - Fork the repository
       - Create new Space on huggingface.co
       - Upload `app.py` and `requirements.txt`
       - Get your unique URL

    2. **Streamlit Community Cloud**
       - Connect your GitHub repository
       - One-click deployment
       - Auto-updates from GitHub

    3. **Heroku / Railway / Render**
       - Connect GitHub repo
       - Configure Python buildpack
       - Deploy and get URL
    """)

    # Customization guide
    st.markdown("---")
    st.markdown("#### Customization Options")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Easy Changes (No Coding):**
        - Update station names and locations
        - Change map colors and themes
        - Modify example queries
        - Update text content
        - Change logo and branding
        """)

    with col2:
        st.markdown("""
        **Advanced Options:**
        - Connect to your database
        - Integrate real-time data feeds
        - Add authentication/access control
        - Custom data visualizations
        - Multi-language support
        """)

    st.markdown("---")
    st.info("""
    📧 **Need Help?** Contact Resonant Knowledge Lab for integration support:
    - Email: info@resonantknowledgelab.org
    - We provide setup assistance and customization services
    """)

with tab5:
    st.markdown("### About This Prototype")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        #### Project Overview

        This prototype demonstrates **Resonant Knowledge Lab's** approach to enabling AI-powered
        data exploration while maintaining full data sovereignty.

        **Key Features:**
        - Natural language querying of expedition data
        - Interactive geospatial visualization
        - Local processing capability (no cloud dependency required)
        - Open-source and reproducible

        #### Partnership

        Built in collaboration with the **Ocean Research Project (ORP)** for their Chesapeake Bay
        Plastic Survey. The demo uses realistic data structure from ORP's Fall 2023 expedition.

        - 25 sampling stations across Chesapeake Bay
        - Multiple data types: microplastic counts, water quality, GPS coordinates
        - October 2023 field campaign
        """)

    with col2:
        st.markdown("""
        #### Technology Stack

        **Current Demo:**
        - Python 3.10+
        - Streamlit for web interface
        - Folium/Leaflet for maps
        - pandas/geopandas for data
        - Placeholder query responses

        **Full Version (Path B):**
        - LangChain RAG pipeline
        - ChromaDB vector store
        - Llama 3.1 (local) or GPT-4/Claude (API)
        - sentence-transformers embeddings

        #### Data Sovereignty Options

        Organizations can choose:
        - **Local LLM**: Complete data sovereignty, run on your infrastructure
        - **API Mode**: Convenience of cloud AI, controlled data exposure
        - **Hybrid**: Both options available

        **RKL Support:**
        - Design and architecture consulting for data sovereignty solutions
        - Infrastructure planning and deployment assistance
        - Pursuing grant funding to build necessary infrastructure (compute hardware, GPT/Claude API subscriptions, etc.)
        - Training and ongoing support for your team
        """)

    st.markdown("---")

    st.markdown("""
    #### Next Steps

    Interested in using this for your research data?

    1. **Try the Demo**: Explore the map and example queries
    2. **Contact Us**: Discuss integrating your actual datasets
    3. **Deploy**: Run on your infrastructure with your data

    **Contact:**
    - Website: [resonantknowledgelab.org](https://resonantknowledgelab.org)
    - Email: info@resonantknowledgelab.org
    - GitHub: [Coming soon]

    #### About Ocean Research Project

    The Ocean Research Project conducts marine plastics research through expedition-based
    data collection aboard the SRV Marie Tharp.

    - Website: [oceanresearchproject.org](http://www.oceanresearchproject.org/)
    - Marine Debris Program: [Link](http://www.oceanresearchproject.org/programs/science/marine-debris/)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6C757D;'>
    <p>ORP Marine Plastics AI-Enabled Story Map | Prototype by Resonant Knowledge Lab</p>
    <p>Ocean Research Project • Resonant Knowledge Lab 501(c)(3)</p>
</div>
""", unsafe_allow_html=True)
