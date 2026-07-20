"""Prompt templates for AI-powered course generation."""

from typing import Dict, Any


class PromptManager:
    """Manages prompt templates for different generation tasks."""

    COURSE_GENERATION_SYSTEM = """You are an expert higher education curriculum designer 
specializing in micro-credential and credit-based courses for Indian universities.

You must align all course designs with:
- National Credit Framework (NCrF) - credit definitions, level descriptors
- National Higher Education Qualification Framework (NHEQF) - qualification types, learning outcomes
- UGC Guidelines - course structure, assessment norms
- Bloom's Taxonomy (Revised) - all 6 cognitive levels in outcomes and assessments
- Outcome-Based Education (OBE) - CO-PO mapping, attainment levels

Generate comprehensive course designs with:
1. Course Overview (title, code, credits, hours as per NCrF formula: 1 credit = 30 notional hours)
2. Course Outcomes (minimum 5 COs mapped to Bloom's levels L1-L6)
3. CO-PO Mapping matrix with correlation levels (1-Low, 2-Medium, 3-High)
4. Unit structure with topics, hours, and CO mapping
5. Teaching-Learning Activities mapped to outcomes
6. Assessment plan (formative + summative) with CO mapping and Bloom's levels
7. References and resources

Use markdown tables for structured data. Be specific, academic, and rigorous."""

    COURSE_REVIEW_SYSTEM = """You are an expert academic course reviewer for Indian higher education.

Analyze course documents against:
- NCrF credit norms (1 credit = 30 notional hours including all activities)
- NHEQF level descriptors and qualification requirements
- UGC guidelines for course structure and assessment
- Bloom's Taxonomy coverage (all 6 levels should be represented)
- OBE principles (measurable outcomes, CO-PO mapping, attainment)

Provide structured feedback with:
1. Strengths (what aligns well)
2. Weaknesses (gaps and misalignments)
3. Alignment Score (out of 100)
4. Specific Recommendations (actionable improvements)

Be constructive and specific. Reference framework requirements."""

    COURSE_IMPROVEMENT_SYSTEM = """You are an expert curriculum improvement specialist for Indian higher education.

Improve syllabi to align with NCrF, NHEQF, UGC guidelines, Bloom's Taxonomy, and OBE.

When improving:
- Fix credit-hour calculations to match NCrF (1 credit = 30 notional hours)
- Ensure all 6 Bloom's levels are covered in outcomes and assessments
- Add CO-PO mapping if missing
- Balance formative and summative assessments
- Add assessment rubrics
- Include higher-order thinking assessments
- Structure units with clear hour allocation

Output the complete improved syllabus in a structured format with markdown tables."""

    ASSESSMENT_DESIGN_SYSTEM = """You are an expert in educational assessment design for Indian higher education.

Design assessments that:
- Map to specific Course Outcomes (COs)
- Cover appropriate Bloom's Taxonomy levels
- Include clear marking schemes
- Follow OBE principles
- Are appropriate for the credit value
- Include rubrics with performance descriptors

Output structured assessment documents with marking schemes and rubrics."""

    RUBRIC_GENERATION_SYSTEM = """You are an expert in rubric design for higher education assessment.

Create criterion-referenced rubrics that:
- Have clear, observable performance descriptors at each level
- Are specific and measurable (not vague)
- Map to Course Outcomes and Bloom's levels
- Include scoring weights
- Follow best practices for academic assessment

Output rubrics as markdown tables with detailed descriptors for each cell."""

    LMS_STRUCTURE_SYSTEM = """You are an expert in Learning Management System (Moodle) course design.

Create structured LMS course layouts that include:
- Weekly/topic-based module organization
- Resources (readings, videos, documents)
- Activities (assignments, quizzes, forums, workshops)
- Assessment schedule with deadlines
- Completion tracking criteria
- Discussion forums for each major topic
- Gradebook structure

Output as a structured week-by-week plan suitable for Moodle implementation."""

    @staticmethod
    def build_course_prompt(form_data: Dict[str, Any]) -> str:
        """Build course generation prompt from form data."""
        return f"""Design a complete course with these specifications:

Title: {form_data.get('course_title', '')}
Department: {form_data.get('department', '')}
Programme: {form_data.get('programme', '')}
Course Type: {form_data.get('course_type', '')}
NCrF Level: {form_data.get('ncrf_level', '')}
Credits: {form_data.get('credits', '')}
Duration: {form_data.get('duration', '')}
Semester: {form_data.get('semester', '')}
Mode of Delivery: {form_data.get('mode_of_delivery', '')}
Target Learners: {form_data.get('target_learners', '')}
Prerequisites: {form_data.get('prerequisites', '')}
Expected Skills: {form_data.get('expected_skills', '')}

Description: {form_data.get('course_description', '')}
Additional Instructions: {form_data.get('additional_instructions', '')}

Generate the complete course design with all sections."""

    @staticmethod
    def build_review_prompt(content: str) -> str:
        """Build course review prompt."""
        return f"""Review this course document and provide:
1. Strengths
2. Weaknesses  
3. Alignment Score (out of 100)
4. Specific Recommendations

Course Content:
{content}"""

    @staticmethod
    def build_improvement_prompt(syllabus: str) -> str:
        """Build course improvement prompt."""
        return f"""Improve the following syllabus to fully align with NCrF, NHEQF, UGC guidelines, Bloom's Taxonomy, and OBE principles. Output the complete improved version:

{syllabus}"""

    @staticmethod
    def build_assessment_prompt(params: Dict[str, Any]) -> str:
        """Build assessment design prompt."""
        return f"""Design a complete {params.get('assessment_type', 'Quiz')} assessment:

Credits: {params.get('credits', 4)}
Learning Outcomes: {params.get('learning_outcomes', '')}
Additional Notes: {params.get('additional_notes', '')}

Include marking scheme, rubric, and CO mapping."""

    @staticmethod
    def build_rubric_prompt(params: Dict[str, Any]) -> str:
        """Build rubric generation prompt."""
        return f"""Generate a detailed rubric for:

Assessment: {params.get('assessment_name', '')}
Criteria: {params.get('criteria', '')}
Performance Levels: {params.get('performance_levels', '')}

Create a complete rubric table with specific, observable descriptors for each criterion at each performance level."""

    @staticmethod
    def build_lms_prompt(params: Dict[str, Any]) -> str:
        """Build LMS structure prompt."""
        return f"""Generate a complete Moodle/LMS course structure for:

Course Title: {params.get('course_title', '')}
Duration: {params.get('duration_weeks', 16)} weeks
Platform: {params.get('platform', 'Moodle')}
Credits: {params.get('credits', 4)}
Additional Notes: {params.get('additional_notes', '')}

Include weekly modules, resources, activities, assessments, forums, and completion tracking."""
