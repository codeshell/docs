import os
import re
import urllib.parse
import datetime
from pathlib import Path

# import mkdocs.structure.pages
from babel.dates import format_date
from dateutil import parser
from pydantic import BaseModel

def define_env(env):
    # Variables are accessible as {{ variables-key-name }} in templates
    env.variables["oe-version"] = "1.0"

    def get_last_part_URL(url):
        """Get the last part of an URL.

        Args:
            url (str): the URL

        Returns:
            str: the last part of the URL
        """
        if not url.endswith("/"):
            url = url + "/"
        head, tail = os.path.split(url)
        return "/" + tail if tail != "" else ""


    def regex_replace(s, find, replace):
        """A non-optimal implementation of a regex filter"""
        return re.sub(find, replace, s)


    def log(text):
        """Prints text to the console, in case you need to debug something.

        Using mainly in the template files.
        Parameters:
            text (str): The text to print.
        Returns:
            str: An empty string.
        """
        print(text)
        return ""


    def time_time(time):
        """Converts a time string to a human-readable format.

        Parameters:
            time (any): The time string to convert.
        Returns:
            str|datetime:  The converted time.
        """
        time = time.replace("-", "/")
        time = parser.parse(time).isoformat()
        try:
            time = datetime.datetime.fromisoformat(time)
            return datetime.datetime.strftime(time, "%d %B %Y")
        except AttributeError:
            return datetime.datetime.strftime(str(time), "%d %B %Y")
        except ValueError:
            print("value error!")
            return time


    def to_local_time(time, locale):
        """Convert to local time.

        Args:
            time (any): the time to convert
            locale (any): the locale to use

        Returns:
            str: the converted time
        """
        if isinstance(time, datetime.time) or isinstance(time, datetime.date):
            time = time.isoformat()
        date = time.replace("-", "/")
        date = parser.parse(date)
        return format_date(date, locale=locale)


    def time_todatetime(time):
        """convert time to datetime.

        Args:
            time (any): time to convert

        Returns:
            datetime: the converted time
        """
        return parser.parse(time)


    def time_to_iso(time):
        """Convert time to ISO format.

        Args:
            time (any): Time to convert

        Returns:
            any|str: convert time or the original time if error
        """
        if isinstance(time, datetime.time) or isinstance(time, datetime.date):
            time = time.isoformat()
        time = time.replace("-", "/")
        try:
            return parser.parse(time).isoformat()
        except AttributeError:
            return time


    def page_exists(page):
        """Check if a page exists.

        Args:
            page (any): The page to check

        Returns:
            bool: true if exists
        """
        return Path(page).exists()


    def url_decode(url):
        """decode an url in a template.

        Args:
            url (any): THE URL

        Returns:
            str : the decoded url
        """
        return urllib.parse.unquote(url)


    def value_in_frontmatter(key, metadata):
        """Check if a key exists in a dictionnary.

        Args:
            key (any): the key to check
            metadata (any): the dictionnary to check

        Returns:
            bool: true if exists
        """
        if key in metadata:
            return metadata[key]
        else:
            return None

    def get_attachments_config(config):
        DEFAULT_EXTENSION = [
        ".avif",
        ".bmp",
        ".gif",
        ".jpeg",
        ".jpg",
        ".png",
        ".svg",
        ".webp",
        ".flac",
        ".m4a",
        ".mp3",
        ".ogg",
        ".wav",
        ".webm",
        ".3gp",
        ".mkv",
        ".mov",
        ".mp4",
        ".ogv",
        ".webm",
        ".pdf",
        ]

        class Attachments(BaseModel):
            folder: str | Path | None = "assets/img/"
            exclude: list[str] = []
            extensions: list[str] = DEFAULT_EXTENSION

        attachment_extra = config.get("extra", {}).get("attachments", {})
        if not attachment_extra:
            attachment_extra = Attachments()
        if isinstance(attachment_extra, dict):
            attachment_extra = Attachments(**attachment_extra)
        else:
            attachment_extra = Attachments(folder=attachment_extra)
        return attachment_extra

    def get_attachments_folder(config):
        return re.sub(r"\/$", "", get_attachments_config(config).folder)

    def icon_exists(path, config):
        path = Path(config["docs_dir"]) / "_assets" / path
        return Path(path).exists()


    def replace_by_name(name: list[str] | str):
        if isinstance(name, list):
            return " ".join(name)
        return name


    def first(name: list[str] | str):
        if isinstance(name, list):
            return name[0]
        return name


    def links(name: list[str] | str):
        if isinstance(name, list):
            return "/".join(name)
        return name


    # def is_section(path):
    #     if isinstance(path, mkdocs.structure.pages.Page):
    #         return False
    #     return True
    @env.filter
    def iso_time(text):
        return "whatever"


    env.filter(my_filter, "custom_name")
    env.filter(time_time, "convert_time")
    env.filter(time_to_iso, "iso_time")
    env.filter(time_todatetime, "time_todatetime")
    env.filter(page_exists, "page_exists")
    env.filter(url_decode, "url_decode")
    env.filter(log, "log")
    env.filter(to_local_time, "to_local_time")
    env.filter(value_in_frontmatter, "value_in_frontmatter")
    env.filter(regex_replace, "regex_replace")
    env.filter(get_last_part_URL, "get_last_part_URL")
    env.macro(icon_exists, "icon_exists")
    # env.filter(is_section, "is_section")
    env.filter(replace_by_name, "replace_by_name")
    env.filter(first, "first")
    env.filter(links, "links")
    env.filter(get_attachments_folder, "get_attachments_folder")
