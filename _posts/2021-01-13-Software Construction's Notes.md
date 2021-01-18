---
layout: post
title: Software Construction's Notes
Subtitle: 整理自 mit6.031 课程，主要使用 Java 语言同事适用于其他语言。
tags: [软件工程]
---

## 测试

## 规范

## 设计规范

## 可变性与不可变性

## 避免 debug

* make bugs impossible

  ​	静态检查在编译期消除bug，动态检查动态捕捉异常；

  ​	不可变也是一种常用的阻止bug出现的设计原则；

  ​	使用final避免重新分配。

* Localize bugs

  ```java
  /**
   * @param x  requires x >= 0
   * @return approximation to square root of x
   */
  public double sqrt(double x) { 
      if (! (x >= 0)) throw new IllegalArgumentException("required x >= 0, but was: " + x);
      ...
  }
  ```

  检查前置条件也是一种防御式编程。

  增量开发：

  * 单元测试
  * 回归测试

  模块化和封装：Modularity & encapsulation

* 断言 Assertions

  ```JAVA
  assert x >= 0 : "x is " + x;
  ```

  **Java 断言默认情况是关闭的，通过设置 -ea 可以开启断言。**

  测试JUnit最好开启断言，测试断言是否开启：

  ```java
  @Test
  public void testAssertionsEnabled() {
      assertThrows(AssertionError.class, () -> { assert false; });
  }
  ```

  * 断言选择:
    * 方法参数要求
    * 方法返回值要求（self check)。对于sqrt自检 `assert Math.abs(r*r - x) < .0001`
    * 避免琐碎的断言，如同不必要的注释
    * 不要用断言测试程序外部的条件，例如文件是否存在
    * 断言不应该有副作用（side-effects)

## 抽象数据类型

抽象意味着：

* Abstraction：使用更简单，更高级的想法忽略或隐藏低级细节
* Modularity:
* Encapsulation:
* Information hiding
* Separation of concerns

操作区分：

* Creators： t* -> T
* Producers: T+, t* -> T
* Observers: T+, t* -> t
* Mutators: T+, t* -> void|t|T

## Debugging

## 递归

## 并发



## 线程安全性

## 回调



