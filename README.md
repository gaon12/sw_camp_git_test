# Git 명령어
## 프로젝트 폴더 생성
* 여기에선 프로젝트 폴더 이름을 'prgit' 으로 하겠습니다.
```
$ mkdir prgit
$ cd prgit
```

## 깃 정보 입력
```
$ git config --global user.name "Jeong Sol"
$ git config --global user.email solsol0609@naver.com
```

## 저장소 생성, add, commit
```
$ git init
$ git add random_test.py
$ git commit -m "in order to redefine random.py"
```

커밋 메시지를 변경하기 원한다면, 다음과 같이 입력합니다.
```
$ git commit --amend
```

## 리모트 저장소(Remote Repository)로 푸시(Push)
```
$ git push
```

단, <code>commit</code>이 되어 있어야 합니다.

## 무시할 파일 설정
<code>.gitignore</code> 파일을 생성 후, 무시할 파일을 설정합니다.

```
$ touch .gitignore
```

이후 .gitignore 파일을 열고, 다음 문법에 따라 수정하면 됩니다.

### 특정 폴더 제외
```
[DIRECTORY_NAME]
```

예 : <code>logs</code>

### 특정 파일 제외
```
[FILE_NAME].[EXTENSION]
```

예 : <code>test.log</code>

### 특정 확장자 제외
```
*.[EXTENSION]
```

예 : <code>*.log</code>

### 폴더 안 특정 파일 제외
```
[DIRECTORY_NAME]/[FILE_NAME].[EXTENSION]
```

예 : <code>log/result.log</code>

## 파일 변경사항 확인
```
$ git diff
```
working directory에 있는 파일과 staging area에 있는 파일의 차이를 보여줍니다.

추가된 줄은 <code>+</code>, 삭제된 줄은 <code>-</code>로 표시됩니다. 줄 단위로 변경사항을 확인합니다.

전체 버전의 HEAD와 비교하기 원한다면, 다음과 같이 입력합니다.
```
$ git diff HEAD
```

## 깃 역사(git history)
지금까지 깃으로 작업한 내용을 볼 수 있습니다.
```
$ git log
```

한줄로 보고 싶다면, 다음과 같이 입력합니다.
```
$ git log --oneline
```

원하는 갯수만큼 보고 싶다면 다음과 같이 입력합니다. 여기서는 3개로 하겠습니다.

```
$ git log -3
```