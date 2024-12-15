function dicFunc()
    n = n/nil
end

function errorhandler(error)
    print("ERROR: " .. error)
    print(debug.debug)
    print(debug.traceback())
end

status = xpcall(dicFunc, errorhandler)