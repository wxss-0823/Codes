mymetatable = {}
mytable = setmetatable({key = "value"}, {__newindex = 
    function (t, k, v)
        rawset(mymetatable, k, v .. t.key)
    end
})

mytable.xxx = "yyy"
print(mymetatable.xxx, mytable.xxx)