#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <cstdlib>
#include <windows.h>
#include <winbase.h>


const int INC = 20;
using namespace std;
class Date {   //Date类 ：日期类
public:
    int day;     //日
    int month;   //月
    int year;    //年
    Date(int d = 1, int m = 1, int y = 2012) {    //构造函数  默认初始日期2012.1.1
        //判断日期的合法性
        if (d > 0 && d < 32)day = d; else day = 1;
        if (m > 0 && m < 13)month = m; else m = 1;
        if (y > 0)year = y; else year = 2012;
    }
    void setDay(int d) { day = d; }       //设置日
    void setMonth(int m) { month = m; }   //设置月
    void setYear(int y) { year = y; }     //年
    int getDay() { return day; }         //获取年月日
    int getMonth() { return month; }
    int getYear() { return year; }
    void disp() { cout << year << "/" << month << "/" << day; }   //显示日期
    Date operator+(int dtmp);
    bool isLeapYear(int yy);              //判断是否为闰年
};
bool Date::isLeapYear(int yy) {          //判断是否为闰年
    if (yy % 400 == 0)
        return true;
    else if (yy % 100 != 0 && yy % 4 == 0)
        return true;
    else return false;
}

Date Date::operator+(int dtmp) {         //重载+运算符
    //bool Date::isLeapYear(int yy);
    int yy = year, mm = month, dd = day, mtmp, m2;     //年份yy   月份mm   日dd    借阅天数 dtmp
    bool flag;
    while (dtmp >= 0)
    {
        if (isLeapYear(yy))
        {
            dtmp -= 366;
            flag = true;
        }
        else
        {
            dtmp -= 365;
            flag = false;
        }
        yy++;
    }
    if (flag)
        dtmp += 366;
    else dtmp += 365;
    yy--;
    if (isLeapYear(yy))
    {
        m2 = 29;
    }
    else
    {
        m2 = 28;
    }
    mtmp = dtmp + dd;
    int m_day[] = { 0,31,m2,31,30,31,30,31,31,30,31,30,31 };   //每月天数
    for (; mtmp > m_day[mm];)
    {
        mtmp -= m_day[mm];
        if (mm == 12)
        {
            mm = 0;
            yy++;
        }
        mm++;
    }
    dd = mtmp;
    Date dt(yy, mm, dd);
    return dt;     //返回一个新日期
}
class Book {
    //书号、书名、作者、出版社、出版日期、出版定价、存馆数量
private:
    string num;   //s书号
    string title;   //标题
    string author;   //作者
    string publisher;   //出版社
    Date publishdate;   //Date类：出版日期
    float price;   //价格
    int howmany;    //存馆数量
public:
    Book(string num0 = "24416-5", string title0 = "数据结构", string author0 = "王红梅,胡明,王涛",
        string pub0 = "清华大学出版社", int bd = 1, int bm = 1, int by = 2012, float pr = 29.0, int ct = 10) :publishdate((bd, bm, by)) {
        num = num0; title = title0; author = author0; publisher = pub0; price = pr; howmany = ct;
    }
    void setNum(string num0) { num = num0; }      //设置书号
    void setTitle(string title0) { title = title0; }   //设置标题
    void setAuthor(string author0) { author = author0; }   //设置作者
    void setPublisher(string publisher0) { publisher = publisher0; }   //设置出版社
    void setPublishdate(int bd, int bm, int by) { Date d(bd, bm, by); publishdate = d; }    //设置出版日期，先构造在复制
    void setHowmany(int ct) { howmany = ct; }    //设置库存
    void setPrice(float pr) { price = pr; }   //设置价格
    string getNum() { return num; }        // 获取 书号 标题 作者 等信息
    string getTitle() { return title; }
    string getAuthor() { return author; }
    string getPublisher() { return publisher; }
    Date getPublishdate() { return publishdate; }
    int getHowmany() { return howmany; }
    float getPrice() { return price; }
    void dispABook() {
        cout << num << '\t' << title << '\t' << author << '\t' << publisher << '\t';       //获取Book信息  ：书号标题  作者 出版社  日期
        getPublishdate().disp();    //获取日期信息
        cout << '\t' << price << '\t' << howmany << '\n';
    }
    friend class InBook;               //友元类
    friend class ReaderBorrowBook;
};
class Reader {
    //学号、姓名、学院、专业班级  读者类
private:
    string num;    //学号
    string name;    //姓名
    string college;   //专业
    string classno;   //班级
public:
    Reader(string num0 = "20150000", string name0 = "NoName", string college0 = "信息学院", string clsn = "网络工程15-1") {
        num = num0; name = name0; college = college0; classno = clsn;
    }         //构造函数初始化信息
    void setNum(string num0) { num = num0; }            //功能函数 设置信息
    void setName(string name0) { name = name0; }
    void setCollege(string college0) { college = college0; }
    void setClassno(string clsn) { classno = clsn; }
    string getNum() { return num; }   //功能函数   获取信息
    string getName() { return name; }
    string getCollege() { return college; }
    string getClassno() { return classno; }
    void dispAReader() {                    //显示信息
        cout << num << "\t" << name << "\t" << college << "\t" << classno << "\n";
    }
    friend class Inreader;
    friend class ReaderBorrowBook;
};

