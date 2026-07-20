# 🎓 Micro-Credential Course Designer

A production-ready Streamlit application for higher education faculty to design, review, and improve credit-based and micro-credential courses aligned with national and international academic frameworks.

## Overview

The Micro-Credential Course Designer helps faculty at **Dr. B.R. Ambedkar Open University** and other institutions create academically rigorous courses that comply with:

- **NCrF** - National Credit Framework
- **NHEQF** - National Higher Education Qualification Framework
- **UGC Guidelines** - University Grants Commission standards
- **Bloom's Taxonomy** - Cognitive domain alignment
- **OBE** - Outcome-Based Education principles

## Features

| Feature | Description |
|---------|-------------|
| 📘 Course Design | Generate complete course structures with outcomes, units, and activities |
| 🔍 Course Review | Analyze existing courses for framework alignment |
| ✨ Course Improvement | Enhance syllabi to meet current standards |
| 📝 Assessment Design | Create OBE-aligned assessments |
| 📊 Rubric Generator | Build criterion-referenced rubrics |
| 💻 LMS Structure | Design Moodle-ready course layouts |
| 📥 Export | Download proposals in DOCX, PDF, or Markdown |

## Quick Start

### Prerequisites

- Python 3.12+
- pip

### Installation

```bash
# Clone or download the project
cd micro_course_designer

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The application will open at `http://localhost:8501`.

## Project Structure

```
micro_course_designer/
├── app.py                          # Main application entry point
├── pages/
│   ├── 1_Generate_Course.py        # Course generation page
│   ├── 2_Review_Course.py          # Course review page
│   ├── 3_Improve_Course.py         # Course improvement page
│   ├── 4_Assessment_Designer.py    # Assessment design page
│   ├── 5_Rubric_Generator.py       # Rubric generation page
│   └── 6_LMS_Structure.py          # LMS structure page
├── components/
│   ├── header.py                   # Header component
│   ├── sidebar.py                  # Sidebar navigation
│   ├── cards.py                    # Card components
│   ├── footer.py                   # Footer component
│   └── forms.py                    # Form components
├── services/
│   ├── openai_client.py            # OpenAI API client (placeholder)
│   ├── prompts.py                  # Prompt templates
│   ├── retrieval.py                # Knowledge retrieval service
│   └── exports.py                  # Document export service
├── assets/
│   ├── logo.png                    # University logo placeholder
│   └── styles.css                  # Custom CSS styles
├── knowledge/                      # Knowledge documents directory
├── generated/                      # Generated output directory
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Architecture

The application follows a modular architecture:

- **Pages**: Each page is a self-contained Streamlit script handling one feature
- **Components**: Reusable UI elements (header, footer, cards, forms)
- **Services**: Business logic separated from UI (AI client, prompts, exports)
- **Assets**: Static files (CSS, logos)

## Future Integration

The codebase is designed to support future AI integration with:

- **OpenAI Responses API** for intelligent course generation
- **Knowledge Document Upload** for RAG-based content creation
- **Export Services** for generating DOCX, PDF, and Markdown documents

## Technology Stack

- Python 3.12
- Streamlit
- streamlit-option-menu
- streamlit-extras
- python-docx
- reportlab
- pandas
- openpyxl
- plotly
- OpenAI SDK

## Version

**v1.0** - Initial release with placeholder content and complete UI.

## License

Internal use - Dr. B.R. Ambedkar Open University.
