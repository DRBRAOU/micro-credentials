"""OpenAI API client for course generation."""

import os
from typing import Dict, Any, Optional
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def _get_secret(key: str, default: str = "") -> str:
    """Get secret from Streamlit secrets (Cloud) or env vars (local)."""
    try:
        import streamlit as st
        return st.secrets.get(key, os.getenv(key, default))
    except Exception:
        return os.getenv(key, default)


class OpenAIClient:
    """Client for OpenAI Responses API."""

    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or _get_secret("OPENAI_API_KEY")
        self.model = _get_secret("OPENAI_MODEL", "gpt-4o-mini")
        self.client = OpenAI(api_key=self.api_key)

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """Send a prompt to OpenAI and return the response text.

        Args:
            system_prompt: System-level instruction.
            user_prompt: User-level content/question.

        Returns:
            Generated text response.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.7,
                max_tokens=4096,
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            return f"Error: {str(e)}"

    def generate_course(self, form_data: Dict[str, Any], context: str = "") -> str:
        """Generate a complete course design."""
        from services.prompts import PromptManager

        system = PromptManager.COURSE_GENERATION_SYSTEM
        if context:
            system += f"\n\nReference documents context:\n{context}"
        user = PromptManager.build_course_prompt(form_data)
        return self.generate(system, user)

    def review_course(self, content: str, context: str = "") -> str:
        """Review uploaded course content."""
        from services.prompts import PromptManager

        system = PromptManager.COURSE_REVIEW_SYSTEM
        if context:
            system += f"\n\nReference documents context:\n{context}"
        user = PromptManager.build_review_prompt(content)
        return self.generate(system, user)

    def improve_course(self, syllabus: str, context: str = "") -> str:
        """Improve an existing syllabus."""
        from services.prompts import PromptManager

        system = PromptManager.COURSE_IMPROVEMENT_SYSTEM
        if context:
            system += f"\n\nReference documents context:\n{context}"
        user = PromptManager.build_improvement_prompt(syllabus)
        return self.generate(system, user)

    def generate_assessment(self, params: Dict[str, Any], context: str = "") -> str:
        """Generate assessment design."""
        from services.prompts import PromptManager

        system = PromptManager.ASSESSMENT_DESIGN_SYSTEM
        if context:
            system += f"\n\nReference documents context:\n{context}"
        user = PromptManager.build_assessment_prompt(params)
        return self.generate(system, user)

    def generate_rubric(self, params: Dict[str, Any], context: str = "") -> str:
        """Generate rubric."""
        from services.prompts import PromptManager

        system = PromptManager.RUBRIC_GENERATION_SYSTEM
        if context:
            system += f"\n\nReference documents context:\n{context}"
        user = PromptManager.build_rubric_prompt(params)
        return self.generate(system, user)

    def generate_lms_structure(self, params: Dict[str, Any], context: str = "") -> str:
        """Generate LMS course structure."""
        from services.prompts import PromptManager

        system = PromptManager.LMS_STRUCTURE_SYSTEM
        if context:
            system += f"\n\nReference documents context:\n{context}"
        user = PromptManager.build_lms_prompt(params)
        return self.generate(system, user)
