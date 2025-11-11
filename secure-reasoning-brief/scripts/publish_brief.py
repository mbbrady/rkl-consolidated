#!/usr/bin/env python3
"""
Secure Reasoning Brief Agent - Publisher

This script takes the summarized articles JSON and generates a formatted
Hugo-compatible Markdown brief for the RKL website.
"""

import os
import sys
import json
import logging
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
from collections import Counter
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BriefGenerator:
    """Generates formatted Hugo-compatible markdown briefs from article JSON"""

    def __init__(self):
        pass

    def generate_brief(self, articles_data: Dict, date_str: str) -> str:
        """Generate a complete Hugo-compatible brief from articles JSON"""
        articles = articles_data.get("articles", [])
        metadata = articles_data.get("metadata", {})

        if not articles:
            logger.warning("No articles to generate brief from")
            return ""

        # Generate front matter
        front_matter = self._generate_front_matter(articles, date_str)

        # Generate executive summary
        exec_summary = self._generate_executive_summary(articles)

        # Generate article sections
        articles_md = self._generate_articles_section(articles)

        # Analyze themes
        themes_md = self._generate_themes_section(articles)

        # Generate recommendations
        recommendations_md = self._generate_recommendations_section(articles)

        # Generate footer
        footer = self._generate_footer(metadata)

        # Assemble the brief
        brief = f"""{front_matter}

## Executive Summary

{exec_summary}

---

## Featured Articles

{articles_md}

---

## Key Themes This Week

{themes_md}

---

## Recommended Actions for Organizations

{recommendations_md}

---

{footer}
"""
        return brief

    def _generate_front_matter(self, articles: List[Dict], date_str: str) -> str:
        """Generate Hugo front matter"""
        # Extract all unique tags
        all_tags = set()
        for article in articles:
            all_tags.update(article.get("tags", []))

        tags_yaml = "\n".join([f'  - "{tag}"' for tag in sorted(all_tags)])

        # Parse date
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            formatted_date = date_obj.strftime("%B %d, %Y")
        except:
            formatted_date = date_str

        front_matter = f"""---
title: "Secure Reasoning Brief - {formatted_date}"
date: {date_str}
draft: false
type: "briefs"
description: "Weekly digest of advances in verifiable AI, trustworthy AI, and AI governance"
tags:
{tags_yaml if tags_yaml else '  []'}
categories:
  - "Secure Reasoning"
  - "AI Safety"
  - "AI Governance"
---"""
        return front_matter

    def _generate_executive_summary(self, articles: List[Dict]) -> str:
        """Generate executive summary based on article count and themes"""
        num_articles = len(articles)

        # Get top categories
        category_counter = Counter()
        for article in articles:
            category_counter[article.get("category", "general")] += 1

        top_categories = category_counter.most_common(3)
        category_text = ", ".join([f"{cat} ({count})" for cat, count in top_categories])

        summary = f"""This week's brief covers **{num_articles} significant developments** in AI safety, verification, and governance.

**Content breakdown:** {category_text}

Key themes include advances in formal verification methods, new governance frameworks for AI deployment, and ongoing research in interpretability and alignment. Organizations should pay particular attention to developments in {top_categories[0][0] if top_categories else 'AI governance'} as these may inform near-term policy and implementation decisions."""

        return summary

    def _generate_articles_section(self, articles: List[Dict]) -> str:
        """Generate the articles section"""
        articles_md = []

        for article in articles:
            article_md = f"""### {article.get("title", "Untitled")}

**Source:** {article.get("source", "Unknown")} | **Date:** {article.get("date", "N/A")} | **Category:** {article.get("category", "general")}

**Technical Summary:**
{article.get("technical_summary", "No summary available.")}

**What This Means for Organizations:**
{article.get("lay_explanation", "No explanation available.")}

**Tags:** {", ".join(article.get("tags", []))}

**[Read More]({article.get("link", "#")})**

---"""
            articles_md.append(article_md)

        return "\n\n".join(articles_md)

    def _generate_themes_section(self, articles: List[Dict]) -> str:
        """Analyze and generate key themes section"""
        # Count tag occurrences
        tag_counter = Counter()
        category_counter = Counter()

        for article in articles:
            tags = article.get("tags", [])
            category = article.get("category", "general")

            tag_counter.update(tags)
            category_counter[category] += 1

        # Get top themes
        top_tags = tag_counter.most_common(5)
        top_categories = category_counter.most_common(3)

        themes_md = []

        if top_tags:
            themes_md.append("**Most Common Topics:**")
            for tag, count in top_tags:
                themes_md.append(f"- **{tag}** ({count} article{'s' if count > 1 else ''})")

        themes_md.append("")

        if top_categories:
            themes_md.append("**Content Distribution:**")
            for category, count in top_categories:
                themes_md.append(f"- {category.title()}: {count} article{'s' if count > 1 else ''}")

        return "\n".join(themes_md)

    def _generate_recommendations_section(self, articles: List[Dict]) -> str:
        """Generate recommendations based on article themes"""
        # Count categories
        category_counter = Counter()
        tag_counter = Counter()

        for article in articles:
            category_counter[article.get("category", "general")] += 1
            tag_counter.update(article.get("tags", []))

        recommendations = []

        # Security-focused recommendation
        if category_counter.get("security", 0) > 0:
            recommendations.append(
                "- **Review Security Practices:** Several security-related developments this week "
                "warrant review of current AI system security protocols and deployment practices."
            )

        # Research-focused recommendation
        if category_counter.get("research", 0) > 3:
            recommendations.append(
                "- **Track Research Trends:** High volume of research publications suggests "
                "rapidly evolving technical landscape in AI safety and verification. Consider "
                "establishing regular monitoring processes."
            )

        # Safety/alignment recommendation
        if "alignment" in tag_counter or "AI safety" in tag_counter:
            recommendations.append(
                "- **Update Safety Frameworks:** New safety and alignment research should inform "
                "updates to organizational AI governance frameworks and deployment guidelines."
            )

        # Governance recommendation
        if category_counter.get("policy", 0) > 0 or "governance" in tag_counter:
            recommendations.append(
                "- **Review Governance Policies:** Recent policy developments may require "
                "updates to organizational AI governance documentation and compliance procedures."
            )

        # Verification/interpretability recommendation
        if "verification" in tag_counter or "interpretability" in tag_counter:
            recommendations.append(
                "- **Evaluate Verification Tools:** Consider incorporating formal verification "
                "or interpretability methods into AI system development and audit processes."
            )

        # Industry developments
        if category_counter.get("industry", 0) > 0:
            recommendations.append(
                "- **Monitor Industry Practices:** Stay informed about how leading organizations "
                "are implementing trustworthy AI principles in production environments."
            )

        # Default recommendation if none generated
        if not recommendations:
            recommendations.append(
                "- **Continue Monitoring:** Maintain awareness of developments in verifiable and "
                "trustworthy AI practices through regular review of this brief."
            )

        return "\n".join(recommendations)

    def _generate_footer(self, metadata: Dict) -> str:
        """Generate footer with metadata"""
        footer = f"""## About This Brief

This brief was generated by the RKL Secure Reasoning Brief Agent using **Type I secure reasoning**—all analysis occurred locally on RKL infrastructure using open-source AI models (Llama 3.2/Mistral via Ollama).

**Sources monitored:** ArXiv (AI, Security), AI Alignment Forum, Google AI Blog, and other research feeds

**Date range:** {metadata.get("date_range", "N/A")}
**Articles processed:** {metadata.get("num_articles", "N/A")}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}

---

*For questions or to suggest additional sources, contact [info@resonantknowledgelab.org](mailto:info@resonantknowledgelab.org)*"""
        return footer


