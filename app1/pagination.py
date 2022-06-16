from django.core.paginator import Paginator

List=['Aravind','Adarsh','Aslam','Anandhu']
Split=Paginator(List,2)
print(Split.count)
print(Split.num_pages)
page=(Split.page(1))
print(page.object_list)
page2=(Split.page(2))
print(page2.object_list)
print(page.has_next())
print(page2.has_next())
print(page2.has_previous())
print(page.next_page_number())
print(page2.previous_page_number())
print(page2.start_index())
print(page.start_index())
print(page2.end_index())
print(page.end_index())