class BorrowBook
{                   //借阅的书类
private:
    string num;                //学号、姓名、书号、书名、借阅日期、应还日期、归还日期
    string name;
    string booknum;
    string title;
    Date borrowdate;
    Date toreturndate;
    Date returndate;
    BorrowBook(string num0 = "20150000", string name0 = "NoName", string booknum0 = "24416-5",
        string title0 = "数据结构", int bd = 1, int bm = 1, int by = 2012, int td = 1, int tm = 5, int ty = 2012, int rd = 1, int rm = 3, int ry = 2012)
        :borrowdate(bd, bm, by), toreturndate(td, tm, ty), returndate(rd, rm, ry)
    {
        num = num0; name = name0; booknum = booknum0; title = title0;  //初始化
    }
    void setNum(string num0) { num = num0; }  //设置学号
    void setName(string name0) { name = name0; }//设置名字
    void setBookNum(string num0) { booknum = num0; }//设置书号
    void setTitle(string title0) { title = title0; }//书名
    void setBorrowdate(int bd, int bm, int by) { Date d(bd, bm, by); borrowdate = d; }//借阅日期
    void setToreturndate(int td, int tm, int ty) { Date d(td, tm, ty); toreturndate = d; }//
    void setReturndate(int rd, int rm, int ry) { Date d(rd, rm, ry); returndate = d; }//归还日期
    string getNum() { return num; }   //获取学号
    string getName() { return name; }//获取名字
    string getBookNum() { return booknum; }//书号
    string getTitle() { return title; }//书名
    Date getBorrowdate() { return borrowdate; }//得到日期
    Date getReturndate() { return returndate; }
    Date getToreturndate() { return toreturndate; }
    void dispBorrowBook()     //显示值
    {
        cout << num << "\t" << name << "\t" << booknum << "\t" << title << "\t";
        borrowdate.disp(); cout << "\t";
        toreturndate.disp(); cout << "\t";
        returndate.disp(); cout << "\n";
    }
    friend class InBorrowBook;
    friend class ReaderBorrowBook;

};
void string2date(string pdates, int d[])
{
    int k = 0, by, bm, bd;
    while ((pdates[k] < '0' || pdates[k]>'9') && k < pdates.length())k++;
    by = 0;
    for (; pdates[k] != '/' && k < pdates.length(); k++)
        by = by * 10 + pdates[k] - '0';
    k++; bm = 0;
    for (; pdates[k] != '/' && k < pdates.length(); k++)
        bm = bm * 10 + pdates[k] - '0';
    if (pdates[k] == '/') {
        k++; bd = 0;
        for (; k < pdates.length(); k++)
            bd = bd * 10 + pdates[k] - '0';
    }
    else bd = 1;
    d[0] = by; d[1] = bm; d[2] = bd;
}
class InBook
{
public:
    Book* book;    //book[n],很多本书
    int bookcount;     //记数
    void write2Bookfile()
    {
        string num, title, author, publisher, pdates;
        Date pdate;
        int i, bd, bm, by, ct;           //多余变量吧
        float price;
        ofstream outf(".\\book.txt", ios::out);
        //写入的文件名应该与读出的文件名相同；调试时可以取不同的文件名，以免覆盖掉原文件
        if (!outf)
        {
            cerr << "File could not be open." << endl;
        }
        outf << "图书信息\n";
        for (int i = 0; i < bookcount; i++)                 //写入图书信息
        {
            Date pd = book[i].getPublishdate();
            outf << book[i].getNum() << '\t' << book[i].getTitle() << '\t';
            outf << book[i].getAuthor() << '\t' << book[i].getPublisher() << '\t';
            outf << pd.getYear() << "/" << pd.getMonth() << "/" << pd.getDay();
            outf << '\t' << book[i].getPrice() << '\t' << book[i].getHowmany() << '\n';
        }
        outf.close();                 //关闭文件
    }
    int inbookFile(const char* fileName, int delLine)    //获取图书信息
    {
        cout << 1 << endl;
        string num, title, author, publisher, pdates;
        Date pdate;
        int i, bd, bm, by, ct;
        float price;
        ifstream inf(fileName, ios::in);
        if (!inf)
        {
            cerr << "File could not be open." << endl; return 1;
        }
        char s[80];
        for (i = 1; i <= delLine; i++)
            inf.getline(s, 80);
        i = 0;
        while (!inf.eof())//  { inf.getline( s, 80 ) ;    cout << s << endl ;  }
        {
            inf.getline(s, 80, '\t');//num=s;
            inf.getline(s, 80, '\t'); title = s;
            inf.getline(s, 80, '\t');//author=s;
            inf.getline(s, 80, '\t');//publisher=s;
            inf.getline(s, 80, '\t');//pdates=s;
            inf >> price >> ct;
            if (title.length() > 0)        i++;
        }
        bookcount = i;
        cout << bookcount << endl;
        inf.clear();
        inf.seekg(0, ios::beg);
        for (i = 1; i <= delLine; i++)
            inf.getline(s, 80);
        book = new Book[bookcount + INC];
        for (i = 0; i < bookcount; i++)
        {
            inf.getline(s, 80, '\t'); num = s;
            inf.getline(s, 80, '\t'); title = s;
            inf.getline(s, 80, '\t'); author = s;
            inf.getline(s, 80, '\t'); publisher = s;
            inf.getline(s, 80, '\t'); pdates = s;
            inf >> price >> ct;//inf,getchar();
            if (title.length() > 0) {
                int d[3];
                if (num[0] == 10)num = num.substr(1);
                string2date(pdates, d);
                by = d[0]; bm = d[1]; bd = d[2];
                book[i] = Book();
                book[i].setNum(num);
                book[i].setTitle(title);
                book[i].setAuthor(author);
                book[i].setPublisher(publisher);
                book[i].setPrice(price);
                book[i].setHowmany(ct);
                book[i].setPublishdate(bd, bm, by);
            }
        }
        inf.close();
        return bookcount;
    }
    friend class ReaderBorrowBook;
    int addbook(string num, string title, string author, string publisher, int bd, int bm, int by, float price, int ct)//添加图书信息
    {
        int i = bookcount;
        book[i] = Book();
        book[i].setNum(num);
        book[i].setTitle(title);
        book[i].setAuthor(author);
        book[i].setPublisher(publisher);
        book[i].setPrice(price);
        book[i].setHowmany(ct);
        book[i].setPublishdate(bd, bm, by);
        ++bookcount;
        return bookcount;
    }
    void searchbookbytitle(string title)         //按照书名查找
    {
        bool found = false;
        for (int i = 0; i < bookcount; i++)
            if ((book[i].getTitle()).find(title) != string::npos) {
                //cout<<book[i].getTitle()<< book[i].getTitle().find(title)<<endl;
                cout << i << "\t";
                book[i].dispABook();
                found = true;
                //return i;
            }
        if (!found)cout << "book title:" << title << " not found." << endl;
        //return -1;
    }
    int searchbookbytitlep(string title) {    //精确查找
        for (int i = 0; i < bookcount; i++)
            if (book[i].getTitle() == title) {
                //cout<<book[i].getTitle()<< book[i].getTitle().find(title)<<endl;
                cout << i << "\t";
                book[i].dispABook();
                return i;
            }
        cout << "book title:" << title << " not found." << endl;
        return -1;
    }
    void searchbookbyauthor(string author)    //按照作者查找
    {
        bool found = false;
        for (int i = 0; i < bookcount; i++)
            if ((book[i].getAuthor()).find(author) != string::npos) {
                //cout<<book[i].getTitle()<< book[i].getTitle().find(title)<<endl;
                cout << i << "\t";
                book[i].dispABook();
                found = true;
                //return i;
            }
        if (!found)cout << "book author:" << author << " not found." << endl;
        //return -1;
    }
    int searchbookbyauthorp(string author) //精确查找
    {
        for (int i = 0; i < bookcount; i++)
            if (book[i].getAuthor() == author) {
                //cout<<book[i].getTitle()<< book[i].getTitle().find(title)<<endl;
                cout << i << "\t";
                book[i].dispABook();
                return i;
            }
        cout << "book author:" << author << " not found." << endl;
        return -1;
    }
    void searchbookbypub(string pub)    //按照出版社查找
    {
        bool found = false;
        for (int i = 0; i < bookcount; i++)
            if ((book[i].getPublisher()).find(pub) != string::npos) {
                //cout<<book[i].getTitle()<< book[i].getTitle().find(title)<<endl;
                cout << i << "\t";
                book[i].dispABook();
                found = true;
                //return i;
            }
        if (!found)cout << "book publisher:" << pub << " not found." << endl;
        //return -1;
    }
    int searchbookbypubp(string pub)
    {
        for (int i = 0; i < bookcount; i++)
            if (book[i].getPublisher() == pub) {
                //cout<<book[i].getTitle()<< book[i].getTitle().find(title)<<endl;
                cout << i << "\t";
                book[i].dispABook();
                return i;
            }
        return -1;
    }
    void searchbookbynum(string num)
    {//模糊查找包含num的串
        bool found = false;
        for (int i = 0; i < bookcount; i++)
            if ((book[i].getNum()).find(num) != string::npos) {
                //cout<<book[i].getTitle()<< book[i].getTitle().find(title)<<endl;
                cout << i << "\t";
                book[i].dispABook();
                found = true;
                //         return i;
            }
        if (!found)cout << "book num:" << num << " not found." << endl;
        //         return -1;
    }
    int searchbookbynump(string num)
    {//精确查找等于num的串
        for (int i = 0; i < bookcount; i++)
            if ((book[i].getNum()) == num) {
                //cout<<book[i].getTitle()<< book[i].getTitle().find(title)<<endl;
                cout << i << "\t";
                book[i].dispABook();
                return i;
            }
        return -1;
    }
    void sortbookbynum()      //按照书号排序
    {
        for (int i = 0; i < bookcount; i++) {
            int k = i;
            for (int j = i + 1; j < bookcount; j++)
                if (book[j].getNum() < book[k].getNum()) k = j;
            //cout<<k<<" k&i "<<i<<" :"<<book[i].getNum()<<"---"<<book[k].getNum()<<endl;
            if (k != i) {
                Book t = book[i]; book[i] = book[k]; book[k] = t;
            }
        }
    }
    void sortbookbytitle()     //按照标题排序
    {
        for (int i = 0; i < bookcount; i++)
        {
            int k = i;
            for (int j = i + 1; j < bookcount; j++)
                if (book[j].getTitle() < book[k].getTitle()) k = j;
            if (k != i) {
                Book t = book[i]; book[i] = book[k]; book[k] = t;
            }
        }
    }
    void changebookbynum(string oldnum, string newnum)     //按书号改信息
    {
        int k = searchbookbynump(oldnum);
        if (k >= 0) {
            book[k].setNum(newnum);
            cout << "changebookbynum successed:" << endl;
            book[k].dispABook();
        }
        else cout << "changebook failed. No book of num=" << oldnum << endl;
    }
    void deletebookbynum(string num)     //按书号删除书目
    {
        int k = searchbookbynump(num);
        if (k >= 0) {
            cout << "Book to be deleted :" << endl;
            book[k].dispABook();
            book[k] = book[bookcount - 1];
            cout << "deletebookbynum successed:" << endl;
            bookcount--;
            //return bookcount;
        }
        else cout << "deletebook  failed. No book of num=" << num << endl;
    }

