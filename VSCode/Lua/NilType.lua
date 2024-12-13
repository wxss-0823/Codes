tabl1 = { key1 = "value", key2 = "value2", "value3"}
for k, v in pairs(tabl1) do
    print(k .. " - " .. v)
end

-- Delete key1
tabl1.key1 = nil
for k, v in pairs(tabl1) do 
    print(k .. " - " .. v)
end