# 🌊 ORP Marine Plastics AI-Enabled Story Map

An interactive story map for exploring the Ocean Research Project's Chesapeake Bay microplastic survey data using natural language queries and AI-powered data exploration.

![Demo](https://img.shields.io/badge/Demo-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10+-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Overview

This AI-enabled story map demonstrates how marine research organizations can make their expedition data more accessible through:

- **Natural language querying** - Ask questions in plain English
- **Interactive geospatial visualization** - Explore 25 sampling stations across Chesapeake Bay
- **Data sovereignty** - Options for local or cloud-based AI processing
- **WordPress integration** - Easy embedding in existing websites

Built in partnership between **Ocean Research Project** and **Resonant Knowledge Lab**.

## 🚀 Quick Start

### Run Locally

```bash
# Clone the repository
git clone https://github.com/mbbrady/orp-marine-plastics-storymap.git
cd orp-marine-plastics-storymap

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Deploy to Hugging Face Spaces

1. Create a new Space on [Hugging Face](https://huggingface.co/new-space)
2. Choose **Streamlit** as the SDK
3. Upload `app.py` and `requirements.txt`
4. Your story map will be live at `https://huggingface.co/spaces/YOUR-USERNAME/SPACE-NAME`

## 🔗 WordPress Integration

### Method 1: Embed via iframe (Recommended)

Add this code to your WordPress page using a "Custom HTML" block:

```html
<iframe
    src="https://huggingface.co/spaces/YOUR-USERNAME/orp-marine-plastics"
    width="100%"
    height="800"
    frameborder="0"
    style="border: none; border-radius: 8px;">
</iframe>
```

### Method 2: Test Integration Locally

We've included `test_integration.html` which shows how the story map looks embedded in a webpage:

1. Make sure the Streamlit app is running locally (port 8501)
2. Open `test_integration.html` in your web browser
3. You'll see a mock ORP website page with the story map embedded

This lets you preview the integration before deploying!

## ✨ Features

### Interactive Map
- 25 Chesapeake Bay sampling stations from Fall 2023 expedition
- Dark minimalist theme with CartoDB Dark Matter basemap
- Clickable markers with popup details
- Real station names and locations from ORP survey

### Natural Language Queries
- 10 example queries demonstrating AI capabilities
- Ask about:
  - Highest/lowest microplastic concentrations
  - Temperature and salinity patterns
  - Geographic filtering (e.g., "Potomac River stations")
  - Data comparisons and summaries

### Data Explorer
- Filter data by microplastic count, temperature, and salinity
- Interactive data table
- Download filtered results as CSV
- Real-time filtering

### Integration Guide
- Step-by-step WordPress embedding instructions
- Self-hosting deployment guide
- Customization options
- Testing instructions

### About Section
- Project overview
- Technology stack details
- Data sovereignty options
- Partnership information

## 📊 Sample Data

The demo uses realistic sample data based on ORP's Fall 2023 Chesapeake Bay Plastic Survey structure:

- **25 sampling stations** across the Chesapeake Bay
- **Data types**: Microplastic counts (particles/m³), water temperature (°C), salinity, GPS coordinates
- **Time period**: October 2023

*Note: This is demonstration data. Contact ORP for actual survey results.*

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Mapping**: Folium/Leaflet with CartoDB Dark Matter theme
- **Data Processing**: pandas, geopandas
- **Deployment**: Hugging Face Spaces, Streamlit Community Cloud, or self-hosted

**Future capabilities** (not in current demo):
- LangChain RAG pipeline for real natural language processing
- ChromaDB vector store for semantic search
- Local LLM support (Llama 3.1) or cloud APIs (GPT-4, Claude)
- sentence-transformers for embeddings

## 🔐 Data Sovereignty Options

Organizations can choose their preferred approach:

- **Local LLM**: Complete data sovereignty, runs on your infrastructure
- **API Mode**: Convenience of cloud AI (GPT-4/Claude) with controlled data exposure
- **Hybrid**: Both options available based on use case

RKL provides:
- Design and architecture consulting
- Infrastructure planning and deployment assistance
- Grant funding pursuit for necessary infrastructure (compute hardware, API subscriptions)
- Training and ongoing support

## 📁 Repository Structure

```
orp-marine-plastics-storymap/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── test_integration.html       # WordPress integration test page
├── README.md                   # This file
└── .gitignore                  # Git ignore patterns
```

## 🤝 About the Partnership

### Ocean Research Project (ORP)

The Ocean Research Project conducts marine plastics research through expedition-based data collection aboard the SRV Marie Tharp.

- Website: [oceanresearchproject.org](http://www.oceanresearchproject.org/)
- Marine Debris Program: [Link](http://www.oceanresearchproject.org/programs/science/marine-debris/)

### Resonant Knowledge Lab (RKL)

Resonant Knowledge Lab is a 501(c)(3) nonprofit enabling AI-powered data exploration while maintaining full data sovereignty for organizations.

- Website: [resonantknowledgelab.org](https://resonantknowledgelab.org)
- Email: info@resonantknowledgelab.org

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- Ocean Research Project for partnership and data structure
- Chesapeake Bay research community
- Open-source mapping and data visualization communities

## 📧 Contact & Support

For questions, customization, or integration assistance:

- **Technical Issues**: Open an issue on GitHub
- **Partnership Inquiries**: info@resonantknowledgelab.org
- **ORP Inquiries**: Visit [oceanresearchproject.org](http://www.oceanresearchproject.org/)

---

**Built with 💙 for ocean conservation and open science**

*Prototype developed by Resonant Knowledge Lab in partnership with Ocean Research Project*