    void changebookbytitle(string oldtitle, string newtitle)
    {      //按标题修改书目
        int k = searchbookbytitlep(oldtitle);
        if (k >= 0) {
            book[k].setTitle(newtitle);

            cout << "changebookbytitle successed:" << endl;
            book[k].dispABook();
        }
        else cout << "changebook failed. No book of title=" << oldtitle << endl;
    }

    void deletebookbytitle(string title) {        //按书名删除书
        int k = searchbookbytitlep(title);
        if (k >= 0) {
            cout << "Book to be deleted :" << endl;
            book[k].dispABook();
            book[k] = book[bookcount - 1];
            cout << "deletebookbytitle successed:" << endl;
            bookcount--;
            //return bookcount;
        }
        else cout << "deletebook  failed. No book of title=" << title << endl;

    }
};
class InReader {
public:
    Reader* reader; int readercount;  //reader[n],读者总数
    void write2Readerfile()     //写入读者信息
    {
        string a1, b1, c1, d1;
        ofstream fout(".\\reader.txt", ios::out);
        if (!fout)
        {
            cerr << "File could not be open." << endl;
        }
        fout << "读者信息\n";
        for (int i = 0; i < readercount; i++)
            fout << reader[i].getNum() << '\t' << reader[i].getName() << '\t' << reader[i].getCollege() << '\t' << reader[i].getClassno() << endl;
        fout.close();


    }
    int inreaderFile(const char* fileName, int delLine)   //获取读者信息
    {
        cout << 1 << endl;
        string num, name, college, classno;
        int i;
        ifstream inf(fileName, ios::in);
        if (!inf)
        {
            cerr << "File could not be open." << endl; return 1;
        }
        char s[80];
        for (i = 1; i <= delLine; i++)
            inf.getline(s, 80);
        i = 0;
        while (!inf.eof())//  { inf.getline( s, 80 ) ;    cout << s << endl ;  }
        {
            inf.getline(s, 80, '\t');//num=s;
            inf.getline(s, 80, '\t'); name = s;
            inf.getline(s, 80, '\t');//college=s;
            inf.getline(s, 80);//classno=s;
            if (name.length() > 0)        i++;
        }
        readercount = i;
        cout << readercount << endl;
        inf.clear();
        inf.seekg(0, ios::beg);
        for (i = 1; i <= delLine; i++)
            inf.getline(s, 80);
        reader = new Reader[readercount + INC];
        for (i = 0; i < readercount; i++)
        {
            inf.getline(s, 80, '\t'); num = s;
            inf.getline(s, 80, '\t'); name = s;
            inf.getline(s, 80, '\t'); college = s;
            inf.getline(s, 80); classno = s;
            if (name.length() > 0) {
                if (num[0] == 10)num = num.substr(1);
                reader[i] = Reader();
                reader[i].setNum(num);
                reader[i].setName(name);
                reader[i].setCollege(college);
                reader[i].setClassno(classno);
            }
        }
        inf.close();
        return readercount;

    }
    int addreader(string num, string name, string college, string classno)   //添加读者
    {
        int i = readercount;
        reader[i] = Reader();
        reader[i].setNum(num);
        reader[i].setName(name);
        reader[i].setCollege(college);
        reader[i].setClassno(classno);

        ++readercount;
        return readercount;
    }
    void searchreaderbynum(string num) {       //按学号查询读者
        bool found = false;
        for (int i = 0; i < readercount; i++)
            if ((reader[i].getNum()).find(num) != string::npos) {
                cout << i << "\t";
                reader[i].dispAReader();
                found = true;
                //return i;
            }
        if (!found)cout << "reader of num: " << num << " not found" << endl;
        //return -1;
    }
    int searchreaderbynump(string num) {     //按学号精确查询读者
        for (int i = 0; i < readercount; i++)
            if (reader[i].getNum() == num) {
                cout << i << "\t";
                reader[i].dispAReader();
                return i;
            }
        return -1;
    }
    void searchreaderbyname(string nnname)     //按名字查询读者
    {
        for (int i = 0; i < readercount; i++)
            if (reader[i].getName() == nnname)
            {
                cout << i << "\t";
                reader[i].dispAReader();
                // return i;
            }
        // return -1;
    }
    int searchreaderbynamep(string nnname) {//模糊查找
        for (int i = 0; i < readercount; i++)
            if (reader[i].getName() == nnname) {
                cout << i << "\t";
                reader[i].dispAReader();
                return i;
            }
        return -1;
    }
    void searchreaderbyzybj(string zzy)   //按学院查找
    {
        for (int i = 0; i < readercount; i++)
            if (reader[i].getCollege() == zzy)
            {
                cout << i << "\t";
                reader[i].dispAReader();
                //  return i;
            }
        //  return -1;

    }
    int searchreaderbyzybjp(string zzy) {   //精确查找
        for (int i = 0; i < readercount; i++)
            if (reader[i].getCollege() == zzy) {
                cout << i << "\t";
                reader[i].dispAReader();
                return i;
            }
        return -1;
    }
    int searchreaderbyzybjjp(string bbj) {  //按专业班级查找
        for (int i = 0; i < readercount; i++)
            if (reader[i].getClassno() == bbj) {
                cout << i << "\t";
                reader[i].dispAReader();
                return i;
            }
        return -1;
    }
    void searchreaderbyzybjj(string bbj)   //模糊查找
    {
        for (int i = 0; i < readercount; i++)
            if (reader[i].getClassno() == bbj)
            {
                cout << i << "\t";
                reader[i].dispAReader();
                // return i;
            }
        // return -1;

    }
    void deletereaderbyxuehao(string xxhh) {        //按学号删除读者
        int k = searchreaderbynump(xxhh);
        if (k >= 0) {
            cout << "reader to be deleted :" << endl;
            reader[k].dispAReader();
            reader[k] = reader[readercount - 1];
            cout << "deletereaderbyxuehao successed:" << endl;
            readercount--;
            //return bookcount;
        }
        else cout << "deletereader  failed. No reader of xuehao=" << xxhh << endl;

    }
    void deletereaderbyxingming(string xxh1h) {        //按姓名删除读者
        int k = searchreaderbynamep(xxh1h);
        if (k >= 0) {
            cout << "reader to be deleted :" << endl;
            reader[k].dispAReader();
            reader[k] = reader[readercount - 1];
            cout << "deletereaderbyxingming successed:" << endl;
            readercount--;
            //return bookcount;
        }
        else cout << "deletereader  failed. No reader of xingming=" << xxh1h << endl;

    }
    void sortreaderbyxuahao()   //按学号排序
    {

        for (int i = 0; i < readercount; i++)
        {
            int k = i;
            for (int j = i + 1; j < readercount; j++)
                if (reader[j].getNum() < reader[k].getNum()) k = j;
            if (k != i) {
                Reader t = reader[i]; reader[i] = reader[k]; reader[k] = t;
            }
        }


    }
    void sortreaderbyxueyuan()   //按学院排序
    {

        for (int i = 0; i < readercount; i++)
        {
            int k = i;
            for (int j = i + 1; j < readercount; j++)
                if (reader[j].getCollege() < reader[k].getCollege()) k = j;
            if (k != i) {
                Reader t = reader[i]; reader[i] = reader[k]; reader[k] = t;
            }
        }


    }
    void changereaderbyxuehao(string old, string news)    //修改学号
    {
        int k = searchreaderbynump(old);
        if (k >= 0) {
            reader[k].setNum(news);
            cout << "changereaderbyxuehao successed:" << endl;
            reader[k].dispAReader();
        }
        else cout << "changereader failed. No reader of num=" << old << endl;
    }
    void changereaderbyxingming(string old, string news)   //修改姓名
    {
        int k = searchreaderbynamep(old);
        if (k >= 0) {
            reader[k].setName(news);
            cout << "changereaderbyxuehao successed:" << endl;
            reader[k].dispAReader();
        }
        else cout << "changereader failed. No reader of num=" << old << endl;
    }
    void changereaderbyxueyuan(string old, string news)   //修改学院
    {
        int k = searchreaderbyzybjp(old);
        if (k >= 0) {
            reader[k].setCollege(news);
            cout << "changereaderbyxuehao successed:" << endl;
            reader[k].dispAReader();
        }
        else cout << "changereader failed. No reader of num=" << old << endl;
    }

