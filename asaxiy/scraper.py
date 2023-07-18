from bs4 import BeautifulSoup
import requests


class WebScraperTool:
    def search_keywords_to_url_format(self, words: str):
        searching_format_str = "+".join(words.split())
        compound_url = f"https://asaxiy.uz/uz/product?key={searching_format_str}"
        return compound_url

    def get_item_url(self, url: str):
        page_to_scrape = requests.get(url)
        soup = BeautifulSoup(page_to_scrape.content, "html.parser")
        url = soup.find("a", href=True, onclick="selectItemGtag()")
        if url:
            item_url = f"https://asaxiy.uz/uz/product/{url['href']}"
            return item_url
        return False

    def scrapping_web_page(self, url: str):
        page_to_scrape = requests.get(url)
        soup = BeautifulSoup(page_to_scrape.content, "html.parser")
        return self.compounding_data(soup, url)

    def compounding_data(self, soup_response, data_url: str):
        product_title = soup_response.find("h1", {"class": "product-title"})
        product_price = soup_response.find(
            "span", {"itemprop": "price", "class": "price-box_new-price"}
        )
        installment_product = soup_response.find("div", {"class": "installment__price"})
        is_product_available = soup_response.find(
            "span",
            {
                "class": "text__content-name",
                "style": "color:#34D374;font-size: 18px;font-weight: 600;",
            },
        )
        product_description = soup_response.find("div", {"class": "description__item"})
        product_image = (
            soup_response.find("div", {"class": "swiper-wrapper"})
            .find("img")
            .get("src")
            or "https://www.shopnbag.co.za/assets/img/default_product.jpg"
        )

        product_installment_price = (
            installment_product.text.strip() if installment_product else "Yo'q"
        )

        data = (
            f"<b>📝  Product nomi : </b>{product_title.text.strip()} \n"
            f"<b>💵  Narxi : </b>{product_price.text.strip()} \n"
            f"<b>🏧  Bo'lib tulash narxi : </b>{product_installment_price}\n"
            f"<b>📦  Holati : </b>{is_product_available.text.strip()}\n \n \n"
            f"<b>🧾  Tarif : </b>{product_description.text.strip()}\n"
        )

        return [product_image, data]
