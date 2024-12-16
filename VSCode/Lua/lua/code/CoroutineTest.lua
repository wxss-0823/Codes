function foo()
    print("Coroutine foo beginning!")
    local value = coroutine.yield("Resume coroutine.")
    print("Coroutine foo resume. The reception value is " .. tostring(value))
    print("Coroutine is over!")
end

-- Create Coroutine
local co = coroutine.create(foo)

-- Start Coroutine
local status, result = coroutine.resume(co)
print(status, result)

-- Resume Coroutine and deliver a value
local status, result = coroutine.resume(co, "test")
print(status, result)
