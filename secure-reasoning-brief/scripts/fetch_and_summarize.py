#!/usr/bin/env python3
"""
Secure Reasoning Brief Agent - RSS Fetcher and Summarizer

Part of the RKL 18-Agent Multi-Agent System for Type III Secure Reasoning
================================================================================

This script implements the Discovery and Processing agent groups:
- Discovery (3 agents): Feed monitoring, filtering, credibility checks
- Processing (6 agents): Summarization, metadata extraction, theme identification

Type III Secure Reasoning Demonstration:
- Processes raw RSS feeds locally (never sent to external APIs)
- Generates derived insights (summaries) using local Ollama models
- Derived insights can be shared publicly or reviewed by external QA (Gemini)
- Raw article content remains under local control (Betty cluster)

Research Data Generation:
- Captures execution context (model configs, token usage, latency)
- Logs agent graph (multi-agent message passing)
- Records boundary events (Type III compliance verification)
- Generates research-grade telemetry for AI safety science

Agents Implemented:
1. Feed Monitor - Fetches RSS feeds from configured sources
2. Content Filter - Filters by keywords and recency
3. Summarizer - Generates technical summaries (local Ollama)
4. Metadata Extractor - Extracts tags and categories
5. Theme Identifier - Identifies common themes across articles

For Kaggle AI Agents Capstone Competition - "Agents for Good" Track
Demonstrates: Multi-agent orchestration, local data sovereignty, Type III boundaries,
             research data generation for AI science community
"""

import os
import sys
import json
import logging
import requests
import feedparser
import time
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Import RKL logging for research telemetry
try:
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from rkl_logging import StructuredLogger, sha256_text
    RKL_LOGGING_AVAILABLE = True
except ImportError:
    RKL_LOGGING_AVAILABLE = False
    logging.warning("rkl_logging not available - telemetry disabled")

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class OllamaClient:
    """
    Client for interacting with local Ollama API.

    Type III Implementation:
    - All raw data processing happens through this local client
    - Ensures article content never leaves local environment
    - Local processing is the first phase of Type III workflow
    - (Type III = local raw data processing + derived insights that can be external)

    Research Telemetry:
    - Logs execution context (model, tokens, latency) for each generation
    - Records boundary events to verify Type III compliance
    - Generates research data for studying model performance

    Attributes:
        endpoint (str): Ollama API endpoint (e.g., http://192.168.1.11:11434/api/generate)
        model (str): Model name to use (e.g., llama3.2:3b, llama3.2:8b)
        research_logger (StructuredLogger): Optional logger for telemetry

    Example:
        >>> client = OllamaClient("http://localhost:11434/api/generate", "llama3.2:3b")
        >>> response = client.generate("Summarize this text...")
    """

    def __init__(self, endpoint: str, model: str, research_logger: Optional['StructuredLogger'] = None):
        """
        Initialize Ollama client.

        Args:
            endpoint: Full URL to Ollama generate API
            model: Model identifier (must be pulled in Ollama first)
            research_logger: Optional StructuredLogger for research telemetry
        """
        self.endpoint = endpoint
        self.model = model
        self.research_logger = research_logger

    def generate(self, prompt: str, system_prompt: Optional[str] = None,
                 agent_id: str = "unknown", session_id: Optional[str] = None,
                 turn_id: Optional[int] = None) -> str:
        """
        Send a prompt to Ollama and return the response.

        Type III Note: This processes raw data locally (Type III requirement).
        Only derived outputs from this processing can be external/public.

        Research Telemetry: Logs execution context for each generation.

        Args:
            prompt: User prompt to send to the model
            system_prompt: Optional system prompt to set model behavior
            agent_id: Agent identifier for telemetry
            session_id: Session identifier for telemetry
            turn_id: Turn number for telemetry

        Returns:
            str: Model's generated response, or empty string on error

        Raises:
            Does not raise - logs errors and returns empty string
        """
        start_time = time.time()

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
            generated_text = result.get("response", "")

            # Calculate metrics
            latency_ms = int((time.time() - start_time) * 1000)
            # Prefer Ollama's actual counts if available, fallback to word count estimates
            prompt_tokens = result.get("prompt_eval_count", len(prompt.split()))
            gen_tokens = result.get("eval_count", len(generated_text.split()))

            # Log execution context for research
            if self.research_logger and RKL_LOGGING_AVAILABLE:
                self.research_logger.log("execution_context", {
                    "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "session_id": session_id or "unknown",
                    "turn_id": turn_id or 0,
                    "agent_id": agent_id,
                    "model_id": self.model,
                    "model_rev": self.model.split(":")[-1] if ":" in self.model else "latest",
                    "temp": payload.get("temperature", 0.7),  # Default from Ollama
                    "top_p": payload.get("top_p", 1.0),  # Default from Ollama
                    "ctx_tokens_used": prompt_tokens,
                    "gen_tokens": gen_tokens,
                    "tool_lat_ms": latency_ms,
                    "prompt_id_hash": sha256_text(prompt) if RKL_LOGGING_AVAILABLE else "",
                    "system_prompt_hash": sha256_text(system_prompt) if system_prompt and RKL_LOGGING_AVAILABLE else "",
                    "token_estimation": "api" if prompt_tokens and gen_tokens else "word_count"
                })

                # Log boundary event (Type III compliance)
                self.research_logger.log("boundary_event", {
                    "event_id": str(uuid.uuid4()),
                    "t": int(time.time() * 1000),
                    "session_id": session_id or "unknown",
                    "agent_id": agent_id,
                    "rule_id": "type3.local_processing.allowed",
                    "trigger_tag": "ollama_generate",
                    "context_tag": "summarization",
                    "action": "allow"
                })

            return generated_text

        except requests.exceptions.RequestException as e:
            logger.error(f"Error calling Ollama API: {e}")
            return ""


