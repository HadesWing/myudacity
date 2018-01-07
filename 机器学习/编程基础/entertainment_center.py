# -*- coding:utf8 -*-

import sys
import media
import fresh_tomatoes
import json

# 从json文件中获取影片相关信息
def getFavorateMovies(filename):
	fileMovie = open(filename);
	content = json.load(fileMovie);
	fileMovie.close();
	return content;

# 支持UTF-8中文编码
reload(sys);
sys.setdefaultencoding('utf8');

movies = [];
filename = r"myfavoratemovies";
favorateMovies = getFavorateMovies(filename);
for i in range(len(favorateMovies)):
	m = media.Movie(favorateMovies[i]["title"],favorateMovies[i]["sotryline"],favorateMovies[i]["poster_image_url"],favorateMovies[i]["trailer_url"]);
	movies.append(m);

fresh_tomatoes.open_movies_page(movies);
