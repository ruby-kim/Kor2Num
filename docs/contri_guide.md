# Contributor Guide

## version: `x.y.z`

- x: Large-scale update
  - 0: **incomplete** making code: number text -> real text
  - 1: fix bugs 0.x.x version
- y: Modify [ cardinal / ordinal ] numbers
  - 0: cardinal number
  - 1: ordinal number
- z: Number of revisions

## Commit 메시지 구조

```
type: subject

body

footer
```

## Commit Type

- feat: 새로운 기능 추가
- fix: 버그 수정
- docs: 문서 수정
- refactor: 코드 리펙토링
- test: 테스트 코드, 리펙토링 테스트 코드 추가
- chore: 빌드 업무 수정, 패키지 매니저 수정

## Subject

- 제목은 50자를 넘기지 않고, 마침표를 붙이지 않는다

## Body

- 선택사항
- 부연설명이 필요하거나 커밋의 이유를 설명할 때 작성
- 제목과 구분되기 위해 한 칸 띄워 작성

## Footer

- 선택사항
- (예정) 추후 github issue로 관리 시 이슈 트래킹을 위해 사용
