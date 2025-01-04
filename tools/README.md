How to use text_to_html.py

How to use text_to_html-meeting_dates.py tool.py

What are additional files used for in html_code_data\meeting_dates
- html_start.txt is html_code used for the beginning of the new html page
- html_end.txt is html code used for the final part of the new html page
- news.html_page_replace is html_code used for the modifying of the news.html page

- text_to_convert.txt is text that will be modified to html code

text_to_html-meeting_dates.py code creates new news.year.month.day.html file. This is achieved in following way:
1) new empty .html file is created
2) html_start.txt is added to empty file created in 1)
3) text_to_convert.txt text is converted to html code and then added to the file created in 1)
4) html_end.txt is added in the end to the file created in 1)
5) .html file name is changed to news.xxxx.yy.zz where xxxx is current year, yy is current month and zz is current day
6) .html file is moved to ../page/news folder where the rest of our news .html files are
7) link to newly created .html file is added to news.html
8) link to newly created .html file is updated in index.html
9) we have new fully working .html file
