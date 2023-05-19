# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import mysql.connector

# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
#
#
# class ScrapingrecipesPipeline:
#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host = 'localhost',
#             user = 'root',
#             password = 'rV4a84kuoHXDPnW8RyHRDbK7',
#             database = 'lunch_recipes'
#         )

        # Create cursor, used to execute commands
        # self.cur = self.conn.cursor()

        # Create lunch_recipes table if none exists
        # self.cur.execute("""
        # CREATE TABLE IF NOT EXISTS lunch_recipes(
        #     id int NOT NULL auto_increment,
        #     link text,
        #     image text,
        #     title text,
        #     PRIMARY KEY (id)
        # )
        # """)

    # def process_item(self, item, spider):
        # Define insert statement
        # self.cur.execute("""insert into lunch_recipes (link, image, title) values (%s,%s,%s)""", (
        #     item["link"],
        #     item["image"],
        #     item["title"]
        # ))

        # Execute insert of data into database
        # self.conn.connect()

    # def close_spider(self, spider):

        # Close cursor & connection to database
        # self.cur.close()
        # self.conn.close()