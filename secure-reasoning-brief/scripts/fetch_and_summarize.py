#!/usr/bin/env python3
"""
Secure Reasoning Brief Agent - RSS Fetcher and Summarizer

This script fetches articles from configured RSS feeds, filters them by relevant
keywords, and uses a local Ollama model to generate technical summaries and
lay explanations.
"""

import os
import sys
import json
import logging
import requests
import feedparser
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class OllamaClient:
    """Client for interacting with local Ollama API"""

    def __init__(self, endpoint: str, model: str):
        self.endpoint = endpoint
        self.model = model

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Send a prompt to Ollama and return the response"""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        if system_prompt:
            payload["system"] = system_prompt

        try:
            response = requests.post(self.endpoint, json=payload, timeout=120)
            response.raise_for_status()
            result = response.json()
            return result.get("response", "")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error calling Ollama API: {e}")
            return ""


class ArticleSummarizer:
    """Handles article summarization using Ollama"""

    def __init__(self, ollama_client: OllamaClient, max_words: int = 80):
        self.client = ollama_client
        self.max_words = max_words

    def summarize_article(self, title: str, content: str, link: str) -> Dict:
        """Generate technical summary and lay explanation for an article"""

        # System prompt for technical summary
        system_prompt = """You are an AI research analyst specializing in verifiable AI,
trustworthy AI, and AI governance. Provide concise, accurate technical summaries."""

        # Technical summary prompt
        tech_prompt = f"""Summarize this article in {self.max_words} words or less, focusing on
technical details and key findings:

Title: {title}
Content: {content[:1500]}

Provide only the summary, no preamble."""

        technical_summary = self.client.generate(tech_prompt, system_prompt)

        # Lay explanation prompt
        lay_prompt = f"""Based on this article, explain in 2-3 sentences what this means for
organizations adopting AI systems. Focus on practical implications, risks, or opportunities.

Title: {title}
Content: {content[:1500]}

Provide only the explanation, no preamble."""

        lay_explanation = self.client.generate(lay_prompt, system_prompt)

        # Tag extraction prompt
        tag_prompt = f"""Extract 3-5 relevant tags from this article. Choose from:
verifiable AI, trustworthy AI, AI governance, AI safety, interpretability, alignment,
responsible AI, AI policy, secure reasoning, formal verification, machine learning,
deep learning, neural networks, bias, fairness, transparency, accountability.

Title: {title}
Content: {content[:1000]}

