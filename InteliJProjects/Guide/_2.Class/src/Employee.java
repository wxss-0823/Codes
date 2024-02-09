public class Employee {
    String name;
    int age;
    String designation;
    double salary;
    // Employee 类的构造函数
    public Employee(String name){
        this.name = name;
    }
    // 设置 age 的值
    public void empAge(int empAge){
        this.age = empAge;
    }
    /* 设置 salary 的值 */
    public void empSalary(double empSalary){
        this.salary = empSalary;
    }
    /* 设置 designation 的值 */
    public void empDesignation(String empDesignation){
        this.designation = empDesignation;
    }
    /* 打印信息 */
    public void printEmployee(){
        System.out.println("名字:" + name);
        System.out.println("年龄:" + age);
        System.out.println("职位:" + designation);
        System.out.println("工资:" + salary);
    }
}