    void changereaderbyzybj(string old, string news)   //修改专业班级
    {
        int k = searchreaderbyzybjjp(old);
        if (k >= 0) {
            reader[k].setClassno(news);
            cout << "changereaderbyxuehao successed:" << endl;
            reader[k].dispAReader();
        }
        else cout << "changereader failed. No reader of num=" << old << endl;
    }
    friend class ReaderBorrowBook;
};
class InBorrowBook {
public:
    friend class ReaderBorrowBook;
    BorrowBook* borrowbook; int borrowbookcount;   //borrowbook[n],借书总数
    void searchborrowbookbyxuehao(string b)
    {
        for (int i = 0; i < borrowbookcount; i++)
            if (borrowbook[i].getNum() == b)
            {
                cout << i << "\t";
                borrowbook[i].dispBorrowBook();
                // return i;
            }
        // return -1;
    }
    void searchborrowbookbysm(string b)     //按书名查找借阅书
    {
        for (int i = 0; i < borrowbookcount; i++)
            if (borrowbook[i].getTitle() == b)
            {
                cout << i << "\t";
                borrowbook[i].dispBorrowBook();
                // return i;
            }
        // return -1;
    }

    void write2BorrowBookfile()   //写入借书文件
    {

        ofstream ffout(".\\borrowbook.txt", ios::out);
        if (!ffout)
        {
            cerr << "File could not be open." << endl;
        }
        ffout << "借阅信息\n";
        for (int i = 0; i < borrowbookcount; i++)
        {
            Date bbb = borrowbook[i].getBorrowdate();
            Date ddd = borrowbook[i].getToreturndate();
            Date ccc = borrowbook[i].getReturndate();
            ffout << borrowbook[i].getNum() << '\t' << borrowbook[i].getName() << '\t' << borrowbook[i].getBookNum() << '\t' << borrowbook[i].getTitle() << '\t' << bbb.getYear() << "/" << bbb.getMonth() << "/"
                << bbb.getDay() << '\t' << ddd.getYear() << "/" << ddd.getMonth() << "/" << ddd.getDay() << '\t' << ccc.getYear() << "/" << ccc.getMonth() << "/" << ccc.getDay() << endl;
        }



    }
    int inborrowbookFile(const char* fileName, int delLine)   //获取借阅图书信息
    {
        cout << 1 << endl;
        string num, name, booknum, title;
        string borrowdates;
        string toreturndates;
        string returndates;
        int i;
        ifstream inf(fileName, ios::in);
        if (!inf)
        {
            cerr << "File could not be open." << endl; return 1;
        }
        char s[80];
        for (i = 1; i <= delLine; i++)
            inf.getline(s, 80);
        i = 0;
        while (!inf.eof())
        {
            inf.getline(s, 80, '\t');
            inf.getline(s, 80, '\t');
            inf.getline(s, 80, '\t');
            inf.getline(s, 80);
            if (strlen(s) > 1)        i++;
        }
        borrowbookcount = i;
        cout << borrowbookcount << endl;
        inf.clear();
        inf.seekg(0, ios::beg);
        for (i = 1; i <= delLine; i++)
            inf.getline(s, 80);
        borrowbook = new BorrowBook[borrowbookcount + INC];
        for (i = 0; i < borrowbookcount; i++)
        {
            inf.getline(s, 80, '\t'); num = s;
            inf.getline(s, 80, '\t'); name = s;
            inf.getline(s, 80, '\t'); booknum = s;
            inf.getline(s, 80, '\t'); title = s;
            inf.getline(s, 80, '\t'); borrowdates = s;
            inf.getline(s, 80, '\t'); toreturndates = s;
            inf.getline(s, 80, '\n'); returndates = s;
            if (name.length() > 0) {
                if (num[0] == 10)num = num.substr(1);
                borrowbook[i] = BorrowBook();
                int d[3];
                string2date(borrowdates, d);
                int by = d[0], bm = d[1], bd = d[2];
                borrowbook[i].setBorrowdate(bd, bm, by);
                string2date(toreturndates, d);
                by = d[0]; bm = d[1]; bd = d[2];
                borrowbook[i].setToreturndate(bd, bm, by);
                string2date(returndates, d);
                by = d[0]; bm = d[1]; bd = d[2];
                borrowbook[i].setReturndate(bd, bm, by);
                borrowbook[i].setNum(num);
                borrowbook[i].setName(name);
                borrowbook[i].setBookNum(booknum);
                borrowbook[i].setTitle(title);
            }
        }
        inf.close();

        return borrowbookcount;
    }
    friend class ReaderBorrowBook;
    int searchbyreaderbook(string readernum, string booknum)     //按学号查询
    {
        for (int i = 0; i < borrowbookcount; i++)
            if ((borrowbook[i].getNum()) == readernum && (borrowbook[i].getBookNum()) == booknum) {
                cout << i << "\t";
                borrowbook[i].dispBorrowBook();
                return i;
            }
        return -1;

    }
};
class ReaderBorrowBook {

