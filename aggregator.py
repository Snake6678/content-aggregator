import requests
from typing import List, Dict, Any

class ContentAggregator:
    """
    A class to fetch, process, and format content from various sources.
    Designed to be extensible for multiple content providers.
    """
    
    HACKER_NEWS_API_URL = "https://hacker-news.firebaseio.com/v0"

    def __init__(self, num_stories: int = 5, output_file: str = "README.md"):
        """
        Initializes the aggregator with configuration.

        Args:
            num_stories (int): The number of stories to fetch.
            output_file (str): The path to the file to be updated.
        """
        self.num_stories = num_stories
        self.output_file = output_file
        self.session = requests.Session()
        # Set a user-agent to be a good internet citizen
        self.session.headers.update({
            "User-Agent": "AutomatedContentAggregator/1.0"
        })

    def _fetch_json(self, url: str) -> Any:
        """Fetches JSON from a URL with error handling."""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching URL {url}: {e}")
            return None

    def fetch_hacker_news_stories(self) -> List[Dict[str, str]]:
        """
        Fetches the top stories from Hacker News.

        Returns:
            List[Dict[str, str]]: A list of story dictionaries.
        """
        print("Fetching Hacker News top story IDs...")
        top_stories_url = f"{self.HACKER_NEWS_API_URL}/topstories.json"
        story_ids = self._fetch_json(top_stories_url)

        if not story_ids:
            return []

        stories = []
        for story_id in story_ids[:self.num_stories]:
            item_url = f"{self.HACKER_NEWS_API_URL}/item/{story_id}.json"
            story_details = self._fetch_json(item_url)
            if story_details and 'title' in story_details and 'url' in story_details:
                stories.append({
                    "title": story_details['title'],
                    "url": story_details['url']
                })
        return stories

    def format_as_markdown(self, stories: List[Dict[str, str]]) -> str:
        """Formats a list of stories into a Markdown string."""
        if not stories:
            return "### 📰 Latest Hacker News Stories\n\nCould not fetch new stories at this time."

        markdown_lines = ["### 📰 Latest Hacker News Stories\n"]
        for story in stories:
            # Simple sanitization to prevent breaking markdown
            title = story['title'].replace('[', '(').replace(']', ')')
            markdown_lines.append(f"- [{title}]({story['url']})")
        
        return "\n".join(markdown_lines)

    def write_to_file(self, content: str) -> None:
        """Writes content to the configured output file."""
        print(f"Writing content to {self.output_file}...")
        try:
            with open(self.output_file, "w", encoding="utf-8") as f:
                f.write(content)
            print("File updated successfully.")
        except IOError as e:
            print(f"Error writing to file {self.output_file}: {e}")

    def run(self) -> None:
        """The main execution method for the aggregator."""
        stories = self.fetch_hacker_news_stories()
        markdown_content = self.format_as_markdown(stories)
        self.write_to_file(markdown_content)

if __name__ == "__main__":
    aggregator = ContentAggregator(num_stories=5, output_file="README.md")
    aggregator.run()