class GitHubPublisher:
    """Publishes briefs to GitHub repository"""

    def __init__(self, repo_path: Path):
        self.repo_path = repo_path

    def commit_and_push(self, file_path: Path, commit_message: str, auto_push: bool = False) -> bool:
        """Commit and optionally push a file to the repository"""
        try:
            # Check if we're in a git repository
            result = subprocess.run(
                ["git", "rev-parse", "--git-dir"],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                logger.error(f"Not a git repository: {self.repo_path}")
                return False

            # Add file
            subprocess.run(
                ["git", "add", str(file_path)],
                cwd=self.repo_path,
                check=True
            )

            # Commit
            subprocess.run(
                ["git", "commit", "-m", commit_message],
                cwd=self.repo_path,
                check=True
            )

            logger.info("Successfully committed changes")

            # Optionally push
            if auto_push:
                subprocess.run(
                    ["git", "push"],
                    cwd=self.repo_path,
                    check=True
                )
                logger.info("Successfully pushed to remote")

            return True

        except subprocess.CalledProcessError as e:
            logger.error(f"Git command failed: {e}")
            return False


def main():
    """Main entry point"""
    # Load environment variables
    load_dotenv()

    # Get configuration
    script_dir = Path(__file__).parent.parent
    content_dir = script_dir / "content" / "briefs"

    # Find latest articles JSON
    json_files = sorted(content_dir.glob("*_articles.json"), reverse=True)

    if not json_files:
        logger.error("No article JSON files found")
        sys.exit(1)

    latest_json = json_files[0]
    logger.info(f"Using article data from: {latest_json}")

    # Load articles data
    with open(latest_json) as f:
        articles_data = json.load(f)

    # Extract date from filename
    date_str = latest_json.stem.split("_")[0]  # e.g., "2025-11-11" from "2025-11-11_articles.json"

    # Generate brief
    logger.info("Generating Hugo-compatible brief...")
    generator = BriefGenerator()
    brief_content = generator.generate_brief(articles_data, date_str)

    if not brief_content:
        logger.error("Failed to generate brief")
        sys.exit(1)

    # Determine output path (Hugo website content directory)
    website_dir = script_dir.parent / "website"
    hugo_briefs_dir = website_dir / "content" / "briefs"
    hugo_briefs_dir.mkdir(parents=True, exist_ok=True)

    brief_filename = f"{date_str}-secure-reasoning-brief.md"
    brief_path = hugo_briefs_dir / brief_filename

    # Save brief
    with open(brief_path, "w") as f:
        f.write(brief_content)

    logger.info(f"Brief saved to: {brief_path}")

    # Optionally publish to GitHub
    publish_to_github = os.getenv("PUBLISH_TO_GITHUB", "false").lower() == "true"
    auto_push = os.getenv("AUTO_PUSH", "false").lower() == "true"

    if publish_to_github:
        logger.info("Committing to git repository...")
        publisher = GitHubPublisher(website_dir)

        commit_msg = f"Add Secure Reasoning Brief for {date_str}\n\nGenerated by RKL Brief Agent using Type I secure reasoning"
        success = publisher.commit_and_push(brief_path, commit_msg, auto_push)

        if success:
            logger.info("Successfully committed to git")
            if auto_push:
                logger.info("Changes pushed to remote - Netlify will auto-deploy")
            else:
                logger.info("Run 'git push' manually to deploy to Netlify")
        else:
            logger.warning("Failed to commit to git (brief still saved locally)")
    else:
        logger.info("GitHub publishing disabled (set PUBLISH_TO_GITHUB=true to enable)")

    logger.info("Done!")


if __name__ == "__main__":
    main()