    InBook bk;   //声明三个类
    InReader rd;
    InBorrowBook bb;
public:
    void write2file() {
        bk.write2Bookfile();     //写入文件保存信息
        rd.write2Readerfile();
        bb.write2BorrowBookfile();

    }
    void init() {                                 //打开三个文件
        bk.inbookFile(".\\book.txt", 1);
        rd.inreaderFile(".\\reader.txt", 1);
        bb.inborrowbookFile(".\\borrowbook.txt", 1);
    }
    void dispBook() {                     //显示书信息
        for (int i = 0; i < bk.bookcount; i++)
        {
            cout << i << ":";
            bk.book[i].dispABook();
        }
    }
    void dispReader() {                    //显示读者信息
        for (int i = 0; i < rd.readercount; i++)
        {
            cout << i << ":"; rd.reader[i].dispAReader();
        }
    }
    void dispBorrowbook() {                   //借书信息查询
        for (int i = 0; i < bb.borrowbookcount; i++)
        {
            cout << i << ":"; bb.borrowbook[i].dispBorrowBook();
        }
    }
    void dispCount() {                         //总数显示
        cout << bk.bookcount << endl; cout << rd.readercount << endl; cout << bb.borrowbookcount << endl;
    }
    void addbook()    //添加书
    {

        string num, title, author, publisher;
        char num0[80], tit[80], auth[80], pub[80];
        int pd, pm, py, howmany;
        float price;
        Date publishdate;
        cout << "书号、书名、作者、出版社、出版日期(yyyy mm dd)、定价、存馆数量" << endl;

        string num1 = "24416-5", title0 = "数据结构", author0 = "王红梅,胡明,王涛", pub0 = "清华大学出版社";
        int pd0 = 1, pm0 = 1, py0 = 2012;
        float price0 = 29.0;
        int howmany0 = 10;
        //bookcount=
        cin >> num1 >> title0 >> author0 >> pub0 >> pd0 >> pm0 >> py0 >> price0 >> howmany0;

        bk.addbook(num1, title0, author0, pub0, pd0, pm0, py0, price0, howmany0);
        bk.write2Bookfile();
        int i = bk.bookcount - 1;
        cout << i << ":";
        bk.book[i].dispABook();
    }
    void addreader() {                         //添加读者
        string num, name, college, classno;
        char num0[80], nam[80], coll[80], clas[80];
        cout << "学号\t姓名\t学院\t专业班级:" << endl;

        string num1 = "20151000", name0 = "王涛", college0 = "computer", class0 = "network class 1";
        cin >> num1 >> name0 >> college0 >> class0;
        rd.addreader(num1, name0, college0, class0);
        rd.write2Readerfile();
        int i = rd.readercount - 1;
        cout << i << ":";
        rd.reader[i].dispAReader();
    }
    void searchBook() {                         //查书
        cout << "2．图书信息查询：分别按书名, 按作者名, 按出版社进行查询。" << endl;
        char tit[80];
        string title = "数据结构", author = "胡明", pub = "机械工业";
        int i, j, k, select;
        while (1) {
            cout << "图书信息查询：" << endl;
            cout << "1．按书名查询" << endl;
            cout << "2．按作者名查询" << endl;
            cout << "3．按出版社查询" << endl;
            cout << "0. return" << endl;
            cin >> select;
            cin.get();
            switch (select) {
            case 1:
                cout << "书名:";
                getline(cin, title, '\n');
                bk.searchbookbytitle(title);
                break;
            case 2:
                cout << "作者名:";
                getline(cin, author, '\n');
                bk.searchbookbyauthor(author);
                break;
            case 3:
                cout << "出版社:";
                getline(cin, pub, '\n');
                bk.searchbookbypub(pub); break;
            case 0:return;
            }
        }
    }
    void sortbook() {           //排序
        int select;
        cout << "3．图书信息排序：按书号、书名等按升序进行排序。" << endl;
        cout << "图书信息排序：" << endl;
        cout << "1．按书号排序" << endl;
        cout << "2．按书名排序" << endl;
        cout << "0. return" << endl;
        cin >> select;
        switch (select) {
        case 1:
            cout << "书号:";
            bk.sortbookbynum();
            dispBook();
            break;
        case 2:
            cout << "书名:";
            bk.sortbookbytitle();
            dispBook();
            break;
        case 0:return;
        }
    }
    void editbook() {                  //编辑书
        string oldtitle = "VisualBasic 程序设计教程", newtitle = "VisualBasic 程序设计教程-C", oldnum = "40667", newnum = "40667-C";
        int select;
        cout << "4．图书信息的修改、删除：按书号或书名进行图书的修改和删除。" << endl;
        while (1) {
            cout << "图书信息的修改、删除：" << endl;
            cout << "1．按书号修改" << endl;
            cout << "2．按书号删除" << endl;
            cout << "3．按书名修改" << endl;
            cout << "4．按书名删除" << endl;
            cout << "0. return" << endl;
            cin >> select;
            cin.get();
            switch (select) {
            case 1:
                cout << "old书号:";
                getline(cin, oldnum, '\n');
                cout << "new书号:";
                getline(cin, newnum, '\n');
                cout << "changebookbynum: " << oldnum << " to " << newnum << endl;
                bk.changebookbynum(oldnum, newnum);
                //dispBook();
                break;
            case 2:
                cout << "delete书号:";
                getline(cin, oldnum, '\n');
                cout << "delete书号:" << oldnum << endl;
                bk.deletebookbynum(oldnum);
                //dispBook();
                break;
            case 3:
                cout << "old书名:";
                getline(cin, oldtitle, '\n');
                cout << "new书名:";
                getline(cin, newtitle, '\n');
                cout << "changebookbytitle: " << oldtitle << " to " << newtitle << endl;
                bk.changebookbytitle(oldtitle, newtitle);
                //dispBook();
                break;
            case 4:
                cout << "delete书名:";
                getline(cin, oldtitle, '\n');
                cout << "deletebookbytitle: " << oldtitle << endl;
                bk.deletebookbytitle(oldtitle);
                //dispBook();
                break;
            case 0:
                bk.write2Bookfile();
                cout << "修改成功" << endl;
                return;
            }
        }
    }
    void readerborrowabook() {                       //借阅
        cout << "9．图书借阅：输入学号+书号，如果该书图书信息表中的存馆数量大于0，则可以借出，" << endl;
        string rdnum = "20061709", booknum = "33071", name, title;
        int select, rdpos, bookpos, y, m, d;
        while (1) {
            cout << "图书借阅：" << endl;
            cout << "1．借书" << endl;
            cout << "0．return" << endl;
            cin >> select;
            cin.get();
            if (select == 0)return;
            cout << "borrow学号:";
            getline(cin, rdnum, '\n');
            cout << "borrow书号:";
            getline(cin, booknum, '\n');
            bookpos = bk.searchbookbynump(booknum);
            rdpos = rd.searchreaderbynump(rdnum);
            if (bookpos > 0 && rdpos > 0) {
                int hm = bk.book[bookpos].getHowmany();
                if (hm > 0) {
                    name = rd.reader[rdpos].getName();
                    title = bk.book[bookpos].getTitle();
                    bk.book[bookpos].setHowmany(hm - 1); //修改图书信息表中的存馆数量
                    bb.borrowbook[bb.borrowbookcount].setNum(rdnum);
                    bb.borrowbook[bb.borrowbookcount].setBookNum(booknum);
                    bb.borrowbook[bb.borrowbookcount].setName(name);
                    bb.borrowbook[bb.borrowbookcount].setTitle(title);

                    SYSTEMTIME ct;
                    GetLocalTime(&ct);//取系统时间，如果用GetSystemTime(&ct);那么获取的是格林尼治标准时间
                    y = ct.wYear;
                    m = ct.wMonth;
                    d = ct.wDay;
                    Date toret = Date(d, m, y) + 60;
                    bb.borrowbook[bb.borrowbookcount].setBorrowdate(d, m, y);
                    bb.borrowbook[bb.borrowbookcount].setToreturndate(toret.getDay(), toret.getMonth(), toret.getYear());
                    bb.borrowbook[bb.borrowbookcount].setReturndate(1, 1, 1);
                    bb.borrowbookcount++;
                }
                else cout << booknum << " 存馆数量=0" << ". can't be borrowed. " << endl;
            }
            else {
                if (bookpos < 0)cout << "No book " << booknum << ". can't borrow!" << endl;
                if (rdpos < 0)cout << "No reader " << rdnum << ". can't borrow!" << endl;
            }
        }
    }
    void readerreturnabook() {   //归还
        cout << "10．图书归还：输入学号+书名，修改图书信息表中的存馆数量，图书借阅表中记录该同学的归还日期。" << endl;
        char tit[80];
        string rdnum = "20061709", booknum = "33071", name, title;
        int selectttt, rdpos, bookpos, y, m, d;
        while (1) {
            cout << "图书归还：" << endl;
            cout << "1．还书" << endl;
            cout << "0．return" << endl;
            cin >> selectttt;
            cin.get();
            if (selectttt == 0) { return; }
            cout << "return学号:" << endl;
            getline(cin, rdnum, '\n');

            cout << "return书号:";
            getline(cin, booknum, '\n');

            bookpos = bk.searchbookbynump(booknum);
            rdpos = rd.searchreaderbynump(rdnum);
            int k;
            k = bb.searchbyreaderbook(rdnum, booknum);
            if (k >= 0) {
                if (bookpos > 0 && rdpos > 0) {
                    bk.book[bookpos].setHowmany(bk.book[bookpos].getHowmany() + 1);
                    SYSTEMTIME ct;
                    GetLocalTime(&ct);//取系统时间
                    y = ct.wYear;
                    m = ct.wMonth;
                    d = ct.wDay;
                    bb.borrowbook[k].setReturndate(d, m, y);
                }

                else {
                    if (bookpos < 0)cout << "No book " << booknum << ". can't return!" << endl;
                    if (rdpos < 0)cout << "No reader " << rdnum << ". can't return!" << endl;
                }
            }
            else cout << "No borrowbook " << endl;
        }
    }

