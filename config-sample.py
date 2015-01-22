DEBUG = True

FLATPAGES_ROOT = 'contents' # Directory to store markdown files
FLATPAGES_AUTO_RELOAD = DEBUG # Useful for development purpose
FLATPAGES_EXTENSION = '.md' # Default extension for markdown file
FREEZER_DESTINATION_IGNORE = '.git*' # Will ignore .git directory under build/ instead of overwriting everytime you freeze

SITE = {
	'title': 'Your blog title', # Required
	'description': 'Your blog description', # Required
	'author': 'Your name', # Required
	'limit': 10, # Required
	'summary_offset': 180, # Optional
	'feed_limit': 15, # Optional
	'analytics': 'UA-XXX-VVV', # Optional
	'disqus': True, # Optional
	'github_domain': 'vivek.github.io', # Optional
	'github_repo': 'https://github.com/vividvilla/vividvilla.github.io.git' # Optional
}
