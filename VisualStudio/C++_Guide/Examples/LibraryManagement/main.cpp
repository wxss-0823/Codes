#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <cstdlib>
#include <windows.h>
#include <winbase.h>


const int INC = 20;
using namespace std;
class Date {   //Date�� ��������
public:
    int day;     //��
    int month;   //��
    int year;    //��
    Date(int d = 1, int m = 1, int y = 2012) {    //���캯��  Ĭ�ϳ�ʼ����2012.1.1
        //�ж����ڵĺϷ���
        if (d > 0 && d < 32)day = d; else day = 1;
        if (m > 0 && m < 13)month = m; else m = 1;
        if (y > 0)year = y; else year = 2012;
    }
    void setDay(int d) { day = d; }       //������
    void setMonth(int m) { month = m; }   //������
    void setYear(int y) { year = y; }     //��
    int getDay() { return day; }         //��ȡ������
    int getMonth() { return month; }
    int getYear() { return year; }
    void disp() { cout << year << "/" << month << "/" << day; }   //��ʾ����
    Date operator+(int dtmp);
    bool isLeapYear(int yy);              //�ж��Ƿ�Ϊ����
};
bool Date::isLeapYear(int yy) {          //�ж��Ƿ�Ϊ����
    if (yy % 400 == 0)
        return true;
    else if (yy % 100 != 0 && yy % 4 == 0)
        return true;
    else return false;
}

Date Date::operator+(int dtmp) {         //����+�����
    //bool Date::isLeapYear(int yy);
    int yy = year, mm = month, dd = day, mtmp, m2;     //���yy   �·�mm   ��dd    �������� dtmp
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
    int m_day[] = { 0,31,m2,31,30,31,30,31,31,30,31,30,31 };   //ÿ������
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
    return dt;     //����һ��������
}
class Book {
    //��š����������ߡ������硢�������ڡ����涨�ۡ��������
private:
    string num;   //s���
    string title;   //����
    string author;   //����
    string publisher;   //������
    Date publishdate;   //Date�ࣺ��������
    float price;   //�۸�
    int howmany;    //�������
public:
    Book(string num0 = "24416-5", string title0 = "���ݽṹ", string author0 = "����÷,����,����",
        string pub0 = "�廪��ѧ������", int bd = 1, int bm = 1, int by = 2012, float pr = 29.0, int ct = 10) :publishdate((bd, bm, by)) {
        num = num0; title = title0; author = author0; publisher = pub0; price = pr; howmany = ct;
    }
    void setNum(string num0) { num = num0; }      //�������
    void setTitle(string title0) { title = title0; }   //���ñ���
    void setAuthor(string author0) { author = author0; }   //��������
    void setPublisher(string publisher0) { publisher = publisher0; }   //���ó�����
    void setPublishdate(int bd, int bm, int by) { Date d(bd, bm, by); publishdate = d; }    //���ó������ڣ��ȹ����ڸ���
    void setHowmany(int ct) { howmany = ct; }    //���ÿ��
    void setPrice(float pr) { price = pr; }   //���ü۸�
    string getNum() { return num; }        // ��ȡ ��� ���� ���� ����Ϣ
    string getTitle() { return title; }
    string getAuthor() { return author; }
    string getPublisher() { return publisher; }
    Date getPublishdate() { return publishdate; }
    int getHowmany() { return howmany; }
    float getPrice() { return price; }
    void dispABook() {
        cout << num << '\t' << title << '\t' << author << '\t' << publisher << '\t';       //��ȡBook��Ϣ  ����ű���  ���� ������  ����
        getPublishdate().disp();    //��ȡ������Ϣ
        cout << '\t' << price << '\t' << howmany << '\n';
    }
    friend class InBook;               //��Ԫ��
    friend class ReaderBorrowBook;
};
class Reader {
    //ѧ�š�������ѧԺ��רҵ�༶  ������
private:
    string num;    //ѧ��
    string name;    //����
    string college;   //רҵ
    string classno;   //�༶
public:
    Reader(string num0 = "20150000", string name0 = "NoName", string college0 = "��ϢѧԺ", string clsn = "���繤��15-1") {
        num = num0; name = name0; college = college0; classno = clsn;
    }         //���캯����ʼ����Ϣ
    void setNum(string num0) { num = num0; }            //���ܺ��� ������Ϣ
    void setName(string name0) { name = name0; }
    void setCollege(string college0) { college = college0; }
    void setClassno(string clsn) { classno = clsn; }
    string getNum() { return num; }   //���ܺ���   ��ȡ��Ϣ
    string getName() { return name; }
    string getCollege() { return college; }
    string getClassno() { return classno; }
    void dispAReader() {                    //��ʾ��Ϣ
        cout << num << "\t" << name << "\t" << college << "\t" << classno << "\n";
    }
    friend class Inreader;
    friend class ReaderBorrowBook;
};