    void searchreader()
    {
        string xuehao, xingming, zzy, bbj;
        cout << "6.读者信息查询：分别按学号、姓名、班级等进行查询。" << endl;
        int selectt;
        while (1) {
            cout << "读者信息查询：" << endl;
            cout << "1．按学号查询" << endl;
            cout << "2．按姓名查询" << endl;
            cout << "3. 按学院查询" << endl;
            cout << "4. 按专业班级查询" << endl;
            cout << "0. return" << endl;
            cin >> selectt;
            cin.get();
            switch (selectt)
            {
            case 1: cout << "学号：" << endl;
                getline(cin, xuehao, '\n');
                cout << 1 << endl;
                rd.searchreaderbynum(xuehao);
                break;
            case 2:cout << "姓名：" << endl;
                getline(cin, xingming, '\n');
                rd.searchreaderbyname(xingming);
                break;
            case 3:cout << "学院： " << endl;
                getline(cin, zzy, '\n');
                rd.searchreaderbyzybj(zzy);
                break;
            case 4:cout << "专业班级： " << endl;
                getline(cin, bbj, '\n');
                rd.searchreaderbyzybjj(bbj);
                break;
            case 0: return;

            }
        }



    }

    void sortreader()
    {
        int selectt1;
        cout << "7：读者信息排序：按学号、学院等按升序进行排序。" << endl;
        cout << "读者信息排序：" << endl;
        cout << "1．按学号排序" << endl;
        cout << "2．按学院排序" << endl;
        cout << "0. return" << endl;
        cin >> selectt1;
        switch (selectt1) {
        case 1:
            cout << "学号:";
            rd.sortreaderbyxuahao();
            dispReader();
            break;
        case 2:
            cout << "学院:";
            rd.sortreaderbyxueyuan();
            dispReader();
            break;
        case 0:return;
        }
    }
    void editreader()
    {
        string xh, xm, xy, bj, newxh, newxm, newxy, newbj;

        int select2;
        cout << "8．学生信息的修改、删除：。" << endl;

        while (1) {
            cout << "学生信息的修改、删除：" << endl;
            cout << "1．按学号修改" << endl;
            cout << "2．按学号删除" << endl;
            cout << "3．按姓名修改" << endl;
            cout << "4．按姓名删除" << endl;
            cout << "0. return" << endl;
            cin >> select2;
            cin.get();
            switch (select2)
            {
            case 1:cout << "要修改学生的学号为：" << endl;
                cin >> xh;
                cout << "请输入新学号" << endl;
                cin >> newxh;
                rd.changereaderbyxuehao(xh, newxh);
                break;
            case 2:cout << "要删除的学生学号为：" << endl;
                cin >> xh;
                rd.deletereaderbyxuehao(xh);
                break;
            case 3:cout << "修改的学生姓名为：" << endl;
                cin >> xm;
                cout << "请输入修改后的姓名：" << endl;
                cin >> newxm;
                rd.changereaderbyxingming(xm, newxm);
                break;
            case 4:cout << "要删除的学生姓名为：" << endl;
                cin >> xm;
                rd.deletereaderbyxingming(xm);
                break;
            case 0: rd.write2Readerfile();
                cout << "修改成功";
                return;

            }

        }
    }
    void searchreaderborrowbook()
    {
        int bz;
        string xxh, ssm;
        while (1)
        {
            cout << "11．图书借阅查询：分别按学号、书名、学院等进行查询。" << endl;
            cout << "1.按学号查询" << endl;
            cout << "2.按书名查询" << endl;
            cout << "0.return" << endl;
            cin >> bz;
            switch (bz)
            {
            case 1:cout << "请输入学号" << endl;
                cin >> xxh;
                bb.searchborrowbookbyxuehao(xxh); break;
            case 2:cout << "请输入书名" << endl;
                cin >> ssm; bb.searchborrowbookbysm(ssm); break;
            case 0:
                return;

            }


        }
    }
};
int main() {
    ReaderBorrowBook rbb;
    rbb.init();
    rbb.dispBook();
    rbb.dispReader();
    rbb.dispBorrowbook();
    rbb.dispCount();
    int select;
    while (1) {
        cout << "菜单选择功能：" << endl;
        cout << "1．图书信息添加功能：包括书号、书名、作者、出版社名称、存馆数量、定价等" << endl;
        cout << "2．图书信息查询：分别按书名, 按作者名, 按出版单位等进行查询。" << endl;
        cout << "3．图书信息排序：按书号、书名等按升序进行排序。" << endl;
        cout << "4．图书信息的修改、删除：按书号或书名进行图书的修改和删除。" << endl;
        cout << "5．读者信息添加功能：包括学号、姓名、学院、专业班级等。" << endl;
        cout << "6．读者信息查询：分别按学号、姓名、班级等进行查询。" << endl;
        cout << "7．读者信息排序：按学号、学院等按升序进行排序。" << endl;
        cout << "8．读者信息的修改、删除：按学号+姓名进行读者信息的修改和删除。" << endl;
        cout << "9．图书借阅：输入学号+书号，如果该书图书信息表中的存馆数量大于0，则可以借出," << endl;
        cout << "借出相应数量后修改图书信息表中的存馆数量，在图书借阅表添加该同学的借阅。" << endl;
        cout << "10．图书归还：输入学号+书名，修改图书信息表中的存馆数量，在图书借阅表中记录该同学的归还时间。" << endl;
        cout << "11．图书借阅查询：分别按学号、书名、学院等进行查询。" << endl;
        cout << "0.  exit" << endl;
        cin >> select;
        switch (select) {
        case 1:rbb.addbook();    rbb.dispCount(); break;
        case 2:rbb.searchBook(); break;
        case 3:rbb.sortbook(); break;
        case 4:rbb.editbook(); break;
        case 5:rbb.addreader();    rbb.dispCount(); break;
        case 6:rbb.searchreader(); break;
        case 7:rbb.sortreader(); break;
        case 8:rbb.editreader(); break;
        case 9:rbb.readerborrowabook(); break;
        case 10:rbb.readerreturnabook(); break;
        case 11:rbb.searchreaderborrowbook(); break;
        case 0:rbb.write2file(); exit(0);
        }
    }
    return 0;
}
