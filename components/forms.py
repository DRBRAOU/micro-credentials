"""Form components for course generation and assessment inputs."""

import streamlit as st
from typing import Dict, Any, Optional


def render_course_form() -> Optional[Dict[str, Any]]:
    """Render the course generation input form."""
    with st.form("course_form", clear_on_submit=False):
        col1, col2 = st.columns(2)

        with col1:
            course_title = st.text_input("Course Title", placeholder="e.g., Data Science Fundamentals")
            department = st.text_input("Department", placeholder="e.g., Computer Science")
            programme = st.text_input("Programme", placeholder="e.g., B.Sc. Computer Science")
            course_type = st.selectbox(
                "Course Type",
                options=["Skill Based", "Value Added", "Micro-Credential", "Credit Course"],
            )
            ncrf_level = st.selectbox("NCrF Level", options=[f"Level {i}" for i in range(1, 11)])
            credits = st.number_input("Credits", min_value=1, max_value=20, value=4)

        with col2:
            duration = st.text_input("Duration", placeholder="e.g., 16 weeks")
            semester = st.selectbox(
                "Semester",
                options=[f"Semester {i}" for i in range(1, 9)],
            )
            mode_of_delivery = st.selectbox(
                "Mode of Delivery",
                options=["Online", "Offline", "Blended", "Hybrid"],
            )
            target_learners = st.text_input("Target Learners", placeholder="e.g., UG Year 2 students")
            prerequisites = st.text_input("Prerequisites", placeholder="e.g., Basic programming")
            expected_skills = st.text_input("Expected Skills", placeholder="e.g., Python, Statistics")

        course_description = st.text_area("Course Description", placeholder="Describe the course...", height=100)
        additional_instructions = st.text_area("Additional Instructions", placeholder="Any specific requirements...", height=80)

        submitted = st.form_submit_button("Generate Course", use_container_width=True)

        if submitted:
            return {
                "course_title": course_title,
                "department": department,
                "programme": programme,
                "course_type": course_type,
                "ncrf_level": ncrf_level,
                "credits": credits,
                "duration": duration,
                "semester": semester,
                "mode_of_delivery": mode_of_delivery,
                "target_learners": target_learners,
                "prerequisites": prerequisites,
                "expected_skills": expected_skills,
                "course_description": course_description,
                "additional_instructions": additional_instructions,
            }
    return None


def render_assessment_form() -> Optional[Dict[str, Any]]:
    """Render the assessment designer input form."""
    with st.form("assessment_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        with col1:
            assessment_type = st.selectbox(
                "Assessment Type",
                options=["Quiz", "Assignment", "Project", "Presentation", "Case Study"],
            )
            credits = st.number_input("Credits", min_value=1, max_value=20, value=4)
        with col2:
            learning_outcomes = st.text_area("Learning Outcomes", placeholder="List the learning outcomes...", height=120)

        additional_notes = st.text_area("Additional Notes", placeholder="Any specific requirements...", height=60)
        submitted = st.form_submit_button("Generate Assessment", use_container_width=True)

        if submitted:
            return {
                "assessment_type": assessment_type,
                "credits": credits,
                "learning_outcomes": learning_outcomes,
                "additional_notes": additional_notes,
            }
    return None


def render_rubric_form() -> Optional[Dict[str, Any]]:
    """Render the rubric generator input form."""
    with st.form("rubric_form", clear_on_submit=False):
        assessment_name = st.text_input("Assessment Name", placeholder="e.g., Final Project Report")
        criteria = st.text_area(
            "Criteria",
            placeholder="List criteria separated by commas (e.g., Content Quality, Organization, Research Depth)",
            height=80,
        )
        performance_levels = st.selectbox(
            "Performance Levels",
            options=[
                "3 Levels (Excellent, Satisfactory, Needs Improvement)",
                "4 Levels (Excellent, Good, Satisfactory, Needs Improvement)",
                "5 Levels (Exemplary, Proficient, Competent, Developing, Beginning)",
            ],
        )
        submitted = st.form_submit_button("Generate Rubric", use_container_width=True)

        if submitted:
            return {
                "assessment_name": assessment_name,
                "criteria": criteria,
                "performance_levels": performance_levels,
            }
    return None
