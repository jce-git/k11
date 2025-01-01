How to use text_to_code.py tool

html_start.txt is the beginning of the html page

text_to_convert.txt is text that will be modified to html code (in case of text_to_html-meeting_dates it will be copied facebook post text)

html_end.txt is the final part of the html page

code creates new .html file that is done in following way:
1) new empty .html file is created
2) html_start is added to empty file created in 1) (it's located in html_code_data folder)
3) text_to_convert.txt text is converted to html code and then added to the file created in 1)
4) html_end is added to the file created in 1) (it's located in html_code_data folder)
5) .html file is moved to folder where the rest of our .html files are
6) we have new fully working .html file
