from selenium import webdriver

print("## 검색어를 입력하시오. ")
keyword = input()

# 드라이버 추출하기
driver = webdriver.Chrome()

# 검색 페이지 로딩 ( 3초 기다림 )
path = "https://search.naver.com/search.naver?query=" + keyword
driver.get(path)
print("## 페이지 로딩", path)

print("## 네이버책 가져오기")
sh_book_tops = driver.find_elements_by_class_name("sh_book_top")
for sh_book in sh_book_tops:
    sh_book_title = sh_book.find_element_by_tag_name('dl').find_element_by_tag_name('dt')
    print(" - ", sh_book_title.text)





