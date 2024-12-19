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

mingw32-gcc -shared -o luasql/mysql.dll src/luasql.o src/ls_mysql.o -LD:/Users/MySQL/mysql-9.1.0-winx64/lib -lmysqlclient -LD:/Users/ProjectFiles/Codes/VSCode/Lua/lua -llua54 -lm

# 1. 转换 lua54.dll 为 liblua54.a
pexports D:/Users/ProjectFiles/Codes/VSCode/Lua/lua/lua54.dll > lua54.def dlltool -d lua54.def -l liblua54.a
move liblua54.a D:/Users/ProjectFiles/Codes/VSCode/Lua/lua/lib

# 2. 转换 libmysqlclient.dll 为 libmysqlclient.a
pexports D:/Users/MySQL/mysql-9.1.0-winx64/bin/libmysqlclient.dll > libmysqlclient.def
dlltool -d libmysqlclient.def -l libmysqlclient.a
move libmysqlclient.a D:/Users/MySQL/mysql-9.1.0-winx64/lib

# 3. 链接生成 luasql/mysql.dll
mingw32-gcc -shared -o luasql/mysql.dll src/luasql.o src/ls_mysql.o \
-LD:/Users/MySQL/mysql-9.1.0-winx64/lib -lmysqlclient \
-LD:/Users/ProjectFiles/Codes/VSCode/Lua/lua/lib -llua54 -lm