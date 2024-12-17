# directory of VC
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2022\Visual Studio Tools\VC

# install luasocket for test
luarocks --lua-version=5.4 --tree=D:/Users/ProjectFiles/Codes/VSCode/Lua/lua/luarocks install luasocket --verbose

# install luasql-mysql
luarocks --tree=D:/Users/ProjectFiles/Codes/VSCode/Lua/lua/luarocks install luasql-mysql MYSQL_INCDIR=D:/Users/MySQL/mysql-9.1.0-winx64/include MYSQL_LIBDIR=D:/Users/MySQL/mysql-9.1.0-winx64/lib --verbose

# manually compile rockspec to install luasql-mysql
luarocks --tree=D:/Users/ProjectFiles/Codes/VSCode/Lua/lua/luarocks install "D:\Program Files (x86)\Microsoft Edge\luasql-2.6.0\luasql-2.6.0\rockspec\luasql-mysql-2.6.0-1.rockspec" MYSQL_INCDIR=D:/Users/MySQL/mysql-9.1.0-winx64/include MYSQL_LIBDIR=D:/Users/MySQL/mysql-9.1.0-winx64/lib

# process luasql.o
mingw32-gcc -O2 -c -o src/luasql.o -ID:/Users/ProjectFiles/Codes/VSCode/Lua/lua/include src/luasql.c -ID:/Users/MySQL/mysql-9.1.0-winx64/include

# process ls_mysql.o
mingw32-gcc -O2 -c -o src/ls_mysql.o -ID:/Users/ProjectFiles/Codes/VSCode/Lua/lua/include src/ls_mysql.c -ID:/Users/MySQL/mysql-9.1.0-winx64/include

# link .o for dll
mingw32-gcc  -shared -o luasql/mysql.dll src/luasql.o src/ls_mysql.o -LD:/Users/MySQL/mysql-9.1.0-winx64/lib -lmysqlclient D:\Users\ProjectFiles\Codes\VSCode\Lua\lua\lua54.dll -lm