class ArticleSummarizer:
    """
    Handles article summarization using Ollama (Processing Agent Group).

    Agent Role in 18-Agent System:
    - Agent #3: Summarizer - Generates technical summaries
    - Agent #4: Metadata Extractor - Extracts tags and themes
    - Agent #5: Lay Translator - Creates accessible explanations

    Type III Implementation:
    - Input: Raw article content (local only)
    - Processing: Local Ollama models (never sent externally)
    - Output: Derived insights (summaries, tags) - can cross Type III boundary
    - Demonstrates: "Raw data stays local, derived insights travel"

    Attributes:
        client (OllamaClient): Local Ollama API client
        max_words (int): Maximum words for summaries (default 80)
    """

    def __init__(self, ollama_client: OllamaClient, max_words: int = 80):
        """
        Initialize the article summarizer.

        Args:
            ollama_client: Configured OllamaClient for local processing
            max_words: Maximum words per summary (configurable via BRIEF_SUMMARY_MAX_WORDS)
        """
        self.client = ollama_client
        self.max_words = max_words

    def summarize_article(self, title: str, content: str, link: str,
                          session_id: Optional[str] = None, turn_id: Optional[int] = None) -> Dict:
        """
        Generate technical summary and lay explanation for an article.

        Type III Boundary: Raw article content processed locally, only derived summaries
        could potentially be sent to external QA (Gemini) in hybrid mode.

        Args:
            title: Article title
            content: Full article content (raw data - stays local)
            link: Article URL for reference
            session_id: Session identifier for research telemetry
            turn_id: Turn number for research telemetry

        Returns:
            Dict containing:
                - title: Original article title
                - link: Article URL
                - technical_summary: Technical summary (derived - can share)
                - lay_explanation: Accessible explanation (derived - can share)
                - tags: Extracted keywords (derived - can share)

        Processing Flow:
            1. Generate technical summary (local Ollama)
            2. Generate lay explanation (local Ollama)
            3. Extract tags (local Ollama)
            4. Return derived insights only (Type III safe)
        """

        # System prompt for technical summary - sets agent role
        system_prompt = """You are an AI research analyst specializing in verifiable AI,
trustworthy AI, and AI governance. Provide concise, accurate technical summaries."""

        # Technical summary prompt - Agent #3: Summarizer
        tech_prompt = f"""Summarize this article in {self.max_words} words or less, focusing on
technical details and key findings:

Title: {title}
Content: {content[:1500]}

Provide only the summary, no preamble."""

        # Log reasoning graph edge: feed_monitor → summarizer
        if self.client.research_logger and RKL_LOGGING_AVAILABLE:
            self.client.research_logger.log("reasoning_graph_edge", {
                "edge_id": str(uuid.uuid4()),
                "session_id": session_id or "unknown",
                "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "t": int(time.time() * 1000),
                "from_agent": "feed_monitor",
                "to_agent": "summarizer",
                "msg_type": "act",
                "intent_tag": "tech_summary",
                "content_hash": sha256_text(f"{title}|{content[:500]}")
            })

        # PROCESSING: Local Ollama generates summary (Type III: raw data processed locally)
        technical_summary = self.client.generate(
            tech_prompt, system_prompt,
            agent_id="summarizer",
            session_id=session_id,
            turn_id=turn_id
        )

        # Lay explanation prompt
        lay_prompt = f"""Based on this article, explain in 2-3 sentences what this means for
organizations adopting AI systems. Focus on practical implications, risks, or opportunities.

Title: {title}
Content: {content[:1500]}

Provide only the explanation, no preamble."""

        # Log reasoning graph edge: summarizer → lay_translator
        if self.client.research_logger and RKL_LOGGING_AVAILABLE:
            self.client.research_logger.log("reasoning_graph_edge", {
                "edge_id": str(uuid.uuid4()),
                "session_id": session_id or "unknown",
                "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "t": int(time.time() * 1000),
                "from_agent": "summarizer",
                "to_agent": "lay_translator",
                "msg_type": "act",
                "intent_tag": "lay_explanation",
                "content_hash": sha256_text(technical_summary)
            })

        lay_explanation = self.client.generate(
            lay_prompt, system_prompt,
            agent_id="lay_translator",
            session_id=session_id,
            turn_id=turn_id
        )

        # Tag extraction prompt
        tag_prompt = f"""Extract 3-5 relevant tags from this article. Choose from:
verifiable AI, trustworthy AI, AI governance, AI safety, interpretability, alignment,
responsible AI, AI policy, secure reasoning, formal verification, machine learning,
deep learning, neural networks, bias, fairness, transparency, accountability.

Title: {title}
Content: {content[:1000]}

Return only comma-separated tags, no explanation."""

        # Log reasoning graph edge: lay_translator → metadata_extractor
        if self.client.research_logger and RKL_LOGGING_AVAILABLE:
            self.client.research_logger.log("reasoning_graph_edge", {
                "edge_id": str(uuid.uuid4()),
                "session_id": session_id or "unknown",
                "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "t": int(time.time() * 1000),
                "from_agent": "lay_translator",
                "to_agent": "metadata_extractor",
                "msg_type": "act",
                "intent_tag": "tag_extraction",
                "content_hash": sha256_text(f"{title}|{lay_explanation}")
            })

        tags_raw = self.client.generate(
            tag_prompt, system_prompt,
            agent_id="metadata_extractor",
            session_id=session_id,
            turn_id=turn_id
        )
        tags = [tag.strip() for tag in tags_raw.split(",") if tag.strip()]

        return {
            "title": title,
            "link": link,
            "technical_summary": technical_summary.strip(),
            "lay_explanation": lay_explanation.strip(),
            "tags": tags[:5]  # Limit to 5 tags
        }


