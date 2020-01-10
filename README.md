# twitter-profile-update-action
Action for update twitter profile regularly

## 사용하기 위해서

1. Twitter API에 액세스 하기 위한 개발자 계정에 지원합니다.
   * https://developer.twitter.com/en/apply-for-access
2. Twitter app을 생성하고, consumer key와 consumer secret key를 generate합니다.
3. Twurl을 설치합니다.
   * https://github.com/twitter/twurl
4. Twurl Authorization을 합니다.

```bash
twurl authorize --consumer-key key       \
                --consumer-secret secret
```

위 커맨드를 실행하면 Twitter에 Authorization하기 위한 PIN이 있는 URL이 나오는데, 생성된 PIN을 터미널에 입력하면 됩니다.

5. Bearer Token을 만듭니다.

```bash
twurl authorize --bearer --consumer-key key       \
                         --consumer-secret secret
```

6. 로컬에서 생성된 `~/.twurlrc` 파일을 github secrets에 `TWURLRC`로 추가합니다.
7. 이 Repository를 Fork하고, `main/__main__.py`의 print문을 수정합니다.
8. workflows의 TwitterBioUpdate를 삭제 후 재생성합니다. 재생성한 `TwitterBioUpdate.yml`에 원래 내용을 복사-붙여넣기 합니다.

## 자동화 주기 설정하기

`/.github/workflows/TwitterBioUpdate.yml`의 [on.schedule](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/workflow-syntax-for-github-actions#onschedule)를 수정합니다. 
`on.schedule`은 POSIX [cron syntax](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows#scheduled-events-schedule)를 따릅니다.

가장 짧은 자동화 주기는 5분입니다.


```yml
name: TwitterBioUpdate

on:
  push:
    branches:
      - master
  schedule:
    - cron: '*/60 * * * *'

---중략---
```

`on.schedule`의 cron syntax는 다음과 같습니다.
```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of the month (1 - 31)
│ │ │ ┌───────────── month (1 - 12 or JAN-DEC)
│ │ │ │ ┌───────────── day of the week (0 - 6 or SUN-SAT)
│ │ │ │ │                                   
│ │ │ │ │
│ │ │ │ │
* * * * *
```