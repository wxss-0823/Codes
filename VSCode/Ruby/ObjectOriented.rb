class Box
    attr_reader :name, :counter
    @@counter = 0
    def initialize()
        @name = "111"
        @@counter += 1
    end

    def getcounter
        @@counter  
    end
end

box1 = Box.new
# box1.name = "123"
puts box1.name
puts box1.getcounter

box2 = Box.allocate
puts box2.getcounter
