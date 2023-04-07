## Thread🛤
---
1. ### [th_ex01_basic.py](./th_ex01_basic.py)
   - `threading` 모듈에 **함수** 를 전달하여 실행
   - `Main thread` 가 먼저 들어올지, `Sub thread` 가 먼저 들어올지, `Sub thread` 가 끝나기 전에 `Main`이 들어올지 모른다.
2. ### [th_ex02_web_download.py](./th_ex02_web_download.py)
   - 웹 크롤링을 위해 `conda` 환경에서 진행
   - `Sub thread` 가 웹 크롤링 진행
3. ### []()
   - `Thread` 클래스를 **상속** 받아 운영
   - 꼭 부모 클래스의 **생성자** 를 호출해야한다.
   - `run` 을 재정의 해야한다.
      - `target` 에 주어진 **함수**의 일을 `run`에서 진행 
   - 만약 `start()` 를 하지않고 `run()`을 하면 **현재의 스레드** 가 `run`을 실행 → 작업스레드 생성되지 않는다.
   