class BorrowBook
{                   //���ĵ�����
private:
    string num;                //ѧ�š���������š��������������ڡ�Ӧ�����ڡ��黹����
    string name;
    string booknum;
    string title;
    Date borrowdate;
    Date toreturndate;
    Date returndate;
    BorrowBook(string num0 = "20150000", string name0 = "NoName", string booknum0 = "24416-5",
        string title0 = "���ݽṹ", int bd = 1, int bm = 1, int by = 2012, int td = 1, int tm = 5, int ty = 2012, int rd = 1, int rm = 3, int ry = 2012)
        :borrowdate(bd, bm, by), toreturndate(td, tm, ty), returndate(rd, rm, ry)
    {
        num = num0; name = name0; booknum = booknum0; title = title0;  //��ʼ��
    }
    void setNum(string num0) { num = num0; }  //����ѧ��
    void setName(string name0) { name = name0; }//��������
    void setBookNum(string num0) { booknum = num0; }//�������
    void setTitle(string title0) { title = title0; }//����
    void setBorrowdate(int bd, int bm, int by) { Date d(bd, bm, by); borrowdate = d; }//��������
    void setToreturndate(int td, int tm, int ty) { Date d(td, tm, ty); toreturndate = d; }//
    void setReturndate(int rd, int rm, int ry) { Date d(rd, rm, ry); returndate = d; }//�黹����
    string getNum() { return num; }   //��ȡѧ��
    string getName() { return name; }//��ȡ����
    string getBookNum() { return booknum; }//���
    string getTitle() { return title; }//����
    Date getBorrowdate() { return borrowdate; }//�õ�����
    Date getReturndate() { return returndate; }
    Date getToreturndate() { return toreturndate; }
    void dispBorrowBook()     //��ʾֵ
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
    Book* book;    //book[n],�ܶ౾��
    int bookcount;     //����
    void write2Bookfile()
    {
        string num, title, author, publisher, pdates;
        Date pdate;
        int i, bd, bm, by, ct;           //���������
        float price;
        ofstream outf(".\\book.txt", ios::out);
        //д����ļ���Ӧ����������ļ�����ͬ������ʱ����ȡ��ͬ���ļ��������⸲�ǵ�ԭ�ļ�
        if (!outf)
        {
            cerr << "File could not be open." << endl;
        }
        outf << "ͼ����Ϣ\n";
        for (int i = 0; i < bookcount; i++)                 //д��ͼ����Ϣ
        {
            Date pd = book[i].getPublishdate();
            outf << book[i].getNum() << '\t' << book[i].getTitle() << '\t';
            outf << book[i].getAuthor() << '\t' << book[i].getPublisher() << '\t';
            outf << pd.getYear() << "/" << pd.getMonth() << "/" << pd.getDay();
            outf << '\t' << book[i].getPrice() << '\t' << book[i].getHowmany() << '\n';
        }
        outf.close();                 //�ر��ļ�
    }
    int inbookFile(const char* fileName, int delLine)    //��ȡͼ����Ϣ
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
    int addbook(string num, string title, string author, string publisher, int bd, int bm, int by, float price, int ct)//���ͼ����Ϣ
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
    void searchbookbytitle(string title)         //������������
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
    int searchbookbytitlep(string title) {    //��ȷ����
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
    void searchbookbyauthor(string author)    //�������߲���
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
    int searchbookbyauthorp(string author) //��ȷ����
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
    void searchbookbypub(string pub)    //���ճ��������
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
    {//ģ�����Ұ���num�Ĵ�
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
    {//��ȷ���ҵ���num�Ĵ�
        for (int i = 0; i < bookcount; i++)
            if ((book[i].getNum()) == num) {
                //cout<<book[i].getTitle()<< book[i].getTitle().find(title)<<endl;
                cout << i << "\t";
                book[i].dispABook();
                return i;
            }
        return -1;
    }
    void sortbookbynum()      //�����������
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
    void sortbookbytitle()     //���ձ�������
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
    void changebookbynum(string oldnum, string newnum)     //����Ÿ���Ϣ
    {
        int k = searchbookbynump(oldnum);
        if (k >= 0) {
            book[k].setNum(newnum);
            cout << "changebookbynum successed:" << endl;
            book[k].dispABook();
        }
        else cout << "changebook failed. No book of num=" << oldnum << endl;
    }
    void deletebookbynum(string num)     //�����ɾ����Ŀ
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
    {      //�������޸���Ŀ
        int k = searchbookbytitlep(oldtitle);
        if (k >= 0) {
            book[k].setTitle(newtitle);

            cout << "changebookbytitle successed:" << endl;
            book[k].dispABook();
        }
        else cout << "changebook failed. No book of title=" << oldtitle << endl;
    }

    void deletebookbytitle(string title) {        //������ɾ����
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
    Reader* reader; int readercount;  //reader[n],��������
    void write2Readerfile()     //д�������Ϣ
    {
        string a1, b1, c1, d1;
        ofstream fout(".\\reader.txt", ios::out);
        if (!fout)
        {
            cerr << "File could not be open." << endl;
        }
        fout << "������Ϣ\n";
        for (int i = 0; i < readercount; i++)
            fout << reader[i].getNum() << '\t' << reader[i].getName() << '\t' << reader[i].getCollege() << '\t' << reader[i].getClassno() << endl;
        fout.close();


    }
    int inreaderFile(const char* fileName, int delLine)   //��ȡ������Ϣ
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
    int addreader(string num, string name, string college, string classno)   //��Ӷ���
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
    void searchreaderbynum(string num) {       //��ѧ�Ų�ѯ����
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
    int searchreaderbynump(string num) {     //��ѧ�ž�ȷ��ѯ����
        for (int i = 0; i < readercount; i++)
            if (reader[i].getNum() == num) {
                cout << i << "\t";
                reader[i].dispAReader();
                return i;
            }
        return -1;
    }
    void searchreaderbyname(string nnname)     //�����ֲ�ѯ����
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
    int searchreaderbynamep(string nnname) {//ģ������
        for (int i = 0; i < readercount; i++)
            if (reader[i].getName() == nnname) {
                cout << i << "\t";
                reader[i].dispAReader();
                return i;
            }
        return -1;
    }
    void searchreaderbyzybj(string zzy)   //��ѧԺ����
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
    int searchreaderbyzybjp(string zzy) {   //��ȷ����
        for (int i = 0; i < readercount; i++)
            if (reader[i].getCollege() == zzy) {
                cout << i << "\t";
                reader[i].dispAReader();
                return i;
            }
        return -1;
    }
    int searchreaderbyzybjjp(string bbj) {  //��רҵ�༶����
        for (int i = 0; i < readercount; i++)
            if (reader[i].getClassno() == bbj) {
                cout << i << "\t";
                reader[i].dispAReader();
                return i;
            }
        return -1;
    }
    void searchreaderbyzybjj(string bbj)   //ģ������
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
    void deletereaderbyxuehao(string xxhh) {        //��ѧ��ɾ������
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
    void deletereaderbyxingming(string xxh1h) {        //������ɾ������
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
    void sortreaderbyxuahao()   //��ѧ������
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
    void sortreaderbyxueyuan()   //��ѧԺ����
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
    void changereaderbyxuehao(string old, string news)    //�޸�ѧ��
    {
        int k = searchreaderbynump(old);
        if (k >= 0) {
            reader[k].setNum(news);
            cout << "changereaderbyxuehao successed:" << endl;
            reader[k].dispAReader();
        }
        else cout << "changereader failed. No reader of num=" << old << endl;
    }
    void changereaderbyxingming(string old, string news)   //�޸�����
    {
        int k = searchreaderbynamep(old);
        if (k >= 0) {
            reader[k].setName(news);
            cout << "changereaderbyxuehao successed:" << endl;
            reader[k].dispAReader();
        }
        else cout << "changereader failed. No reader of num=" << old << endl;
    }
    void changereaderbyxueyuan(string old, string news)   //�޸�ѧԺ
    {
        int k = searchreaderbyzybjp(old);
        if (k >= 0) {
            reader[k].setCollege(news);
            cout << "changereaderbyxuehao successed:" << endl;
            reader[k].dispAReader();
        }
        else cout << "changereader failed. No reader of num=" << old << endl;
    }

    void changereaderbyzybj(string old, string news)   //�޸�רҵ�༶
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
    BorrowBook* borrowbook; int borrowbookcount;   //borrowbook[n],��������
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
    void searchborrowbookbysm(string b)     //���������ҽ�����
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

    void write2BorrowBookfile()   //д������ļ�
    {

        ofstream ffout(".\\borrowbook.txt", ios::out);
        if (!ffout)
        {
            cerr << "File could not be open." << endl;
        }
        ffout << "������Ϣ\n";
        for (int i = 0; i < borrowbookcount; i++)
        {
            Date bbb = borrowbook[i].getBorrowdate();
            Date ddd = borrowbook[i].getToreturndate();
            Date ccc = borrowbook[i].getReturndate();
            ffout << borrowbook[i].getNum() << '\t' << borrowbook[i].getName() << '\t' << borrowbook[i].getBookNum() << '\t' << borrowbook[i].getTitle() << '\t' << bbb.getYear() << "/" << bbb.getMonth() << "/"
                << bbb.getDay() << '\t' << ddd.getYear() << "/" << ddd.getMonth() << "/" << ddd.getDay() << '\t' << ccc.getYear() << "/" << ccc.getMonth() << "/" << ccc.getDay() << endl;
        }



    }
    int inborrowbookFile(const char* fileName, int delLine)   //��ȡ����ͼ����Ϣ
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
    int searchbyreaderbook(string readernum, string booknum)     //��ѧ�Ų�ѯ
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

    InBook bk;   //����������
    InReader rd;
    InBorrowBook bb;
public:
    void write2file() {
        bk.write2Bookfile();     //д���ļ�������Ϣ
        rd.write2Readerfile();
        bb.write2BorrowBookfile();

    }
    void init() {                                 //�������ļ�
        bk.inbookFile(".\\book.txt", 1);
        rd.inreaderFile(".\\reader.txt", 1);
        bb.inborrowbookFile(".\\borrowbook.txt", 1);
    }
    void dispBook() {                     //��ʾ����Ϣ
        for (int i = 0; i < bk.bookcount; i++)
        {
            cout << i << ":";
            bk.book[i].dispABook();
        }
    }
    void dispReader() {                    //��ʾ������Ϣ
        for (int i = 0; i < rd.readercount; i++)
        {
            cout << i << ":"; rd.reader[i].dispAReader();
        }
    }
    void dispBorrowbook() {                   //������Ϣ��ѯ
        for (int i = 0; i < bb.borrowbookcount; i++)
        {
            cout << i << ":"; bb.borrowbook[i].dispBorrowBook();
        }
    }
    void dispCount() {                         //������ʾ
        cout << bk.bookcount << endl; cout << rd.readercount << endl; cout << bb.borrowbookcount << endl;
    }
    void addbook()    //�����
    {

        string num, title, author, publisher;
        char num0[80], tit[80], auth[80], pub[80];
        int pd, pm, py, howmany;
        float price;
        Date publishdate;
        cout << "��š����������ߡ������硢��������(yyyy mm dd)�����ۡ��������" << endl;

        string num1 = "24416-5", title0 = "���ݽṹ", author0 = "����÷,����,����", pub0 = "�廪��ѧ������";
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
    void addreader() {                         //��Ӷ���
        string num, name, college, classno;
        char num0[80], nam[80], coll[80], clas[80];
        cout << "ѧ��\t����\tѧԺ\tרҵ�༶:" << endl;

        string num1 = "20151000", name0 = "����", college0 = "computer", class0 = "network class 1";
        cin >> num1 >> name0 >> college0 >> class0;
        rd.addreader(num1, name0, college0, class0);
        rd.write2Readerfile();
        int i = rd.readercount - 1;
        cout << i << ":";
        rd.reader[i].dispAReader();
    }
    void searchBook() {                         //����
        cout << "2��ͼ����Ϣ��ѯ���ֱ�����, ��������, ����������в�ѯ��" << endl;
        char tit[80];
        string title = "���ݽṹ", author = "����", pub = "��е��ҵ";
        int i, j, k, select;
        while (1) {
            cout << "ͼ����Ϣ��ѯ��" << endl;
            cout << "1����������ѯ" << endl;
            cout << "2������������ѯ" << endl;
            cout << "3�����������ѯ" << endl;
            cout << "0. return" << endl;
            cin >> select;
            cin.get();
            switch (select) {
            case 1:
                cout << "����:";
                getline(cin, title, '\n');
                bk.searchbookbytitle(title);
                break;
            case 2:
                cout << "������:";
                getline(cin, author, '\n');
                bk.searchbookbyauthor(author);
                break;
            case 3:
                cout << "������:";
                getline(cin, pub, '\n');
                bk.searchbookbypub(pub); break;
            case 0:return;
            }
        }
    }
    void sortbook() {           //����
        int select;
        cout << "3��ͼ����Ϣ���򣺰���š������Ȱ������������" << endl;
        cout << "ͼ����Ϣ����" << endl;
        cout << "1�����������" << endl;
        cout << "2������������" << endl;
        cout << "0. return" << endl;
        cin >> select;
        switch (select) {
        case 1:
            cout << "���:";
            bk.sortbookbynum();
            dispBook();
            break;
        case 2:
            cout << "����:";
            bk.sortbookbytitle();
            dispBook();
            break;
        case 0:return;
        }
    }
    void editbook() {                  //�༭��
        string oldtitle = "VisualBasic ������ƽ̳�", newtitle = "VisualBasic ������ƽ̳�-C", oldnum = "40667", newnum = "40667-C";
        int select;
        cout << "4��ͼ����Ϣ���޸ġ�ɾ��������Ż���������ͼ����޸ĺ�ɾ����" << endl;
        while (1) {
            cout << "ͼ����Ϣ���޸ġ�ɾ����" << endl;
            cout << "1��������޸�" << endl;
            cout << "2�������ɾ��" << endl;
            cout << "3���������޸�" << endl;
            cout << "4��������ɾ��" << endl;
            cout << "0. return" << endl;
            cin >> select;
            cin.get();
            switch (select) {
            case 1:
                cout << "old���:";
                getline(cin, oldnum, '\n');
                cout << "new���:";
                getline(cin, newnum, '\n');
                cout << "changebookbynum: " << oldnum << " to " << newnum << endl;
                bk.changebookbynum(oldnum, newnum);
                //dispBook();
                break;
            case 2:
                cout << "delete���:";
                getline(cin, oldnum, '\n');
                cout << "delete���:" << oldnum << endl;
                bk.deletebookbynum(oldnum);
                //dispBook();
                break;
            case 3:
                cout << "old����:";
                getline(cin, oldtitle, '\n');
                cout << "new����:";
                getline(cin, newtitle, '\n');
                cout << "changebookbytitle: " << oldtitle << " to " << newtitle << endl;
                bk.changebookbytitle(oldtitle, newtitle);
                //dispBook();
                break;
            case 4:
                cout << "delete����:";
                getline(cin, oldtitle, '\n');
                cout << "deletebookbytitle: " << oldtitle << endl;
                bk.deletebookbytitle(oldtitle);
                //dispBook();
                break;
            case 0:
                bk.write2Bookfile();
                cout << "�޸ĳɹ�" << endl;
                return;
            }
        }
    }
    void readerborrowabook() {                       //����
        cout << "9��ͼ����ģ�����ѧ��+��ţ��������ͼ����Ϣ���еĴ����������0������Խ����" << endl;
        string rdnum = "20061709", booknum = "33071", name, title;
        int select, rdpos, bookpos, y, m, d;
        while (1) {
            cout << "ͼ����ģ�" << endl;
            cout << "1������" << endl;
            cout << "0��return" << endl;
            cin >> select;
            cin.get();
            if (select == 0)return;
            cout << "borrowѧ��:";
            getline(cin, rdnum, '\n');
            cout << "borrow���:";
            getline(cin, booknum, '\n');
            bookpos = bk.searchbookbynump(booknum);
            rdpos = rd.searchreaderbynump(rdnum);
            if (bookpos > 0 && rdpos > 0) {
                int hm = bk.book[bookpos].getHowmany();
                if (hm > 0) {
                    name = rd.reader[rdpos].getName();
                    title = bk.book[bookpos].getTitle();
                    bk.book[bookpos].setHowmany(hm - 1); //�޸�ͼ����Ϣ���еĴ������
                    bb.borrowbook[bb.borrowbookcount].setNum(rdnum);
                    bb.borrowbook[bb.borrowbookcount].setBookNum(booknum);
                    bb.borrowbook[bb.borrowbookcount].setName(name);
                    bb.borrowbook[bb.borrowbookcount].setTitle(title);

                    SYSTEMTIME ct;
                    GetLocalTime(&ct);//ȡϵͳʱ�䣬�����GetSystemTime(&ct);��ô��ȡ���Ǹ������α�׼ʱ��
                    y = ct.wYear;
                    m = ct.wMonth;
                    d = ct.wDay;
                    Date toret = Date(d, m, y) + 60;
                    bb.borrowbook[bb.borrowbookcount].setBorrowdate(d, m, y);
                    bb.borrowbook[bb.borrowbookcount].setToreturndate(toret.getDay(), toret.getMonth(), toret.getYear());
                    bb.borrowbook[bb.borrowbookcount].setReturndate(1, 1, 1);
                    bb.borrowbookcount++;
                }
                else cout << booknum << " �������=0" << ". can't be borrowed. " << endl;
            }
            else {
                if (bookpos < 0)cout << "No book " << booknum << ". can't borrow!" << endl;
                if (rdpos < 0)cout << "No reader " << rdnum << ". can't borrow!" << endl;
            }
        }
    }
    void readerreturnabook() {   //�黹
        cout << "10��ͼ��黹������ѧ��+�������޸�ͼ����Ϣ���еĴ��������ͼ����ı��м�¼��ͬѧ�Ĺ黹���ڡ�" << endl;
        char tit[80];
        string rdnum = "20061709", booknum = "33071", name, title;
        int selectttt, rdpos, bookpos, y, m, d;
        while (1) {
            cout << "ͼ��黹��" << endl;
            cout << "1������" << endl;
            cout << "0��return" << endl;
            cin >> selectttt;
            cin.get();
            if (selectttt == 0) { return; }
            cout << "returnѧ��:" << endl;
            getline(cin, rdnum, '\n');

            cout << "return���:";
            getline(cin, booknum, '\n');

            bookpos = bk.searchbookbynump(booknum);
            rdpos = rd.searchreaderbynump(rdnum);
            int k;
            k = bb.searchbyreaderbook(rdnum, booknum);
            if (k >= 0) {
                if (bookpos > 0 && rdpos > 0) {
                    bk.book[bookpos].setHowmany(bk.book[bookpos].getHowmany() + 1);
                    SYSTEMTIME ct;
                    GetLocalTime(&ct);//ȡϵͳʱ��
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
        cout << "6.������Ϣ��ѯ���ֱ�ѧ�š��������༶�Ƚ��в�ѯ��" << endl;
        int selectt;
        while (1) {
            cout << "������Ϣ��ѯ��" << endl;
            cout << "1����ѧ�Ų�ѯ" << endl;
            cout << "2����������ѯ" << endl;
            cout << "3. ��ѧԺ��ѯ" << endl;
            cout << "4. ��רҵ�༶��ѯ" << endl;
            cout << "0. return" << endl;
            cin >> selectt;
            cin.get();
            switch (selectt)
            {
            case 1: cout << "ѧ�ţ�" << endl;
                getline(cin, xuehao, '\n');
                cout << 1 << endl;
                rd.searchreaderbynum(xuehao);
                break;
            case 2:cout << "������" << endl;
                getline(cin, xingming, '\n');
                rd.searchreaderbyname(xingming);
                break;
            case 3:cout << "ѧԺ�� " << endl;
                getline(cin, zzy, '\n');
                rd.searchreaderbyzybj(zzy);
                break;
            case 4:cout << "רҵ�༶�� " << endl;
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
        cout << "7��������Ϣ���򣺰�ѧ�š�ѧԺ�Ȱ������������" << endl;
        cout << "������Ϣ����" << endl;
        cout << "1����ѧ������" << endl;
        cout << "2����ѧԺ����" << endl;
        cout << "0. return" << endl;
        cin >> selectt1;
        switch (selectt1) {
        case 1:
            cout << "ѧ��:";
            rd.sortreaderbyxuahao();
            dispReader();
            break;
        case 2:
            cout << "ѧԺ:";
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
        cout << "8��ѧ����Ϣ���޸ġ�ɾ������" << endl;

        while (1) {
            cout << "ѧ����Ϣ���޸ġ�ɾ����" << endl;
            cout << "1����ѧ���޸�" << endl;
            cout << "2����ѧ��ɾ��" << endl;
            cout << "3���������޸�" << endl;
            cout << "4��������ɾ��" << endl;
            cout << "0. return" << endl;
            cin >> select2;
            cin.get();
            switch (select2)
            {
            case 1:cout << "Ҫ�޸�ѧ����ѧ��Ϊ��" << endl;
                cin >> xh;
                cout << "��������ѧ��" << endl;
                cin >> newxh;
                rd.changereaderbyxuehao(xh, newxh);
                break;
            case 2:cout << "Ҫɾ����ѧ��ѧ��Ϊ��" << endl;
                cin >> xh;
                rd.deletereaderbyxuehao(xh);
                break;
            case 3:cout << "�޸ĵ�ѧ������Ϊ��" << endl;
                cin >> xm;
                cout << "�������޸ĺ��������" << endl;
                cin >> newxm;
                rd.changereaderbyxingming(xm, newxm);
                break;
            case 4:cout << "Ҫɾ����ѧ������Ϊ��" << endl;
                cin >> xm;
                rd.deletereaderbyxingming(xm);
                break;
            case 0: rd.write2Readerfile();
                cout << "�޸ĳɹ�";
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
            cout << "11��ͼ����Ĳ�ѯ���ֱ�ѧ�š�������ѧԺ�Ƚ��в�ѯ��" << endl;
            cout << "1.��ѧ�Ų�ѯ" << endl;
            cout << "2.��������ѯ" << endl;
            cout << "0.return" << endl;
            cin >> bz;
            switch (bz)
            {
            case 1:cout << "������ѧ��" << endl;
                cin >> xxh;
                bb.searchborrowbookbyxuehao(xxh); break;
            case 2:cout << "����������" << endl;
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
        cout << "�˵�ѡ���ܣ�" << endl;
        cout << "1��ͼ����Ϣ��ӹ��ܣ�������š����������ߡ����������ơ�������������۵�" << endl;
        cout << "2��ͼ����Ϣ��ѯ���ֱ�����, ��������, �����浥λ�Ƚ��в�ѯ��" << endl;
        cout << "3��ͼ����Ϣ���򣺰���š������Ȱ������������" << endl;
        cout << "4��ͼ����Ϣ���޸ġ�ɾ��������Ż���������ͼ����޸ĺ�ɾ����" << endl;
        cout << "5��������Ϣ��ӹ��ܣ�����ѧ�š�������ѧԺ��רҵ�༶�ȡ�" << endl;
        cout << "6��������Ϣ��ѯ���ֱ�ѧ�š��������༶�Ƚ��в�ѯ��" << endl;
        cout << "7��������Ϣ���򣺰�ѧ�š�ѧԺ�Ȱ������������" << endl;
        cout << "8��������Ϣ���޸ġ�ɾ������ѧ��+�������ж�����Ϣ���޸ĺ�ɾ����" << endl;
        cout << "9��ͼ����ģ�����ѧ��+��ţ��������ͼ����Ϣ���еĴ����������0������Խ��," << endl;
        cout << "�����Ӧ�������޸�ͼ����Ϣ���еĴ����������ͼ����ı���Ӹ�ͬѧ�Ľ��ġ�" << endl;
        cout << "10��ͼ��黹������ѧ��+�������޸�ͼ����Ϣ���еĴ����������ͼ����ı��м�¼��ͬѧ�Ĺ黹ʱ�䡣" << endl;
        cout << "11��ͼ����Ĳ�ѯ���ֱ�ѧ�š�������ѧԺ�Ƚ��в�ѯ��" << endl;
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
