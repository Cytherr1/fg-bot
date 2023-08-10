import scrapy


class valostats(scrapy.Spider):
    name = "valostats"
    allowed_domains = ["tracker.gg"]
    start_urls = ["https://tracker.gg/valorant/profile/riot/Dorali%C3%A7e%23UUR/overview"]

    def parse(self, response):
        data = response.css("div.numbers")
        KDRatio = data[1].css("span.value::text").extract_first()
        headshot = data[2].css("span.value::text").extract_first()
        winRate = data[3].css("span.value::text").extract_first()

        yield {
            "KDRatio": str(KDRatio),
            "headshot": str(headshot),
            "winRate": str(winRate),
        }