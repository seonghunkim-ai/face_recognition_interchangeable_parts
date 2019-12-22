# face_recognition_interchangeable_parts

기존의 [face_recognition] 에서 image_scrapper, crop_image 파일을 수정하였습니다.

[face_recognition]: https://github.com/seonghunkim-ai/face_recognition

## Changes

### image_scrapper
- Bing에서 Google로 검색 엔진 사이트 변경

### crop_image
- 원본 이미지에서 얼굴 검출 방식을 변경하였습니다.
  - openCV의 Haar Cascades Classifier -> [OpenFace] (오픈소스 얼굴인식 DNN)
  - 윈도우에서 구동할 경우 
    1. dlib 패키지 맟 CMake를 설치합니다. [ [참조 링크] ]
    1. [OpenFace GitHub페이지]에서 다운받은 프로젝트 내에 있는 requirements.txt의 패키지들을 설치합니다.
      - pip install -r requirements.txt
    1. cmd(Anaconda Prompt)에서 아래 코드를 실행합니다.
      - python setup.py install

[참조 링크]: https://sulastri.tistory.com/3
[OpenFace]: http://cmusatyalab.github.io/openface/
[OpenFace GitHub페이지]: https://github.com/cmusatyalab/openface