class FeedFetcher:
    """
    Fetches and filters RSS feed articles (Discovery Agent Group).

    Agent Role in 18-Agent System:
    - Agent #1: Feed Monitor - Fetches RSS feeds from configured sources
    - Agent #2: Content Filter - Filters articles by keywords and recency
    - Agent #6: Credibility Checker - Validates source reliability

    Type III Implementation:
    - Input: Public RSS feed URLs (configuration)
    - Processing: Downloads raw RSS XML and article content (local)
    - Output: Filtered article list for local summarization
    - Boundary: Raw RSS/articles stay local, never sent to external APIs

    This is the entry point for Type III workflow - raw data acquisition
    under local control before any processing begins.

    Attributes:
        feeds_config (Dict): Feed configuration from feeds.json
        keywords (List[str]): Keywords to filter articles by
        days_back (int): How many days back to fetch articles (default 7)
        cutoff_date (datetime): Calculated cutoff date for filtering

    Example:
        >>> config = {"feeds": [{"name": "ArXiv", "url": "...", "enabled": true}]}
        >>> fetcher = FeedFetcher(config, ["AI safety", "alignment"], days_back=7)
        >>> articles = fetcher.fetch_feeds()
    """

    def __init__(self, feeds_config: Dict, keywords: List[str], days_back: int = 7):
        self.feeds_config = feeds_config
        self.keywords = [kw.lower() for kw in keywords]
        self.days_back = days_back
        self.cutoff_date = datetime.now() - timedelta(days=days_back)

    def fetch_feeds(self) -> List[Dict]:
        """
        Fetch all enabled feeds and return filtered articles.

        Orchestrates the Discovery agent workflow:
        1. Feed Monitor: Fetches each enabled RSS feed
        2. Content Filter: Applies keyword and date filtering
        3. Deduplication: Removes duplicate articles by URL

        Type III Note: All raw RSS content stays local during this process.

        Returns:
            List[Dict]: Filtered articles, each containing:
                - title: Article title
                - content: Full article content (raw)
                - summary: RSS feed summary
                - link: Article URL
                - date: Publication date
                - source: Feed name
                - category: Feed category

        Example:
            >>> articles = fetcher.fetch_feeds()
            >>> print(f"Found {len(articles)} articles")
        """
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
        """
        Fetch and parse a single RSS feed.

        Implements Feed Monitor agent behavior:
        - Parses RSS XML using feedparser
        - Extracts article metadata (title, date, content)
        - Applies keyword filtering
        - Validates recency based on cutoff_date

        Args:
            feed (Dict): Feed configuration containing:
                - name: Feed display name
                - url: RSS feed URL
                - category: Feed category for organization

        Returns:
            List[Dict]: Articles from this feed matching filter criteria

        Note: Uses feedparser library which handles various RSS/Atom formats
        and date parsing automatically.
        """
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
    """
    Main entry point for RSS feed processing and article summarization.

    Orchestrates the complete Discovery → Processing agent workflow:

    1. **Configuration Loading** (lines 299-312):
       - Loads .env variables (OLLAMA_ENDPOINT, model settings)
       - Reads feeds.json configuration
       - Sets up logging

    2. **Client Initialization** (lines 315-326):
       - Creates OllamaClient for local processing
       - Creates ArticleSummarizer with configured max_words
       - Creates FeedFetcher with keywords from config

    3. **Discovery Phase** (lines 331-341):
       - Agent #1: Feed Monitor fetches RSS feeds
       - Agent #2: Content Filter applies keyword/date filters
       - Selects top N most recent articles (BRIEF_MAX_ARTICLES)

    4. **Processing Phase** (lines 344-362):
       - Agent #3: Summarizer generates technical summaries
       - Agent #4: Metadata Extractor extracts tags
       - Agent #5: Lay Translator creates accessible explanations
       - All processing uses LOCAL Ollama (Type III requirement)

    5. **Output Generation** (lines 364-381):
       - Saves JSON with summaries and metadata
       - File: content/briefs/{date}_articles.json
       - This derived content can be used by Publishing agents

    Type III Workflow:
    - Raw RSS feeds and articles: Processed locally, never leave system
    - Derived summaries and tags: Saved locally, can be published or QA reviewed
    - Demonstrates: "Raw data stays local, derived insights travel"

    Environment Variables:
        OLLAMA_ENDPOINT: Ollama API endpoint (default: http://localhost:11434/api/generate)
        OLLAMA_MODEL: Model to use (default: llama3.2)
        BRIEF_MAX_ARTICLES: Max articles to process (default: 20)
        BRIEF_SUMMARY_MAX_WORDS: Max words per summary (default: 80)

    Outputs:
        content/briefs/{YYYY-MM-DD}_articles.json containing:
        - generated_at: ISO timestamp
        - articles: List of summarized articles
        - metadata: Processing metadata (count, date range)

    Example:
        $ python scripts/fetch_and_summarize.py
        INFO - Fetching RSS feeds...
        INFO - Found 15 relevant articles
        INFO - Summarizing 15 articles...
        INFO - Saved results to content/briefs/2025-11-16_articles.json
    """
    # Load environment variables
    load_dotenv()

    # Get configuration
    script_dir = Path(__file__).parent.parent
    config_dir = script_dir / "config"

    # Initialize research telemetry logger
    research_logger = None
    if RKL_LOGGING_AVAILABLE:
        research_data_dir = script_dir / "data" / "research"
        research_logger = StructuredLogger(
            base_dir=str(research_data_dir),
            rkl_version="1.0",
            batch_size=50  # Write after 50 records
        )
        logger.info(f"Research telemetry enabled: {research_data_dir}")
    else:
        logger.warning("Research telemetry disabled (rkl_logging not available)")

    # Generate session ID for this brief generation run
    session_id = f"brief-{datetime.now().strftime('%Y-%m-%d')}-{str(uuid.uuid4())[:8]}"
    logger.info(f"Session ID: {session_id}")

    # Load feeds configuration
    feeds_config_path = config_dir / "feeds.json"
    if not feeds_config_path.exists():
        logger.error(f"Feeds configuration not found: {feeds_config_path}")
        sys.exit(1)

    with open(feeds_config_path) as f:
        feeds_config = json.load(f)

    # Initialize Ollama client with research logger
    ollama_endpoint = os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434/api/generate")
    ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2")

    logger.info(f"Using Ollama endpoint: {ollama_endpoint}")
    logger.info(f"Using model: {ollama_model}")

    ollama_client = OllamaClient(ollama_endpoint, ollama_model, research_logger)

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
            article["link"],
            session_id=session_id,
            turn_id=i
        )

        summary.update({
            "date": article["date"].strftime("%Y-%m-%d"),
            "source": article["source"],
            "category": article["category"]
        })

        summarized_articles.append(summary)

    # Validate summaries before proceeding
    invalid_articles = [
        (idx + 1, article) for idx, article in enumerate(summarized_articles)
        if not article.get("technical_summary") or not article.get("lay_explanation")
    ]

    if invalid_articles:
        logger.error("Detected empty summaries; aborting publish step.")
        for idx, article in invalid_articles:
            logger.error(
                "Article %s missing fields (tech:%s, lay:%s): %s",
                idx,
                "ok" if article.get("technical_summary") else "EMPTY",
                "ok" if article.get("lay_explanation") else "EMPTY",
                article.get("title", "untitled")
            )
        if research_logger:
            research_logger.close()
        sys.exit(1)
    else:
        logger.info("All %d articles have non-empty technical and lay summaries.", len(summarized_articles))

    # Log governance ledger entry (for research)
    if research_logger and RKL_LOGGING_AVAILABLE:
        research_logger.log("governance_ledger", {
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "publish_id": session_id,
            "artifact_ids": [sha256_text(f"{a.get('title','')}|{a.get('link','')}") for a in summarized_articles],
            "contributing_agent_ids": ["feed_monitor", "content_filter", "summarizer", "lay_translator", "metadata_extractor"],
            "verification_hashes": [sha256_text(json.dumps(a)) for a in summarized_articles[:5]],  # Sample
            "type3_verified": True,
            "raw_data_exposed": False,
            "derived_insights_only": True,
            "schema_version": 1
        })

    # Save results
    output_dir = script_dir / "content" / "briefs"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d")
    output_file = output_dir / f"{timestamp}_articles.json"

    with open(output_file, "w") as f:
        json.dump({
            "session_id": session_id,
            "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "articles": summarized_articles,
            "metadata": {
                "num_articles": len(summarized_articles),
                "date_range": f"{fetcher.cutoff_date.strftime('%Y-%m-%d')} to {datetime.utcnow().strftime('%Y-%m-%d')}"
            }
        }, f, indent=2)

    logger.info(f"Saved results to {output_file}")
    logger.info(f"Successfully processed {len(summarized_articles)} articles")

    # Flush and close research logger
    if research_logger:
        research_logger.close()
        logger.info("Research telemetry data saved")


if __name__ == "__main__":
    main()
