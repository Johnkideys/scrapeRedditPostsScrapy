# CSS SELECTORS
posts_divs = response.css('div.thing')

post_titles = response.css('a.title.may-blank::text').get()
dates_of_posts = response.css('p.tagline time::attr(datetime)').get()



next_page = response.css('span.next-button a::attr(href)').get()

