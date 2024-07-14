from selenium.webdriver.common.by import By


header_order_feed_btn = (By.XPATH, './/p[text()="Лента Заказов"]')
order_feed_page_title = (By.XPATH, './/h1[@class="text text_type_main-large mt-10 mb-5"]')
order_feed_card = (By.XPATH, './/li[contains(@class, "OrderHistory_listItem")]')
modal_order_details_content = (By.XPATH, './/p[@class="text text_type_main-medium mb-8"]')
feed_order_number = (By.XPATH, './/p[@class="text text_type_digits-default"]')
new_order_number = (By.XPATH, './/h2[contains(@class, "Modal_modal__title__2L34m text text_type_digits-large mb-8")]')
orders_in_progress = (By.XPATH, './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[1]')
done_all_time_counter = (By.XPATH, './/p[text()="Выполнено за все время:"]/'
                                   'following-sibling::p[contains(@class, "OrderFeed_number")]')
done_today_counter = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/'
                                'following-sibling::p[contains(@class, "OrderFeed_number")]')
