-- define rectangle class
Rectangle = {area = 0, length = 0, breadth = 0}

-- define build func
function Rectangle:new(r, l, b)
    r = r or {}
    setmetatable(r, self)
    self.__index = self
    r.length = l or 0
    r.breadth = b or 0
    r.area = r.length * r.breadth
    return r
end

-- print the area of rectangle
function Rectangle:printArea()
    print("The area of rectangle is: ".. self.area)
end

-- run obj
local rect = Rectangle:new(nil, 12, 23)
rect:printArea()
Rectangle:printArea()