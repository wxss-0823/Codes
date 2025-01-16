require 'rexml/document'
include REXML

xmlfile = File.new("XMLTest.xml")
xmldoc = Document.new(xmlfile)

# 获取 root 元素
root = xmldoc.root
puts "Root element: " + root.attributes["shelf"]

# 输出电影标题
xmldoc.elements.each("collection/movie") do |movie_name|
    puts "Movie title: " + movie_name.attributes["title"]
end

# 输出所有电影类型
xmldoc.elements.each("collection/movie/type") {
  |e| puts "Movie type: " + e.text
}

# 输出 Trigun 的电影描述
xmldoc.elements.each("collection/movie"){
  |movie| if movie.attributes["title"] == "Trigun"
      movie.elements.each("description"){
        |t| puts "Movie description: " + t.text
      }
  end
}