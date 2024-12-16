function testFun(tab,fun)
    for k, v in pairs(tab) do 
        print(fun(k, v))
    end
end

tab = {key1 = "val1", key2 = "val2"}
testFun(tab, 
function(tab, val)
    return(tab .. " = " .. val)
end
)

function test(...)
    a = select(3, ...)
    print(a)
    print(select(3, ...))
end

test(0, 1, 2, 3, 4, 5)