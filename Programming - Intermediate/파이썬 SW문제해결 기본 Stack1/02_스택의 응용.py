# -*- coding: utf-8 -*-
"""
괄호의 종류: 대괄호, 중괄호, 소괄호

조건
1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 함
2. 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 함
3. 괄호 사이에는 포함 관계만 존재함

스택을 이용한 괄호 검사
if( ( i == 0 ) &&& ( j == 0 ) )

괄호를 조사하는 알고리즘 개요
1. 문자열에 있는 괄호를 차례대로 조사
2-1. 왼쪽 괄호를 만나면 스택에 삽입
2-2. 오른쪽 괄호를 만나면 스택에서 top 괄호를 삭제한 후 오른쪽 괄호와 짝이 맞는지 호가인
2-2-1. 스택이 비어있음(조건 1 또는 조건 2에 위배)
2-2-2. 괄호의 짝이 맞지 않음(조건 3에 위배)
2-2-3. 문자열 끝까지 조사한 후에도 스택에 괄호가 남아있음(조건 1에 위배)

함수 호출 관리
프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
1. 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는
   후입선출 구조이므로, 후입선출 구조의 스택을 이용하여 수행순서 관리
2. 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및
   수행 후 복귀할 주소 등의 정보를 스택 프레임에 저장하여 시스템 스택에 삽입
3. 함수의 실행이 끝나면 시스템 스택의 top 원소(스택 프레임)를
   삭제(pop)하면서 프레임에 저장되어있던 복귀주소를 확인하고 복귀
4. 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이
   종료되면 시스템 스택은 공백 스택이 됨

함수 호출 수행 순서
main()호출 -> F_1()호출 -> F_2()호출 -> F_2()종료, F_1()복귀 -> F_1()종료, main()복귀
stack_Frame(main) -> stack_Frame(F_1) -> stack_Frame(F_2)

재귀 호출
1. 자기 자신을 호출하여 순환 수행되는 것
2. 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다
   재귀 호출 방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고
   간단하게 작성할 수 있음
3. 디버깅이 어렵고 잘못 작성하게 되면 수행 시간이 많이 소요됨

ex) 재귀 호출을 작성할 수 있는 함수 - factorial
n에 대한 factorial: 1부터 n까지의 모든 자연수를 곱하여 구하는 연산
마지막에 구한 하위 값을 이용하여 상위 값을 구하는 작업을 반복
"""