Return only comma-separated tags, no explanation."""

        tags_raw = self.client.generate(tag_prompt, system_prompt)
        tags = [tag.strip() for tag in tags_raw.split(",") if tag.strip()]

        return {
            "title": title,
            "link": link,
            "technical_summary": technical_summary.strip(),
            "lay_explanation": lay_explanation.strip(),
            "tags": tags[:5]  # Limit to 5 tags
        }


class FeedFetcher:
    """Fetches and filters RSS feed articles"""

    def __init__(self, feeds_config: Dict, keywords: List[str], days_back: int = 7):
        self.feeds_config = feeds_config
        self.keywords = [kw.lower() for kw in keywords]
        self.days_back = days_back
        self.cutoff_date = datetime.now() - timedelta(days=days_back)

    def fetch_feeds(self) -> List[Dict]:
        """Fetch all enabled feeds and return filtered articles"""
        all_articles = []

        for feed in self.feeds_config.get("feeds", []):
            if not feed.get("enabled", True):
                logger.info(f"Skipping disabled feed: {feed['name']}")
                continue

            logger.info(f"Fetching feed: {feed['name']}")
            articles = self._fetch_single_feed(feed)
            all_articles.extend(articles)

        # Remove duplicates based on link
        unique_articles = {article["link"]: article for article in all_articles}
        filtered_articles = list(unique_articles.values())

        logger.info(f"Fetched {len(filtered_articles)} unique articles")
        return filtered_articles

    def _fetch_single_feed(self, feed: Dict) -> List[Dict]:
        """Fetch a single RSS feed"""
        articles = []

        try:
            parsed = feedparser.parse(feed["url"])

            for entry in parsed.entries:
                # Get article date
                published = entry.get("published_parsed") or entry.get("updated_parsed")
                if published:
                    pub_date = datetime(*published[:6])
                else:
                    pub_date = datetime.now()  # Default to now if no date

                # Check if article is recent enough
                if pub_date < self.cutoff_date:
                    continue

                # Extract content
                title = entry.get("title", "")
                summary = entry.get("summary", "")
                content = entry.get("content", [{}])[0].get("value", summary)
                link = entry.get("link", "")

                # Check if article matches keywords
                text_to_search = f"{title} {summary}".lower()
                if any(keyword in text_to_search for keyword in self.keywords):
                    articles.append({
                        "title": title,
                        "content": content,
                        "summary": summary,
                        "link": link,
                        "date": pub_date,
                        "source": feed["name"],
                        "category": feed.get("category", "general")
                    })

            logger.info(f"Found {len(articles)} relevant articles in {feed['name']}")

        except Exception as e:
            logger.error(f"Error fetching feed {feed['name']}: {e}")

        return articles


def main():
    """Main entry point"""
    # Load environment variables
    load_dotenv()

    # Get configuration
    script_dir = Path(__file__).parent.parent
    config_dir = script_dir / "config"

    # Load feeds configuration
    feeds_config_path = config_dir / "feeds.json"
    if not feeds_config_path.exists():
        logger.error(f"Feeds configuration not found: {feeds_config_path}")
        sys.exit(1)

    with open(feeds_config_path) as f:
        feeds_config = json.load(f)

    # Initialize Ollama client
    ollama_endpoint = os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434/api/generate")
    ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2")

    logger.info(f"Using Ollama endpoint: {ollama_endpoint}")
    logger.info(f"Using model: {ollama_model}")

    ollama_client = OllamaClient(ollama_endpoint, ollama_model)

    # Initialize components
    max_words = int(os.getenv("BRIEF_SUMMARY_MAX_WORDS", "80"))
    summarizer = ArticleSummarizer(ollama_client, max_words)

    keywords = feeds_config.get("keywords", [])
    fetcher = FeedFetcher(feeds_config, keywords)

    # Fetch articles
    logger.info("Fetching RSS feeds...")
    articles = fetcher.fetch_feeds()

    if not articles:
        logger.warning("No articles found matching criteria")
        return

    # Limit number of articles
    max_articles = int(os.getenv("BRIEF_MAX_ARTICLES", "20"))
    articles = sorted(articles, key=lambda x: x["date"], reverse=True)[:max_articles]

    # Summarize articles
    logger.info(f"Summarizing {len(articles)} articles...")
    summarized_articles = []

    for i, article in enumerate(articles, 1):
        logger.info(f"Processing article {i}/{len(articles)}: {article['title'][:60]}...")

        summary = summarizer.summarize_article(
            article["title"],
            article["content"] or article["summary"],
            article["link"]
        )

        summary.update({
            "date": article["date"].strftime("%Y-%m-%d"),
            "source": article["source"],
            "category": article["category"]
        })

        summarized_articles.append(summary)

    # Save results
    output_dir = script_dir / "content" / "briefs"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d")
    output_file = output_dir / f"{timestamp}_articles.json"

    with open(output_file, "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "articles": summarized_articles,
            "metadata": {
                "num_articles": len(summarized_articles),
                "date_range": f"{fetcher.cutoff_date.strftime('%Y-%m-%d')} to {datetime.now().strftime('%Y-%m-%d')}"
            }
        }, f, indent=2)

    logger.info(f"Saved results to {output_file}")
    logger.info(f"Successfully processed {len(summarized_articles)} articles")


if __name__ == "__main__":
    main()
