# 🤳 Django Blog Community Web Application


## 💡 Project Introduction
Django 프레임워크를 활용한 블로그 커뮤니티 웹 애플리케이션입니다.  Reddit 및 Pinterest와 비슷한 스타일의 글 작성 및 공유, 커뮤니티 형성이 가능합니다.
사용자는 반응형 웹 페이지를 통해 다양한 기기에서 접근할 수 있으며, 게시글 작성, 수정, 삭제, 목록 확인 등의 기능을 제공합니다. 
또한, 커뮤니티 생성 및 구독, 댓글 작성, 개인 프로필 설정 등의 기능도 포함되어 있습니다.


## 🪄 Development Timeline
2023.01 ~ 2024.03


## 🗝️ Technology Stack
**IDE**: Pycharm

**Framework**: Django

**Programming Language**: Python

**Frontend**: Bootstrap

**Design Pattern**: MVT (Model/View/Template)

**Database**: Django 기본 제공 데이터베이스 (SQLite)



## 🎯 Functions
1. **회원 관리**
   - 로그인 및 회원가입
   - 개인 프로필 설정
2. **게시글 관리**
   - 게시글 작성, 수정, 삭제, 목록 확인 (CRUD)
   - 댓글 작성
3. **커뮤니티 기능**
   - 커뮤니티 생성
   - 커뮤니티 구독
4. **반응형 웹 디자인**
   - 모바일 환경에서도 최적화된 사용자 경험 제공
  

## 🧀 Implementation Challenges
1. View단의 혼용
   - Class Based View와 Function Based View를 혼용하여 사용하였으며, Class Based View에서는 메서드 오버라이딩을 통해 원하는 기능을 커스터마이징하는 부분
   -  Function Based View에서는 코드의 길이가 길어져 가독성이 떨어지는 문제
2. Template와 View의 데이터 통신
   - Template단과 View단 사이의 데이터 통신 구조 파악
   - View단에서 전달한 데이터를 Template단에서 효율적으로 활용하고 처리하는 최적화 로직을 구현
