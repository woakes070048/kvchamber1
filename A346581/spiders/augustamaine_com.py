from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Augustamaine(BasePortiaSpider):
    name = "www.augustamaine.com"
    allowed_domains = [u'www.augustamaine.com']
    start_urls = [
        u'https://www.augustamaine.com/index.php/2-uncategorised/88-members-by-category']
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
                deny=('.*')
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'#cb_tabid_24',
                [
                    Field(
                        u'Website',
                        '.cbFieldsContentsTab *::text',
                        []),
                    Field(
                        u'Business_Name',
                        '.cbFieldsContentsTab > div:nth-child(2) > .cb_field > div *::text',
                        []),
                    Field(
                        u'Street_Address',
                        '.cbFieldsContentsTab > div:nth-child(3) > .cb_field > div *::text',
                        []),
                    Field(
                        u'City',
                        '.cbFieldsContentsTab > div:nth-child(5) > .cb_field > div *::text',
                        []),
                    Field(
                        u'State',
                        '.cbFieldsContentsTab > div:nth-child(6) > .cb_field > div *::text',
                        []),
                    Field(
                        u'Zip',
                        '.cbFieldsContentsTab > div:nth-child(7) > .cb_field > div *::text',
                        []),
                    Field(
                        u'Email',
                        '.cbFieldsContentsTab > .cbft_emailaddress > .cb_field > div *::text',
                        []),
                    Field(
                        u'Phone',
                        '.cbFieldsContentsTab > div:nth-child(9) > .cb_field > div *::text',
                        [])])]]
